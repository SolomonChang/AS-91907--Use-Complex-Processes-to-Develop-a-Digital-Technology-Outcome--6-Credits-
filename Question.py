import random

class Question:
  def __init__(self, description, options):
    self.description = description
    self.options = options
    index = random.randint(0, 2)
    self.options[0], self.options[index] = self.options[index], self.options[0]
    self.answer_index = index

  def get_question(self):
    return(self.description)
  
  def get_option1(self):
    return(self.options[0])
  
  def get_option2(self):
    return(self.options[1])
    
  def get_option3(self):
    return(self.options[2])
    
  def answer_check(self, number):
    return number == self.answer_index
    