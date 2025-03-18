from neo4j import GraphDatabase

class Neo4jDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def search_documents(self, entities, query_embedding):
        """
        Fetch relevant documents using Neo4j, returning a list of dicts:

        [
          {
            "doc_id": ...,
            "text": ...,
            "doc_distance": ...,
            "doc_similarity": ...,
            "entity_distance": ...,
            "entity_similarity": ...,
            "combined_score": ...
          },
          ...
        ]
        """
        with self.driver.session() as session:
            # STEP 1: Document-based (distance → similarity)
            doc_query = """
            CALL db.index.vector.queryNodes('document_embedding_index', 50, $query_embedding)
            YIELD node AS doc, score AS doc_distance
            RETURN doc.id AS doc_id, doc.text AS text, doc_distance
            """
            doc_results = session.run(doc_query, query_embedding=query_embedding)
            
            doc_scores = {}
            for record in doc_results:
                doc_id = record["doc_id"]
                text = record["text"]
                doc_distance = record["doc_distance"]
                doc_similarity = 1 / (1 + doc_distance)  # Example transform

                doc_scores[doc_id] = {
                    "text": text,
                    "doc_distance": doc_distance,
                    "doc_similarity": doc_similarity,
                    "entity_distance": 0.0,
                    "entity_similarity": 0.0
                }

            # STEP 2: Entity-based (distance → similarity)
            entity_query = """
            CALL db.index.vector.queryNodes('entity_embedding_index', 50, $query_embedding)
            YIELD node AS entity, score AS entity_distance
            MATCH (entity)<-[:HAS_ENTITY]-(doc:Document)
            RETURN doc.id AS doc_id, entity_distance
            """
            entity_results = session.run(entity_query, query_embedding=query_embedding)
            for record in entity_results:
                doc_id = record["doc_id"]
                entity_distance = record["entity_distance"]
                entity_similarity = 1 / (1 + entity_distance)

                if doc_id not in doc_scores:
                    doc_scores[doc_id] = {
                        "text": "",
                        "doc_distance": 0.0,
                        "doc_similarity": 0.0,
                        "entity_distance": 0.0,
                        "entity_similarity": 0.0
                    }
                # You might sum, keep track of max, or average. Example sums:
                doc_scores[doc_id]["entity_distance"] += entity_distance
                doc_scores[doc_id]["entity_similarity"] += entity_similarity

            # STEP 3: Expand entity similarity with Knowledge Graph
            kg_query = """
            MATCH (d:Document)-[:HAS_ENTITY]->(e:NamedEntity)
            WHERE any(entity IN $entities WHERE e.text CONTAINS entity)
            WITH d, COUNT(e) AS entity_count

            OPTIONAL MATCH (e)-[:LINKS_TO]->(w:WikidataConcept)<-[:LINKS_TO]-(e2:NamedEntity)
            WITH d, entity_count, COUNT(e2) AS related_entity_count

            RETURN d.id AS doc_id, (entity_count + related_entity_count) AS kg_score
            """
            kg_results = session.run(kg_query, entities=entities)
            for record in kg_results:
                doc_id = record["doc_id"]
                kg_score = record["kg_score"]
                # Possibly scale or normalize kg_score here if it’s large

                if doc_id not in doc_scores:
                    doc_scores[doc_id] = {
                        "text": "",
                        "doc_distance": 0.0,
                        "doc_similarity": 0.0,
                        "entity_distance": 0.0,
                        "entity_similarity": 0.0
                    }
                doc_scores[doc_id]["entity_similarity"] += kg_score

            # STEP 4: Combine
            results = []
            for doc_id, vals in doc_scores.items():
                combined_score = 0.7 * vals["doc_similarity"] + 0.3 * vals["entity_similarity"]
                result_dict = {
                    "doc_id": doc_id,
                    "text": vals["text"],
                    "doc_distance": vals["doc_distance"],
                    "doc_similarity": vals["doc_similarity"],
                    "entity_distance": vals["entity_distance"],
                    "entity_similarity": vals["entity_similarity"],
                    "combined_score": combined_score
                }
                results.append(result_dict)

            # Sort by combined_score (descending) and return top 4
            results.sort(key=lambda x: x["combined_score"], reverse=True)
            return results[:4]
