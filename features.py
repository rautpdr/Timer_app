#features class
from tkinter import *
from counting import countdown  # ✅ import countdown class


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
resp = 0 #to count number of repitation


class all_features(Tk):

    def __init__(self):
        super().__init__()
        self.timer_label = None
        self.title("Timer-object")
        self.config(padx= 100 , pady= 50 , bg= YELLOW)

        self.canvas = Canvas(width= 200 , height= 224 , bg = YELLOW , highlightthickness=0)
        self.canvas.grid(row = 1 , column = 1)#placing tomato in center
        self.tom_img = PhotoImage(file = "tomato.png")
        self.canvas.create_image(103 , 112 , image = self.tom_img )
        self.timer_text = self.canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 35 , "bold"))

        self.count_instance = countdown(self) #storing count instace to access its methods

    def functions(self):

        #timer label(0,1)
        self.timer_label = Label(text="Timer" , fg= GREEN , font=(FONT_NAME , 20 , "bold") , bg= YELLOW)
        self.timer_label.grid(row = 0, column =1)

        #start button(2,0)
        start_button = Button(text="START" , command= self.start_timer)
        start_button.grid(row = 2 , column = 0)

        #reset button(2,2)
        reset_button = Button(text="RESET" , command= self.reset_timer)
        reset_button.grid(row = 2 , column = 2)

        # ✔ label(3,1)
        check_mark_label = Label(text= "✔" , fg= GREEN , font=(FONT_NAME , 15 , "bold"))
        check_mark_label.grid(row = 3 , column = 1)


    #start timer
    def start_timer(self):
        global resp
        WORK_sec = WORK_MIN * 60
        SHORT_BREAK_sec = SHORT_BREAK_MIN * 60
        LONG_BREAK_sec = LONG_BREAK_MIN * 60
        resp += 1
        if resp % 8 == 0:
            self.timer_label.config(text = "Long Break" , fg = GREEN)
            self.count_instance.count(LONG_BREAK_sec)
        elif resp % 2 == 0:
            self.timer_label.config(text = "Short Break", fg = PINK)
            self.count_instance.count(SHORT_BREAK_sec)
        else:
            self.timer_label.config(text = "Work" , fg = RED)
            self.count_instance.count(WORK_sec)



    #reset timer
    def reset_timer(self):
        self.after_cancel(self.count_instance.timer)
        self.canvas.itemconfig(self.timer_text , text = "00:00" )
        self.timer_label.config(text="Timer" , fg= GREEN , font=(FONT_NAME , 20 , "bold") , bg= YELLOW )
        global resp
        resp = 0








