# coding:utf-8
'''单词查询的GUI版本，比较偷懒，没将函数封装起来，
　　直接使用os.system()来搞的，注意中文解码'''
from Tkinter import *
import os
# 界面就三个组件，Entry, Button, Text
root = Tk()

def button_press(event):
	'''清空text,写入解释，使用系统命令，
	将查询结果存入temp,然后读取'''
	text.delete(1.0, END)
	get_word = word_input.get()
	get_word = u'%s' %get_word
	print get_word
	os.system('python dic.py %s > temp' %get_word.encode('utf-8'))
	word_explination = open('temp', 'r').read()
	if len(word_explination) == 0:
		text.insert(END, 'Sorry, can not find it!')
	text.insert(END, word_explination)

text = Text(root, width = 40, height = 20)
# word_input 单词输入, word_explination 单词解释
word_input = StringVar()
word_input.set('')
entry = Entry(root, textvariable = word_input)
# 按钮行为绑定
button = Button(root, text = "查询")
button.bind('<Button-1>', button_press)
# 组件布局
entry.grid(row = 0, column = 0)
button.grid(row = 0, column = 1)
text.grid(row = 1, column = 0, columnspan = 2)
# 全局调整
root.geometry('280x327+300+300')
# 这个是焦点设置，很实用
entry.focus_force()
mainloop()
