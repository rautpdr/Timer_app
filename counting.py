import math

class countdown():
    def __init__(self , feature_gui):
        self.timer = None
        self.gui = feature_gui  #using feature gui as reference to access its values

    def count(self,time):

        #saperating mins
        minutes = math.floor(time / 60)
        seconds = time % 60

        if time > 0:
            self.timer = self.gui.after(1000 , self.count , time-1)#after 1000ms , calls self.count and passes value time-1
        else:
            self.gui.start_timer()

        if seconds < 10:
            seconds = f"0{seconds}" # if seconds count goes below 10 then want to be displayed MM:0S

        if minutes < 10:
            minutes = f"0{minutes}" # if minutes count goes below 10 then want to be displayed 0M:SS


        self.gui.canvas.itemconfig(self.gui.timer_text , text =f"{minutes}:{seconds}")
















