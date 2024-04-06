import random
from tkinter import *
from tkinter import messagebox

#Building the window
FONT_SIZE = 20
gui = Tk()
gui.title('Letter Guesser')
gui.geometry('400x250')

#Defining what happens when guess button pressed
def on_Guess():
    guess = string_pass.get()
    lettersU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    guessMe = "".join(random.sample(lettersU,1))
    
    messagebox.showinfo('Result', 'You guessed {} \nThe answer was {}'.format(guess, guessMe))
    
#Building the buttons and labels
string_pass = StringVar()
label = Label(text="Guess a Letter", font=("Arial",FONT_SIZE)).pack(pady=20)
guessBox = Entry(textvariable=string_pass,font=('Arial',FONT_SIZE)).pack(pady=10)
guessButton = Button(text="Guess!", command=on_Guess,font=('Arial',FONT_SIZE)).pack(pady=10)


#main process
gui.mainloop()


