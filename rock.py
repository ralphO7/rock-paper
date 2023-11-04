import random 


mylist = ('scissors', "rock", "paper")

def get_input():
  try:
    user_choice = None

    while not user_choice:
      while user_choice not in mylist:
        user_choice = str(input('select  '))
  except ValueError:
    print('oops')
  except :
    print("bye")


user_choice = get_input() 


def get_bot_choice():
  computer_choice = random.choice(mylist)
  return computer_choice


def get_res(value1, value2):
  if value1 == value2:
    print("Tie")

  elif value1 == "rock" and value2 == "scissors":
    print("You win, the bot chose rock, and you chose scissors.")

  elif value1 == "rock" and value2 == "paper":
    print("You lose, the bot chose rock, and you chose paper.")

  elif value1 == "paper" and value2 == "scissors":
    print("You lose, the bot chose paper, and you chose scissors.")


result = get_res(value1=get_bot_choice(), value2=user_choice)

print(result)
