from langchain.messages import HumanMessage,SystemMessage,AIMessage


class WorkingMemory:
    def __init__(self) -> None:
        self._messages=[]
    
    def add_user(self,text):
        self._messages.append(HumanMessage(text))

    def add_ai(self,text):
        self._messages.append(AIMessage(text))

    def history(self):
        for i in range(len(self._messages)):
            pass