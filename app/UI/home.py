import streamlit as st
class SearchUI:
    def __init__(self, search_app):
        self.search_app = search_app

    def run(self):
        st.title("Semantic Search with Neo4j")
        query = st.text_input("Enter your search query:")
        if query:
            entities = []  # Placeholder for entity extraction if needed
            results = self.search_app.search(query, entities)
            
            if results:
                st.subheader("Search Results")
                
                # Display results in two columns
                cols = st.columns(2)
                for idx, res in enumerate(results, start=1):
                    col = cols[idx % 2]  # Alternate between columns
                    col.metric(label=f"Result {idx}", value=f"Score: {res[1]:.2f}", border=True)
                    col.write(f"**Document:** {res[0]}")
                    col.markdown("---")
            else:
                st.warning("No relevant documents found.")
