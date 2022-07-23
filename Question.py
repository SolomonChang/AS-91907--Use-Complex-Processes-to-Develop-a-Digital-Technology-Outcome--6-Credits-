# import random code to use
import random

# class for the questions
class Question:
  def __init__(self, description, options):
    self.description = description
    self.options = options
    index = random.randint(0, 2)
    self.options[0], self.options[index] = self.options[index], self.options[0]
    self.answer_index = index
    
# Funtion for the question
  def get_question(self):
    return(self.description)
 
# Funtion for the option  
  def get_option1(self):
    return(self.options[0])
  
  # Funtion for the option  
  def get_option2(self):
    return(self.options[1])
  
    # Funtion for the option  
  def get_option3(self):
    return(self.options[2])
  
    # Funtion for the answer 
  def answer_check(self, number):
    return number == self.answer_index
    
    
