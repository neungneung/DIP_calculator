import tkinter as tk

class mycalculator:
    def __init__(self):

      self.root = tk.Tk()
<<<<<<< HEAD
<<<<<<< HEAD
      self.display = tk.StringVar()
=======
      self.label_text = tk.StringVar()
      self.label_text.set("mycalculator")
>>>>>>> fea

      self.root.geometry ("300x370")
      self.root.title(mycalculator)

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


      self.root.mainloop()

<<<<<<< HEAD
    def action_03(self, event):
      self.display.set("*")
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
