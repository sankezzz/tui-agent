from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Input, ListView, ListItem, Label

class MyApp(App):

    def on_mount(self): #compose runs only once -- on mount is conventional setup app memory 
        self.history=[]


    def compose(self) -> ComposeResult: #compose give us what to show on the terminal -- runs exaclty once 
        yield Label("Hello, terminal!")# INSTED OF RETURN IT GIVES YEILD , label is the simplest widget
        new_input=Input(placeholder="Please enter something that you wnat ")
        yield new_input
        yield Label("…waiting for you", id="output")

    
    def on_input_submitted(self,event:Input.Submitted)->None:
        self.history.append(event.value)
        all_lines="\n".join(self.history)
        self.query_one("#output",Label).update(f'You typed this shit :{all_lines}')
        event.input.value="" #clears up the terminal 


MyApp().run() # this is actually a while true loop itself 