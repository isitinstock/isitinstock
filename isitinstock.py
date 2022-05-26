from itertools import product
import tkinter as tk
from tkinter import Label, PhotoImage, filedialog, Text, mainloop, messagebox
import os
import requests
from bs4 import BeautifulSoup
import time
import sys
import re
import random

# Sends the Email if it's available to order -----------------------------------
import smtplib
def send_email1():
    global product_link1
    global email1sent
    subject = 'In Stock: ' + str(productName)
    body = 'Your product is now in stock! Check:' + product_link1
    msg = f"Subject: {subject}\n\n{body}"
    #msg = 'Subject: Appointment: ' + product_link
    fromaddr = 'isitinstockapp@gmail.com'
    print(user_email)
    toaddrs = [str(user_email)]
 #   server = smtplib.SMTP('smtp.gmail.com', 587) 
   # server.starttls()
    # add account login name and password,
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.set_debuglevel(1)
    server.ehlo()
    server.login("isitinstockapp@gmail.com", "lwclkdinwmymvbmc")
    # Print the email's contents
    print('From: ' + fromaddr)
    print('To: ' + str(toaddrs))
  #  print('Message: ' + msg)
    # send the email
    server.sendmail(fromaddr, toaddrs, msg)
    # disconnect from the server
    server.quit()
    email1sent = True
def send_email2():
    global product_link2
    global email2sent
    subject = 'In Stock: ' + str(productName2)
    body = 'Your product is now in stock! Check:' + product_link2
    msg = f"Subject: {subject}\n\n{body}"
    #msg = 'Subject: Appointment: ' + product_link
    fromaddr = 'isitinstockapp@gmail.com'
    print(user_email)
    toaddrs = [str(user_email)]
   # server = smtplib.SMTP('smtp.gmail.com', 587) 
   # server.starttls()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.set_debuglevel(1)
    server.ehlo()
    # add account login name and password,
    server.login("isitinstockapp@gmail.com", "lwclkdinwmymvbmc")
    # Print the email's contents
    print('From: ' + fromaddr)
    print('To: ' + str(toaddrs))
 #   print('Message: ' + msg)
    # send the email
    server.sendmail(fromaddr, toaddrs, msg)
    # disconnect from the server
    server.quit()
    email2sent = True

def follow_up_email():
    subject = 'Reminder! Your product is back in stock!'
    body = 'If you missed the last notification, please check your email to see your product that went back into stock. If you already checked your notification, then please ignore this message. You will not recieve any further reminders.'
    msg = f"Subject: {subject}\n\n{body}"
    #msg = 'Subject: Appointment: ' + product_link
    fromaddr = 'isitinstockapp@gmail.com'
    print(user_email)
    toaddrs = [str(user_email)]
  #  server = smtplib.SMTP('smtp.gmail.com', 587) 
  #  server.starttls()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.set_debuglevel(1)
    server.ehlo()
    # add account login name and password,
    server.login("isitinstockapp@gmail.com", "lwclkdinwmymvbmc")
    # Print the email's contents
    print('From: ' + fromaddr)
    print('To: ' + str(toaddrs))
    print('Message: ' + msg)
    # send the email
    server.sendmail(fromaddr, toaddrs, msg)
    # disconnect from the server
    server.quit()
def send_verification():
    global numlist
    numlist = []
    numlist.append(str(random.randint(10000, 99999)))
    subject = 'Your IsItInStock Email Verification Code is: ' + str(numlist[0])
    body = 'Your verification code is ' + str(numlist[0]) +' \n \n Please enter this code in your IsItInStock window to proceed and track the availibiltiy of your favorite products. \n \n This is an automated email you recieved because you are using IsItInStock. If this was not you, then please ignore this email.'
    msg = f"Subject: {subject}\n\n{body}"
    #msg = 'Subject: Appointment: ' + product_link
    fromaddr = 'isitinstockapp@gmail.com'
    print(user_email)
    toaddrs = [str(user_email)]
   # server = smtplib.SMTP('smtp.gmail.com', 587)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.set_debuglevel(1)
    server.ehlo()
  #  server.starttls()
    # add account login name and password,
    server.login("isitinstockapp@gmail.com", "lwclkdinwmymvbmc")
    # Print the email's contents
    print('From: ' + fromaddr)
    print('To: ' + str(toaddrs))
  #  print('Message: ' + msg)
    # send the email
    server.sendmail(fromaddr, toaddrs, msg)
    # disconnect from the server
    server.quit() 
    
# This program creates a pop up window in Tkinter for you to enter your email along with a link to a product page on Amazon, Best Buy, or Walmart. After submitting the information, an automatic tab will open that will refresh itself every 20 seconds, checking to see if the product is in stock. When the product goes into stock, the user will be notified by email.
# The Good_Link variable may be unnecessary.
Good_Link = True

def checkCode():
    user_code = entry3.get()
    print('user code' + user_code) 
    print('actual code'+ str(numlist[0]))
    if str(user_code) == str(numlist[0]):
        DoneButton['state'] = tk.NORMAL
    else:
        messagebox.showinfo("Incorrect Code", "The verification code is incorrect.")


def StartWindow():
# Creates Pop Up Window -------------------------------------------
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Is It In Stock?")

    canvas = tk.Canvas(root, height=700, width=700, bg="#990033")
    canvas.pack()

   
    frame = tk.Frame(root, bg="pink")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    CompanyName = tk.Label(root, text='Is It In Stock?')
    CompanyName.config(font=('impact', 30), bg="pink")
    canvas.create_window(320, 40, window=CompanyName)

    welcome = tk.Label(root, text='Is It In Stock?')
    welcome.config(font=('impact', 30), bg="pink")
    canvas.create_window(320, 40, window=welcome)

    label2 = tk.Label(root, text='Enter Link To Product(s) (up to 2):')
    label2.config(font=('helvetica', 15))
    canvas.create_window(320, 100, window=label2)

    label3 = tk.Label(root, text='Enter Email Address:')
    label3.config(font=('helvetica', 15))
    canvas.create_window(320, 360, window=label3)



    label4 = tk.Label(root, text='Note: You can only enter links \n to track products from Amazon, Walmart, Target, and Best Buy.')
    label4.config(font=('helvetica', 13))
    canvas.create_window(340, 250, window=label4)

    entry1 = tk.Entry (root, width=50, borderwidth=1, highlightcolor="black")
    canvas.create_window(320, 150, window=entry1)

    entry11 = tk.Entry (root, width=50, borderwidth=1, highlightcolor="black")
    canvas.create_window(320, 175, window=entry11)

    entry2 = tk.Entry (root, width=50, borderwidth=1, highlightcolor="black")
    canvas.create_window(320, 400, window=entry2)

    label5 = tk.Label(root, text='You will recieve an email notification \n when the product you entered \n goes back into stock.')
    label5.config(font=('helvetica', 15))
    canvas.create_window(320, 475, window=label5)
    
   
    user_email = ""
    URL_validity = 0
    user_code = ""
    
    
    def getEntries():
        global product_link1
        global product_link2
        global user_email
        global URL_validity
        global user_code
        global entry3
        global link_list
        global twoworks
        global oneworks
        global product_link2_blank
        global product_link1_blank

        product_link1 = entry1.get()
        product_link2 = entry11.get()
        
        user_email = entry2.get()

        if product_link1 == "" and product_link2 != "":
            try:
                response = requests.get(product_link2)
                twoworks = True
                oneworks = False
                product_link2_blank = product_link2
            except: 
                messagebox.showinfo("Invalid Link", "One or more of the URLs are invalid..")

        elif product_link2 == "" and product_link1 != "":
            try:
                response = requests.get(product_link1)
                oneworks = True
                twoworks = False
                product_link1_blank = product_link1
            except: 
                messagebox.showinfo("Invalid Link", "One or more of the URLs are invalid..")
        elif product_link1 != "" and product_link2 != "":
            try:
                response = requests.get(product_link1)
                response2 = requests.get(product_link2)
                oneworks = True
                twoworks = True
                link_list = [str(product_link1), str(product_link2)]
            except:
                messagebox.showinfo("Invalid Link", "One or more of the URLs are invalid..")


               
            
       

        
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', str(user_email))     
        if match == None:
            messagebox.showinfo("Invalid Email", "Please enter a valid Email Address.")  
            
        else:
            
            send_verification()
            label6 = tk.Label(root, text='A 5-digit code has been sent to \n' + str(user_email) + '. \n Please enter it here for verification.')
            label6.config(font=('helvetica', 15))
            canvas.create_window(320, 565, window=label6)
            entry3 = tk.Entry (root, width=16)
            canvas.create_window(320, 625, window=entry3)
            

            SubmitCode = tk.Button(root, text="Enter Code", command=checkCode, padx=10, pady=1, 
            fg="white", bg="#263D42")
            canvas.create_window(450, 625, window=SubmitCode)


            
        return user_email
        return product_link
        return URL_validity
        
    def success():
        root.destroy()
        root3 = tk.Tk()
        root3.resizable(False, False)

        canvas3 = tk.Canvas(root3, height=700, width=700, bg="#990033")
        canvas3.pack()

        frame3 = tk.Frame(root3, bg="pink")
        frame3.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        label33 = tk.Label(root3, text='You will be notified through e-mail when your \n product goes into stock! \n\n Click "Agree" to proceed.')
        label33.config(font=('helvetica', 15))
        canvas3.create_window(340, 300, window=label33)

        AgreeButton = tk.Button(root3, text="Agree", command=root3.destroy, padx=20, pady=20,
        fg="white", bg="#263D42")
        AgreeButton.pack()
        root3.mainloop()
        

    # Takes and Stores Input  ------------------------------------------------------------------------
    SubmitLink = tk.Button(root, text="Confirm Entries", command=getEntries, padx=10, pady=5, 
    fg="white", bg="#263D42")

    global DoneButton
    DoneButton = tk.Button(root, text="Track Product", command=success, padx=10, pady=5,
    fg="white", bg="#263D42", state=tk.DISABLED)
 



    SubmitLink.pack()
    DoneButton.pack()


   
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            sys.exit()


    root.protocol("WM_DELETE_WINDOW", on_closing)



    root.mainloop()  



def executable_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


StartWindow()

# Goes to the product page and gets the product name + availibility-------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driveropen = False
driver2open = False

def get_availibility():
    global availibility
    global html
    global wally
    if "walmart" in product_link1:
        availibility = False
        wally = True
        string = product_link1
        m = string.split('https://www.walmart.com/ip/')[1].split('/')[0]
        global productName
        productName = m
        print(productName)

        if availibility == False:
            
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
            html = requests.get(product_link1, headers=header)
            text = html.text
            


            position = (int(text.find('"availability":"https://schema.org/InStock"')))
            print(str(position))
            if position != -1:
                availibility = True
                send_email1()
                print("Email1 sent.")
            elif position == -1:
                availibility = False
                print(productName +' not available. Checking again in 20 seconds...')
                time.sleep(20)
            
        
        return availibility

    else:

        
        global driver
        global driveropen

        if driveropen == False:
            opts = Options()
            opts.add_experimental_option('excludeSwitches', ['enable-logging'])
            opts.add_experimental_option("detach", True)
            opts.add_argument("--headless")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options = opts)
        #    driver = webdriver.Chrome(executable_path('./driver/chromedriver.exe'), options=opts)
            driver.get(product_link1)
            time.sleep(2)
            html = driver.page_source
            driveropen = True

        if "amazon" in product_link1:
            driver.refresh()
            soup = BeautifulSoup(html,'html.parser')
            title = soup.find(id="buy-now-button")
            print(title)
            cart = soup.find(id="add-to-cart-button")
            print(cart)
            cart_ubb = soup.find(id="add-to-cart-button-ubb")
            print(cart_ubb)
            see_all = soup.find(title="See All Buying Options")
            print(see_all)

            
            
            
            productName = soup.find(id="productTitle").get_text()
            productName = productName.strip()
            print(productName)




            availibility = False
            if "buy-now-button" in str(title):
                availibility = True
            elif "add-to-cart-button" in str(cart):
                availibility = True
            elif "add-to-cart-button-ubb" in str(cart_ubb):
                availibility = True
            elif "See All Buying Options" in str(see_all):
                availibility = True
            else:
                availibility = False
                print(productName +' not available. Checking again in 20 seconds...')
                time.sleep(20)
                
                
            return availibility
        elif "bestbuy" in product_link1:
            soup = BeautifulSoup(html,'html.parser')
            availibility = False
           
            productName = soup.find("h1", {"class": "heading-5 v-fw-regular"}).get_text()
            productName = productName.strip()
            print(productName)

            try:
                title = soup.find("button", {"data-button-state": "ADD_TO_CART"}).get_text()
                print(title)
                availibility = True
            except:
                availibility = False
                print(productName +' not available. Checking again in 20 seconds...')
                time.sleep(20)
                driver.refresh()

        elif "target" in product_link1:
            time.sleep(15)
            soup = BeautifulSoup(html,'html.parser')
            availibility = False
           
            productName = soup.find("h1", {"data-test": "product-title"}).get_text()
            productName = productName.strip()
            print(productName)

            title = soup.find("script", {"id": "json"}).get_text()
            if "InStock" in title:
                print(title)
                availibility = True
            elif "OutOfStock" in title:
                print(str(title))
                availibility = False
                print(productName +' not available. Checking again in 20 seconds...')
                time.sleep(20)
                driver.refresh()
                
            return availibility

def get_availibility2():
    global availibility2
    global html2
    global driver2
    global wally2
    if "walmart" in product_link2:
        availibility2 = False
        wally2 = True
        string2 = product_link2
        m2 = string2.split('https://www.walmart.com/ip/')[1].split('/')[0]
        global productName2
        productName2 = m2
        print(productName2)
        root2 = tk.Tk()


        canvas2 = tk.Canvas(root2, height=700, width=700, bg="#263D42")
        canvas2.pack()

        frame2 = tk.Frame(root2, bg="pink")
        frame2.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        label22 = tk.Label(root2, text='You will be notified through e-mail when your \n product goes into stock! \n\n Click "Agree" to proceed.')
        label22.config(font=('helvetica', 15))
        canvas2.create_window(340, 300, window=label22)

        AgreeButton = tk.Button(root2, text="Agree", command=root2.destroy, padx=20, pady=20,
        fg="pink", bg="#263D42")
        AgreeButton.pack()
        root2.mainloop()

        if availibility2 == False:
            
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
            html2 = requests.get(product_link2, headers=header)
            text2 = html2.text
            


            position2 = (int(text2.find('"availability":"https://schema.org/InStock"')))
            print(str(position2))
            if position2 != -1:
                availibility2 = True
                send_email2()
                print("email2 sent.")
            elif position2 == -1:
                availibility2 = False
                print(productName2 +' not available. Checking again in 20 seconds...')
                time.sleep(20)
            
        
        return availibility2
    
    else:
        global driver2
        global driver2open
        if driver2open == False:
            opts = Options()
            opts.add_experimental_option('excludeSwitches', ['enable-logging'])
            opts.add_experimental_option("detach", True)
            opts.add_argument("--headless")

            driver2 = webdriver.Chrome(ChromeDriverManager().install(), options = opts)
            driver2.get(product_link2)
            html2 = driver2.page_source
            driver2open = True

        if "amazon" in product_link2:
            driver2.refresh()
            soup2 = BeautifulSoup(html2,'html.parser')
            title2 = soup2.find(id="buy-now-button")
            print(title2)
            cart2 = soup2.find(id="add-to-cart-button")
            print(cart2)
            cart_ubb2 = soup2.find(id="add-to-cart-button-ubb")
            print(cart_ubb2)
            see_all2 = soup2.find(title="See All Buying Options")
            print(see_all2)


            
            productName2 = soup2.find(id="productTitle").get_text()
            productName2 = productName2.strip()
            print(productName2)    
                
            availibility2 = False
            if "buy-now-button" in str(title2):
                availibility2 = True
            elif "add-to-cart-button" in str(cart2):
                availibility2 = True
            elif "add-to-cart-button-ubb" in str(cart_ubb2):
                availibility2 = True
            elif "See All Buying Options" in str(see_all2):
                availibility2 = True
            else:
                availibility2 = False
                print(productName2 +' not available. Checking again in 20 seconds...')
                time.sleep(20)

            return availibility2
        elif "bestbuy" in product_link2:
            soup2 = BeautifulSoup(html2,'html.parser')
            availibility2 = False
            
            productName2 = soup2.find("h1", {"class": "heading-5 v-fw-regular"}).get_text()
            productName2 = productName2.strip()
            print(productName2)

            try:
                title2 = soup2.find("button", {"data-button-state": "ADD_TO_CART"}).get_text()
                print(title2)
                availibility2 = True
                print("its availible.")
            except:
                availibility2 = False
                print(productName2 +' not available. Checking again in 20 seconds...')
                time.sleep(20)
                driver2.refresh()

        elif "target" in product_link2:
            time.sleep(15)
            soup2 = BeautifulSoup(html2,'html.parser')
            availibility2 = False
           
            productName2 = soup2.find("h1", {"data-test": "product-title"}).get_text()
            productName2 = productName2.strip()
            print(productName2)

            title2 = str(soup2)
            title2 = title2.find("Out of stock")
            if title2 == -1:
                availibility2 = True
            elif title2 != -1:
                print(str(title2))
                availibility2 = False
                print(productName2 +' not available. Checking again in 20 seconds...')
                time.sleep(20)
                driver2.refresh()
                
            return availibility2

availibility = False
availibility2 = False
global onedone
global twodone
onedone = False
twodone = False
wally = False
wally2 = False

def Execution():
    print('going through execution')
    global onedone
    global twodone
    if oneworks == True and twoworks == True:
        if availibility == False and onedone == False:
            get_availibility()
    
            if availibility == True:

                if wally == False:
                    send_email1()
                    print('email1 sent.')                    
                    driver.close()
                onedone = True
        
        if availibility2 == False and twodone == False:
            get_availibility2()
            
            if availibility2 == True:
                send_email2()
                print('email2 sent.')
                if wally2 == False:
                    driver2.close()
                twodone = True


    elif oneworks == True and twoworks == False:
        if availibility == False:
            get_availibility()

            if availibility == True:
                send_email1()
                print('email1 sent.')
                if wally == False:
                    driver.close()
                onedone = True

        elif availibility == True and onedone == False:
            send_email1()
            print('email1 sent')
            if wally == False:
                driver.close()
            onedone = True

    elif oneworks == False and twoworks == True:
        if availibility2 == False:
            get_availibility2()
        elif availibility2 == True and twodone == False:
            send_email2()
            print('email2 sent')

            if wally2 == False:
                driver2.close()
            twodone = True

while availibility == False and oneworks == True or availibility2 == False and twoworks == True:
    Execution()
