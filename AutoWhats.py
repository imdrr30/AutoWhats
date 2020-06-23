from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import os
from PIL import Image
import json
import requests
from threading import *


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
#"/Users/-----/PycharmProjects/Whtsmon/Driver/chromedriver"
#executable_path=os.environ.get("CHROMEDRIVER_PATH")
chrome_options.add_argument("--window-size=1366,786")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

def getqr():
  driver.get("https://web.whatsapp.com")
  time.sleep(3)
  element = driver.find_element_by_xpath('//canvas[@aria-label = "Scan me!"]')

  location = element.location
  size = element.size
  driver.save_screenshot("shot.png")

  x = location['x']
  y = location['y']
  w = size['width']
  h = size['height']
  width = x + w
  height = y + h

  im = Image.open('shot.png')
  im = im.crop((int(x), int(y), int(width), int(height)))
  im.save('static/qr.png')
  os.remove("shot.png")

def activesession():
  try:
    sessionnotactive = driver.find_element_by_xpath('//div[@class = "G_MLO"]')
    time.sleep(600)
    sessionnotactive = driver.find_element_by_xpath('//div[@class = "S7_rT FV2Qy"]')
    sessionnotactive.click()
  except:
    pass

def resume():
  sessionnotactive = driver.find_element_by_xpath('//div[@class = "S7_rT FV2Qy"]')
  sessionnotactive.click()

def start():
  try:
    os.remove('./static/qr.png')
  except:
    pass
  print("startedddd")
  activesession()
  while True:
    url = 'https://raw.githubusercontent.com/revanrohith/AutoWhats/master/messages.json'
    r = requests.get(url, allow_redirects=True)
    open('messages.json', 'wb').write(r.content)

    with open('messages.json', 'r') as js:
      print(js)
      data = json.load(js)
    time.sleep(2)
    try:
      auser = driver.find_element_by_xpath('//span[@class = "_31gEB"]')
      user = auser.find_element_by_xpath('..')
      user = user.find_element_by_xpath('..')
      user = user.find_element_by_xpath('..')
      user = user.find_element_by_xpath('..')
      #Checking is that a Group
      itext = user.get_attribute('innerHTML')
      if ('status-check' in itext or 'status-dblcheck' in itext or 'class="_5h6Y_ _3Whw5"' in itext or 'added you' in itext or "You're now an admin" in itext or "removed you" in itext ) :
        #if Group Found
        driver.execute_script("var ele = arguments[0];ele.parentNode.removeChild(ele);", user)
        print("Group Detected Unread")
        continue
      else:
        print("User Detected Unread")
        mtime = driver.find_element_by_xpath('//div[@class = "m61XR"]')
        ctime = mtime.get_attribute('innerHTML')
        current_date_and_time = datetime.datetime.now()
        hours_added = datetime.timedelta(hours=5, minutes=30)
        current_date_and_time = current_date_and_time  + hours_added
        if ctime[2]==':':
          ctime= ctime[:5]
          print(ctime)
          print(current_date_and_time.strftime("%H:%M"))
        elif ctime[1]==':':
          ctime = ctime[:4]
          print("elif",ctime)
        if current_date_and_time.strftime("%H:%M")>=ctime:
          user.click()
          print(itext)
          lastm = driver.find_elements_by_xpath('//span[@class = "_3Whw5 selectable-text invisible-space copyable-text"]')
          tmp = lastm[-1].get_attribute('innerHTML')
          s = tmp.find("</span>")
          lmsg = tmp[6:s]
          txtbx = driver.find_element_by_xpath('//div[@spellcheck = "true"]')
          if lmsg in data.keys():
            txtbx.send_keys(data[lmsg])
            txtbx.send_keys(Keys.RETURN)
          else:
            txtbx.send_keys(data['default_message'])
            txtbx.send_keys(Keys.RETURN)
        else:
          continue
    except:
      pass