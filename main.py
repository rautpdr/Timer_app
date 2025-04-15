from tkinter import *
from features import all_features
from counting import countdown

#creating features object
feature = all_features()
feature.functions()

#creating counting object
count_timer = countdown(feature) #giving feature gui to countdown class

#window.mainloop()
feature.mainloop()
