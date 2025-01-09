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
label = tk.Label(root, text="Ask a Question")
entry = tk.Entry(root)
reply = tk.Label(root, text="")
#Button Click
def button_click():
    response = getRandomResponse()
    reply.config(text=response)
def getRandomResponse():
    catagory = random.choice([negative_answers, non_committal_answers, affirmative_answers])
    answer = random.choice(catagory)
    return answer
button = tk.Button(root, text="Shake", command=button_click)
#Arrange widgets
label.pack()
entry.pack()
button.pack()
reply.pack()

root.mainloop()