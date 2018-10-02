#imports

import time
import pickle
import os

#lists

                                #LOGIN

#finds out if u have username or makes a new one
class Loginz(object):
    userlist_file = 'user_list.dat'
    userlist = {}
    userlogin = ''
    if os.path.exists(userlist_file):
        with open(userlist_file,'rb') as rfp:
            userlist = pickle.load(rfp)

    loop = True
    count = 0

    def __init__ (self):
        pass
    def logging_in(self):

        print ("Hello, and welcome to Password Cabinet!")
        time.sleep(1)

        while self.loop:
            intro = input("\n" + "do you have a user account Y/N?" + "\n")

            #Create new account
            if intro.lower() == "n":
                while self.loop:
                    self.userlogin = input("Create username: ")

                    if self.userlogin in self.userlist:
                        print ('\n Username already exists.')
                        print ('\n Please enter a different name.')

                    else:
                        newpass = input("Create password: ")
                        masterpass = 'masterpass'

                        #Add New User
                        self.userlist[self.userlogin] = {}
                        self.userlist[self.userlogin][masterpass] = newpass

                        with open(self.userlist_file,'wb') as wfp:
                            pickle.dump(self.userlist, wfp)

                        print ("\n Thankyou and welome to Password Cabinet!")

                        run.selection()

            elif intro.lower() != "y" and intro.lower() != "n":
                print ("Please press 'y' or 'n'")

            #if user already has account
            else:
                run.enter_details()



        #login menu


    def enter_details(self):

        while self.loop:
            with open(self.userlist_file,'rb') as rfp:
                self.userlist = pickle.load(rfp)
                self.userlogin = input("please enter your Password Cabinet username: ")
                if self.userlogin not in self.userlist:
                    print ("details incorrect")
                else:
                    while self.loop:
                        userpass = input("please enter your Password Cabinet password: ")
                        if self.userlist[self.userlogin]['masterpass'] != userpass:
                            print ("password incorrect")
                            self.count += 1
                            if self.count > 3:
                                print ("ur a hacker... teminating program...")
                                os._exit(0)

                        else:
                            print ("login success!")
                            run.selection()

    def lists(self):
        for key in (self.userlist[self.userlogin].keys()):
            print (key)

    def selection(self):
        loopy = True
        while loopy:
            print('Please choose from the following:')
            print('1: Access account password')
            print('2: Change account password')
            print('3: Add account information')
            print('4: Delete account information')
            print('5: Quit')
            selection = input()
            if selection == '1':
                run.accessing_passwords()
            elif selection == '2':
                run.changing_passwords()
            elif selection == '3':
                run.adding_passwords()
            elif selection == '4':
                run.deleting_passwords()
            elif selection == '5':
                exit(0)

    def accessing_passwords(self):
        loopy = True
        print ('[type \'q\' to return to main menu]')
        print ('[type \'l\' to see list of accounts]')

        while self.loop:
            userquery = input('Enter account: ')
            if userquery == ('l'):
                run.lists()
            elif userquery in self.userlist[self.userlogin]:
                print (self.userlist[self.userlogin][userquery])
            elif userquery == ('q'):
                run.selection()
            else:
                print ('account non-exist')

    def changing_passwords(self):

        print ('[type \'q\' to return to main menu]')
        print ('[type \'l\' to see list of accounts]')

        while self.loop:
            userquery = input('What account password would you like to update?: ')
            if userquery == ('l'):
                run.lists()
            elif userquery in self.userlist[self.userlogin]:
                while self.loop:
                    changepass = input("Please enter new password: ")
                    self.userlist[self.userlogin][userquery] = changepass

                    with open(self.userlist_file,'wb') as wfp:
                        pickle.dump(self.userlist, wfp)

                    run.selection()

            elif userquery == ('q'):
                run.selection()

            else:
                print ('account non-exist')

    def adding_passwords(self):
        print ('[type \'q\' to return to main menu]')
        print ('[type \'l\' to see list of accounts]')

        while self.loop:
            userquery = input('Please enter the account name to be added: ')
            if userquery == ('l'):
                run.lists()
            elif userquery == ('q'):
                run.selection()
            else:
                while self.loop:
                    addpass = input("Please enter new password: ")
                    self.userlist[self.userlogin][userquery] = addpass

                    with open(self.userlist_file,'wb') as wfp:
                        pickle.dump(self.userlist, wfp)

                    run.selection()

    def deleting_passwords(self):
        print ('[type \'q\' to return to main menu]')
        print ('[type \'l\' to see list of accounts]')

        while self.loop:
            userquery = input('Please enter the account name to be deleted: ')

            if userquery == ('l'):
                run.lists()
            elif userquery == ('q'):
                run.selection()
            elif userquery == ('masterpass'):
                print ('You cannot delete your master password')
                break
            elif userquery in self.userlist[self.userlogin]:
                while self.loop:
                    doublecheck = input('Are you sure you want to delete ' + userquery + '\'s data?: ')

                    if doublecheck.lower() == ('y'):
                        del self.userlist[self.userlogin][userquery]

                        with open(self.userlist_file,'wb') as wfp:
                            pickle.dump(self.userlist, wfp)

                            run.selection()

                    else:
                        break
            else:
                print ('account non-exist')



run = Loginz()

run.logging_in()
