from tkinter import *
root =Tk()
root.geometry("400x400")
root.resizable(0,0)
un =Label(root,text ="enter you Name",font =("Arial",15))
un.grid(row =0,column =0,pady =25,sticky =W)
entry1 =Entry(root,font =("Arial",10))
entry1.grid(row =0,column=1,pady =20)

un1 =Label(root,text ="enter your password",font =("Arial",15))
un1.grid(row =1,column ="0",pady=25)

entry2 =Entry(root,font =("Arial",10))
entry2.grid(row =1,column=1 ,pady =20)

b1 =Button(root,text ="SUBMIT",font =("Arial",15),bg ="black",fg ="white")
b1.grid(row =2,column =0 ,columnspan =2)
root.mainloop()


print("code successfully run")