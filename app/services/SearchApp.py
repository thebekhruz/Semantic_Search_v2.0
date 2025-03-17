from neo4j import GraphDatabase
import pandas as pd
import numpy as np
from transformers import pipeline


class SemanticSearchApp:
    """
    Initialize the SemanticSearchApp with a database connection and an embedding model.

    Parameters:
    db (object): The database connection object.
    embed_model (object): The embedding model object.
    """
    
    def __init__(self, db, embed_model):
        self.db = db
        self.embed_model = embed_model
        self.ner_model = pipeline('ner', model='dslim/bert-base-NER', aggregation_strategy="simple")


    def get_named_entities(self, user_input):
        """Extract named entities and return them as a list."""
        
        self.entities = self.ner_model(user_input)
        return [entity['word'] for entity in self.entities]

    def search(self, query, entities=[]):
        """
        Perform a semantic search for the given query.

        Parameters:
        query (str): The search query.
        entities (list): List of named entities to consider.

        Returns:
        list: A list of search results.
        """
        query_embedding = self.embed_model.get_embedding(query)
        entities = self.get_named_entities(query)
        results = self.db.search_documents(entities, query_embedding)
        return results
