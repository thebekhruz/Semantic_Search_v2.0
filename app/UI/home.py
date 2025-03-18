import streamlit as st
class SearchUI:
    def __init__(self, search_app):
        self.search_app = search_app

    def run(self):
        st.title("Semantic Search with Neo4j")
        query = st.text_input("Enter your search query:")
        if query:
            entities =  self.search_app.get_named_entities(query)
            results = self.search_app.search(query, entities)

            # Show the named entities (if any)
            if entities:
                st.subheader("Named Entities Extracted From Your Query")
                st.write(", ".join(entities))
            else:
                st.write("No named entities extracted.")

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
