#imports

import time
import pickle
import os

#lists

userlist_file = 'user_list.dat'
userlist = {}



                                #LOGIN

#finds out if u have username or makes a new one

print ("Hello, and welcome to ClericMT's Cooked Adventure!")
time.sleep(1)
print (("\n"*1) + "Great cookery awaits you...")
time.sleep(1)



loop1 = True

while loop1:
    intro = input("\n" + "do you have an account Y/N?" + "\n")
    
    #Create new account
    if intro.lower() == "n":
        newuser = input("Create a username ")
        newpass = input("Create a password ")
        print ("\n" + "Thankyou and good luck on your first CMTC Adventure!")

        #Add New User
        if os.path.exists(userlist_file):
            with open(userlist_file,'rb') as rfp:
                userlist = pickle.load(rfp)

        userlist[newuser] = newpass

        with open(userlist_file,'wb') as wfp:
            pickle.dump(userlist, wfp)
        
        
        loop1 = False
        break

    elif intro.lower() != "y" and intro.lower() != "n":
        print ("Please press 'y' or 'n'")

    #if user already has account
    else:
        print ("excellent")
        loop1 = False
        break



#login menu

loop2 = True
loop3 = True
count = 0


while loop2:
    with open(userlist_file,'rb') as rfp:       
        userlist = pickle.load(rfp)
        userlogin = input("please enter your username")
        if userlogin not in userlist:
            print ("details incorrect")
        else:
            while loop3:
                userpass = input("please enter your password")
                if userlist[userlogin] != userpass:
                    print ("password incorrect")
                    count += 1
                    if count > 3:
                        print ("ur a hacker... teminating program...")
                        os._exit(0)
                
                else:
                    print ("login success!")
                    loop2 = False
                    loop3 = False
                    break




 
