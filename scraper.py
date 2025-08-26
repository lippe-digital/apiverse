import json

def fetch_tools():
    return [
        {
            "name": "OpenAI GPT",
            "category": "NLP",
            "api_available": True,
            "url": "https://platform.openai.com/",
            "free_tier": True,
            "features": ["Text generation", "Chat", "Embeddings"],
        },
        {
            "name": "Stability AI",
            "category": "Image",
            "api_available": True,
            "url": "https://platform.stability.ai/",
            "free_tier": True,
            "features": ["Image generation", "Upscaling"],
        }
    ]

if __name__ == "__main__":
    tools = {"ai_tools": fetch_tools()}
    with open("ai_tools.json", "w") as f:
        json.dump(tools, f, indent=2)
    print("ai_tools.json updated")
