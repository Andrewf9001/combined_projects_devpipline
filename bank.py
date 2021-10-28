total = 0

def withdrawel():
  global total
  
  withdrawel_input = float(input("How much would you like to withdrawl? (0 to cancel): "))
  withdrawn_total = total - withdrawel_input
  
  if withdrawn_total < 0:
    total
    print(f"\nThis exceeds your balance of ${total:.2f}\n")
    withdrawel()
  elif withdrawn_total > 0:
    total -= withdrawel_input
    print(f"\nPlease take your ${withdrawel_input:.2f}. Your balance is now ${total:.2f}")
  elif withdrawel_input == 0:
    pass


def deposit():
  global total
  deposit_input = float(input("\nHow much would you like to deposit? \n"))
  total += deposit_input
  print(f"\nYou have deposited ${total:.2f}\n")


def balance():
  global total
  print(f"\nYour current balance is {total:.2f}\n")


def bank_start():
  
  while True:
    print("\nPlease select from the following menu options")
    user_input = input("(B)alance\n(D)eposit\n(W)ithdraw\n(Q)uit\n")

    if user_input.lower() == 'q':
      print("Thank you for using the Python Bank")
      break
    elif user_input.lower() == 'b':
      balance()
    elif user_input.lower() == 'd':
      deposit()
    elif user_input.lower() == 'w':
      print(f"\nYou currently have a balance of ${total:.2f}\n")
      withdrawel()

