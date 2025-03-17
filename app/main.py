from neo4j import GraphDatabase
import pandas as pd
import numpy as np
import streamlit as st

from models.embedding import EmbeddingModel
from services.SearchApp import SemanticSearchApp
from database.neo4j_driver import Neo4jDatabase
from UI.home import SearchUI

# Initialize
embedding_model = EmbeddingModel()
db = Neo4jDatabase("bolt://localhost:7687", "neo4j", "12345678")
search_app = SemanticSearchApp(db, embedding_model)
search_ui = SearchUI(search_app)

# Run UI
search_ui.run()

# Close DB connection
db.close()
