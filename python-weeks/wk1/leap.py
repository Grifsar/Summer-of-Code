print("Let's calculate leap years. This program will check to see if the start year and the end year are leap years")
start_year = input("Please give me the first year ")
#check valid year function
def valid_year(checkYear):
 while(checkYear.isalpha()):
  checkYear = input("That is not a valid year. Please enter a valid year. ")
 return checkYear
start_year = valid_year(start_year)
end_year = input("Please give me the second year ")
end_year = valid_year(end_year)
while(int(end_year) <= int(start_year)):
 end_year = input("The ending year can't be before the starting year. ")
 end_year = valid_year(end_year)
current_year = int(start_year)
print("The following years are leap years:")
while(current_year <= int(end_year)):
  if(current_year%400 == 0):
   print(current_year)
   current_year+=1
  elif(current_year%4 == 0 and current_year%100 != 0):
   print(current_year)
   current_year+=1
  else:
   current_year+=1