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

├── scripts/

    └── seed.py          # Script to seed DB with sample data
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

4️⃣ Start the FastAPI application (IMPORTANT)
-----------------------------------------------------------------------------------------------------------

You must start the FastAPI app at least once so that:

The SQLite database is created

Tables are initialized via SQLAlchemy

'''bash 

uvicorn app.main:app --reload

Wait until you see:

Application startup complete.

You can now stop the server (CTRL+C).

🌱 Seed the Database with Sample Data.
---------------------------------------------------------------------------------------------------------

After the app has been started once, run the seed script to populate the database with sample customers, products, and orders.

From the project root:

'''bash 

PYTHONPATH=. python scripts/seed.py

This will:

Insert sample customers

Insert sample products

Insert sample orders (purchase history)

✅ This step is required to test recommendations with real data.

5️⃣ Restart the application
---------------------------------------------------------------------------------------------------------

uvicorn app.main:app --reload

6️⃣ Open API documentation
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


Note
-------------------------------------------------------------------------------------------------
I have used GPT for vibe coding and do the assignment within the respective time.
If you want me to explain the production-grade implementation I can do I have done in our previous projects, like 
how to integrate ServiceNow and zendesk api here and get the data from them and offer the service to customers.
For any clarification, please reach out to me.Logs have not been added They can be added if you want.


