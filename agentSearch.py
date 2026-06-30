import dotenv
import os
from dotenv import load_dotenv
import json
from tavily import TavilyClient

load_dotenv()

search_key=os.getenv("TAVILY_API_KEY")


tavily_client = TavilyClient(api_key=search_key)
response = tavily_client.search("What is PRICE OF STOCK - TTWO ")

path='response.json'

with open(path,"w",encoding="utf-8") as file:
    json.dump(response,file,indent=4)

print(response)