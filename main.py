from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import keyboard
import pyautogui
import schedule
from lecturelinks import *
d=datetime.datetime.now()

def jointoc():
    driver=webdriver.Chrome('D:\\webdrivers\\chromedriver.exe') #to start chrome 
    driver.get(toc) #to get toc lecture link from lecturelinks
    driver.maximize_window() #to maximize the chrome window
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(40)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(5)
    pyautogui.hotkey('ctrl','shift','m') # to mute the lecture
    pyautogui.hotkey('ctrl','shift','o') # to off the video
    time.sleep(60) #lecture time in sec
    pyautogui.hotkey('ctrl','shift','b')
    driver.quit() #to stop the driver
    quitbutton=pyautogui.locateOnScreen("quit.png")
    pyautogui.moveTo(quitbutton)
    pyautogui.click()

def joinjava():
    driver=webdriver.Chrome('D:\\webdrivers\\chromedriver.exe') #to start chrome 
    driver.get(java) #to get java lecture link from lecturelinks
    driver.maximize_window() #to maximize the chrome window
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(40)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(5)
    pyautogui.hotkey('ctrl','shift','m') # to mute the lecture
    pyautogui.hotkey('ctrl','shift','o') # to off the video
    time.sleep(60)
    pyautogui.hotkey('ctrl','shift','b')
    driver.quit() #to stop the driver
    quitbutton=pyautogui.locateOnScreen("quit.png")
    pyautogui.moveTo(quitbutton)
    pyautogui.click()

def joindbms():
    driver=webdriver.Chrome('D:\\webdrivers\\chromedriver.exe') #to start chrome 
    driver.get(dbms) #to get dbms lecture link from lecturelinks
    driver.maximize_window() #to maximize the chrome window
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(40)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(5)
    pyautogui.hotkey('ctrl','shift','m') # to mute the lecture
    pyautogui.hotkey('ctrl','shift','o') # to off the video
    time.sleep(3000) 
    driver.quit() #to stop the driver
    quitbutton=pyautogui.locateOnScreen("quit.png")
    pyautogui.moveTo(quitbutton)
    pyautogui.click()
def joiniot():
    driver=webdriver.Chrome('D:\\webdrivers\\chromedriver.exe') #to start chrome 
    driver.get(iot) #to get iot lecture link from lecturelinks
    driver.maximize_window() #to maximize the chrome window
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(40)
    keyboard.send("enter",do_press=True,do_release=True)

    time.sleep(5)
    pyautogui.hotkey('ctrl','shift','m') # to mute the lecture
    pyautogui.hotkey('ctrl','shift','o') # to off the video
    time.sleep(60)
    driver.quit() #to stop the driver
    quitbutton=pyautogui.locateOnScreen("quit.png")
    pyautogui.moveTo(quitbutton)
    pyautogui.click()
def joinos():
    driver=webdriver.Chrome('D:\\webdrivers\\chromedriver.exe') #to start chrome 
    driver.get(os) #to get os lecture link from lecturelinks
    driver.maximize_window() #to maximize the chrome window
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(40)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(5)
    pyautogui.hotkey('ctrl','shift','m') # to mute the lecture
    pyautogui.hotkey('ctrl','shift','o') # to off the video
    time.sleep(3000)
    driver.quit() #to stop the driver
    quitbutton=pyautogui.locateOnScreen("quit.png")
    pyautogui.moveTo(quitbutton)
    pyautogui.click()
def joincgt():
    driver=webdriver.Chrome('D:\\webdrivers\\chromedriver.exe') #to start chrome 
    driver.get(cgt) #to get cgt lecture link from lecturelinks
    driver.maximize_window() #to maximize the chrome window
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(40)
    keyboard.send("enter",do_press=True,do_release=True)
    pyautogui.hotkey('ctrl','shift','m') # to mute the lecture
    pyautogui.hotkey('ctrl','shift','o') # to off the video
    time.sleep(3000)
    driver.quit() #to stop the driver
    quitbutton=pyautogui.locateOnScreen("quit.png")
    pyautogui.moveTo(quitbutton)
    pyautogui.click()
def joinweb():
    driver=webdriver.Chrome('D:\\webdrivers\\chromedriver.exe') #to start chrome 
    driver.get(web) #to get web lecture link from lecturelinks
    driver.maximize_window() #to maximize the chrome window
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("tab",do_press=True,do_release=True)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(40)
    keyboard.send("enter",do_press=True,do_release=True)
    time.sleep(5)
    pyautogui.hotkey('ctrl','shift','m') # to mute the lecture
    pyautogui.hotkey('ctrl','shift','o') # to off the video
    time.sleep(3000) 
    driver.quit() #to stop the driver
    quitbutton=pyautogui.locateOnScreen("quit.png")
    pyautogui.moveTo(quitbutton)
    pyautogui.click()

schedule.every().monday.at(firstlecture).do(jointoc)
schedule.every().monday.at(secondlecture).do(joiniot)
schedule.every().monday.at(thirdlecture).do(joindbms)
schedule.every().monday.at(fourthlecture).do(joinos)

schedule.every().tuesday.at(firstlecture).do(joinos)
schedule.every().tuesday.at(secondlecture).do(joincgt)
schedule.every().tuesday.at(thirdlecture).do(joinjava)
schedule.every().tuesday.at(fourthlecture).do(joindbms)

schedule.every().wednesday.at(firstlecture).do(joinweb)
schedule.every().wednesday.at(secondlecture).do(joiniot)
schedule.every().wednesday.at(thirdlecture).do(joinjava)
schedule.every().wednesday.at(fourthlecture).do(joindbms)

schedule.every().thursday.at(firstlecture).do(jointoc)
schedule.every().thursday.at(secondlecture).do(joinjava)
schedule.every().thursday.at(thirdlecture).do(joincgt)


schedule.every().friday.at(firstlecture).do(jointoc)
schedule.every().friday.at(secondlecture).do(joinweb)
schedule.every().friday.at(thirdlecture).do(joinos)


schedule.every().saturday.at(firstlecture).do(jointoc)
schedule.every().saturday.at(secondlecture).do(joiniot)
schedule.every().saturday.at(thirdlecture).do(joincgt)

while True:
    schedule.run_pending()
    time.sleep(1)

