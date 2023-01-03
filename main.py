import tkinter as tk

import import_data
import get_message

def get_text(input_text):
    # some code here to process the input text and generate output
    return import_data.get_text(input_text)

# def submit_new_display(input_text, responses, tag):
#     import_data.add_response(input_text, responses, tag, import_data.data)
#     output_label.configure(text="BOT: " + responses)
#     new_display.destroy()

# def create_new_display(input_text):
#     # some code here to create a new display
#     global new_display  # add this line to define new_display as a global variable
#     new_display = tk.Toplevel(root)
#     new_display.title("edit data")
#     new_display.geometry("720x480")
    
    
#     # create 2 Entry widget to accept the input text
#     responses_label = tk.Label(new_display, text="Responses:")
#     responses_label.pack()
#     responses_entry = tk.Entry(new_display)
#     responses_entry.pack()
    
#     tag_label = tk.Label(new_display, text="Tag:")
#     tag_label.pack()
#     tag_entry = tk.Entry(new_display)
#     tag_entry.pack()
    
#     submit_button = tk.Button(new_display, text="Submit", command=lambda: submit_new_display(input_text, responses_entry.get(), tag_entry.get()))
#     submit_button.pack()
    
        
def submit():
    input_text = input_entry.get() # get the input text from the Entry widget
    output_text = get_text(input_text) # get the output text from the get_text function
    # if output_text == "NULL":
    #     create_new_display(input_text)
    # else:
    #     output_label.configure(text="BOT: " + output_text)
        
# create the main window
root = tk.Tk()
root.title("Input Output Example")
root.geometry("720x480")
# create a Label widget to display the input text
input_label = tk.Label(root, text="Input:")
input_label.pack()

# create an Entry widget to accept the input text
input_entry = tk.Entry(root)
input_entry.pack()

# create a Button widget to submit the input text
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# create a Label widget to display the output text
output_label = tk.Label(root, text="Output:")
output_label.pack()

# start the event loop
root.mainloop()
