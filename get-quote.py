import random
def primary():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) -1
  why = random.randint(0, last)
  #print(quotes[why])
  print(quotes[15])
  print(quotes[14])
  print(quotes[13])
if __name__== "__main__":
  primary()
