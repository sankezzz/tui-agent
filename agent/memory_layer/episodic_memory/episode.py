from groq_layer.groq_llm import chatGroq,createEpisodeReflection
import chromadb
import uuid
import os
from dotenv import load_dotenv
load_dotenv()

client = chromadb.CloudClient(
  api_key=os.getenv("CHROMA_API"),
  tenant='d203d676-491c-4155-a116-ac2a54b33abd',
  database='tui-memory'
)

collection = client.get_collection("episodic-memory")
# here i need to add a try catch with all the nessecary things like connection err and other things     


class EpisodicMemory:

    def create_an_episode(self,current_chat_history,convo_id):
        reflection=createEpisodeReflection(current_chat_history)
        self.save_episode(
            convo_id=convo_id,
            current_chat_history=current_chat_history,
            conversation_summary=reflection["conversation_summary"],
            what_to_avoid=reflection["what_to_avoid"],
            what_worked=reflection["what_worked"],
            context_tags=reflection["context_tags"]
        )
        return reflection
        
        
    def save_episode(self,current_chat_history,conversation_summary,what_worked,what_to_avoid,context_tags,convo_id):
        document = (
                f"{conversation_summary}\n"
                f"{what_worked}\n"
                f"{what_to_avoid}\n"
                f"{' '.join(context_tags)}"
            )

        collection.add(
            ids=[str(uuid.uuid4())],
            documents=[document],
            metadatas=[{
                "conversation_id":convo_id,
                "summary":conversation_summary,
                "conversation_tags":context_tags,
                "what_worked":what_worked,
                "what_did_not_work":what_to_avoid
            }]
        )

    def get_previous_episode(self,current_query):
        results=collection.query(
            query_texts=[current_query],
            n_results=2
        )
        return results
