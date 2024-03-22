# # from tkinter import *
# # from mybutton import MyButton


# class MineSweeper:
#     window = Tk()
#     window.title('MineSweeper')
#     ROW = 5
#     COLLUMNS = 5
#     MINES = 5
#     IS_GAMEOVER = False

#     def __init__(self):

#      self.buttons = []
#      for i in range(self.ROW+2):
#             temp = []
#             for j in range(self.COLLUMNS+2):
#                 btn = MyButton(self.window, x=i, y=j)
#                 btn.config(
#                     text='b', command=lambda button=btn: self.click(button))
#                 btn.bind('<Button-3>', self.right_click)
#                 temp.append(btn)
#                 self.buttons.append(temp)

#     def right_click(self):
#                     pass
#     def click(self, click_button: MyButton):
#                     pass
