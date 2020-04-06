
# coding: utf-8

# In[ ]:


import random
import string



def user_details():
    for k ,v in user_details_1.items():
        print(k +  v)
    for k ,v in user_details_2.items():
        print(k +  v)
    

user_details_1 = {}
first_name_1 =input('Enter your first name: ')
user_details_1.update({ 'first_name1: ': first_name_1,})
last_name_1 = input('Enter your last name: ')
user_details_1.update({ 'last_name1: ': last_name_1, })
e_mail_1 = input('Enter your e_mail: ')
user_details_1.update({ 'e_mail1: ': e_mail_1})
    


length = 5
random.choice(string.ascii_lowercase)
result =''.join(random.choice(string.ascii_lowercase)for i in range(length))



password = first_name_1[0:2] + last_name_1[-2:] + result

print(password)


    

    
satisfied_with_password =''
satisfied_with_password = input('Are you satisfied with your password? (Please enter Yes or No):')

if satisfied_with_password =='Yes':
    print(user_details_1)
else:
    your_password = input('Enter your password: ')
    if len(your_password) < 7:
        print('password must be at least seven characters, please try again.')
        your_password = input('Enter your password: ')
    else:
        print(your_password) 

Any_other_customer = ''
Any_other_customer = input('Any other customer? [Yes/No]')
if Any_other_customer == 'Yes':
    user_details_2 = {}
    first_name_2 =input('Enter your first name: ')
    user_details_2.update({ 'first_name2: ': first_name_2,})
    last_name_2 = input('Enter your last name: ')
    user_details_2.update({ 'last_name2: ': last_name_2, })
    e_mail_2 = input('Enter your e_mail: ')
    user_details_2.update({ 'e_mail2: ': e_mail_2})


        
    length = 5
    random.choice(string.ascii_lowercase)
    result =''.join(random.choice(string.ascii_lowercase)for i in range(length))


    password = first_name_2[0:2] + last_name_2[-2:] + result

    print(password)


    satisfied_with_password =''
    satisfied_with_password = input('Are you satisfied with your password? (Please enter Yes or No):')

    if satisfied_with_password =='Yes':
        print(user_details())

    else:
        your_password = input('Enter your password: ')
        if len(your_password) < 7:
            print('password must be at least seven characters, please try again.')
            your_password = input('Enter your password: ')

            print(user_details())
        else:
            print(your_password)  
else:
    for k ,v in user_details_1.items():
        print(k +  v)        
    
    

      
      
    

