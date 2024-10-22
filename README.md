# Chatbot Powered by Retrieval-Augmented Generation and Knowledge Management

This project develops a chatbot utilizing Retrieval-Augmented Generation (RAG) with integrated knowledge management features. The backend is built with FastAPI, using OpenAI's GPT model for text generation, while PostgreSQL with pgvector enables efficient vector storage.

## Features

- Upload and process knowledge documents (PDF and text formats)
- Embed and store segments of knowledge
- Create and manage chat interactions
- Retrieve relevant knowledge and past conversations to generate contextually aware responses
- Monitor token usage across various operations

## Prerequisites

- Python 3.8+
- Postgresql with pgvector
- OpenAI API key

## Installation

1. Clone the repository:
  ```
  git clone https://github.com/Ah-Riz/-ws-gpt_rag.git
  cd -ws-gpt_rag
  ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   In the project root, create a .env file and include the following settings:
   ```
   PG_dbname = "your_postgres_db_name"
   PG_user = "your_postgres_user"
   PG_pw = "your_postgres_password"
   PG_host = "your_postgres_host"
   PG_port = "your_postgres_port"
   PG_new_dbname = "your_postgres_new_db_name"
   OPENAI_KEY = "your_openai_api_key"
   CHATBOT_NAME = "your_chatbot_name"
   CHATBOT_PREPROMT = "your_chatbot_system_message"
   CHUNK_SIZE=200
   OVERLAP_SIZE=20
   TOP_K=5
   TOP_K_HISTORY=2
   ```

4. Set up the PostgreSQL database:
   - Ensure PostgreSQL is installed and running
   - Run the `init_db.py` script to create the database and set up the vector extensions:
     ```
     python init_db.py
     ```

## Usage

1. Start the FastAPI server:
```
uvicorn main:app --reload
```

2. Use the following endpoints:
- **POST /upload-knowledge/**: Upload a PDF or text file to incorporate into the knowledge base.
- **POST /newchat/**: Initiate a new chat session.
- **POST /chat/**: Send a message within an active chat session.
- **GET /token_usage/**: Fetch statistics on token consumption.

## Code Structure 
- **main.py**: The FastAPI application containing the core logic.
- **vector_store.py**: The `VectorStore` class handling database interactions.
- **init_db.py**: Script for initializing the database.
