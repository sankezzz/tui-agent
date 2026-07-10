
class WorkingMemory:
    def __init__(self) -> None:
        self._messages=[]
    
    def add_user(self,text):
        self._messages.append({"role":"user","content":text})

    def add_assistant(self,text):
        self._messages.append({"role":"assistant","content":text})

    def history(self):
        return self._messages
