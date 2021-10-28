def christmas_tree():
  num = int(input("Please enter the number of rows: "))
  trunk = (" " *(num - 2) + "***")

  for n in range(1, num + 1):
    print(" " * (num - n) + "* " * n)

  print(trunk + "\n" + trunk)