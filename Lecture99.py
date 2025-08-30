from tkinter import *
import math

def leftClickButton(event):
    bmi = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    if bmi < 18.5:
        result = "น้ำหนักน้อย / ผอม"
    elif 18.5 <= bmi < 23:
        result = "สมส่วน (ปกติ)"
    elif 23 <= bmi < 25:
        result = "ท้วม / น้ำหนักเกิน"
    elif 25 <= bmi < 30:
        result = "อ้วนระดับ 1"
    else:
        result = "อ้วนระดับ 2"

   
    labelResult.configure(text=result)





MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()
