import tkinter as tk

class mycalculator:
    def __init__(self):

      self.root = tk.Tk()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
      self.display = tk.StringVar()
=======
      self.label_text = tk.StringVar()
      self.label_text.set("mycalculator")
>>>>>>> fea
=======
      self.label_text = tk.StringVar()
      self.label_text.set("mycalculator")
>>>>>>> dev

      self.root.geometry ("300x370")
      self.root.title(mycalculator)

<<<<<<< HEAD
<<<<<<< HEAD
      self.label = tk.Label(self.root, textvariable=self.display, font=('Arial', 18)) 
=======
      self.label = tk.Label(self.root, textvariable=self.display, font=('Arial', 18))
>>>>>>> fea
=======
      self.label_text = tk.StringVar()
      self.label_text.set("mycalculartor")
  
      self.root.geometry ("300x300")
      self.root.title("mycalculator")

      self.label = tk.Label(self.root, textvariable=self.display, font=('Arial', 18)) 
>>>>>>> origin/feature/add--
=======
      self.label = tk.Label(self.root, textvariable=self.display, font=('Arial', 18))
>>>>>>> dev
      self.label.pack()

      self.button = tk.Button(self.root, text="AC", height=3, width=7)
      self.button.place(x=20, y=50)
      self.button = tk.Button(self.root, text="7", height=3, width=7)
      self.button.place(x=20, y=110)
      self.button.bind("<Button-1>", self.action_7)
      self.button = tk.Button(self.root, text="4", height=3, width=7)
      self.button.place(x=20, y=170)
      self.button.bind("<Button-1>", self.action_4)
      self.button = tk.Button(self.root, text="1", height=3, width=7)
      self.button.place(x=20, y=230)
      self.button.bind("<Button-1>", self.action_1)
      self.button = tk.Button(self.root, text="0", height=3, width=16)
      self.button.place(x=20, y=290)
      self.button.bind("<Button-1>", self.action_0)
      self.button = tk.Button(self.root, text="+/-", height=3, width=7)
      self.button.place(x=85, y=50)
      self.button = tk.Button(self.root, text="8", height=3, width=7)
      self.button.place(x=85, y=110)
      self.button.bind("<Button-1>", self.action_8)
      self.button = tk.Button(self.root, text="5", height=3, width=7)
      self.button.place(x=85, y=170)
      self.button.bind("<Button-1>", self.action_5)
      self.button = tk.Button(self.root, text="2", height=3, width=7)
      self.button.place(x=85, y=230)
      self.button.bind("<Button-1>", self.action_2)
      self.button = tk.Button(self.root, text="%", height=3, width=7)
      self.button.place(x=150, y=50)
      self.button = tk.Button(self.root, text="9", height=3, width=7)
      self.button.place(x=150, y=110)
      self.button.bind("<Button-1>", self.action_9)
      self.button = tk.Button(self.root, text="6", height=3, width=7)
      self.button.place(x=150, y=170)
      self.button.bind("<Button-1>", self.action_6)
      self.button = tk.Button(self.root, text="3", height=3, width=7)
      self.button.place(x=150, y=230)
      self.button.bind("<Button-1>", self.action_3)
      self.button = tk.Button(self.root, text=".", height=3, width=7)
      self.button.place(x=150, y=290)
      self.button = tk.Button(self.root, text="/", height=3, width=7)
<<<<<<< HEAD
      self.button.place(x=215, y=50)
      self.button = tk.Button(self.root, text="*", height=3, width=7)
      self.button.place(x=215, y=110)
      self.button.bind("<Button-1>", self.action_03)
=======
      self.button.bind('<Button-1>', self.action_04)

      self.button.place(x=215, y=50)
      self.button = tk.Button(self.root, text="*", height=3, width=7)
      self.button.place(x=215, y=110)
>>>>>>> origin/feature/add--
      self.button = tk.Button(self.root, text="-", height=3, width=7)
      self.button.place(x=215, y=170)
      self.button = tk.Button(self.root, text="+", height=3, width=7)
      self.button.place(x=215, y=230)
<<<<<<< HEAD
      self.button.bind('<Button-1>',self.action_01)
      
      self.button = tk.Button(self.root, text="=", height=3, width=7)
      self.button.place(x=215, y=290)
      self.button.bind("<Button-1>", self.action_00)


      self.root.mainloop()

<<<<<<< HEAD
    def action_03(self, event):
      self.display.set("*")
      print(event)
    
    def action_00(self, event):
      self.display.set("=")
      print(event)
    def action_0(self, event):
      self.display.set("0")
      print(event)
    def action_1(self, event):
      self.display.set("1")
      print(event)
    def action_2(self, event):
      self.display.set("2")
      print(event)
    def action_3(self, event):
      self.display.set("3")
      print(event)
    def action_4(self, event):
      self.display.set("4")
      print(event)
    def action_5(self, event):
      self.display.set("5")
      print(event)
    def action_6(self, event):
      self.display.set("6")
      print(event)
    def action_7(self, event):
      self.display.set("7")
      print(event)
    def action_8(self, event):
      self.display.set("8")
      print(event)
    def action_9(self, event):
      self.display.set("9")
      print(event)
      

<<<<<<< HEAD

=======
>>>>>>> feature/add
=======
    def action_01(self, event):
       self.display.self("+")
       print(event)
       

>>>>>>> fea
=======
      self.button = tk.Button(self.root, text="=", height=3, width=7)
      self.button.place(x=215, y=290)
      self.root.mainloop()

    def action_04(self, event):
       self.display.set("/")
       print(event)
     

>>>>>>> origin/feature/add--
mycalculator()
