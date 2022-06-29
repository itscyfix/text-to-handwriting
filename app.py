import pywhatkit as pw
import time


print("welcome to text to handwriting made by me(kanav/cyfix) you have 2 colors to chose from (red/blue) it may be helpful to those who want to copy and paste their school assignment lmao ")
txt = input("enter the text here : ")
colorr = int(input("what shoulf be the color of pen(blue/red) 1 for blue or 0 for red  :  "))
if colorr == 1:
    colorr = [0,0,138]
else:
    colorr = [255 , 0 , 0]

pw.text_to_handwriting(txt , "demo-$.png" , colorr)
print("see your files you might see demo.png")
time.sleep(5)