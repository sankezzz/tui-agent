
class WorkingMemory:
    def __init__(self) -> None:
        self._messages=[]
        self._episode_context=None
    
    def add_user(self,text):
        self._messages.append({"role":"user","content":text})

    def add_assistant(self,text):
        self._messages.append({"role":"assistant","content":text})

    def set_episodic_context(self,previous_history):
        self._episode_context=previous_history

    def history(self):
        if self._episode_context is None:
            return self._messages
        context_message={"role":"system","content":self._episode_context}
        return[context_message,*self._messages]
    
    # def add_history(self,previous_history):
    #     return self._messages.append({"role":"system","content":previous_history})
    # #here it is appending each history that we are getting from the chroma to the current session rather than replacing it which makes the context too heavy to perfrom now we need to make that short too 
