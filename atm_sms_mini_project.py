#!/usr/bin/python
import getpass
import string
import os
import time
from twilio.rest import Client

def message():
    account_sid = 'ACbf5c7a373fa240165fc0702f6bae0029'
    auth_token = '9ddc5ecbe9662b050ab0af9052d921e0'
  
    client = Client(account_sid, auth_token)
  
    message = client.messages.create(
                              from_='YOUR_TWILIO_NUMBER',
                              body ='YOUR MESSAGE',
                              to ='YOUR_PHONE_NUMBER'
                          )
  
    print(message.sid)
    

# creatinga lists of users, their PINs and bank statements
users = ['user1', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0
# while loop checks existance of the enterd username
print('--------------------')
print('********************')
print('  INDIAN BANK ATM   ')
print('********************')
print('--------------------')
while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
            print('-------------------')
            print('Insert your card')
            time.sleep(3)
            print('Processing...')
            time.sleep(3)
        elif user == users[1]:
            n = 1
            print('-------------------')
            print('Insert your card')
            time.sleep(3)
            print('Processing...')
            time.sleep(3)
        else:
            n = 2
            print('-------------------')
            print('Insert your card')
            time.sleep(3)
            print('Processing...')
            time.sleep(3)
        break
    else:
        print('----------------')
        print('****************')
        print('INVALID USERNAME')
        print('****************')
        print('----------------')

# comparing pin
while count < 3:
    print('------------------')
    print('******************')
    pin = str(getpass.getpass('PLEASE ENTER PIN: '))
    print('******************')
    print('------------------')
    if pin.isdigit():
        if user == 'user1':
            if pin == pins[0]:
                break
            else:
                count += 1
                print('-----------')
                print('***********')
                print('INVALID PIN')
                print('***********')
                print('-----------')
                print()

        if user == 'user2':
            if pin == pins[1]:
                break
            else:
                count += 1
                print('-----------')
                print('***********')
                print('INVALID PIN')
                print('***********')
                print('-----------')
                print()

        if user == 'user3':
            if pin == pins[2]:
                break
            else:
                count += 1
                print('-----------')
                print('***********')
                print('INVALID PIN')
                print('***********')
                print('-----------')
                print()
    else:
        print('------------------------')
        print('************************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('************************')
        print('------------------------')
        count += 1

# in case of a valid pin- continuing, or exiting
if count == 3:
    print('-----------------------------------')
    print('***********************************')
    print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('***********************************')
    print('-----------------------------------')
    time.sleep(5)
    exit()

print('-------------------------')
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
    # os.system('clear')
    print('-------------------------------')
    print('*******************************')
    response = input(
        'SELECT FROM FOLLOWING OPTIONS: \n(1)Balance \n(2)Withdraw \n(3)Debit \n(4)Change PIN  \n(5)Exit \n: ').lower()
    print('*******************************')
    print('-------------------------------')
    valid_responses = ['s', 'w', 'l', 'p', 'q']
    response = response.lower()
    if response == '1':
        print('---------------------------------------------')
        print('*********************************************')
        print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n], 'INR ON YOUR ACCOUNT.')
        print('*********************************************')
        print('---------------------------------------------')

    elif response == '2':
        print('---------------------------------------------')
        print('*********************************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('*********************************************')
        print('---------------------------------------------')
        if cash_out % 10 != 0:
            print('------------------------------------------------------')
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 INR')
            print('******************************************************')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
            print('-----------------------------')
        else:
            amounts[n] = amounts[n] - cash_out
            print('-----------------------------------')
            print('***********************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'INR')
            print('***********************************')
            print('-----------------------------------')
            message()

    elif response == '3':
        print()
        print('---------------------------------------------')
        print('*********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEBIT: '))
        print('*********************************************')
        print('---------------------------------------------')
        print()
        if cash_in % 10 != 0:
            print('----------------------------------------------------')
            print('****************************************************')
            print('AMOUNT YOU WANT TO DEBIT MUST TO MATCH 10 INR')
            print('****************************************************')
            print('----------------------------------------------------')
        else:
            amounts[n] = amounts[n] + cash_in
            print('----------------------------------------')
            print('****************************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'INR')
            print('****************************************')
            print('----------------------------------------')
            
    elif response == '4':
        print('-----------------------------')
        print('*****************************')
        new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
        print('*****************************')
        print('-----------------------------')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            print('------------------')
            print('******************')
            new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
            print('*******************')
            print('-------------------')
            if new_ppin != new_pin:
                print('------------')
                print('************')
                print('PIN MISMATCH')
                print('************')
                print('------------')
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
            print('-------------------------------------')
            print('*************************************')
            print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
            print('*************************************')
            print('-------------------------------------')
    elif response == '5':
        exit()
    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')
