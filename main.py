import random
import os
from art import logo
from art import vs
from game_data import data

point = 0
index = random.randint(0, len(data) - 1)
index_b = random.randint(0, len(data) - 1)

a_followers = data[index]['follower_count']
b_followers = data[index_b]['follower_count']

def correct_answer(a_flw, b_flw):
  if a_flw > b_flw:
    return 'a'
  else:
    return 'b'


print(logo)
print(f"Compare A: {data[index]['name']}, a {data[index]['description']}, from {data[index]['country']}")
print(vs)

print(f"Against B: {data[index_b]['name']}, a {data[index_b]['description']}, from {data[index_b]['country']}")

answer = input("Who has more followers? Type 'A' or 'B': ")

check = answer == correct_answer(a_followers, b_followers)


if check:
  print("You are right!")
  point+=1
else:
  print("You are wrong!")

while check:
  os.system('cls')
  index = index_b
  index_b = random.randint(0, len(data) - 1)
  print(f"Your total point is: {point}")
  print(f"A followers: {a_followers}")
  print(f"B followers: {b_followers}")

  print(a_followers > b_followers)
   
    




# for name in data:
#   print(name['name'])