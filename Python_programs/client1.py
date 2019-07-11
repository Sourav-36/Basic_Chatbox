import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',6234))
print("Connected")

from tkinter import *
w=Tk()
w.title("Client1")
v=StringVar()

def receive1():
    data1=client.recv(1024).decode()
    print("Received from server:"+ str(data1))
    v.set(data1)
    

def submit2():
    message=v.get()
    print("Sending"+ str(message))
    client.send(message.encode())

def reset():
    v.set('')


L=Label(w,text="Client receives & messages to server ",font=("arial",20,"bold"))
E=Entry(w,font=("arial",20,"bold"),textvariable=v)
B1=Button(w,text="Receive from server",font=("arial",20,"bold"),command=receive1)
B2=Button(w,text="Reset",font=("arial",20,"bold"),command=reset)
B3=Button(w,text="Submit to server",font=("arial",20,"bold"),command=submit2)
L.grid(row=1,column=1)
E.grid(row=1,column=2)
B1.grid(row=2,column=1)
B2.grid(row=2,column=2)
B3.grid(row=2,column=3)

w.mainloop()
