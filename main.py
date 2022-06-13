from tkinter import Tk,Label,Entry,Button,IntVar
#SETTING UP THE WINDOW
root = Tk()
root.config(bg='blue')
root.geometry('600x400')
root.title('Percentile Calculator')

tex = ('Verdana',20,'bold')
#lABEL CREATION
L_Rank = Label(root, text='Rank    ->', fg='black', bg='blue', font=tex)
L_App = Label(root, text='No.of.Applicants   ->', fg='red', bg='blue', font=tex)
L_Perc = Label(root, text='Percentile    =', fg='white', bg='blue', font=tex)

#VARIABLE FOR GETTING ENTRY ELEMENTS
rank = IntVar()
app = IntVar()

#ENTRY POINT CREATION
E_Rank = Entry(root, width=20, textvariable=rank)
E_App = Entry(root, width=20, textvariable=app)

# FUNCTION TO BE ADDED INSIDE A BUTTON
def percentile(a,b):
    if b==0 or a==0 or a>b:
        L_W_Result = Label(root, text="Invalid Data \ngiven", fg='violet', bg='blue', font=tex)
        L_W_Result.place(relx=0.58, rely=0.50)
    else:
        result = round((a * 100) / b, 10)
        L_Result = Label(root, text=f"{100 - result}             \n          ", fg='violet', bg='blue', font=tex)
        L_Result.place(relx=0.58, rely=0.50)

# SUBMIT BUTTON

B_Submit = Button(root, text='Submit', width=25, command=lambda:percentile(rank.get(),app.get()))

L_Rank.place(relx=0.33, rely=0.17)
L_App.place(relx=0.05, rely=0.33)
L_Perc.place(relx=0.20, rely=0.50)
E_Rank.place(relx=0.60, rely=0.20)
E_App.place(relx=0.60, rely=0.36)
B_Submit.place(relx=0.5, rely=0.7)

root.mainloop()