from SPARQLWrapper import SPARQLWrapper, JSON
from neo4j import GraphDatabase

# Connect to Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "12345678"
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Function to fetch descriptions from Wikidata
def get_wikidata_description(wiki_id):
    query = f"""
    SELECT ?description ?instanceOfLabel WHERE {{
      wd:{wiki_id} schema:description ?description.
      OPTIONAL {{ wd:{wiki_id} wdt:P31 ?instanceOf. ?instanceOf rdfs:label ?instanceOfLabel. FILTER (lang(?instanceOfLabel) = "en") }}
      FILTER (lang(?description) = "en")
    }} LIMIT 1
    """
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    if results["results"]["bindings"]:
        result = results["results"]["bindings"][0]
        description = result.get("description", {}).get("value", "No description available")
        instance_of = result.get("instanceOfLabel", {}).get("value", "Unknown type")
        return description, instance_of
    return "No description available", "Unknown type"

# Update Neo4j with fetched data
def update_neo4j():
    with driver.session() as session:
        wikidata_nodes = session.run("MATCH (w:WikidataConcept) RETURN w.wikiId AS wikiId")
        for record in wikidata_nodes:
            wiki_id = record["wikiId"]
            description, instance_of = get_wikidata_description(wiki_id)
            session.run(
                "MATCH (w:WikidataConcept {wikiId: $wikiId}) "
                "SET w.description = $description, w.type = $instanceOf",
                wikiId=wiki_id, description=description, instanceOf=instance_of
            )

update_neo4j()
