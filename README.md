Customer Orders & AI Recommendations (POC)
--------------------------------------------------------------------------------------------------------
This project is a FastAPI-based backend service built as a take-home assignment (POC).
It demonstrates clean backend architecture, relational data modeling, async APIs, testing, and AI-powered product recommendations using an LLM.

🚀 Features
-----------------------------------------------------------------------------------------------------------
Manage customers

Manage products

Capture customer purchase history (orders)

Async AI-based product recommendations

Clean separation of concerns (API → Service → Repository → DB / AI)

Deterministic unit tests using pytest

🧰 Tech Stack
-----------------------------------------------------------------------------------------------------------
Python 3.11

FastAPI

SQLAlchemy (SQLite)

LangChain

OpenAI (pluggable, mocked in tests)

Pytest

Docker

📂 Project Structure
----------------------------------------------------------------------------------------------------------
customer_orders/
├── app/

│   ├── api/              # FastAPI routes

│   ├── core/             # DB & config

│   ├── models/           # SQLAlchemy models

│   ├── repositories/     # Data access layer

│   ├── services/         # Business logic

│   ├── ai/               # LLM prompts & chains (LangChain)

│   └── main.py           # Application entry point

│

├── tests/                # Pytest test cases

├── Dockerfile

├── .dockerignore

├── requirements.txt

└── README.md

⚙️ Run Locally
----------------------------------------------------------------------------------------------------------
1️⃣ Create and activate virtual environment

Using conda:

conda create -n custenv python=3.11 -y
conda activate custenv

2️⃣ Install dependencies
-----------------------------------------------------------------------------------------------------------
pip install --no-cache-dir -r requirements.txt

3️⃣ (Optional) Configure LLM API Key
-----------------------------------------------------------------------------------------------------------
If using OpenAI:

export OPENAI_API_KEY="your_api_key_here"

The project also supports mocked LLM logic for testing and local development.

4️⃣ Run the application
-----------------------------------------------------------------------------------------------------------
uvicorn app.main:app --reload

5️⃣ Open API documentation
-----------------------------------------------------------------------------------------------------------
http://127.0.0.1:8000/docs

🧪 Run Tests
-----------------------------------------------------------------------------------------------------------

All tests are local and deterministic.

PYTHONPATH=. pytest -v

Expected output:

6 passed in X.XXs

🔁 Suggested API Flow (Manual Testing)
----------------------------------------------------------------------------------------------------------

GET /customers → should return []

POST /customers → create a customer

POST /products → create products

POST /orders → create orders for the customer

POST /customers/{id}/recommendations → get AI recommendations

🤖 AI Recommendation Design
----------------------------------------------------------------------------------------------------------

Uses the last 5 purchased products of a customer

Prompt enforces strict JSON output

LangChain handles prompt + model + parsing

LLM provider is pluggable (OpenAI / Mock)

The recommendation endpoint is implemented as async.


🐳 Run with Docker
----------------------------------------------------------------------------------------------------------

This project can also be run fully containerized using Docker.

### Build the Docker image
--------------------------------------------------------------------------------------------------------

docker build -t customer-orders .

###Run the container
---------------------------------------------------------------------------------------------------------

docker run -p 8000:8000 customer-orders

Access the API
--------------------------------------------------------------------------------------------------------

Swagger UI: http://localhost:8000/docs



🧠 Summary
----------------------------------------------------------------------------------------------------------

This project demonstrates:

Clean backend architecture

Proper REST semantics

Async AI integration

Practical GenAI usage

Testing discipline

Thoughtful trade-offs for a POC

👤 Author
----------------------------------------------------------------------------------------------------------

Shrish Dubey

AI Engineer


