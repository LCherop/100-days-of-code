import random
from game_data import data
from art import logo,vs
from os import system



def retrieve():
  personA = random.choice(data)
  print("Compare A: "+personA["name"] + ", "+ personA["description"] +", "+ personA["country"])
  print(vs)
  personB = random.choice(data)
  print("Compare B: "+personB["name"] + ", "+personB["description"] +", "+ personB["country"])
  return personA["follower_count"],personB["follower_count"]

def compare():
  score = 0
  fc1 ,fc2 = retrieve()
  entry = input("Who has more followers? Type A or B: ")

  if fc1 > fc2 and entry == "A":
    score += 1
    system('cls')
    compare()
  elif fc2 > fc1 and entry == "B":
    score += 1
    system('cls')
    compare()
  else:
    system('cls')
    print(f"Whoops it's game over. You have scored {score}")
    return 

print(logo)
compare()

