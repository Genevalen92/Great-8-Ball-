import random 
import time

def intro():
  print("Welcome to the great computer eight ball.")
  time.sleep(1)
  print("Where questions you ask will be answered.")
  com_opt = ["Y", "N", "M", "C", "L", "T"]
  com_ans = random.choice(com_opt)
  ans = input("Ask the great computer your question.  ")

  if com_ans == "Y":
    print(f"You asked {ans} and the great computer says Yes.")
  elif com_ans == "N":
    print(f"You asked {ans} and the great computer says No.")
  elif com_ans == "M":
    print(f"You asked {ans} and the great computer says Maybe.")
  elif com_ans == "C":
    print(f"You asked {ans} and the great computer says that its not in the cards buddy")
  elif com_ans == "L":
    print(f"You asked {ans} and the great computer says its likely but don't hold your breath.")
  else:
    print(f"You asked {ans} but the great computer wants you to try again.")
    

  again = input("Would you like to ask the great computer another question? ").lower()

  if again != "yes":
      print("Thanks!!")
  else:
    return intro()
      

  


intro()
