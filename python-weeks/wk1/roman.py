number = input("Please enter a number. ")
while number.isalpha() == True:
  number = input("That isn't a number. Please enter a number. ")

def to_old_roman(n):
  if(int(n) == 0):
    return 0
  old_roman = ""
  if int(n)//1000 > 0:
    amount_m = int(n)//1000
    old_roman = old_roman + "M" * amount_m
    n = int(n) - int(amount_m)*1000
    to_old_roman(n)
  if int(n)//500 > 0:
    amount_d = int(n)//500
    old_roman = old_roman + "D" * amount_d
    n = int(n) - int(amount_d)*500
    to_old_roman(n)
  if int(n)//100 > 0:
    amount_c = int(n)//100
    old_roman = old_roman + "C" * amount_c
    n = int(n) - int(amount_c)*100
    to_old_roman(n)
  if int(n)//50 > 0:
    amount_l = int(n)//50
    old_roman = old_roman + "L" * amount_l
    n = int(n) - int(amount_l)*50
    to_old_roman(n)
  if int(n)//10 > 0:
    amount_x = int(n)//10
    old_roman = old_roman + "X" * amount_x
    n = int(n) - int(amount_x)*10
    to_old_roman(n)
  if int(n)//5 > 0:
    amount_v = int(n)//5
    old_roman = old_roman + "V" * amount_v
    n = int(n) - int(amount_v)*5
    to_old_roman(n)
  if int(n)//1 > 0:
    amount_i = int(n)//1
    old_roman = old_roman + "I" * amount_i
    n = int(n) - int(amount_i)*5
    to_old_roman(n)
  return old_roman

def to_new_roman(n):
  if(int(n) == 0):
    return 0
  new_roman = ""
  if int(n)//1000 > 0:
    amount_m = int(n)//1000
    new_roman = new_roman + "M" * amount_m
    n = int(n) - int(amount_m)*1000
    to_new_roman(n)
  if int(n)//900 > 0:
    amount_cm = int(n)//900
    new_roman = new_roman + "CM" * amount_cm
    n = int(n) - int(amount_cm)*900
    to_new_roman(n)
  if int(n)//500 > 0:
    amount_d = int(n)//500
    new_roman = new_roman + "D" * amount_d
    n = int(n) - int(amount_d)*500
    to_new_roman(n)
  if int(n)//400 > 0:
    amount_cd = int(n)//400
    new_roman = new_roman + "CD"
    n = int(n) - int(amount_cd)*400
    to_new_roman(n)
  if int(n)//100 > 0:
    amount_c = int(n)//100
    new_roman = new_roman + "C" * amount_c
    n = int(n) - int(amount_c)*100
    to_new_roman(n)
  if int(n)//90 > 0:
    amount_xc = int(n)//90
    new_roman = new_roman + "XC"
    n = int(n) - int(amount_xc)*90
    to_new_roman(n)
  if int(n)//50 > 0:
    amount_l = int(n)//50
    new_roman = new_roman + "L" * amount_l
    n = int(n) - int(amount_l)*50
    to_new_roman(n)
  if int(n)//40 > 0:
    amount_xl = int(n)//40
    new_roman = new_roman + "XL"
    n = int(n) - int(amount_xl)*40
    to_new_roman(n)
  if int(n)//10 > 0:
    amount_x = int(n)//10
    new_roman = new_roman + "X" * amount_x
    n = int(n) - int(amount_x)*10
    to_new_roman(n)
  if int(n)//9 > 0:
    amount_ix = int(n)//9
    new_roman = new_roman + "IX"
    n = int(n) - int(amount_ix)*9
    to_new_roman(n)
  if int(n)//5 > 0:
    amount_v = int(n)//5
    new_roman = new_roman + "V" * amount_v
    n = int(n) - int(amount_v)*5
    to_new_roman(n)
  if int(n)//4 > 0:
    amount_iv = int(n)//4
    new_roman = new_roman + "IV"
    n = int(n) - int(amount_iv)*4
    to_new_roman(n)
  if int(n)//1 > 0:
    amount_i = int(n)//1
    new_roman = new_roman + "I" * amount_i
    n = int(n) - int(amount_i)*5
    to_new_roman(n)
  return new_roman

print("The old roman numeral for that number is " + to_old_roman(number))
print("The new roman numeral for that number is " + to_new_roman(number))