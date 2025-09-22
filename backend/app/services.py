from langchain_ollama import  OllamaLLM


def generate_content(prompt: str, platform: str, tone:str, content_type:str) -> str:

    full_prompt = f"""
    Generate a {content_type} for {platform} in a {tone} tone. The user's prompt is: {prompt}
    """
    llm = OllamaLLM(model="llama3:latest", temperature=0.4, top_k=5,base_url="http://host.docker.internal:11434")

    response = llm.invoke(full_prompt)

    return response