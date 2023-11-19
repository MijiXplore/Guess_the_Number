import random
from art import logo, vs
from game_data import data
import os

def format_account(account):
  """Takes the account data and return in printable format"""
  account_name = account['name']
  account_desr = account['description']
  account_ctr = account['country']
  return f"{account_name}, a {account_desr}, from {account_ctr}"

def check_answer(guess, a_followers, b_followers):
  """Takes guess and compare with correct answer then returns true or false"""
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'

print(logo)
point = 0
game_continues = True

account_a = random.choice(data)
account_b = random.choice(data)

while game_continues:
  account_a = account_b
  if account_a == account_b:
    account_b = random.choice(data)

  a_followers = account_a['follower_count']
  b_followers = account_b['follower_count']
  
  print(f"Compare: {format_account(account_a)}")
  print(vs)
  print(f"Against: {format_account(account_b)}")

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  is_correct = check_answer(guess, a_followers, b_followers)
  
  os.system('cls')
  print(logo)
  if is_correct:
    point += 1
    print(f"You are right. Score: {point}")
  else:
    game_continues = False
    print(f"Sorry, You are wrong. Final score: {point}")