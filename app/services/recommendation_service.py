from app.ai.chains import recommendation_chain

async def generate_recommendations(purchased_products: list[dict]):
    result = await recommendation_chain.ainvoke(
        {
            "purchase_history": purchased_products
        }
    )
    return result.recommendations
