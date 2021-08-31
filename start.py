from tkinter import*
import os
import sys
from functools import partial 
from PIL import ImageTk,Image
from tkinter.filedialog import asksaveasfile

def session():
	pass
	
def donothing():
	pass

def login_success(username):
	global screen3
	screen3=Toplevel(screen)
	screen3.title("Dashboard")
	screen3.geometry("300x300")

	usernamelogin = username
	Label(screen3,text="Welcome!"+usernamelogin,fg="green",font=("Calibri",13)).pack()
	Button(screen3,text="log out",height="2",width="25").pack()

def userpsw_not_recoginzed():
	global screen4
	screen4=Toplevel(screen)
	screen4.title("Dashboard")
	screen4.geometry("300x300")
	Label(screen4,text="User Password is not regconized!Please check!",fg="Red",font=("Calibri",13)).pack()

def user_not_found():
	global screen5
	screen5=Toplevel(screen)
	screen5.title("Dashboard")
	screen5.geometry("300x300")
	Label(screen5,text="User is not register yet!",fg="Red",font=("Calibri",13)).pack()


def login_user():
	username1 = username_verify.get()
	password1 = password_verify.get()
	username_entry1.delete(0,END)
	password_entry1.delete(0,END)

	list_of_files = os.listdir()
	if username1 in list_of_files:
		file1 = open(username1,"r")
		verify = file1.read().splitlines()
		print(verify)
		if password1 in verify:
			login_success(username1)
			
		else:
			userpsw_not_recoginzed()
			#print("not regconized")
	else:
		user_not_found()
		#print("not found")


def register_user():
	username_info=username.get()
	password_info=password.get()


	file = [('All File', '.')]
	file = asksaveasfile(filetypes = file, defaultextension = file)
	#file=open(username_info+".txt","w")
	#file=open(username_info,"w")
	file.write(username_info+"\n")
	file.write(password_info)
	file.close()

	username_entry.delete(0, END)
	password_entry.delete(0, END)

	Label(screen1,text="Register success!",fg="green",font=("Calibri",13)).pack()

def Register():
	global screen1
	screen1=Toplevel(screen)
	screen1.title("Register")
	screen1.geometry("300x300")

	global username
	global password
	global username_entry
	global password_entry
	username = StringVar()
	password = StringVar()

	menubar = Menu(screen1)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Log in", command=Log_in)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=screen1.quit)
	menubar.add_cascade(label="File", menu=filemenu)
	screen1.config(menu=menubar)

	Label(screen1,text="Register", bg="black", fg="yellow",width="300",height="2",font=("Calibri",13)).pack()
	Label(screen1,text="").pack()

	Label(screen1,text="username *",height="2",width="30").pack()
	username_entry = Entry(screen1,textvariable=username,width="30")
	username_entry.pack()
	Label(screen1,text="").pack()

	Label(screen1,text="Password *",height="2",width="30").pack()
	password_entry = Entry(screen1,textvariable=password,width="30")
	password_entry.pack()
	Label(screen1,text="").pack()

	Button(screen1,text="Register",height="2",width="25",command=register_user).pack()
	Button(screen1,text="X",height="2",width="3",command=screen1.quit).pack()

def Log_in():
	global screen2
	screen2=Toplevel(screen)
	screen2.title("Log IN")
	screen2.geometry("300x300")

	Label(screen2,text="Log in", bg="black", fg="yellow",width="300",height="2",font=("Calibri",13)).pack()
	Label(screen2,text="").pack()

	global username_verify
	global password_verify
	global username_entry1
	global password_entry1
	username_verify = StringVar()
	password_verify = StringVar()

	Label(screen2,text="username *",height="2",width="30").pack()
	username_entry1 = Entry(screen2,textvariable=username_verify,width="30")
	username_entry1.pack()
	Label(screen2,text="").pack()

	Label(screen2,text="password *",height="2",width="30").pack()
	password_entry1 = Entry(screen2,textvariable=password_verify,width="30")
	password_entry1.pack()
	Label(screen2,text="").pack()

	Button(screen2,text="Log In",height="2",width="25",command=login_user).pack()
	Button(screen2,text="X",height="2",width="3",command=screen2.quit).pack()

def Calculator():
	os.system('calculator.py')


def main_screen():
	global screen
	screen=Tk()
	screen.geometry("9000x9000")
	screen.iconbitmap("c:/pythonFile/img/P2.ico")
	screen.title("Notes")

	menubar = Menu(screen)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="New", command=donothing)
	filemenu.add_command(label="Open", command=donothing)
	filemenu.add_command(label="Save", command=donothing)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=screen.quit)
	menubar.add_cascade(label="File", menu=filemenu)
	screen.config(menu=menubar)

	img=ImageTk.PhotoImage(Image.open ("C:/pythonFile/img/regist.png"))
	img1=ImageTk.PhotoImage(Image.open("C:/pythonFile/img/login.png"))
	img2=ImageTk.PhotoImage(Image.open("C:/pythonFile/img/cal.jpg"))
	imgbot=ImageTk.PhotoImage(Image.open("C:/pythonFile/img/fastBird1_2.png"))

	lable_bg=Label(text="", bg="#D3D3D3",width="900",height="6")
	lable_bg.grid(row = 0, column = 0,columnspan = 200,sticky = W)

	bot_Title=Label(image=imgbot,bg="#D3D3D3",width="100",height="90",fg="yellow")
	bot_Title.grid(row = 0, column = 0,sticky = W)
	lable_Title=Label(text="Welcome From Hommie", bg="#D3D3D3",height="1",fg="black",font=("Brush Script MT",30))
	lable_Title.grid(row = 0, column = 1,columnspan = 1,sticky = W)

	login_btn = Button(text="LogIN",image=img1,height="100",width="105",command=Log_in)
	login_btn.grid(row = 2, column = 1,sticky = W)
	login_lbl=Label(text="Log In",width="15",height="2",fg="black",font=("Arial",8,"bold"))
	login_lbl.grid(row = 3, column = 1,sticky = W)

	reg_btn=Button(text="Register",image=img,height="100",width="105",command=Register)
	reg_btn.grid(row = 4, column = 1,sticky = W)
	login_lbl=Label(text="Register",width="15",height="2",fg="black",font=("Arial",8,"bold"))
	login_lbl.grid(row = 5, column = 1,sticky = W)

	hol=Button(text="Register",image=img2,height="100",width="105",command=Calculator)
	hol.grid(row = 4, column = 5,sticky = W)

	screen.mainloop()

main_screen()