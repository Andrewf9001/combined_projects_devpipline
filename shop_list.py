import os

def add_item():
  with open("shopping_list.txt", "a", 1) as shop_file:

    while True:
      shop_input = input("\nWhat would you like to add ('Return' to return to main menu)?\n")
      if shop_input.lower() == 'return':
        break
      else:
        shop_file.write(shop_input + "\n")
        print(f'\n"{shop_input.title()}" has been added to the shopping list')


def clear_list():
  with open("shopping_list.txt", "w") as shop_file:
    print("\nYour shopping list has been cleared")


def print_list():
  filesize = os.path.getsize("shopping_list.txt")

  if filesize == 0:
    print(f"\nThere are 0 items in your shopping list\n")
  else:
    with open("shopping_list.txt", "r") as shop_file:
      shop_list = shop_file.readlines()
      print("\nYour shopping list:")
      
      for item in shop_list:
        titled = item.title()
        print(titled.strip())
    
    print()


def shop_start():

  while True:
    print("\n--------------------------")
    print("What would you like to do?\n")
    shopping_input = input("(P)rint the shopping list\n(A)dd an item to the shopping list\n(C)lear the shopping list\n(Q)uit\n")

    if shopping_input.lower() == 'q':
      print("\nExiting the program. Your shopping list has been saved in 'shopping_list.txt'.\nGoodbye!")
      break
    elif shopping_input.lower() == 'p':
      print_list()
    elif shopping_input.lower() == 'c':
      clear_list()
    elif shopping_input.lower() == 'a':
      add_item()