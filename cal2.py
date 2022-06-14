from tkinter import *
import calendar

def showCal():
    new_gui = Tk()

    new_gui.config(background = "aqua")

    new_gui.title("CALENDAR")

    new_gui.geometry("650x700")

    fetch_year = int(year_field.get())
    fetch_month = int(month_field.get())

    cal_content = calendar.month(fetch_year,fetch_month)

    cal_month = Label(new_gui,text=cal_content,font="Consolas 35 bold")

    cal_month.grid(row=8,column=5,padx=80,pady=60)

    new_gui.mainloop()

if __name__ == "__main__":
    gui = Tk()
    gui.config(background="aqua")
    gui.title("CALENDAR")
    gui.geometry("650x700")
    #bg = PhotoImage(file="images.png")
   #label1 = Label(gui,image=bg)
   # label1.pack()

    cal = Label(gui,text="-:Welcome to Mangesh's Calendar:-",bg="dark gray",font=("times",30,'bold'))
    year = Label(gui,text="Enter Year ->",bg="light green",font=("times",28,'bold'))
    year_field = Entry(gui,font=("times",20,'bold'))

    month = Label(gui, text="Enter Month ->", bg="light green", font=("times", 28, 'bold'))
    month_field = Entry(gui, font=("times", 20, 'bold'))

    Show = Button(gui,text="Show Calendar",fg="Black",bg="Red",command=showCal,font=("times",15,'bold'))

    Exit = Button(gui,text="Exit",fg="Black",bg="Red",command=exit,font=("times",14,'bold'))

    cal.grid(row=1,column=5,padx=17,pady=60)
    year.grid(row=2,column=5,pady=10)
    #year_field.place(row=3,column=5width=150, height=50)
    year_field.grid(row=3,column=5,pady=20,ipadx=10,ipady=10)
    month.grid(row=4,column=5,pady=20,ipadx=10,ipady=10)
    month_field.grid(row=6,column=5,pady=20,ipadx=10,ipady=10)
    Show.grid(row=7,column=5,pady=20)
    Exit.grid(row=9,column=5)

    gui.mainloop()