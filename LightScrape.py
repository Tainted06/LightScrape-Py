import os
import time
from bs4 import BeautifulSoup
import random
import cv2
import xlsxwriter
import pytesseract
import cfscrape
import cloudscraper
from tkinter import Tk, filedialog

# Clear console
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# File choosing Window
root = Tk()
root.withdraw()
root.attributes('-topmost', True)

# Terms and Conditions Text
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

# Checking Response
if(agree != 'y'):
    if(agree !='n'):
        clearConsole()
        print("Only Type y or n!")
        exit()
    if(agree =='n'):
        clearConsole()
        print("You need to agree to the terms to use this program!")
        exit()

clearConsole()

# Setting the options, folder to store the images/ocr/xlsx files, amount of images to scrape,
# charecters after url to scrape, ocr, xlsx, and verifying that the answers are valid
print("Folder to store scraped images and other files: ", end="", flush=True)
time.sleep(1)
mainfolderr = filedialog.askdirectory()
if(mainfolderr == ''):
    clearConsole()
    print("Please choose a folder!")
    exit()
print(mainfolderr)
mainfolder = mainfolderr + '/'
char = input("How many charecters after https://prnt.sc/ do you want to scrape? (6 or 7 recommended, do not go above 7): ")
if(char.isnumeric()):
    if(int(char) > 7):
        clearConsole()
        print("Do not choose a number bigger than 7!")
        exit()
    if(int(char) < 1):
        clearConsole()
        print("Choose a number larger than 1!")
        exit()
else:
    clearConsole()
    print("Only Type Numbers!")
    exit()
amount = input("Amount of images to scrape: ")
if(amount.isnumeric()):
    if(int(amount)<1):
        clearConsole()
        print("Choose a number larger than 1!")
        exit()
else:
    clearConsole()
    print("Only Type Numbers!")
    exit()
ocr = input("Use OCR? (y or n): ")
if(ocr != 'n'):
    if(ocr != 'y'):
        clearConsole()
        print("Only Type y or n!")
        exit()
xlsx = input("Should the results be stored in a xlsx file? (y or n): ")
if(xlsx != 'n'):
    if(xlsx != 'y'):
        clearConsole()
        print("Only Type y or n!")
        exit()

clearConsole()

# All charecters with upper and lower case alphabet, and numbers for generating random links
charr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'w', '1', '2', '3', '4', '6', '5', '7', '8', '9', '0']

# OCR Make File
if(ocr == 'y'):
    o= open(mainfolder + "ocr.txt","w+")

# XLSX Make File
if(xlsx == 'y'):
    workbook = xlsxwriter.Workbook(mainfolder+'output.xlsx')
    worksheet = workbook.add_worksheet()
    currentnumworkshett = 0
    worksheet.write('A1', 'Number')
    worksheet.write('B1', 'Percent')
    worksheet.write('C1', 'Lightshot Link')
    worksheet.write('D1', 'Image Link')
    worksheet.write('E1', 'Image Location')

# Main Scraping Code
n = 0
while(n<int(amount)):
    n = n+1
    # Setting random combination
    if(int(char) == 1):
        combination = random.choice(charr) 
    if(int(char) == 2):
        combination = random.choice(charr) + random.choice(charr) 
    if(int(char) == 3):
        combination = random.choice(charr) + random.choice(charr) + random.choice(charr) 
    if(int(char) == 4):
        combination = random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) 
    if(int(char) == 5):
        combination = random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) 
    if(int(char) == 6):
        combination = random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr)
    if(int(char) == 7):
        combination = random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr)
    if(int(char) == 8):
        combination = random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr) + random.choice(charr)

    # Random Link
    link = 'https://prnt.sc/' + combination

    # Scraping for image link
    scraper = cloudscraper.create_scraper()
    page = scraper.get(link).text
    soup = BeautifulSoup(page, "html.parser")
    title = soup.find("meta", property="og:image")
    url = title["content"] if title else "not found"

    if(url != "not found"):

        # Adding https: to the url if the url does not have it
        if url[0] != 'h':
            url = 'https:' + url

        # Downloading the image
        downloadscraper = cfscrape.create_scraper()
        urll = url.strip()
        cfurl = downloadscraper.get(urll).content
        name = urll.split('/')[-1]
        with open(mainfolder+name, 'wb') as f:
            f.write(cfurl)
        f.close()

        # OCR if ocr is selected 
        if(ocr == 'y'):
            pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
            imgg = cv2.imread(mainfolder+name)
            imgg = cv2.cvtColor(imgg, cv2.COLOR_BGR2RGB)
            text = pytesseract.image_to_string(imgg)
            o.write('\n============================== '+name+' =============================='+text+'\n')

        # Save output in xlsx if selected
        if(xlsx == 'y'):
            currentnumworkshett = currentnumworkshett+1
            worksheet.write('A'+str(currentnumworkshett+1), n)
            worksheet.write('B'+str(currentnumworkshett+1), round(n/int(amount))) # remove till . add %
            worksheet.write('C'+str(currentnumworkshett+1), link)
            worksheet.write('D'+str(currentnumworkshett+1), url)
            worksheet.write('E'+str(currentnumworkshett+1), mainfolder+name)
        
        # Output
        print(str(n) + " | " + str(round((n/int(amount)*100))) + " percent | " + str(link) + " | " + str(url) + " | " + mainfolder + name)

# Close xlsx file
workbook.close()

# Close ORC text file
o.close()

print("\n\nDone!")
