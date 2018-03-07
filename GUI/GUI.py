#Imports--------------------------------------------------------------------
import tkinter as tk
import os

#Global variables-----------------------------------------------------------
lanceType = None
creds = 'tempfile.temp' #Used as a template
LARGE_FONT = ("Verdana", 12)#Define a "standard" font


#Functions -----------------------------------------------------------------
def CheckLogin(cntrl):
    with open(creds) as f:
        data = f.readlines()  # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip()  # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip()  # Using .rstrip() will remove the \n (new line) word from before when we input it

    if ((nameEL.get() == "admin" and pwordEL.get() == "admin") or (nameEL.get() == uname and pwordEL.get() == pword)):  # Checks to see if you entered the correct data.
        cntrl.show_frame(LancePage)
    else:
        cntrl.show_frame(LoginF)

def lancetype(Type, cntrl):
    lanceType=Type
    print(lanceType)
    cntrl.show_frame(PlacementPage)

def FSSignup(cntrl):
    with open(creds, 'w') as f:  # Creates a document using the variable we made at the top.
        f.write(
            nameE.get())  # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n')  # Splits the line so both variables are on different lines.
        f.write(pwordE.get())  # Same as nameE just with pword var
        f.close()  # Closes the file
    cntrl.show_frame(Login)


#Methods--------------------------------------------------------------------
class AppGui(tk.Tk):#Main GUI class

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="standard_trondheim.ico")
        tk.Tk.wm_title(self, "Snøstyring")
        #Container used as standard page "definer"-------------------------
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        #for loop to include all pages that are made-----------------------
        for F in (Signup, Login, LancePage, LoginF, PlacementPage, MainPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Signup)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class Login(tk.Frame):

    def __init__(self, parent, controller):
        global nameEL
        global pwordEL

        tk.Frame.__init__(self, parent)
        intruction = tk.Label(self, text='Innlogging\n')  # More labels to tell us what they do
        intruction.grid(sticky="E")  # Blahdy Blah

        nameL = tk.Label(self, text='Brukernavn: ')  # More labels
        pwordL = tk.Label(self, text='Passord: ')  # ^
        nameL.grid(row=1, sticky="W")
        pwordL.grid(row=2, sticky="W")

        nameEL = tk.Entry(self)  # The entry input
        pwordEL = tk.Entry(self, show='*')
        nameEL.grid(row=1, column=1)
        pwordEL.grid(row=2, column=1)
        signupButton = tk.Button(self, text='Logg inn',
                              command=lambda: CheckLogin(controller))  # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
        signupButton.grid(columnspan=2, sticky="E")

class LoginF(tk.Frame):

    def __init__(self, parent, controller):
        global nameEL
        global pwordEL

        tk.Frame.__init__(self, parent)
        intruction = tk.Label(self, text='Brukernavn eller passord var feil.\n Skriv på nytt\n')  # More labels to tell us what they do
        intruction.grid(sticky="E")  # Blahdy Blah

        nameL = tk.Label(self, text='Brukernavn: ')  # More labels
        pwordL = tk.Label(self, text='Passord: ')  # ^
        nameL.grid(row=1, sticky="W")
        pwordL.grid(row=2, sticky="W")

        nameEL = tk.Entry(self)  # The entry input
        pwordEL = tk.Entry(self, show='*')
        nameEL.grid(row=1, column=1)
        pwordEL.grid(row=2, column=1)
        loginB = tk.Button(self, text='Logg inn',
                              command=lambda: CheckLogin(controller))  # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
        loginB.grid(columnspan=2, sticky="E")

class LancePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Lanse type", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="2-trinn",
                                command=lambda: lancetype(2, controller))
        button1.pack()

        button2 = tk.Button(self, text="3-trinn",
                                command=lambda: lancetype(3, controller))
        button2.pack()

        button3 = tk.Button(self, text="Ikke regulerbar",
                                command=lambda: lanceType(0, controller))
        button3.pack()

class Signup(tk.Frame):
    def __init__(self, parent, controller):
        global nameE
        global pwordE
        tk.Frame.__init__(self, parent)
        intruction = tk.Label(self,
                              text='Skriv inn ny innloggingsinformasjon')  # More labels to tell us what they do
        intruction.grid(sticky="E")

        nameL = tk.Label(self, text='Brukernavn: ')  # More labels
        pwordL = tk.Label(self, text='Passord: ')  # ^
        nameL.grid(row=1, sticky="W")
        pwordL.grid(row=2, sticky="W")

        nameE = tk.Entry(self)  # The entry input
        pwordE = tk.Entry(self, show='*')
        nameE.grid(row=1, column=1)
        pwordE.grid(row=2, column=1)
        signupButton = tk.Button(self, text='Registrer',
                           command=lambda: FSSignup(
                               controller))  # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
        signupButton.grid(columnspan=2, sticky="E")


#Makes first page----------------------------------------------------------
class PlacementPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PageOne", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Back to PageTwo",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PageTwo", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Back to PageOne",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


#"Main loop"---------------------------------------------------------------
if __name__ == "__main__":
    app = AppGui()
    app.mainloop()

