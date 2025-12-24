from langchain_core.output_parsers import PydanticOutputParser
from app.ai.schemas import RecommendationOutput
from app.ai.prompt import recommendation_prompt
from app.ai.llm import get_llm

# Output parser enforces structured response
parser = PydanticOutputParser(
    pydantic_object=RecommendationOutput
)

# Get LLM (mock or real)
llm = get_llm()

# LangChain pipeline
recommendation_chain = (
    recommendation_prompt
    | llm
    | parser
)
