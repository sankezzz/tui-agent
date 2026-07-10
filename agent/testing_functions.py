
from memory_layer.working_memory.working import WorkingMemory
from groq_layer.groq_llm import createEpisodeReflection,chatGroq
from memory_layer.episodic_memory.episode import EpisodicMemory



class TestingIngest:
    def __init__(self) -> None:
        self.memory=WorkingMemory()


    def give_memory_output(self,user_input,previous_history):
        self.memory.add_user(user_input)
        self.memory.add_history(previous_history)
        response=chatGroq(self.memory.history())
        self.memory.add_assistant(response)
        print("Bot Response : ",response)
        print("----------------------------sepertate------------------------------------------------")
        print("memory till now :" ,self.memory.history())

        return self.memory.history()



# we need to create an object so that i can run the fucntions inside the class 
tester=TestingIngest()
episode=EpisodicMemory()

user_input_count=3
while True:
    user=input("give some prompt : ")
    print("getting previous memory -------")
    previous_memory=episode.get_previous_episode(user)
    print("---------------------previous memory---------------------------------")
    print(previous_memory)
    
    if user=="exit":
        print("-------------------------reflection-----------------------------------------------")
        reflection=episode.create_an_episode(history,1)
        print("Reflection saved to db ")
        print("Reflection after saving : ",reflection )
        break

    history=tester.give_memory_output(user_input=user,previous_history=previous_memory)
    

    
