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

#value1 : bot 
#value2 : user

def get_res(value1, value2) -> str:
  if value1 == value2:
    return "tie "

  elif value1 == "rock" and value2 == "scissors":
    return "you and idiot u lose"
  
  elif value1 == "rock" and value2 == "paper":
    return "you won"
  
  elif value1 == "paper" and value2 == "scissors":
    return "you won"
  else : return

print(get_bot_choice())  
result = get_res(value2=user_choice, value1=get_bot_choice())
print(result)

