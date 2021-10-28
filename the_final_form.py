from bank import bank_start
from binary_calc import main
from calendar import calendar_start
from christmas_tree import christmas_tree
from magic_8ball import magic_ball
from shop_list import shop_start

def continue_func():
  print()
  print("Press <enter> to continue")
  print("-"*30)
  input()

print("\nWelcome please select from the following options")

def final_form():
  while True:
    print()
    print("(B)ank\n(Bi)nary Calculator\n(C)alendar\n(Ch)ristmas Tree\n(M)agic 8-Ball\n(S)hopping List")
    print("\nPress enter or 'Q' to quit")
    choice = input().lower()

    if choice == '' or choice == 'q':
      print('\nThank you for coming, Goodbye\n')
      break
    elif choice == 'b':
      bank_start()
      continue_func()
    elif choice == 'bi':
      main()
      continue_func()
    elif choice == 'c':
      calendar_start()
      continue_func()
    elif choice == 'ch':
      christmas_tree()
      continue_func()
    elif choice == 'm':
      magic_ball()
      continue_func()
    elif choice == 's':
      shop_start()
      continue_func()


final_form()