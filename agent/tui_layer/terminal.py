from textual.app import App, ComposeResult
from textual.widgets import Input, ListView, ListItem, Label , Markdown
from memory_layer.working_memory.working import WorkingMemory
from groq_layer.groq_llm import chatGroq


class MyApp(App):
    CSS="""
    Screen {
    align: center middle;
}

ListView {
    width: auto;
    height: auto;
    margin: 2 2;
}

Label {
    padding: 1 2;
}
"""

    # BINDINGS=[("d","delete","delete a highlighted task"),("e","edit","edits a given todo")] #(key, action_name , here delete and the fucntion name is action_delete so it fires when pressed d , description)

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Place your prompt in this and get your output ",id="title")
        yield ListView()                       # empty list at startup
        

    def on_input_submitted(self, event: Input.Submitted) -> None:            
        text = event.value.strip()
        groq_thinking="Qwen is thinking .............. "
        new_row = ListItem(Label(groq_thinking))        # build one row
        self.query_one(ListView).append(new_row)
        
        groq_fail="groq did not respond "
        if not text:                           # ignore empty Enters
            return
        response=chatGroq(text)
        if not response:
            new_row = ListItem(Label(groq_fail))        # build one row
            self.query_one(ListView).append(new_row)
            return   # add it to the screen, live
        #now how do i put this thing into markdown 
        # new_row = ListItem(Label(response))  
        new_row=ListItem(Markdown(response)    )  # build one row
        self.query_one(ListView).append(new_row)   # add it to the screen, liv 
        event.input.value = ""



