# File structure
# 1. Install Tkinter 
# 2. Initializing window
# 3. Creating functions 
# 4. Creating buttons

from tkinter import *
def Story1(win):
    def final(tl: Toplevel, name, sports, city, playername, drink, breakfast):
        text=f'''
            One day me and  my bestie {name} decided to play a {sports} game in {city}.
            But we weren't able to play. So, we went to watch the game and our favorite player{playername}.
            We drank {drink} and also had some  {breakfast}. We really enjoyed it! We are looking forward to go again and enjoy.
        '''
        
        tl.geometry(newGeometry='500x550')
        
        Label(tl, text="Story:", wraplength=tl.winfo_width()). place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=300)
        
    NewScreen=Toplevel(win, bg="skyblue")
    NewScreen.title("Unforgettable Day")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='Unforgettable Day').place(x=100, y=0)
    
    Label(NewScreen, text='Game Played: ').place(x=0, y=35)
    Label(NewScreen, text='Enter a city:  ').place(x=0, y=70)
    Label(NewScreen, text='Enter the name of a player: ').place(x=0, y=110)
    Label(NewScreen, text='Enter the name of drink').place(x=0, y=150)
    Label(NewScreen, text='Enter the name of a breakfast').place(x=0, y=180)
    
        
    Name=Entry(NewScreen, width=17)
    Name.place(x=250, y=35)
        
    sports=Entry(NewScreen, width=17)
    sports.place(x=250, y=70)
    
    city=Entry(NewScreen, width=17)
    city.place(x=250, y=110)
    
    player=Entry(NewScreen, width=17)
    player.place(x=250, y=150)
    
    drink=Entry(NewScreen, width=17)
    drink.place(x=250, y=190)
    
    breakfast=Entry(NewScreen, width=17)
    breakfast.place(x=250, y=230)
    
    
    submitButton=Button(NewScreen, text="Submit Now! ", background="lightblue", font=('Times', 12), command=lambda:final(NewScreen, Name.get(), sports.get(), city.get(),player.get(),  drink.get(), breakfast.get()))
    submitButton.place(x=10, y=270)
    
    NewScreen.mainloop()

def Story2(win):
    def final(tl: Toplevel, occupation, randomNoun, feeling, emotion , verb):
        text=f'''
        When I was a child, I wanted to become a {occupation}
    but as I grew up I got into the {randomNoun} and decided to becoma an Engineer. Then I went into a job that I was not {feeling} at. 
    After getting {emotion} I decided to do what I love. 
    Despite getting lower {verb} than I used to get in my previous job. I am feeling pleased. 
        
        '''    
        
        tl.geometry('500x570')
        
        Label(tl, text='Story: ', wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)
    NewScreen=Toplevel(win, bg='pink') 
    NewScreen.title("Goals")
    NewScreen.geometry('500x500')
    
    Label(NewScreen, text='Goals').place(x=150, y=0)
    Label(NewScreen, text="Enter a profession: ").place(x=0, y=35)
    Label(NewScreen, text="Enter a random noun: ").place(x=0, y=70)
    Label(NewScreen, text="Enter a feeling: ").place(x=0, y=110)
    Label(NewScreen, text="Enter a emotion: ").place(x=0, y=150)
    Label(NewScreen, text="Enter a verb").place(x=0, y=190)
    
    occupation=Entry(NewScreen, width=17)
    occupation.place(x=250, y=35)
    
    randomNoun=Entry(NewScreen, width=17)
    randomNoun.place(x=250, y=70)
    
    feeling=Entry(NewScreen, width=17)
    feeling.place(x=250, y=110)
    
    emotion=Entry(NewScreen, width=17)
    emotion.place(x=250, y=140)
    
    verb=Entry(NewScreen, width=17)
    verb.place(x=250, y=170)
    
    submitButton= Button(NewScreen, text="Submit", background="skyblue", font=('Times', 12), command=lambda:final(NewScreen, occupation.get(), randomNoun.get(), feeling.get(), emotion.get(), verb.get()))
    submitButton.place(x=150, y=250)

def Story3(win):

    def final():
        text=f"""
One day me and my bestie {name.get()} decided to play {sports.get()} in {city.get()}.
But we couldn't play, so we watched {player.get()}.
We drank {drink.get()} and had {breakfast.get()} for breakfast.
It was an unforgettable day!
"""
        result.config(text=text)

    new = Toplevel(win)
    new.title("Unforgettable Day")

    Label(new, text="Unforgettable Day", font=("Times",16)).grid(row=0,column=0,columnspan=2,pady=10)

    Label(new,text="Friend name").grid(row=1,column=0)
    Label(new,text="Sport").grid(row=2,column=0)
    Label(new,text="City").grid(row=3,column=0)
    Label(new,text="Player").grid(row=4,column=0)
    Label(new,text="Drink").grid(row=5,column=0)
    Label(new,text="Breakfast").grid(row=6,column=0)

    global name,sports,city,player,drink,breakfast

    name=Entry(new)
    sports=Entry(new)
    city=Entry(new)
    player=Entry(new)
    drink=Entry(new)
    breakfast=Entry(new)

    name.grid(row=1,column=1)
    sports.grid(row=2,column=1)
    city.grid(row=3,column=1)
    player.grid(row=4,column=1)
    drink.grid(row=5,column=1)  
    breakfast.grid(row=6,column=1)

    Button(new,text="Generate Story",command=final).grid(row=7,column=0,columnspan=2,pady=10)

    global result
    result=Label(new,text="",wraplength=400)
    result.grid(row=8,column=0,columnspan=2)    

Screen=Tk()
Screen.title("Generate Story and Goals ")
Screen.geometry('400x400')

Screen.config(bg='gray')

Label(Screen, text='Generate Story and Goals').place(x=100, y=20)

Story1Button= Button(Screen, text='Unforgettable Days', font=('Times', 14), command=lambda: Story1(Screen), bg='gray')
Story1Button.place(x=130, y=90) 

story2Button=Button(Screen, text="Goals", font=('Times', 14), command=lambda: Story2(Screen), bg='gray')
story2Button.place(x=160, y=150)

story3Button=Button(Screen, text="Grid: Unforgettable Days", font=('Times', 14), command=lambda: Story3(Screen), bg='gray')
story3Button.place(x=120, y=210)


Screen.update()
Screen.mainloop()
  
        
        







