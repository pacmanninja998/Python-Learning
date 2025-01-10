import tkinter as tk
import random
affirmative_answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good", 
    "Yes",
    "Signs point to yes"
]
non_committal_answers = [
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again"
]
negative_answers = [
    "Don't count on it",
    "My reply is no", 
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

#Create Main Window
root = tk.Tk()
root.title("Magic 8 Ball")

#Create Widgets
label = tk.Label(root, text="Ask a Question: ")
entry = tk.Entry(root)
reply = tk.Label(root, text="", height=3)

#Button Click
def shake_click():
    response = getRandomResponse()
    reply.config(text=response)
def getRandomResponse():
    catagory = random.choice([negative_answers, non_committal_answers, affirmative_answers])
    answer = random.choice(catagory)
    return answer
def clear_click():
    entry.delete(0, tk.END)
    reply.config(text="")
def quit_click():
    root.destroy()
shake = tk.Button(root, text="Shake", command=shake_click, width=12)
clear = tk.Button(root, text="Reset", command=clear_click, width=12)
again = tk.Button(root, text="Play Again", command=clear_click, width=12)
quit_button = tk.Button(root, text="Quit", command=quit_click, width=12)
#Arrange widgets
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
reply.grid(row=1, column=0, columnspan=2)
shake.grid(row=2, column=0)
clear.grid(row=2, column=1)
again.grid(row=3, column=0)
quit_button.grid(row=3, column=1)
#Keep window Open
root.mainloop()