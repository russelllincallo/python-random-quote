import random

def primary():
  print("Keep it logically awesome.")

  #quotes_0
  last0 = 15
  rnd0 = random.randint(0, last0)
  f0 = open("quotes_0.txt")
  quotes0 = f0.readlines()
  f0.close()
  print(quotes0[rnd0])
  
  #quotes_1
  last1 = 19
  rnd1 = random.randint(0, last1)
  f1 = open("quotes_1.txt")
  quotes1 = f1.readlines()
  f1.close()
  print(quotes1[rnd1])

if __name__== "__main__":
  primary()
