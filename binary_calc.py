def continue_func():
  print()
  print("Press <enter> to continue")
  print("-"*30)
  input()

# Decimal to Binary
def dec_to_bin(dec_num):
  original_num = int(dec_num)
  binary_num = [128,64,32,16,8,4,2,1]
  binary = []
  bin_string = ''

  for num in binary_num:
    if original_num >= num:
      original_num -= num
      binary.append(1)
    else:
      binary.append(0)

  for original_num in binary:
    bin_string += str(original_num)

  return bin_string

# Binary to Decimal Conversion
def bin_to_dec(bin_str):
  binary_string = str(bin_str)
  bin_to_list = list(binary_string)
  value = 0

  for num in range(len(bin_to_list)):
    digit = bin_to_list.pop()
    if digit == '1':
      value = value + pow(2, num)
  
  return value


def bin_inverse(bin_str):
  output = ''
  neg_output = ''

  if bin_str[0] == '0':
    for el in bin_str:
      if el == '1':
        output += '0'
      else:
        output += '1'

    add_one = bin_add(output, '1')
    return add_one
     
  elif bin_str[0] == '1':
    sub_one = bin_sub(bin_str, '1')
    for el in sub_one:
      if el == '0':
        neg_output += '1'
      elif el == '1':
        neg_output += '0'
    return neg_output


def bin_add(bin_str_1, bin_str_2):
  max_width = max(len(bin_str_1), len(bin_str_2))
  bin_str_1 = bin_str_1.zfill(max_width)
  bin_str_2 = bin_str_2.zfill(max_width)

  output = ''
  carry = 0
  for i in reversed(range(len(bin_str_1))):
    if carry == 0:
      if bin_str_1[i] == '0' and  bin_str_2[i] == '0':
        output = output + '0'
        carry = 0
      elif bin_str_1[i] == '1' and  bin_str_2[i] == '1':
        output += '0'
        carry = 1
      else:
        output += '1'
        carry = 0
    else:
      if bin_str_1[i] == '0' and  bin_str_2[i] == '0':
        output = output + '1'
        carry = 0
      elif bin_str_1[i] == '1' and  bin_str_2[i] == '1':
        output += '1'
        carry = 1
      else:
        output += '0'
        carry = 1
  if carry == 1:
    output += '1'
  return output[::-1]


def bin_sub(bin_str_1, bin_str_2):
  max_length = max(len(bin_str_1), len(bin_str_2))
  bin_str_1 = bin_str_1.zfill(max_length)[::-1]
  bin_str_2 = bin_str_2.zfill(max_length)[::-1]
  output = ''
  borrow = 0

  for i in range(max_length):
    num1 = bin_str_1[i]
    num2 = bin_str_2[i]
      
    if borrow == 1:
        if num1 == '1':
          num1 = '0'
          borrow = 0
        else:
          num1 = '1'
    if num1 == num2:
        output += '0'
    elif num1 == '1':
        output += '1'
    else:
        output += '1'
        borrow = 1

  if borrow == 1:
    return "Error: Negative Result"

  return output[::-1] 


def bin_div(bin_str_1, bin_str_2):
  if bin_sub(bin_str_1, bin_str_2) == "Error: Negative Result":
    return "Error: No fractions allowed"
   
  output = ''
  result = ''

  for i, ch in enumerate(bin_str_1):
    result += ch
    sub_result = bin_sub(result, bin_str_2)

    if sub_result == "Error: Negative Result":
        output += '0'
    else:
        output += '1'
        result = sub_result
  
  return output


def bin_mul(bin_str_1, bin_str_2):
  output = ''

  for i, el in enumerate(reversed(bin_str_2)):
    if el == '1':
      multi_val = bin_str_1 + ('0' * i)
      output = bin_add(multi_val, output)

  return output


def hex_to_dec(hex_str):
  final_value = 0
  output = ''
  hex_dict = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15
  }

  for i, el in enumerate(hex_str):
    value = hex_dict[el]
    multiply = value * (16 ** (len(hex_str) - (i + 1)))
    final_value += multiply
    output = str(final_value)
  
  return output


def dec_to_hex(dec_num):
  output = ''
  count = 1
  values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  keys = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

  while count != 0:
    floor_div = int(dec_num) // 16
    remainder = int(dec_num) % 16
    index_value = values.index(remainder)
    hex_value = keys[index_value]
    output += hex_value
    dec_num = floor_div
    count = dec_num

  return output[::-1]


def hex_to_bin(hex_str):
  hex_dec_conv = hex_to_dec(hex_str)
  print(hex_dec_conv) 

  dec_bin_conv = dec_to_bin(hex_dec_conv)

  return dec_bin_conv

def bin_to_hex(bin_str):
  bin_hex = bin_to_dec(bin_str)
  dec_hex = dec_to_hex(bin_hex)

  return dec_hex


def menu():
  print("")
  print("  *** Binary Calculator ***")
  print("")
  print("(B)inary to Decimal Conversion")
  print("(Bi)nary to Hexidecimal Conversion")
  print("(D)ecimal to Binary Conversion")
  print("(De)cimal to Hexadecimal Conversion")
  print("(N)egative Binary Conversion")
  print("(H)exadecimal to Decimal Conversion")
  print("(He)xadecimal to Binary Conversion")
  print("(A)dd two Binary Numbers")
  print("(S)ubtract two Binary Numbers")
  print("(M)ultiply two Binary Numbers")
  print(" D(i)vide two Binary Numbers")
  print("(Q)uit")
  print("\n")


def input_one_check():
  user_input = input("Enter the first binary number : ")
  output = ''

  if user_input.isnumeric():
    for num in user_input:
      conv_num = int(num)
      if conv_num > 1 or conv_num < 0:
        print("Invalid digits, please use 1's and 0's")
        continue_func()
        main()
      else:
        output += str(num)
    return output
  else:
    print("Invalid Binary")
    continue_func()
    main()


def input_two_check():
  user_input = input("Enter the second binary number: ")
  output = ''

  if user_input.isnumeric():
    for num in user_input:
      conv_num = int(num)
      if conv_num > 1 or conv_num < 0:
        print("Invalid digits, please use 1's and 0's")
        continue_func()
        main()
      else:
        output += str(num)
    return output
  else:
    print("Invalid Binary")
    continue_func()
    main()


def main():
  while True:
    menu()
    choice = str(input('Enter choice from menu: ')).lower()
    print("")
    if choice == 'b':
      print("")
      bin_input = input("Enter Binary Number (8-digits): ")
      data = ''

      if bin_input.isnumeric():
        for num in bin_input:
          conv_num = int(num)
          if conv_num > 1 or conv_num < 0:
            print("Invalid digits, please use 1's and 0's")
            continue_func()
          else:
            data += str(num)
        binary_value = bin_to_dec(data)
        print(f"Decimal value of the entered binary: {binary_value}")
        continue_func()
      else:
        print("Invalid Binary")
        continue_func()
    elif choice == 'bi':
      bin_hex_input = input("Please enter a Binary number to convert: ")
      bin_hex_conv = bin_to_hex(bin_hex_input)
      print(f"Hexidecimal value of the entered Binary: {bin_hex_conv}")
    elif choice == 'n':
      negative_input = input("Enter in a binary number (0-124): ")
      n_data = ''

      if negative_input.isnumeric():
        for n_num in negative_input:
          negative_int = int(n_num)
          if negative_int > 1 or negative_int < 0:
            print("Invalid digits, please use 1's and 0's")
            continue_func()
          else:
            n_data += str(n_num)
        negative_value = bin_inverse(n_data)
        print(f"Decimal value of the entered binary: {negative_value}")
        continue_func()
      else:
        print("Invalid Binary")
        continue_func()
    elif choice == 'd':
      num_input = input("Enter a Decimal Number (0-255): ")
      if num_input.isnumeric():
        dec_int = int(num_input)
        if dec_int >= 0 and dec_int <= 255:
          dec_str = str(num_input)
          conv_dec = dec_to_bin(dec_str)
          print(f"Binary value is: {conv_dec}")
          continue_func()
        else:
          print("Decimal number out of range")
          continue_func()
      else:
        print("\nInvalid Decimal")
        continue_func()
    elif choice == 'de':
      dec_conv_input = input("Enter a Decimal Number (0-255): ")

      if dec_conv_input.isnumeric():
        dec_hex_conv = dec_to_hex(dec_conv_input)
        print(f"Hexadecimal value is: {dec_hex_conv}")
        continue_func()
      else:
        print("Invalid Decimal")
        continue_func()

    elif choice == 'h':
      hex_conv_input = input("Please enter a Hexadecimal: ")

      hex_dec_conv = hex_to_dec(hex_conv_input)
      print(f"Your Hexadecimal converted to Decimal is: {hex_dec_conv}")
      continue_func()

    elif choice == 'he':
      hex_input = input("Please enter a Hexadecimal to convert: ")
      hex_bin_conv = hex_to_bin(hex_input)
      print(f"Binary value is: {hex_bin_conv}")
      continue_func()


    elif choice == 'a':
      add_one = input_one_check()
      add_two = input_two_check()

      binary_addition = bin_add(add_one, add_two)
      print(f"= {binary_addition}")
      continue_func()
    elif choice == 's':
      sub_one = input_one_check()
      sub_two = input_two_check()

      binary_subtraction = bin_sub(sub_one, sub_two)
      print(f"= {binary_subtraction}")
      continue_func()
    elif choice == 'm':
      mul_one = input_one_check()
      mul_two = input_two_check()
      
      binary_multiplied = bin_mul(mul_one, mul_two)
      print(f"= {binary_multiplied}")
      continue_func()
    elif choice == 'i':
      div_one = input_one_check()
      div_two = input_two_check()

      binary_divide = bin_div(div_one, div_two)
      print(f"= {binary_divide}")
      
      continue_func()
    elif choice == 'q':
      print('Good Bye!')
      break
    else:
      continue