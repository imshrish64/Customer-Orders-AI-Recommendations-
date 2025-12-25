FROM python:3.11.14-alpine

WORKDIR /Projects/customer_orders

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
