# Semantic Search with Neo4j & Streamlit

## 🔍 Unlocking the Power of AI-Driven Search

**Imagine effortlessly retrieving meaningful insights from vast collections of historical and textual data.** This project brings together **Natural Language Processing (NLP), Graph Databases (Neo4j), and Vector Search** to create an advanced **semantic search engine**. Originally developed as part of my university experience, this system was built for **Our Heritage, Our Stories (OHOS)** as a **charity initiative** to help preserve and explore historical narratives through AI-driven search. It enables intuitive, context-aware search experiences, bridging technology and cultural heritage.

---

## 🚀 Project Overview

**Goal:** Build a **fast, intelligent, and context-aware** search engine using **Neo4j, Sentence Transformers, and Streamlit**.

🔹 **Graph Database Integration**: Leverages **Neo4j** to store relationships between documents and named entities.  
🔹 **Vector Search**: Uses **sentence embeddings** to capture **semantic meaning**, enabling highly relevant search results.  
🔹 **Named Entity Recognition (NER)**: Identifies key entities (people, locations, artifacts) for enriched search.  
🔹 **Streamlit UI**: Delivers an interactive, user-friendly interface for real-time exploration.


📌 **Insert Image of Project Architecture**

---

## 🧠 Why Graph Databases for Search?
Traditional keyword-based search fails to capture **context** and **relationships** between data points. This project takes a different approach:

📍 **Neo4j as a Knowledge Graph**: Connects documents through **entities, categories, and metadata**.

📍 **Vector Search + Graph Queries**: Enhances results by combining **cosine similarity with entity-based filtering**.

📌 **Insert Image of Graph Representation in Neo4j**

---

## 🛠️ Tech Stack

- **Neo4j**: Stores and queries document relationships efficiently.
- **Sentence Transformers (`all-MiniLM-L6-v2`)**: Generates embeddings for semantic similarity.
- **Streamlit**: Provides an interactive front-end for easy user access.
- **Python (OOP Design)**: Ensures modular, scalable code.

📌 **Insert Screenshot of UI in Action**

---

## 📌 Features

✅ **Graph-Powered Search**: Documents are connected by relationships, not just keywords.  
✅ **Hybrid Search (Entities + Vectors)**: Uses both **semantic similarity** and **named entities** for better ranking.  
✅ **Fast Retrieval**: Optimized for real-time queries.  
✅ **Modular Codebase**: Follows best practices with **separate services, models, and utilities**.

📌 **Insert GIF of a User Performing a Search**

---

## 🔬 How It Works

1️⃣ **Preprocessing**: Documents are embedded using **Sentence Transformers**.  
2️⃣ **Graph Storage**: Data is stored in **Neo4j** as a **knowledge graph**.  
3️⃣ **Querying**: User inputs a search query, and the system retrieves documents via:  
   - **Graph Traversal (Entity Match)**
   - **Vector Similarity Search (Cosine Distance)**
   - **Hybrid Score (Weighted Combination of Both)**
4️⃣ **Ranking & Display**: The top results are shown in **Streamlit** with interactive UI elements.

📌 **Insert Flow Diagram Explaining Query Process**

---

## 📈 Results & Performance

⚡ **Achieves high accuracy** in returning **semantically relevant documents**.

📌 **Insert Performance Benchmark Chart (e.g., Time per Query, Accuracy Comparisons, Scalability Metrics)**

---

## 📚 Skills Demonstrated

✅ **Graph Databases & Neo4j**: Querying & designing graph-based search systems.  
✅ **NLP & Embeddings**: Using sentence transformers for semantic understanding.  
✅ **Vector Search**: Implementing **cosine similarity** for relevance ranking.  
✅ **Full-Stack Development**: Backend (Python, Neo4j) + Frontend (Streamlit).  
✅ **Optimization & Scalability**: Efficient querying for large datasets.

📌 **Insert Image Representing Tech Skills (E.g., Python, Neo4j, NLP Logos)**

---

## 🔗 Want to Try It?

1️⃣ **Clone the Repo**  
```bash
git clone https://github.com/yourusername/semantic-search.git
cd semantic-search
```

2️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

3️⃣ **Run the App**  
```bash
streamlit run main.py
```

📌 **Insert GIF of App Running in Terminal**

---

## 🎯 Next Steps & Improvements

🔹 **Support for Multimodal Search**: Incorporate **image + text embeddings**.  
🔹 **Faster Query Execution**: Optimize Neo4j indexes for large datasets.  
🔹 **Improved UI/UX**: Add **visual graphs for entity relationships**.  
🔹 **Deploy as a Web App**: Host on **Streamlit Cloud** or **Heroku**.

📌 **Insert Roadmap Graphic with Future Enhancements**

---

## 💡 Let's Connect!

🚀 Interested in AI-powered search, graph databases, or data science? Let's discuss!  
📧 **Email**: [your.email@example.com](mailto:your.email@example.com)  
🔗 **LinkedIn**: [linkedin.com/in/yourname](https://linkedin.com/in/yourname)  
💻 **GitHub**: [github.com/yourusername](https://github.com/yourusername)  

📌 **Insert Personal Branding Image (E.g., LinkedIn Profile, GitHub Banner)**

