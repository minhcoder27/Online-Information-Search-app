from functools import singledispatchmethod
from re import sub
from tkinter import *
from PIL import Image,ImageTk
from matplotlib.pyplot import margins
import tkinter.messagebox as mbox



root=Tk()
root.title("Hồ sơ online")
root.geometry("400x50")
root.iconbitmap("icoco.ico")
namesdt = Label(root, text=" số điện thoại học sinh:",fg="#3399FF",bd=0)
namesdt.config(font=("Transformers Movie",10))
namesdt.grid(column=0, row=0)

def out():
    f = open("information.csv",mode="r",encoding="utf-8-sig")
    x=0
    check =0
    sdt = txt.get()
    while True:
        x+=1
        check = 1
        line = f.readline()
        if line == '':
            break
        line = line.replace(',','')

        a = line.strip('""').rstrip().split('"')
    
        a.remove(a[0])
        b = ["không","có một"]
        for i in a:
            if len(i)==0:
                a.remove(i)
            
        if sdt ==a[20]:
            mbox.showinfo("Hồ sơ học sinh", """Mã học sinh: """ +a[1]+"""
                                                Họ và tên: """+a[2]+"""
                                                Lớp: """+a[0]+"""
                                                Ngày tháng năm sinh: """+a[3]+"""
                                                Giới tính: """+a[4]+"""
                                                Hộ khẩu thường trú: """+a[5]+"""
                                                Nơi ở hiện tại: """+a[6]+"""
                                                Quê quán: """+a[8]+"""
                                                Dân tộc: """+a[9]+"""
                                                Số điện thoại: """+a[20]+"""
                                                Tôn giáo: """+a[10]+"""
                                                Diện chính sách: """+a[11]+"""
                                                Cận nghèo: """+b[int(a[12])]+"""
                                                Đoàn viên: """+b[int(a[13])]+"""
                                                Đội viên: """+b[int(a[14])]+"""
                                                Giáo viên: """+b[int(a[15])]+"""
                                                Tên cha: """+a[16]+"""
                                                Nghề nghiệp: """+a[17]+"""
                                                Số điện thoại: """+a[21]+"""
                                                Tên mẹ: """+a[18]+"""
                                                Nghề nghiệp: """+a[19]+"""
                                                Số điện thoại: """+a[22])
            check =0
            break
    if check ==1:
        mbox.showwarning("Lỗi!", "Số điện thoại chưa được cập nhật trên hệ thống!")
    f.close()
    print(x)
txt = Entry(root, width=20)
txt.grid(column=1, row=0)
bt = Button(root, text=" nhập",command=out)
bt.grid(column=2,row=0)
        
                
                



root.mainloop()