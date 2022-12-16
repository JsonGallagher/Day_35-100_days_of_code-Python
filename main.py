import os
import time

# Set empty list
myList = []

# Clear screen function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Display list function
def view_list():
  cls()
  print("Here's what you have on your to do list currently: ")
  i = 1
  for item in myList:
      print(f"{i}) {item}")
      i += 1
  print()

print("TO DO LIST MANAGER 📝")
print()

while True:
  command = input("Do you want to view, add, remove, clear, or edit an item on your to do list? ")
  if command.lower() == 'view':
    cls()
    if not myList:
      print("You do not have anything on your list")
      print()
    else:
      view_list()
  elif command.lower() == 'add':
    print()
    item = input("What would you like to add to the list? ").title()
    myList.append(item)
    view_list()
  elif command.lower() == 'remove':
    remove_item = input("What would you like to remove from the list? ").title()
    confirm_removal = input("Are you sure you want to remove this? y or n ")
    if confirm_removal.lower() == 'y':
      if remove_item in myList:
          myList.remove(remove_item)
          view_list()
      else:
        print()
        print("Invalid entry")
        time.sleep(2)
        break
  elif command.lower() == 'clear':
    myList.clear()
    view_list()
  elif command.lower() == 'edit':
    idx = int(input("Which item # would you like to edit? ")) - 1
    edited_item = input("What would you like it to say? ").title()
    myList[idx] = edited_item
    view_list()
  else:
    print('Please enter a valid command')
    print()
    continue