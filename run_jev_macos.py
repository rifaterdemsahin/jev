import os
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

def main():
    print("🧠 Starting JEV macOS Native Execution Loop...")
    
    # 1. Connect to local Ollama
    print("🔌 Connecting to Local Apple Silicon Ollama (localhost:11434)...")
    mac_llm = Ollama(model="llama3", base_url="http://localhost:11434")
    mac_embedder = OllamaEmbeddings(model="nomic-embed-text")
    
    # 2. Read this project's README as the target file
    file_path = "README.md"
    print(f"📄 Reading local file: {file_path}")
    with open(file_path, "r") as file:
        raw_document = file.read()
        
    # 3. Action A: Extract Graph Relationships via Llama 3
    print("\n🕸️ [JEV Action A] Extracting Graph Nodes using Apple Silicon...")
    prompt = f"Extract 3 main entities and their relationships from this text. Output ONLY the relationships in this format (Entity A -> Relationship -> Entity B):\n\n{raw_document[:1000]}"
    try:
        graph_nodes = mac_llm.invoke(prompt)
        print("\n--- Extracted Neo4j Relationships ---")
        print(graph_nodes)
        print("-------------------------------------")
    except Exception as e:
        print(f"Error calling LLM: {e}")
        return

    # 4. Action B: Chunk and Vectorize
    print("\n🔪 [JEV Action B] Chunking text...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(raw_document)
    print(f"Created {len(chunks)} chunks.")
    
    print("🔢 Vectorizing text via Nomic-Embed...")
    try:
        vector_embeddings = mac_embedder.embed_documents(chunks[:2]) # Just doing top 2 for speed
        print(f"Successfully generated {len(vector_embeddings)} vector arrays!")
        print(f"Sample Vector Dimension: {len(vector_embeddings[0])} dimensions.")
    except Exception as e:
        print(f"Error generating embeddings: {e}")
        return
        
    print("\n✅ JEV Local Ingestion Example Complete!")

if __name__ == "__main__":
    main()
