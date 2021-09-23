import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print('Do you agree to the following?\n')
print("\033[1;31;40m - This program is purely for educational purposes  ")
print("\033[1;31;40m - You will not use this program for any malicious purposes  ")
print("\033[1;31;40m - Any damage caused by this program is not the creators responsibility  ")
print("\033[1;31;40m - These are random images taken by people, because of this there may be gore, NSFW, obscene images, and more  ")
print("\033[1;31;40m - Only continue if you don't mind seeing images as such  ")
print("\033[1;31;40m DO NOT CONTINUE USING THIS PROGRAM IF YOU DO NOT AGREE WITH THE ABOVE  ")
print("\033[1;31;40m Any damage caused by the use of this application is in no way the responsibility of the creator.  \n\n")
print("\033[1;32;40m If you agree to the above, please type the letter y  ")
print("\033[1;31;40m If you do not agree to the above, please type the letter n  \n\n")
agree = input("\033[1;37;40m Response: ")

if(agree != 'y'):
    if(agree !='n'):
        clearConsole()
        print("Only Type y or n!")
        exit()
    if(agree =='n'):
        clearConsole()
        print("You need to agree to the terms to use this program!")
        exit()