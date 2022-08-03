##################################################
### Script To Copy Contents Of File To WebPage ###
#### Version 0.2 - Creation Date - 03/08/2022 ####
############# Author - Imp0st3r ##################
##################################################

# Python modules to import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyperclip

msg = open('comments.txt', 'r').read() # Enter the path to the file you wish to read from

options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://my/web/target/') # Enter the website you wish to copy your data to

search_box = driver.find_element(By.NAME, 'author') # Search for the element on the web page called 'author'
search_box.send_keys('Enter a name') # Enter the name you wish to use

sleep (2)

eml_box = driver.find_element(By.NAME, 'email') # Search for the element on the web page called 'email'
eml_box.send_keys('MyName@MyDomain.com') # Enter the email address you wish to use

sleep (2)

msg_box = driver.find_element(By.NAME, 'comment') # Search for the element on the web page called 'comment'
pyperclip.copy(msg) # Using Payperclip copy the contents of the file opened above to the clipboard
msg_box.send_keys(Keys.CONTROL, 'v') # Using Selenium paste the contents from the clip board to the web site

sleep (3)

post_comment = driver.find_element(By.NAME, 'submit') # Search for the element on the web page called submit
post_comment.submit() # Submit post

driver.quit() # Quit program
