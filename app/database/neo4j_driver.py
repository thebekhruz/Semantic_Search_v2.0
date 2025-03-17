from neo4j import GraphDatabase

class Neo4jDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def search_documents(self, entities, query_embedding):
        """Fetch relevant documents using Neo4j, considering both named entities and embeddings."""
        with self.driver.session() as session:
            # Step 1: Find documents mentioning extracted entities
            entity_query = """
            MATCH (d:Document)-[:HAS_ENTITY]->(e:NamedEntity)
            WHERE any(entity in $entities WHERE e.text CONTAINS entity)
            RETURN d.id AS doc_id, d.text AS text, d.embedding AS embedding, COUNT(e) AS entity_score
            ORDER BY entity_score DESC
            LIMIT 50
            """
            results = session.run(entity_query, entities=entities)

            # Step 2: Use Neo4j GDS to compute cosine similarity
            vector_query = """
            CALL db.index.vector.queryNodes('document_embedding_index', 10, $query_embedding)
            YIELD node, score
            RETURN node.text AS text, score
            """
            vector_results = session.run(vector_query, query_embedding=query_embedding)

            # Step 3: Merge Entity + Vector Scores
            docs = []
            entity_scores = {record["text"]: record["entity_score"] for record in results}

            for record in vector_results:
                doc_text = record["text"]
                similarity_score = record["score"]
                entity_score = entity_scores.get(doc_text, 0)

                # Weighted Score: 70% cosine similarity, 30% entity match count
                final_score = 0.7 * similarity_score + 0.3 * (entity_score / max(1, len(entities)))
                docs.append((doc_text, final_score))

            # Sort documents by final score
            docs.sort(key=lambda x: x[1], reverse=True)
            return docs[:4]  # Return top 4 results