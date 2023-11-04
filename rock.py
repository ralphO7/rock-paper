import random 


mylist = ['scissors', "rock", "paper"]

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
  rand = random.randint(0, 2)
  computer_choice = mylist[rand]
  return computer_choice


def get_res(value1, value2) -> str:

  if value1 == value2:
    return "Tie"
  
  elif value1 == "rock" and value2 == "scissors":
    return "You win, the bot chose rock, and you chose scissors."
  
  elif value1 == "scissors" and value2 == "rock":
    return "You win, the bot chose rock, and you chose scissors."

  elif value1 ==" paper" and value2 == "rock":
    "You lose, the bot chose rock, and you chose paper."
  
  elif value1 =="rock" and value2 == "paper":
    "You lose, the bot chose rock, and you chose paper."

  elif value1 == "paper" and value2 == "scissors":
    return "You lose, the bot chose paper, and you chose scissors."
  
  elif value1 == "scissors" and value2 == "paper":
    return "You lose, the bot chose paper, and you chose scissors."

  return "Invalid input or a tie occurred."

print(get_bot_choice())
print(get_res(value2=user_choice, value1=get_bot_choice()))
