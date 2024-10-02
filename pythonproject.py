#PYTHON PROJECT.
#MORSE CODE TRANSLATOR

from tkinter import *

#sound
def sound(mor):
    #sound
    import pygame
    pygame.init()
    dot= pygame.mixer.Sound('/Users/nafeess/Documents/dot.wav')
    dash = pygame.mixer.Sound('/Users/nafeess/Documents/dash.wav')
    
    #loop time
    import time
    for i in range(0,len(mor)):
        for j in mor[i]:
            if j=='.':
                dot.play()
                time.sleep(0.18)
            elif j=='-':
                dash.play()
                time.sleep(0.18)
            elif j==' ':
                time.sleep(0.3)
            elif j=='/':
                time.sleep(0.4)
    pygame.quit()

#text to morse  
def ttm(text):
    #morse code
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
        '-': '-....-', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
        '=': '-...-', '+': '.-.-.', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '!': '-.-.--',
        '@': '.--.-.', ' ': '/'
    }

    #morse code function
    #creating the list====
    morse=[]
    string=list(text.upper())
    #printing the morse code
    for char in string:
        if char in MORSE_CODE_DICT:
            print(MORSE_CODE_DICT[char],end=' ')
            morse.append(MORSE_CODE_DICT[char])
        else:
            print('?',end=' ')

    #converting the list to string
    mor=' '.join(morse)

    return mor

#OUTPUT SCREEN
def convert():
    Owin=Tk()
    Owin.geometry("600x450+500+300")
    Owin.title("Morse Code Translator")
    Owin.configure(bg="#8DAED0")
    label1=Label(Owin,bg="#8DAED0",fg="BLACK",font=('Chalkboard',30),text="Your Morse Code Is:")
    label1.place(relx=0.5,rely=0.2,anchor= CENTER)
    entry=textentry.get()
    label2=Label(Owin,bg="#8DAED0",fg="BLACK",font=('Chalkboard',30),text=ttm(entry))
    label2.place(relx=0.5,rely=0.6,anchor= CENTER)
    sbutton=Button(Owin,bg="#3B6693",fg="BLACK",text="Sound",command=lambda:sound(ttm(entry)))
    sbutton.place(relx=0.5,rely=0.7,anchor= CENTER)
    Owin.mainloop()


#INPUT SCREEN
Fwin=Tk()
Fwin.geometry("600x450+500+300")
Fwin.title("Morse Code Translator")
Fwin.configure(bg="#A7C7E7")
enterlabel=Label(Fwin,bg="#A7C7E7",fg="#3A4959",font=('Chalkboard',30),text="ENTER TEXT")
enterlabel.place(relx=0.5,rely=0.2,anchor= CENTER)
textentry= Entry(Fwin,bg="#8DAED0",fg="WHITE",font=('Chalkboard',30))
textentry.place(relx=0.5,rely=0.4,anchor= CENTER)
entry=textentry.get()
conbutton=Button(Fwin,bg="#3B6693",fg="BLACK",text="CONVERT",command= convert)
conbutton.place(relx=0.5,rely=0.6,anchor=CENTER)
    
Fwin.mainloop()


