# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defied as below. def hello_name (user_name):

def hello_name (user_name):
    
    user_name = ("Lexter Cayabyab")
    message = "hello" + user_name.title() + "!"
    print (message)



# Question 2
# Write a python function, first_odds that prints the odd numbers 1-100 and returns nothing 
def first_odds():

number = 100

for num in range(1, number + 1, 2):
   print(num, end=" ")



# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of code has been defined as below.
def max_num_in_list (a_list):
   
    num = [5, 65, 874, 15, 54, 1092]
    print max(num)



# Question 4
# Write a funmction to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year (a_year):
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False
  

year = input("Enter the year you want to check:")
if(checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")



# Question 5
# Write a function to check to see if all numbers in the lists are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but {1,2,4,5} are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):

listA = [14, 17, 19, 15, 16, 18]
sorted_list = sorted(listA)
range_list=list(range(min(listA), max(listA)+1))
if sorted_list == range_list:
   print("listA has consecutive numbers")
else:
   print("listA has no consecutive numbers")

listB = [6, 8, 15, 32, 17, 4]
sorted_list = sorted(listB)
range_list=list(range(min(listB), max(listB)+1))
if sorted_list == range_list:
   print("ListB has consecutive numbers")
else:
   print("ListB has no consecutive numbers")
