from tui_layer.terminal import MyApp
from dotenv import load_dotenv
import os

load_dotenv()

import chromadb

# client = chromadb.CloudClient(
#   api_key=os.getenv("CHROMA_API"),
#   tenant='d203d676-491c-4155-a116-ac2a54b33abd',
#   database='tui-memory'
# )

MyApp().run()

