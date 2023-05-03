import login
from tkinter import *

def signup():
    """
    Allows user to create a new account by filling out the user and the password field.
    """

    """Window Initialization"""
    signInWindow = Tk()
    signInWindow.geometry('640x360')
    signInWindow.title('Signup')
    signInWindow['bg'] = 'white'
    signInWindow.config(bg='white')
    font = ("Arial", 12)
    title_font = ("Arial bold", 18)

    """Window Commands"""
    def submit():
        if((landlordFirstName.get() != "") and (password.get() != "")):
            """
            First check if all fields have been filled, then add to file.
            If we had more time, to improve this application, we would add more 
            security measures to prevent attacks such as buffer overflow.
            """
            with open('landlordAccount.txt', 'a') as file:
              file.write(f"{landlordFirstName.get()}\n")
              file.write(f"{password.get()}\n")
            loginPage()
        else:
            # If insufficient data is provided, alert the user.
            errorLabel.config(text="Please enter all fields.", fg="red")

    def loginPage():
        #Return user to the login page.
        signInWindow.destroy()
        login.login()

    """Window Contents"""
    Label(signInWindow,
        text="Register To Landlord ",
        padx=20,
        pady=20,
        bg='white',
        font=title_font).pack(expand=True, fill=BOTH)

    landlordFirstNameFrame = Frame(signInWindow)
    landlordFirstNameFrame.pack(side=TOP, pady=5)
    Label(landlordFirstNameFrame, text="Username: ", font=font).pack(side=LEFT)
    landlordFirstName = Entry(landlordFirstNameFrame)
    landlordFirstName.pack(side=LEFT)

    passwordFrame = Frame(signInWindow)
    passwordFrame.pack(side=TOP, pady=5)
    Label(passwordFrame, text="Password: ", font=font).pack(side=LEFT)
    password = Entry(passwordFrame, show="*")
    password.pack(side=LEFT)

    submitBtn = Button(signInWindow, text="Submit", command=submit, font=font)
    submitBtn.pack()

    loginFrame = Frame(signInWindow)
    loginFrame.pack(side=TOP, pady=10)
    Label(loginFrame, text="Already have an account? ",
        font=font).pack(side=LEFT)
    loginBtn = Button(loginFrame,
        text="Login",
        font=font,
        fg="blue",
        bd=0,
        command=loginPage)
    loginBtn.pack(side=LEFT)
    errorLabel = Label(signInWindow, font=font)
    errorLabel.pack(side=TOP, pady=5)
    signInWindow.mainloop()