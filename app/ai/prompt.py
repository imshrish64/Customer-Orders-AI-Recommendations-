from langchain_core.prompts import ChatPromptTemplate

recommendation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a product recommendation engine. "
            "You analyze purchase history and suggest relevant next products. "
            "Return ONLY valid JSON."
        ),
        (
            "human",
            """
Customer recently bought these products:
{purchase_history}

Based on this history:
- infer customer interests
- suggest 3 realistic products they may buy next

Return JSON strictly in this format:
{{
  "recommendations": [
    {{
      "product_name": "...",
      "category": "...",
      "reason": "..."
    }}
  ]
}}
"""
        ),
    ]
)
