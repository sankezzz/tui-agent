from textual.app import App, ComposeResult
from textual.widgets import Input, ListView, ListItem, Label , Markdown
from memory_layer.working_memory.working import WorkingMemory
from memory_layer.episodic_memory.episode import EpisodicMemory
from textual import work 
import uuid 
from groq_layer.groq_llm import chatGroq



class MyApp(App):
    CSS="""
   Screen {
    layout: vertical;
}

ListView {
    height: 3fr;
    width: 100%;
}

Input {
    dock: bottom;
}

"""

    def on_mount(self):
        self.memory=WorkingMemory()
        self.episode=EpisodicMemory()
        self.convo_id=str(uuid.uuid4())

    # BINDINGS=[("d","delete","delete a highlighted task"),("e","edit","edits a given todo")] #(key, action_name , here delete and the fucntion name is action_delete so it fires when pressed d , description)

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Place your prompt in this and get your output ",id="title")
        yield ListView()                       # empty list at startup
        
    

    def show_result(self, thinking_row: ListItem, content: str, is_error: bool) -> None:
        if is_error:
            thinking_row.query_one(Label).update(content)
        else:
            thinking_row.remove()
            self.query_one(ListView).append(ListItem(Markdown(content)))


    @work(thread=True)
    def get_bot_response(self,text:str,thinking_row:ListItem,exclusive=True )-> None:
        previous_memory=self.episode.get_previous_episode(text)
        self.memory.add_user(text=text)
        self.memory.set_episodic_context(previous_history=previous_memory)

        response=chatGroq(self.memory.history())

        if not response:
            self.call_from_thread(self.show_result,thinking_row,"Groq failed to respond",is_error=True)
            return 
        
        self.memory.add_assistant(response)
        self.call_from_thread(self.show_result,thinking_row,response,is_error=False)




    async def action_quit(self) -> None:
        self.episode.create_an_episode(self.memory.history(), self.convo_id)
        self.exit()




    def on_input_submitted(self, event: Input.Submitted) -> None: 

        text = event.value.strip()
        if not text:                           # ignore empty Enters
            return
        event.input.value = ""

        user_query=ListItem(Label(text))
        thinking_row=ListItem(Label("Qwen is thinking ... "))
        self.query_one(ListView).append(user_query)
        self.query_one(ListView).append(thinking_row)
        self.query_one(ListView).scroll_end(animate=True)


        self.get_bot_response(text,thinking_row)

        


