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