import time
import os


class LCG_Class:
  def __init__(self):
    custom_seed = os.name+os.getcwd()+str(time.time())+os.path.join(os.path.dirname(__file__), "..")+os.path.dirname(__file__)
    self.s = 1
    for i in range(len(custom_seed)):
        ch = custom_seed[i]
        in1 = ord(ch) 
        self.s = self.s * in1
    self.s = int(str(self.s)[:10]) + time.time()
    self.a = 1664525
    self.c = 1013904223
    self.m = 2**32

  def seed(self,seed):
    self.s = seed

  def randnumbers(self,n):
    numbers = []
    for i in range(n):
      self.s = (self.a * self.s + self.c) % self.m
      numbers.append(int(self.s))
      
    return numbers

  def randnumber(self):
    self.s = (self.a * self.s + self.c) % self.m
      
    return int(self.s)

  def randrange(self,start,end):
    return self.choice(range(start,end))

  def randint(self,start, end):
    return self.choice(range(start,(end+1)))

  def choice(self, the_list):
    count = 0
    number = len(the_list)
 
    while (number > 0):
     number = number//10
     count = count + 1
    while True:
     sequance = int(str(self.randnumber())[-count:])
     if not (len(the_list)-1) < sequance:
       return the_list[sequance]

  def shuffle(self,the_list):
    copy_of_list = the_list.copy()
    for i in reversed(range(len(the_list))):
      selection = self.choice(copy_of_list)
      the_list[i] = selection
      copy_of_list.remove(the_list[i])

  def sample(self, the_list, k):
    copy_of_list = the_list.copy()
    self.shuffle(copy_of_list)
    return copy_of_list[-k:]

  def random(self):
    return (self.randint(0, 10**5)/ 10**5)

  def uniform(self,start,end):
    return self.randint(start, end) + self.random()


LCG = LCG_Class()
