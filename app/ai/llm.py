import json
from typing import Any, List, Optional

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from langchain_openai import ChatOpenAI

from app.core.config import settings


class MockLLM(BaseChatModel):
    """
    LangChain-compatible mock chat model.
    """

    def _generate(
        self,
        messages: List[Any],
        stop: Optional[List[str]] = None,
        run_manager: Optional[Any] = None,
    ) -> ChatResult:
        """
        Must return ChatResult with generations.
        """

        # Read purchase history from prompt (real data!)
        last_message = messages[-1].content.lower()

        if "electronics" in last_message:
            recommendations = [
                {
                    "product_name": "Laptop Stand",
                    "category": "Accessories",
                    "reason": "Improves ergonomics for laptop users"
                },
                {
                    "product_name": "Wireless Keyboard",
                    "category": "Electronics",
                    "reason": "Commonly paired with laptops"
                }
            ]
        else:
            recommendations = [
                {
                    "product_name": "Gift Card",
                    "category": "General",
                    "reason": "Popular across all customers"
                }
            ]

        content = json.dumps(
            {"recommendations": recommendations},
            ensure_ascii=False
        )

        message = AIMessage(content=content)

        generation = ChatGeneration(message=message)

        return ChatResult(generations=[generation])

    @property
    def _llm_type(self) -> str:
        return "mock-chat-model"


def get_llm() -> BaseChatModel:
    if settings.USE_REAL_LLM:
        return ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model=settings.OPENAI_MODEL,
            temperature=0.3,
        )

    return MockLLM()
