print("			▀▄▀▄▀▄ SECRET MESSAGE PORTAL ▄▀▄▀▄▀")


print("Hi.....!!!! Welcome to Secret Message Portal..<3")
print("we have options for you:")
print("Simple coding-c")
print("Simple Decoding-d")
print("Mail Your Friend-m")
l=input("Choose your option-")


def code():
	alpha="abcdefghijklmnopqrstuvwxyz"
	key=3
	newmsg=''
	msg=input("Enter the message you want to encrypt...  ")
	for character in msg:
		if character in alpha:
			posi=alpha.find(character)
			nposi=(posi+key)%26
			newcar=alpha[nposi]
			newmsg +=newcar
		else:
			newmsg +=character
	print("Your emcrypted message is-")
	print(newmsg)
	
def decode():
	alpha="abcdefghijklmnopqrstuvwxyz"
	key=3
	newmsg=''
	msg=input("Enter the decrypted message....")
	for character in msg:
		if character in alpha:
			posi=alpha.find(character)
			nposi=(posi-key)%26
			newcar=alpha[nposi]
			newmsg +=newcar
		else:
			newmsg +=character
	print("The decrypted message was-")
	print(newmsg)

def mail():
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
		msg=input("Enter the message you want to encrypt... ")
		for character in msg:
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
		msg=input("Enter the decrypted message....")
		for character in msg:
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


if(l=='c'):
	code()
elif(l=='d'):
	decode()
elif(l=='n'):
	name()
elif(l=='l'):
	letter()
elif(l=='f'):
	fun()
elif(l=='m'):
	mail()
else:
	print("WRONG KEY")
	exit()
