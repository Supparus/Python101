from tkinter import * #import มาทั้งหมด
from tkinter import ttk #import theme of tk
from tkinter import messagebox


GUI = Tk() #หน้าจอหลักของโปรแกรม
GUI.title('BMI Calculator') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดหน้าต่างโปรแกรม กว้างxสูง


B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท') #ปุ่ม ใช้ธีม ttk
B1.pack(ipadx=20,ipady=20) #ทำให้ปุ่มอยู่กลางหน้าจอ,internal padding แกน x,y

L1 = Label(GUI,text='BMI Calculator',font=('Angsana New',30),fg='blue',bg='black') #ป้าย
L1.place(x=20,y=20)

def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
    #messagebox.showwarning('เงินในบัญชี',text)
    #messagebox.showerror('เงินในบัญชี',text)

#FB1 = Frame(GUI) #สร้างกรอบ
FB1 = LabelFrame(GUI,text='money')
FB1.place(x=200,y=200) #นำ Place ไปไว้ในกรอบ Frame
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2) #เอา FB1 มาใช้แทน GUI / ผูกกับ messagebox
B2.pack(ipadx=20,ipady=20,padx=30,pady=30)

#B2.place(x=50,y=200) #กำหนดโลเคชัน0.0 ซ้ายบน


################

GUI.mainloop()

