#calculator project
import tkinter as tk
window=tk.Tk()
window.geometry("545x500")  
window.title("Calculator")
window.config(bg="pink")
main_string=""
def calc():
    global main_string
    try:
        result = eval(main_string)
        if result==int(result):
            result=int(result)
        
        main_string = str(result)
        label.config(text=main_string)
        
    except:
        main_string = ""
        label.config(text="Error")


def clear():
    global main_string
    label.config(text="")
    main_string=""



def click(x):
    global main_string
    main_string+=str(x)
    label.config(text=main_string)



def backspace():
    global main_string
    main_string=list(main_string)
    del main_string[-1]
    main_string="".join(main_string)
    label.config(text=main_string)


label=tk.Label(window,text="                                      ",bg="White",font=("Arial",25,"bold"))
label.grid(row=0,column=0,columnspan=7,pady=102,padx=15,rowspan=5)
b0=tk.Button(window,text=0,font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click(0))
b1=tk.Button(window,text=1,font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click(1))
b2=tk.Button(window,text=2,font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click(2))
b3=tk.Button(window,text=3,font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click(3))
b4=tk.Button(window,text=4,font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click(4))
b5=tk.Button(window,text=5,font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click(5))
b6=tk.Button(window,text=6,font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click(6))
b7=tk.Button(window,text=7,font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click(7))
b8=tk.Button(window,text=8,font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click(8))
b9=tk.Button(window,text=9,font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click(9))
plus=tk.Button(window,text="+",font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click("+"))
minus=tk.Button(window,text="-",font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click("-"))
vurma=tk.Button(window,text="*",font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click("*"))
bolme=tk.Button(window,text="/",font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click("/"))
beraber=tk.Button(window,text="=",font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=calc)
c=tk.Button(window,text="C",font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=clear)
b=tk.Button(window,text="⌫",font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=backspace)
l_parantez=tk.Button(window,text="(",font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click("("))
r_parantez=tk.Button(window,text=")",font=("Arial",20,"bold"),bg="#c000c0",fg="white",width=4,height=2,relief="solid",command=lambda: click(")"))
b0.grid(row=10,column=3)
r_parantez.grid(row=10,column=5)
c.grid(row=11,column=5)
l_parantez.grid(row=12,column=4)
b.grid(row=12,column=5)
b1.grid(row=12,column=0)
b2.grid(row=12,column=1)
b3.grid(row=12,column=2)
b4.grid(row=11,column=0)
b5.grid(row=11,column=1)
b6.grid(row=11,column=2)
b7.grid(row=10,column=0)
b8.grid(row=10,column=1)
b9.grid(row=10,column=2)
plus.grid(row=12,column=3)
minus.grid(row=10,column=4)
vurma.grid(row=11,column=3)
bolme.grid(row=11,column=4)
beraber.grid(row=10,column=6,rowspan=3,sticky="ns")















window.mainloop()