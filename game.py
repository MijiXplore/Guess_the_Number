import random
import os
from art import logo
from art import vs
# Get list
from game_data import data
# generate two items from list to compare
# set a function to get random index)

# Functions
def get_index2_data(data, n):
    """Generates random index for option 2 without repeating option 1"""
    data_copy = data.copy()
    data_copy.pop(n)
    return data_copy

def get_follower_count(data, index):
  """Gets the follower counts for the displayed options"""
  return data[index]['follower_count']

# set a function to get correct answer based on comarison condition
def compare_count(a, b):
  """Checks the the follower counts to determine the higher"""
  if a > b:
    return 'a'
  else:
    return 'b'
  
def correct_answer(answer, compare_count):
    return answer == compare_count
  
def game():
  print(logo)
  print(f"Your total point is: {point}")
  print(f"Compare A: {data[index1]['name']}, a {data[index1]['description']}, from {data[index1]['country']}")
  print(vs)

  print(f"Against B: {data2[index2]['name']}, a {data2[index2]['description']}, from {data2[index2]['country']}")
  # Get the follower_count for the generated items

  # ask user to choose an option
  answer = input("Who has more followers? Type 'A' or 'B': ")
  return answer
  
# Calculations


index1 =  random.randint(0, len(data)-1)
data2 = get_index2_data(data, index1)
index2 = random.randint(0, len(data2)-1)


point = 0

a_follower = get_follower_count(data, index1)
b_follower = get_follower_count(data2, index2)
print(a_follower)
print(b_follower)

answer = game()

# compare user answer with correct answer


# if the answer is wrong, notify user and end game
while correct_answer(answer, compare_count(a_follower, b_follower)):
    point += 1
    os.system('cls')
    print(f"Your total point is: {point}")
    index1 = index2
    data[index1]['name'] = data2[index2]['name']
    data[index1]['description'] = data2[index2]['description']
    data[index1]['country'] = data2[index2]['country']
    a_follower = b_follower
    data2 = get_index2_data(data, index1)
    index2 = random.randint(0, len(data2) - 1)
    # a_follower = get_follower_count(data, index1)
    b_follower = get_follower_count(data2, index2)
    # print(f"Compare A: {data[index1]['name']}, a {data[index1]['description']}, from {data[index1]['country']}")
    # print(f"Against B: {data2[index2]['name']}, a {data2[index2]['description']}, from {data2[index2]['country']}")
    # answer = input("Who has more followers? Type 'A' or 'B': ")
    game()
print("You are wrong. Game over!")
print(f"You scored a total of {point} point(s)")
    
    
#   continue game
#     replace option a with option b
#     generate new option b