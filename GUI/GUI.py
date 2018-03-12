# Imports---------------------------------------------------------------------------------------------------------------
import tkinter as tk


# Global variables------------------------------------------------------------------------------------------------------
lanceType = None
placement = None
creds = 'tempfile.temp'  # Variable that becomes login data document
large_font = ("Verdana", 12)  # Used to store font type

# Functions ------------------------------------------------------------------------------------------------------------

def CheckLogin(cntrl, nameEL, pwordEL):  # Used to check if username and password is correct.
    with open(creds) as f:
        data = f.readlines()  # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip()  # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip()  # Using .rstrip() will remove the \n (new line) word from before when we input it

    if ((nameEL.get() == "admin" and pwordEL.get() == "admin") or
            (nameEL.get() == uname and pwordEL.get() == pword)):  # Checks to see if you entered the correct data.

        cntrl.show_frame(SnTypePage)
    else:
        cntrl.show_frame(LoginF)


def CheckReLogin(cntrl, nameEL, pwordEL):#  Used to check if username and password is correct.
    with open(creds) as f:
        data = f.readlines()  # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip()  # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip()  # Using .rstrip() will remove the \n (new line) word from before when we input it

    if ((nameEL.get() == "admin" and pwordEL.get() == "admin") or
            (nameEL.get() == uname and pwordEL.get() == pword)):  # Checks to see if you entered the correct data.
        cntrl.show_frame(Home)
    else:
        cntrl.show_frame(LoginF)


def lancetype(Type, cntrl):  #  Used to change value of global variable, and change GUI window
    global lanceType
    lanceType = Type
    print('har oppdatert type til: ' + str(lanceType))  #  Used to check if value of lanceType is changed
    cntrl.show_frame(PlacementPage)  # Changes GUI window to PlacementPage
    return lanceType


def Place(place, cntrl):  # Used to change value of global variable, and change GUI window
    global placement
    placement = place
    print('lansen er plassert: '+ str(placement))
    cntrl.show_frame(Home)  # Changes GUI window to Home
    return placement


def FSSignup(cntrl):#  Used to add a user to the GUI. So far only one user can be added.
    with open(creds, 'w') as f:  # Creates a document using the variable we made at the top.
        f.write(nameE.get())           # nameE is the variable we were storing the input to.
                                       # Tkinter makes us use .get() to get the actual string.
        f.write('\n')  # Splits the line so both variables are on different lines.
        f.write(pwordE.get())  # Same as nameE just with pword var
        f.close()  # Closes the file
    cntrl.show_frame(Login)


#  Classes--------------------------------------------------------------------------------------------------------------
class AppGui(tk.Tk):  # Main GUI class

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="standard_trondheim.ico")  # Sets GUI icon
        tk.Tk.wm_title(self, "Snøstyring")  # Sets GUI title

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)  # Define window
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Signup, Login, SnTypePage, LoginF, PlacementPage, Home):  # Includes all pages

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Login(tk.Frame):  # Login page

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        intruction = tk.Label(self, text='Innlogging\n')
        intruction.grid()

        nameL = tk.Label(self, text='Brukernavn: ')
        pwordL = tk.Label(self, text='Passord: ')
        nameL.grid(row=1, sticky="W")
        pwordL.grid(row=2, column=0, sticky="E")

        nameEL = tk.Entry(self)
        pwordEL = tk.Entry(self, show='*')
        nameEL.grid(row=1, column=1)
        pwordEL.grid(row=2, column=1)

        loginB = tk.Button(self, text='Logg inn',
                              command=lambda: CheckLogin(controller, nameEL, pwordEL))
        loginB.grid(columnspan=2, sticky="E")


class ReLogin(tk.Frame):  # Login page

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        intruction = tk.Label(self, text='Innlogging\n')
        intruction.grid(sticky="E")

        nameL = tk.Label(self, text='Brukernavn: ')
        pwordL = tk.Label(self, text='Passord: ')
        nameL.grid(row=1, sticky="W")
        pwordL.grid(row=2, sticky="W")

        nameEL = tk.Entry(self)
        pwordEL = tk.Entry(self, show='*')
        nameEL.grid(row=1, column=1)
        pwordEL.grid(row=2, column=1)

        loginB = tk.Button(self, text='Logg inn',
                              command=lambda: CheckReLogin(controller, nameEL, pwordEL))
        loginB.grid(columnspan=2, sticky="E")


class LoginF(tk.Frame): # Login failed page

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        intruction = tk.Label(self, text='Brukernavn eller passord var feil.\n Skriv på nytt\n')
        intruction.grid(sticky="E")  # Grid label

        nameL = tk.Label(self, text = 'Brukernavn: ')
        pwordL = tk.Label(self, text = 'Passord: ')
        nameL.grid(row=1, sticky="W")
        pwordL.grid(row=2, sticky="W")

        nameEL = tk.Entry(self)
        pwordEL = tk.Entry(self, show='*')
        nameEL.grid(row=1, column=1)
        pwordEL.grid(row=2, column=1)

        loginB = tk.Button(self, text='Logg inn',
                              command=lambda: CheckLogin(controller, nameEL, pwordEL))
        loginB.grid(columnspan=2, sticky="E")


class SnTypePage(tk.Frame): # Snowgun type page
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Lanse type", font=large_font)
        label.grid(sticky="N")

        button0 = tk.Button(self, text="Ikke regulerbar",
                            command=lambda: lancetype(0, controller))
        button0.grid(row=1, sticky="W")

        button1 = tk.Button(self, text="2-trinn",
                                command=lambda: lancetype(2, controller))
        button1.grid(row=2, sticky="W")

        button2 = tk.Button(self, text="3-trinn",
                                command=lambda: lancetype(3, controller))
        button2.grid(row=3,sticky="W")


class Signup(tk.Frame): # Signup page
    def __init__(self, parent, controller):
        global nameE
        global pwordE

        tk.Frame.__init__(self, parent)

        intruction = tk.Label(self,
                              text='Skriv inn ny innloggingsinformasjon')
        intruction.grid(sticky="E")

        nameL = tk.Label(self, text='Brukernavn: ')
        pwordL = tk.Label(self, text='Passord: ')
        nameL.grid(row=1, sticky="W")
        pwordL.grid(row=2, sticky="W")

        nameE = tk.Entry(self)
        pwordE = tk.Entry(self, show='*')
        nameE.grid(row=1, column=1)
        pwordE.grid(row=2, column=1)

        signupButton = tk.Button(self, text='Registrer',
                           command=lambda: FSSignup(controller))
        signupButton.grid(columnspan=2, sticky="E")


class PlacementPage(tk.Frame):  # This has to be cleaned up
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hvor er lansa plassert?", font=large_font)
        label.grid()

        h = 4
        w = 8

        button1 =tk.Button(self, text="9",
                            command=lambda: Place(9, controller),height = h, width = w)
        button1.grid(row=1, column = 1)
        button2 = tk.Button(self, text="10",
                            command=lambda: Place(10, controller),height = h, width = w)
        button2.grid(row=1, column=2)
        button3 = tk.Button(self, text="11",
                            command=lambda: Place(11, controller),height = h, width = w)
        button3.grid(row=1, column=3)
        button4 = tk.Button(self, text="12",
                            command=lambda: Place(12, controller),height = h, width = w)
        button4.grid(row=1, column=4)
        button5 = tk.Button(self, text="13",
                            command=lambda: Place(13, controller),height = h, width = w)
        button5.grid(row=1, column=5)
        button6 = tk.Button(self, text="14",
                            command=lambda: Place(14, controller),height = h, width = w)
        button6.grid(row=2, column=1)
        button7 = tk.Button(self, text="15",
                            command=lambda: Place(15, controller),height = h, width = w)
        button7.grid(row=2, column=2)
        button8 = tk.Button(self, text="16",
                            command=lambda: Place(16, controller),height = h, width = w)
        button8.grid(row=2, column=3)
        button9 = tk.Button(self, text="17",
                            command=lambda: Place(17, controller),height = h, width = w)
        button9.grid(row=2, column=4)
        button10 = tk.Button(self, text="18",
                            command=lambda: Place(18, controller),height = h, width = w)
        button10.grid(row=2, column=5)
        button11 = tk.Button(self, text="19",
                            command=lambda: Place(19, controller),height = h, width = w)
        button11.grid(row=3, column=1)

        button12 = tk.Button(self, text="20",
                            command=lambda: Place(20, controller),height = h, width = w)
        button12.grid(row=3, column=2)
        button13 = tk.Button(self, text="21",
                            command=lambda: Place(21, controller),height = h, width = w)
        button13.grid(row=3, column=3)

        button14 = tk.Button(self, text="22",
                            command=lambda: Place(22, controller),height = h, width = w)
        button14.grid(row=3, column=4)
        button15 = tk.Button(self, text="23",
                            command=lambda: Place(23, controller),height = h, width = w)
        button15.grid(row=3, column=5)

        button16 = tk.Button(self, text="24",
                            command=lambda: Place(24, controller),height = h, width = w)
        button16.grid(row=4, column=1)
        button17 = tk.Button(self, text="25",
                            command=lambda: Place(25, controller),height = h, width = w)
        button17.grid(row=4, column=2)

        button18 = tk.Button(self, text="26",
                            command=lambda: Place(26, controller),height = h, width = w)
        button18.grid(row=4, column=3)

        button19 = tk.Button(self, text="27",
                             command=lambda: Place(27, controller),height = h, width = w)
        button19.grid(row=4, column=4)


class Home(tk.Frame):  # Main page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("type: ", lanceType), font=large_font)
        label.grid(row=0, column=0)

        button1 = tk.Button(self, text="9",
                            command=lambda: Place(9, controller), )
        button1.grid(row=1, column=1)

    def getValue(self, label):



  #  "Main loop"--------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = AppGui()
    app.mainloop()

