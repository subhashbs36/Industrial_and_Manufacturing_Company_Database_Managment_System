from tkinter import *
from tkinter import ttk

def main():
    app = Tk()
    ob = LoginPage(app)
    app.mainloop()

class LoginPage:

    def __init__(self, win):
        self.win = win
        self.win.geometry("1350x750")
        self.win.title("Pharmacy Managent System | Admin Login")

        #create the top labels of the page 
        self.title_lbl = Label(self.win, text= "Pharmacy Management System", bg="green", fg="white",bd= 6, relief= GROOVE, font=("Aerial", 25, "bold") )
        self.title_lbl.pack(side=TOP,fill=X)

        self.login_lbl= Label(self.win, text = "Admin Login", fg= "#FF69B4",bg= "#121212",bd=6, relief= FLAT, font= ("Aerial",20), anchor=NW)
        self.login_lbl.pack(side= TOP, fill=X,expand=False)

        #create a frame on the page 
        self.main_frame = Frame(self.win, bg= "#121212", bd= 6, relief= RIDGE)
        self.main_frame.place(x=345, y=185, width= 725, height=470) 
        #Entry inside frame
        self.entry_frame = LabelFrame(self.main_frame, text= "Enter Details", bg = "#121212", fg= "#FF69B4", bd=4, relief= RIDGE,font=("Aerial", 18))
        self.entry_frame.pack(side=TOP,fill=BOTH)

        #----------Text Variables----------------
        
        username = StringVar()
        password = StringVar()

        #-----------------------------------------

        self.username_lbl = Label(self.entry_frame, text= "Username : ", font=("Aerial", 15), fg= "#121212",bg= "#FF69B4")
        self.username_lbl.grid(row=0, column=0, padx=50, pady=25)

        self.username_ent = Entry(self.entry_frame, border=9, textvariable = username,font=("Aerial", 15) )
        self.username_ent.grid(row=0, column= 1, padx=2, pady= 25)

        self.password_lbl = Label(self.entry_frame, text= "Password : ", bg="#FF69B4", font= ("Aerial", 15))
        self.password_lbl.grid(row=1, column=0, padx=50, pady=40)

        self.password_ent = Entry(self.entry_frame, border=9, textvariable = password,font=("Aerial", 15), show= "*" )
        self.password_ent.grid(row=1, column= 1, padx=2, pady= 40)

        self.false_frame1 = Frame(self.entry_frame, bd=0, bg= "#121212")

        #Buttons Frame
        self.button_frame = LabelFrame(self.main_frame, text= "Options", bg="#121212", fg= "#FF69B4",bd=4, relief= RIDGE, font= ("Aerial", 16))
        self.button_frame.pack(side= TOP, fill= BOTH)

        #-----------Button Function---------------
        def submit_func():
            if username.get() == "123" and password.get() == "123":
                pass
            else:
                #msg box to be added here
                print ("Wrong username or password") 

        def reset_func():
            username.set("")
            password.set((""))

        def exit_func():
            #Add a msg box here
            self.win.destroy()

        #-------------------------------------------

        #Buttons
        self.submit_btn = Button(self.button_frame, text= "Submit", bd=8, command= submit_func, font=("Aerial", 13), width= 15, anchor=CENTER)
        self.submit_btn.grid(row=0, column=2, padx=8, pady=20)

        self.reset_btn = Button(self.button_frame, text= "Reset", bd=8, command= reset_func, font=("Aerial", 13), width= 6, height= 1, anchor=CENTER)
        self.reset_btn.grid(row=0, column=3, padx=8, pady=20)

        self.exit_btn = Button(self.button_frame, text= "Exit", bd=8, command= exit_func, font=("Aerial", 13), width= 6, anchor=CENTER)
        self.exit_btn.grid(row=0, column=4, padx=8, pady=20)
        
        self.dummy1_btn = Label(self.button_frame, text= "", bg="#121212")
        self.dummy1_btn.grid(row=0, column=1, padx=160, pady=20)


if __name__ == "__main__":
    
    main()
