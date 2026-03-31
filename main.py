import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
 
load_dotenv()
 
# Endpoint van je Azure OpenAI resource
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
 
if not endpoint or not api_version or not deployment:
    raise RuntimeError("Azure OpenAI env-variabelen ontbreken.")
 
# Azure AD token provider
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)
 
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_version=api_version,
    azure_ad_token_provider=token_provider,
)
 
resp = client.chat.completions.create(
    model=deployment,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Zeg op een vrlijke manier de connectie met de LLM werkt"},
    ],
    max_tokens=50,
)
 
print(resp.choices[0].message.content)
 
 