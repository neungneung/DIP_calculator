import tkinter as tk

class mycalculator:
    number_now = 0
    number_last = 0
    operator = ""
    def __init__(self):

      self.root = tk.Tk()
      self.label_text = tk.StringVar()
      self.label_text.set("mycalculator")

      self.root.geometry ("300x370")
      self.root.title(mycalculator)

      self.label = tk.Label(self.root, textvariable=self.display, font=('Arial', 18))
      self.label.pack()

      self.button = tk.Button(self.root, text="AC", height=3, width=7)
      self.button.place(x=20, y=50)
      self.button = tk.Button(self.root, text="7", height=3, width=7)
      self.button.place(x=20, y=110)
      self.button = tk.Button(self.root, text="4", height=3, width=7)
      self.button.place(x=20, y=170)
      self.button = tk.Button(self.root, text="1", height=3, width=7)
      self.button.place(x=20, y=230)
      self.button = tk.Button(self.root, text="0", height=3, width=16)
      self.button.place(x=20, y=290)
      self.button = tk.Button(self.root, text="+/-", height=3, width=7)
      self.button.place(x=85, y=50)
      self.button = tk.Button(self.root, text="8", height=3, width=7)
      self.button.place(x=85, y=110)
      self.button = tk.Button(self.root, text="5", height=3, width=7)
      self.button.place(x=85, y=170)
      self.button = tk.Button(self.root, text="2", height=3, width=7)
      self.button.place(x=85, y=230)
      self.button = tk.Button(self.root, text="%", height=3, width=7)
      self.button.place(x=150, y=50)
      self.button = tk.Button(self.root, text="9", height=3, width=7)
      self.button.place(x=150, y=110)
      self.button = tk.Button(self.root, text="6", height=3, width=7)
      self.button.place(x=150, y=170)
      self.button = tk.Button(self.root, text="3", height=3, width=7)
      self.button.place(x=150, y=230)
      self.button = tk.Button(self.root, text=".", height=3, width=7)
      self.button.place(x=150, y=290)
      self.button = tk.Button(self.root, text="/", height=3, width=7)
      self.button.place(x=215, y=50)
      self.button = tk.Button(self.root, text="*", height=3, width=7)
      self.button.place(x=215, y=110)
      self.button = tk.Button(self.root, text="-", height=3, width=7)
      self.button.place(x=215, y=170)
      self.button.bind('<Button-1>',self.action_02)
      self.button = tk.Button(self.root, text="+", height=3, width=7)
      self.button.place(x=215, y=230)
      self.button.bind('<Button-1>',self.action_01)
      
      self.button = tk.Button(self.root, text="=", height=3, width=7)
      self.button.place(x=215, y=290)


      self.root.mainloop()
    
    def c(self):
      if self.operator == "":return
      self.number_now = eval("self.number_last"+self.operator+"self.number_now")

    def action_01(self, event):
       self.c()
       self.operator = "+"
       self.number_last = self.number_now
       self.display.set(str(self.number_now))
       self.number_now = 0
       print(event)
    
    def action_02(self, event):
       self.c()
       self.operator = "-"
       self.number_last = self.number_now
       self.display.set(str(self.number_now))
       self.number_now = 0
       print(event)
       
       

mycalculator()
