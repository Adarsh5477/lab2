# 1. LIST
# Write a PYTHON script with List comprehension for the following
# • Is the given list divisible by 3 or NOT?
# • Square of even numbers in a list
# • Sum of digits of all EVEN numbers in a list
# • Remove duplicate numbers in a list
#dummy comment.

my_list=[19,39,50,20,20,25,30,33,37,12]

#Q1.1 Is the given list divisible by 3 or NOT?
updated_list=[x if x%3==0 else "Not Divisible by 3" for x in my_list]
print(updated_list)

#Q1.2 Square of even numbers in a list
upadted_squared_list=[x*x if x%2==0 else x for x in my_list]
print("The upadated squared list is ",upadted_squared_list)

#Q1.3 Sum of digits of all EVEN numbers in a list
def calc_sum(x):
    sum=0
    temp=x
    while(temp>0):
        rem=temp%10
        sum=sum+rem
        temp=int(temp/10)
    return sum
                  
upadted_sum_list=[calc_sum(x) if x%2==0 else x for x in my_list]
print("original list:",my_list)

print("updated list",upadted_sum_list)

#Q1.4 Remove duplicate numbers in a list

removed_duplicate_list1=[]
[removed_duplicate_list1.append(x) for x in my_list if x not in removed_duplicate_list1 ]
print("original list:",my_list)
print("updated list after removing ",removed_duplicate_list1)

# 2. Dictionary
# Create a dictionary to store the details of your company employees (name as key and
# birthdate as value).
# { ‘Virat Kohli’: ‘5 November 1988’, ‘Umesh Yadav’: ‘25 October 1987’, ‘Manish Pandey’:
# ‘10 September 1989’, ‘Rohit Sharma’: ‘30 April 1987’, ‘Ravindra Jadeja’: ‘6 December
# 1988’, ‘Hardik Pandya’: ‘11 October 1993’ }
# Write a function birthDate() that takes the full name of your employees(as a string) and
# displays the given employee’s birthdate.
# >>>birthDate(‘Rohit Sharma’)
# ‘30 April 1987’

#Q2 DICT
employee_detals={ "Virat Kohli": "5 November 1988", "Umesh Yadav": "25 October 1987", "Manish Pandey":
 "10 September 1989", "Rohit Sharma": "30 April 1987", "Ravindra Jadeja": "6 December1988", "Hardik Pandya": "11 October 1993" }

def birthDate(name):
    print(employee_detals[name])

birthDate("Virat Kohli")
