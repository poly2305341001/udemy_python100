def clear(): 
  print('') 
  print('') 
  print('')
#HINT: You can call clear() to clear the output in the console.
from d009_module import logo
print(logo)

# participants = {}
# while True:
#   name = input("What is your name?")
#   bid = int(input("How much?"))
#   participants[name] = bid
#   answer = input("more person? yes or no")
#   if answer == "yes":
#     clear()
#   else:
#     break

# max_bid = 0
# for name in participants:
#   if participants[name] > max_bid:
#     max_bid = participants[name]   

# if participants[name] == max_bid:
#   print(f"The winner is {name}, the bid is ${max_bid}")

participants = []

while True:
  name = input("What is your name?")
  bid = int(input("How much?"))
  person = {"name": name, "bid": bid}

  participants.append(person)
  answer = input("more person? yes or no")
  if answer == "yes":
    clear()
  else:
    break

max_bid = participants[0]["bid"]
max_name = ""
for p in participants:
  if p["bid"] > max_bid:
    max_bid = p["bid"]
    max_name = p["name"]

# max_bid = participants[0]["bid"]
# max_name = ""
# for idx in range(0,len(participants)):
#   if participants[idx]["bid"] > max_bid:
#     max_bid = participants[idx]["bid"]
#     max_name = participants[idx]["name"]


print(f"The winner is {max_name}, the bid is ${max_bid}")