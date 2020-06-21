from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1366,786")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:77.0) Gecko/20100101 Firefox/77.0")
driver = webdriver.Chrome("/Users/revan/PycharmProjects/Whtsmon/Driver/chromedriver", chrome_options=chrome_options)
driver.get("https://web.whatsapp.com")


while True:
  time.sleep(2)
  try:
    auser = driver.find_element_by_xpath('//span[@class = "_31gEB"]')
    user = auser.find_element_by_xpath('..')
    user = user.find_element_by_xpath('..')
    user = user.find_element_by_xpath('..')
    user = user.find_element_by_xpath('..')
    #Checking is that a Group
    itext = user.get_attribute('innerHTML')
    if ('class="_5h6Y_ _3Whw5"' in itext or 'added you' in itext or "You're now an admin" in itext or "removed you" in itext ) :
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
      current_date_and_time = current_date_and_time + hours_added
      if ctime[2]==':':
        ctime= ctime[:5]
      elif ctime[1]==':':
        ctime = ctime[:4]
      if current_date_and_time.strftime("%H:%M")>=ctime:
        user.click()
        print(itext)
        lastm = driver.find_elements_by_xpath('//span[@class = "_3Whw5 selectable-text invisible-space copyable-text"]')
        tmp = lastm[-1].get_attribute('innerHTML')
        s = tmp.find("</span>")
        lmsg = tmp[6:s]
        txtbx = driver.find_element_by_xpath('//div[@spellcheck = "true"]')
        sbb = driver.find_elements_by_xpath('//div[@class="_1JNuk"]')
        if lmsg=='busy ?':
          txtbx.send_keys("Yep call you later")
          txtbx.send_keys(Keys.RETURN)
        else:
          txtbx.send_keys("The Person you reached is Offline and will text you soon")
          txtbx.send_keys(Keys.RETURN)
      else:
        continue
  except:
    pass