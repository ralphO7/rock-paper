import random 


mylist = ['pierre', "papier", "scisseau"]

def get_input():
  try:
    user_choice = None

    while not user_choice:
      user_choice = str(input('select'))
  except:
    print('oops')


user_choice = get_input() 

def get_bot_choice():
  rand = random.randint(0, 2)
  computer_choice = mylist[rand]
  return "I selected {}".format(computer_choice)

#value1 : bot 
#value2 : user

def get_res(value1, value2):
  if value1 == value2:
    print("tie")



