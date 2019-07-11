import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',6234))
server.listen(5)
c,addr=server.accept()
print("Connection from: ",str(addr))

from tkinter import *
w=Tk()
w.title("Server1")
v1=StringVar()


def submit():
    s1=v1.get()
    print("Sending: "+ str(s1))
    c.send(s1.encode())

def receive():
    data=c.recv(1024).decode()
    print("From connected user: "+ str(data))
    v1.set(data)


def reset():
    v1.set('')
    


    
L=Label(w,text="Server message to client",font=("arial",20,"bold"))
E=Entry(w,font=("arial",20,"bold"),textvariable=v1)
B1=Button(w,text="Submit to client",font=("arial",20,"bold"),command=submit)
B2=Button(w,text="Reset",font=("arial",20,"bold"),command=reset)
B3=Button(w,text="Receive from client",font=("arial",20,"bold"),command=receive)
L.grid(row=1,column=1)
E.grid(row=1,column=2)
B1.grid(row=2,column=1)
B2.grid(row=2,column=2)
B3.grid(row=2,column=3)

w.mainloop()
