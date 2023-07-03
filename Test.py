from tkinter import *
#สร้างหน้าจอ
root = Tk() 
#ตั้งค่าหน้าจอ
root.title("My GUI")
root.geometry("300x300+500+200")
root.resizable(0,0)
#สร้างปุ่ม
btn1=Button(root,text="ปุ่มที่ 1",font=("Times",30),bg="red")
btn1.pack()
root.mainloop()