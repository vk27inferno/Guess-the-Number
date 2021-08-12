class GuessNumber:
    font = ("Comic Sans MS", 15, "bold")
    title = "Guess the Number!"
    ask = "Guess a number between {} and {}: "
    
    def __init__(self, minNum = 0, maxNum = 1000, tries = 10):
        self.min = minNum
        self.max = maxNum
        self.retries = tries
        self.reset()

    def reset(self):
        self.tries = self.retries
        from random import randint
        self.num = randint(self.min, self.max)

    def play(self):

        def askReplay():
            self.bind = window.bind('<Return>', lambda event: replay())
            window.bind('<Key>', lambda event: window.destroy())

        def replay():
            self.reset()
            logLabel['text'] = ''
            triesLabel['text'] = "{} Oops left.".format(self.tries)
            window.unbind('<Key>')
            window.bind('<Return>', process)

        def isValid(string):
            try:
                string = eval(string)
                return True
            except:
                return False

        def inRange(num):
            if num >= self.min and num <= self.max:
                return True

        def updateTries():
            self.tries -= 1
            triesLabel['text'] = "{} Oops left.".format(self.tries)

        def log(state):
            if state == 'no tries':
                logLabel['text'] = "You ran out of tries.\nEnter to Replay; Any Key to exit."
            elif state == 'invalid':
                logLabel['text'] = "Enter only a number."
            elif state == 'outOfDomain':
                logLabel['text'] = "It's out of range."
            elif state == 'match':
                logLabel['text'] = "You guessed it.\nEnter to Replay; Any Key to exit."
            elif state == 'too low':
                logLabel['text'] = "Too low..."
            elif state == 'low':
                logLabel['text'] = "Low."
            elif state == 'low close':
                logLabel['text'] = "A bit lower."
            elif state == 'too high':
                logLabel['text'] = "Too high..."
            elif state == 'high':
                logLabel['text'] = "High."
            elif state == 'high close':
                logLabel['text'] = "A bit higher."

        def process(event):
            user = enter.get().strip()
            if isValid(user):
                user = float(eval(user))
                if inRange(user):
                    if user == self.num:
                        log('match')
                        askReplay()
                    elif user < self.num:
                        if user < self.num - (self.max - self.min) * 0.22:
                            log('too low')
                        elif user < self.num - (self.max - self.min) * 0.05:
                            log('low')
                        else:
                            log('low close')
                        updateTries()
                    else:
                        if user > self.num + (self.max - self.min) * 0.3:
                            log('too high')
                        elif user > self.num + (self.max - self.min) * 0.05:
                            log('high')
                        else:
                            log('high close')
                        updateTries()
                else:
                    log('outOfDomain')
            else:
                log('invalid')

            enter.delete(0, 'end')

            if self.tries == 0:
                log('no tries')
                askReplay()

        def changeTheme():
            if themeButton['text'] == 'Dark':
                themeButton['text'] = 'Light'
                bg = 'white'
                fg = 'black'
            else:
                themeButton['text'] = 'Dark'
                bg = 'black'
                fg = 'white'
                
            window.config(bg = bg)
            enter['insertbackground'] = fg
            for i in [frame1, frame2]:
                i['bg'] = bg
            for i in [askLabel, themeButton, enter, triesLabel, logLabel]:
                i['bg'] = bg
                i['fg'] = fg

        ## GUI Design
        from tkinter import Tk, Label, Entry, Frame, Button

        # Main Window
        window = Tk()
        window.title(self.title)
        window.geometry("600x150")

        frame1 = Frame(master = window)
        frame1.pack(fill = 'x')
        askLabel = Label(master = frame1, font = self.font, text = self.ask.format(self.min, self.max))
        askLabel.pack()
        themeButton = Button(master = frame1, font = ("Comic Sans MS", 10), text = 'Light' , command = changeTheme)
        themeButton.pack(side = 'right')
        frame2 = Frame(master = window)
        frame2.pack()
        enter = Entry(master = frame2, font = self.font, width = 5)
        enter.focus_set()
        enter.pack(side = 'left')
        triesLabel = Label(master = frame2, font = self.font, text = "   {} Oops left.".format(self.tries))
        triesLabel.pack(side = 'left')
        logLabel = Label(master = window, font = self.font)
        logLabel.pack()

        # MainLoop, Theme & Event Handlers
        changeTheme()
        window.bind('<Return>', process)
        window.mainloop()

game = GuessNumber()
game.play()
