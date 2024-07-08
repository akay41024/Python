from tkinter import *
root = Tk()
# root.geometry("600X500+70+70")
#first row
lbl=Label(root, text="Calculator", font=("Arial",25), fg="black", bg="skyblue")
lbl.place(x=80,y=80,width=200, height=100)
lbl.pack()
ent=Entry(root, text="Calculator", font=("Arial",30), fg="black", bg="white")
ent.place(x=200,y=80,width=600, height=100)
# ent.pack()
b1= Button(root,text="C", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=800,y=80,width=200, height=100)
b1= Button(root,text="7", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=200,y=180,width=200, height=100)
b1= Button(root,text="8", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=400,y=180,width=200, height=100)
b1= Button(root,text="9", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=600,y=180,width=200, height=100)
b1= Button(root,text="*", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=800,y=180,width=200, height=100)

#Second row
b1= Button(root,text="6", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=200,y=280,width=200, height=100)
b1= Button(root,text="5", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=400,y=280,width=200, height=100)
b1= Button(root,text="4", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=600,y=280,width=200, height=100)
b1= Button(root,text="-", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=800,y=280,width=200, height=100)

#Third row


b1= Button(root,text="3", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=200,y=380,width=200, height=100)
b1= Button(root,text="2", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=400,y=380,width=200, height=100)
b1= Button(root,text="1", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=600,y=380,width=200, height=100)
b1= Button(root,text="+", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=800,y=380,width=200, height=100)

#Fourth row

b1= Button(root,text="00", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=200,y=480,width=200, height=100)
b1= Button(root,text="0", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=400,y=480,width=200, height=100)
b1= Button(root,text="/", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=600,y=480,width=200, height=100)
b1= Button(root,text="=", font=("Arial",25),fg="white", bg="gray", activebackground="blue")
b1.place(x=800,y=480,width=200, height=100)
mainloop()