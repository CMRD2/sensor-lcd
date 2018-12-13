import tkinter as tk


from tkinter import *


r = Tk()


L1 = Label(r, text="TEXT")
L1.pack( side = TOP)
E1 = Entry(r, bd =5)
E1.pack(side = TOP)

def myaction():
	f=E1.get()
	print(f)
	d=var.get()


	if(d==1):
		alpha="abcdefghijklmnopqrstuvwxyz"
		key=3
		newmsg=''
		for character in f:
			if character in alpha:
				posi=alpha.find(character)
				nposi=(posi+key)%26
				newcar=alpha[nposi]
				newmsg +=newcar
			else:
				newmsg +=character		
		print("Your encrypted message is-")
		print(newmsg)
		exit()


	elif(d==2):
		alpha="abcdefghijklmnopqrstuvwxyz"
		key=3
		newmsg=''
		for character in f:
			if character in alpha:
				posi=alpha.find(character)
				nposi=(posi-key)%26
				newcar=alpha[nposi]
				newmsg +=newcar
			else:
				newmsg +=character
		print("The decrypted message was-")
		print(newmsg)
		exit()

	elif(d==3):
		import smtplib
		#IMPORT SMTPLIB
		#TO SEND EMAIL
		smtpserver=smtplib.SMTP("smtp.gmail.com",587)
		smtpserver.starttls()
		#TO USE TLS
		receiver=input('To-   ')
		sender=input('From-   ')
		password=input('Password   ')
		#LOGIN IN TO YOUR ACC
		smtpserver.login(sender,password)
		print("Encrypt-x/Decrypt-y")
		r=input("Choose your option-")
		if(r=='x'):
			alpha="abcdefghijklmnopqrstuvwxyz"
			key=3
			newmsg=''
			for character in f:
				if character in alpha:
					posi=alpha.find(character)
					nposi=(posi+key)%26
					newcar=alpha[nposi]
					newmsg +=newcar
				else:
					newmsg +=character
			print("Your encrypted message is-  ")
			print(newmsg)
		elif(r=='y'):
			alpha="abcdefghijklmnopqrstuvwxyz"
			key=3
			newmsg=''
	
			for character in f:
				if character in alpha:
					posi=alpha.find(character)
					nposi=(posi-key)%26
					newcar=alpha[nposi]
					newmsg +=newcar
				else:
					newmsg +=character
			print("The decrypted message was-")
			print(newmsg)
		else:
			print("Exiting Mail......")
			exit()
		smtpserver.sendmail(sender,receiver,newmsg)
		print('YOUR MESSAGE HAS BEEN SENT')
		smtpserver.close()



def sel():

   selection = "You selected the option " + newmsg
   label.config(text = selection)


var = IntVar()
R1 = Radiobutton(r, text="code", variable=var, value=1,
				  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(r, text="decode", variable=var, value=2,
				  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(r, text="mail", variable=var, value=3,
				  command=sel)
R3.pack( anchor = W)



r.title('secret message') 
button = tk.Button(r, text='Submit', width=25, command=myaction) 
button.pack() 


label = Label(r)
label.pack()
r.mainloop()

exit()