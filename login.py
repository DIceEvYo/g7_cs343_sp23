from tkinter import *
import Homepage
import signup

def login():
  """
  If the user already has an account, they can fill in their credentials here.
  If not they can click the signup button to create an account.
  The user must have an account in order to enter the program.
  """

  """Window Initialization"""
  loginWindow = Tk()
  loginWindow.geometry('640x360')
  loginWindow.title('Login')
  loginWindow['bg'] = 'white'
  loginWindow.config(bg='white')
  font = ("Arial", 12)
  title_font = ("Arial bold", 18)

  """Window Commands"""
  def submit():
    #Open the landlordAccount.txt file and check for a username and password match
    usernameVal = user.get()
    passwordVal = password.get()
    if ((usernameVal != "") and (passwordVal != "")):
      """
      First check if all fields have been filled, then add to file.
      If we had more time, to improve this application, we would add more 
      security measures to prevent attacks such as buffer overflow.
      """
      with open("landlordAccount.txt", "r") as f:
        data = []
        for line in f:
          data.append(line.strip())
        for index in range(0, len(data), 2):
          if (data[index] == usernameVal and data[index+1] == passwordVal):
            # If match found, display page3
            loginWindow.destroy()
            Homepage.homepage()
          else:
            # If no match found, display error message
            errorLabel.config(text="Incorrect username or password", fg="red")
          f.close()
    else:
      # If insufficient data is provided, alert the user.
      errorLabel.config(text="Please enter all fields.", fg="red")

  def signUpPage():
    #Bring user to the sign up page.
    loginWindow.destroy()
    signup.signup()

  """Window Contents"""
  Label(loginWindow,
    text="Welcome back Landlord! ",
    padx=20,
    pady=20,
    bg='white',
    font=title_font).pack(expand=True, fill=BOTH)

  userFrame = Frame(loginWindow)
  userFrame.pack(side=TOP, pady=5)
  Label(userFrame, text="Username: ", font=font).pack(side=LEFT)
  user = Entry(userFrame)
  user.pack(side=LEFT)

  passwordFrame = Frame(loginWindow)
  passwordFrame.pack(side=TOP, pady=5)
  Label(passwordFrame, text="Password: ", font=font).pack(side=LEFT)
  password = Entry(passwordFrame, show="*")
  password.pack(side=LEFT)

  submitBtn = Button(loginWindow, text="Login", command=submit, font=font)
  submitBtn.pack()

  loginFrame = Frame(loginWindow)
  loginFrame.pack(side=TOP, pady=10)
  Label(loginFrame, text="Don't have an account? ", font=font).pack(side=LEFT)
  loginBtn = Button(loginFrame,
    text="Signup",
    font=font,
    fg="blue",
    bd=0,
    command=signUpPage)
  loginBtn.pack(side=LEFT)

  errorLabel = Label(loginWindow, font=font)
  errorLabel.pack(side=TOP, pady=5)
  loginWindow.mainloop()