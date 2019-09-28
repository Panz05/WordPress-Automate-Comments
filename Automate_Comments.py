##################################################
### Script To Copy Contents Of File To WebPage ###
#### Version 0.1 - Creation Date - 04/05/2018 ####
############# Author - Imp0st3r ##################
##################################################

# Python modules to import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyperclip

msg = open('Path To File', 'r').read() # Enter the path to the file you wish to read from

driver = webdriver.Chrome('Path To chromedriver.exe') # Enter the path to the ChromeDrive.exe file
driver.get('My WebSite') # Enter the website you wish to copy your data to

usr_box = driver.find_element_by_id('author') # Search for the element on the web page called 'author'
usr_box.send_keys('MyNameHere') # Enter the name you wish to use

sleep (2)

eml_box = driver.find_element_by_id('email') # Search for the element on the web page called 'email'
eml_box.send_keys('MyName@MyDomain.com') # Enter the email address you wish to use

sleep (2)

msg_box = driver.find_element_by_id('comment') # Search for the element on the web page called 'comment'
pyperclip.copy(msg) # Using Payperclip copy the contents of the file opened above to the clipboard
msg_box.send_keys(Keys.CONTROL, 'v') # Using Selenium paste the contents from the clip board to the web site

sleep (3)

post_comment = driver.find_element_by_id('submit') # Search for the element on the web page called submit
post_comment.click() # Submit post

driver.quit() # Quit program