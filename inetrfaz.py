from tkinter import*
raiz=Tk()
raiz.title("posicionamiento")
raiz.geometry("400x150")
pd=Label(raiz,text="posicionamiento diferente")
pd.grid()
p=Label(raiz,text="posicionamiento")
p.config(relief="sunken")
p.grid()
p1=Label(raiz,text="posicionamiento 1")
p1.grid()
p2=Label(raiz,text="posicionamiento 2")
p2.grid()
p3=Label(raiz,text="posicionamiento 3")
p3.grid()
raiz.mainloop()









