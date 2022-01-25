import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import webbrowser
import time
from datetime import datetime
from tkinter import *
from tkinter import font as tkFont
window=Tk()
window.title('Mable')
window.geometry("3000x1800+10+10")
bg = PhotoImage(file = "mablebackground10.png")
label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)
helv= tkFont.Font(family='Helvetica', size=15, weight='bold')
helv1= tkFont.Font(family='Helvetica', size=13, weight='bold')
helvs= tkFont.Font(family='Helvetica', size=6, weight='bold')
notep=Label(window,text='Your notepad',font=helv,height=4, width=15)
notep.place(x=1200,y=0)
def speak(text):
    friend=pyttsx3.init()
    friend.say(text)
    friend.runAndWait()  
def pronounce():
    speak('What is the word you would want me to pronounce?')
    global ent
    ent=Entry(window,width=30,font=helv1)
    ent.place(x=700,y=250)
    lab=Label(window,text="Enter the word here",font=helv1)
    lab.place(x=700,y=220)
    bt=Button(window,text="Submit",font=helv1,command=pronounce2)
    bt.place(x=700,y=280)
    window.update()
    
def pronounce2():
    i=ent.get()
    speak(i)
def getaudio():
    k=''
    g=0
    count=0
    con=0
    spl=30
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while(g==0):
            if(count==0):
                speak('How can I help you?')
            else:
                speak('How can I help you now?')   
            print('Mable is listening...')
            audio = r.listen(source,phrase_time_limit=5)
            a = r.recognize_google(audio)
            print(a)
            a=a.lower()
            l=len(a)
            b=' '
            if 'how are you' in a:
                speak('I am fine. How about you')
                audio = r.listen(source,phrase_time_limit=3)
                q = r.recognize_google(audio)
                if 'good' in q:
                    b='I am glad to hear that'
            elif 'what is your name' in a:
                speak('I am Mable. What is your name?')
                print('Mable is listening...')
                audio = r.listen(source,phrase_time_limit=3)
                a = r.recognize_google(audio)
                b='Nice to talk to you'+ a
            elif 'what is the full form of ai' in a:
                b='AI means artificial intelligence'
            elif 'bye' in a:
                b='Bye and talk to you later'
                g=1
            elif 'wikipedia' in a:
                a= a.replace("wikipedia", "")
                a= a.replace("search", "")
                speak("I am searching wikipedia")
                result=wikipedia.summary(a,sentences=3)
                wik=Message(window,text=result,font=helv1)
                wik.place(x=1000,y=350)
                window.update()
                speak(result)
            elif 'youtube' in a:
                speak('Opening youtube')
                webbrowser.open("https://www.youtube.com/")
            elif 'open google' in a:
                speak('Opening google')
                webbrowser.open("https://www.google.com/")
            elif 'spell' in a:
                for i in range(5,l):
                    ch=a[i]
                    k=k+ch
                sp=Label(window,text='The spelling is'+k,font=helv1)
                sp.place(x=1200,y=spl*20)
                spl=spl+1
                k=''
                window.update()
                for i in range(5,l):
                    ch=a[i]
                    speak(ch)
            elif 'stop' in a:
                g=1
                b='It was nice speaking to you'
            elif 'wait' in a:
                speak('Waiting')
                time.sleep(8)
            elif 'joke' in a:
                b=pyjokes.get_joke()
            elif 'the time' in a:
                now = datetime.now()
                b = now.strftime("%H:%M:%S")
            elif 'pronounce' in a:
                pronounce()
                return
            elif 'calculator' in a:
                calcu()
                return
            elif "a note" in a:
                speak("What should i write")
                audio = r.listen(source,phrase_time_limit=5)
                q = r.recognize_google(audio)
                con=con+1
            elif "show notes" in a:
                speak("Showing Notes")
                np=Label(window,text=q,font=helv1)
                np.place(x=1200,y=50+con*25)
                window.update()
            else:       
                b='I do not understand'
            speak(b)
            count=count+1
expression = ""
helv= tkFont.Font(family='Helvetica', size=15, weight='bold')
helv1= tkFont.Font(family='Helvetica', size=13, weight='bold')
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)
	
def equalpress():
	try:

		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:

		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")
def calcu():
        if __name__ == "__main__":
                    global equation
                    equation = StringVar()
                    expression_field = Entry(window, textvariable=equation,font=helv)
                    expression_field.grid(columnspan=4, ipadx=70)
                    button1 = Button(window, text=' 1 ', fg='black', bg='blue',font=helv1,command=lambda: press(1), height=4, width=15)
                    button1.grid(row=2, column=0)
                    button2 = Button(window, text=' 2 ', fg='black', bg='blue',font=helv1,command=lambda: press(2), height=4, width=15)
                    button2.grid(row=2, column=1)
                    button3 = Button(window, text=' 3 ', fg='black', bg='blue',font=helv1,command=lambda: press(3), height=4, width=15)
                    button3.grid(row=2, column=2)
                    button4 = Button(window, text=' 4 ', fg='black', bg='blue',font=helv1,command=lambda: press(4), height=4, width=15)
                    button4.grid(row=3, column=0)
                    button5 = Button(window, text=' 5 ', fg='black', bg='blue',font=helv1,command=lambda: press(5), height=4, width=15)
                    button5.grid(row=3, column=1)
                    button6 = Button(window, text=' 6 ', fg='black', bg='blue',font=helv1,command=lambda: press(6), height=4, width=15)
                    button6.grid(row=3, column=2)
                    button7 = Button(window, text=' 7 ', fg='black', bg='blue',font=helv1,command=lambda: press(7), height=4, width=15)
                    button7.grid(row=4, column=0)
                    button8 = Button(window, text=' 8 ', fg='black', bg='blue',font=helv1,command=lambda: press(8), height=4, width=15)
                    button8.grid(row=4, column=1)
                    button9 = Button(window, text=' 9 ', fg='black', bg='blue',font=helv1,command=lambda: press(9), height=4, width=15)
                    button9.grid(row=4, column=2)
                    button0 = Button(window, text=' 0 ', fg='black', bg='blue',font=helv1,command=lambda: press(0), height=4, width=15)
                    button0.grid(row=5, column=0)
                    plus = Button(window, text=' + (PLUS) ', fg='black', bg='green',font=helv1,command=lambda: press("+"), height=4, width=15)
                    plus.grid(row=2, column=3)
                    minus = Button(window, text=' - (MINUS) ', fg='black', bg='green',font=helv1,command=lambda: press("-"), height=4, width=15)
                    minus.grid(row=3, column=3)
                    multiply = Button(window, text=' X (MULTIPLY) ', fg='black', bg='green',font=helv1,command=lambda: press("*"), height=4, width=15)
                    multiply.grid(row=4, column=3)
                    divide = Button(window, text=' / (DIVIDE) ', fg='black', bg='green',font=helv1,command=lambda: press("/"), height=4, width=15)
                    divide.grid(row=5, column=3)
                    equal = Button(window, text=' = (EQUALS TO)', fg='black', bg='orange',font=helv1,command=equalpress, height=4, width=15)
                    equal.grid(row=5, column=2)
                    clear1 = Button(window, text='Clear', fg='black', bg='orange',font=helv1,command=clear, height=4, width=15)
                    clear1.grid(row=5, column='1')
                    Decimal= Button(window, text='.', fg='black', bg='yellow',font=helv1,command=lambda: press('.'), height=4, width=15)
                    Decimal.grid(row=6, column=0)
calc=Button(window, text="Calculator",bg='black',fg='white',command=calcu,font=helv,height=5, width=15)
calc.place(x=800, y=500)
talk=Button(window, text="Talk to Mable",bg='black',fg='white',command=getaudio,font=helv,height=5, width=15)
talk.place(x=600, y=500)
pron=Button(window, text="Pronounce a word",bg='black',fg='white',command=pronounce,font=helv,height=5, width=15)
pron.place(x=700, y=350)
stop1=Button(window, text="Stop",bg='black',fg='red',command=window.destroy,font=helv,height=5, width=15)
stop1.place(x=900, y=0)
window.mainloop()  

