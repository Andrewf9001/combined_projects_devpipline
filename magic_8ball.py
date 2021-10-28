import random

def magic_ball():
  answer = True

  while answer:
    question = input("\nAsk the magic 8 ball a question: (press enter to quit) ")
    answers = random.randint(1,20)

    if question == "":
      print("\nOkay, goodbye!\n")
      break
    elif answers == 1:
      print("\nIt is certain.")
    elif answers == 2:
      print("\nIt is decidedly so.")
    elif answers == 3:
      print("\nWithout a doubt.")
    elif answers == 4:
      print("\nYes definitely.")
    elif answers == 5:
      print("\nYou may rely on it.")
    elif answers == 6:
      print("\nAs I see it, yes.")
    elif answers == 7:
      print("\nMost likely.")
    elif answers == 8:
      print("\nOutlook good.")
    elif answers == 9:
      print("\nYes.")
    elif answers == 10:
      print("\nSigns point to yes.")
    elif answers == 11:
      print("\nReply hazy, try again.")
    elif answers == 12:
      print("\nAsk again later.")
    elif answers == 13:
      print("\nBetter not tell you now.")
    elif answers == 14:
      print("\nCannot predict now.")
    elif answers == 15:
      print("\nConcentrate and ask again.")
    elif answers == 16:
      print("\nDon't count on it.")
    elif answers == 17:
      print("\nMy reply is no.")
    elif answers == 18:
      print("\nMy sources say no.")
    elif answers == 19:
      print("\nOutlook not so good.")
    elif answers == 20:
      print("\nVery doubtful.")