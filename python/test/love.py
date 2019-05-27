from tkinter import *
from tkinter import messagebox


def closeWindow():
    messagebox.showinfo(title="警告",message = "不许关闭，好好回答")
   # messagebox.showerror(title="警告",message = "")
    return

def closeAllWindow():
    window.destroy()

def Love():
    
    love = Toplevel(window)
    love.geometry("300x100+610+260")
    love.title("好巧，我也是")
    label = Label(love,text = "好巧我也是", font =( "楷体", 25 ))
    label.pack()
    btn = Button(love,text= "确定", width = 10, height = 2, command = closeAllWindow)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW", closelove)
    

def closelove():
    messagebox.showinfo(title="爱你", message="再考虑一下嘛")
    
def closenolove():
    nolove()
    
    
def nolove():
    noLove = Toplevel(window)
    noLove.geometry("300x100")
    noLove.title("考虑一下嘛")
    label = Label(noLove, text="考虑一下嘛", font=("楷体", 25))
    label.pack()
    btn = Button(noLove, text="好的", width=10, height=2, command=noLove.destroy)
    btn.pack()
    noLove.protocol("WM_DELETE_WINDOW", closenolove)
   
    

#创建窗口
window = Tk()

#设置窗口的标题
window.title("你喜欢我？？？")
#设置窗口的大小
window.geometry("380x420+590+230")
#窗口的位置
#window.geometry("+590+230")

window.protocol("WM_DELETE_WINDOW", closeWindow)


#标签控件
labell = Label(window,text = "hey,小姐姐！",font = ('微软雅黑',15),fg = 'red')
#定位 grid网格式的布局 pack place
labell.grid()
label2 = Label(window,text = "喜欢我？？", font = ('微软雅黑',30),fg = 'green')
#sticky 对齐方式 ，N S W E
label2.grid(row = 1,column = 1,sticky = E)
#显示图片
photo = PhotoImage(file = './cc.png')

imageLable = Label(window,image = photo)
#columnspan 组件跨越的列数
imageLable.grid(row = 2,columnspan = 2)

#按钮
btn1= Button(window,text = "喜欢",width = 15, height = 2,command = Love)
btn1.grid(row = 3,column = 0,sticky = W)
btn2= Button(window,text = "不喜欢",command = nolove)
btn2.grid(row = 3,column = 1,sticky = E)

#显示窗口 消息循环
window.mainloop()
