import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.validation import add_regex_validation

class Gradebook(ttk.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.name = ttk.StringVar(value="")
        self.student_id = ttk.StringVar(value="")
        self.course_name = ttk.StringVar(value="")
        self.final_score = ttk.StringVar(value="")
        self.data = []
        self.colors = master_window.style.colors
# Create text/numerical inputs
def create_form_entry(self, label, variable):
    return

 # Create meter   
def create_meter(self):
    return

#create buttons
def create_buttonbox(self):
        return

# Action when user clicks submit button
def on_submit(self):
    return



if __name__ == "__main__":
    app = ttk.Window("Gradebook", "superhero", resizable=(False, False))
    Gradebook(app)
    app.mainloop()
