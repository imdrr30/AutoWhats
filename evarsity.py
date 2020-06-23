from selenium import webdriver
from PIL import Image
import os
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
#"/Users/-----/PycharmProjects/Whtsmon/Driver/chromedriver"
#executable_path=os.environ.get("CHROMEDRIVER_PATH")
#driver.set_window_size(1920, 1080)
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
name=''


def gen(name,index,dval):
    a = open('temp/{}.html'.format(name),'r')
    aa= a.readlines()

    del aa[0:dval]

    n = open('temp/{}.html'.format(name),'w+')
    for lines in aa:
        n.write(lines)
    n.close()

    f = open("data/{}.html".format(name), "r")
    contents = f.readlines()
    f.close()

    a = open('temp/{}.html'.format(name),'r')
    aa= a.read()


    contents.insert(index, aa)

    f = open("templates/{}.html".format(name), "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

def loadcp():
    try:
        os.remove("./static/captcha.png")
    except:
        pass
    driver.get("https://evarsity.srmist.edu.in/srmsip/")
    time.sleep(2)
    element = driver.find_element_by_id("cpimg1")
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
    im.save('static/captcha.png')
    os.remove("shot.png")
    def insloader():
        ins = driver.find_element_by_id("sdivcolor")
        cap = ins.get_attribute('innerHTML')
        if cap=='Enter above word verification':
            return 'Enter Captcha'
        return cap
    return insloader()



def loadava():
    time.sleep(2)
    element = driver.find_element_by_id("img1")

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
    im.save('static/avatar.png')
    os.remove("shot.png")


def getname():
    n = driver.find_elements_by_xpath('//font[@style = "color:#ccc;font-size: 13px;font-family:Tahoma, verdana, sans-serif;"]')
    return n[1].get_attribute('innerHTML')



def login(us,ps,cp):
    print("Passing Login Details")
    a = driver.find_elements_by_xpath('//input[@class = "inputcls"]')
    print("elements found")
    a[0].send_keys(us)
    a[1].send_keys(ps)
    a[2].send_keys(cp)
    print("Values passed found")
    driver.execute_script("loginform()")
    print("logging")
    #time.sleep(3)


def getdataatt():
    #time.sleep(2)
    a = driver.find_element_by_xpath("//*[text()[contains(., 'Attendance')]]")
    driver.execute_script(a.get_attribute('onclick'))
    time.sleep(2)
    att = driver.find_element_by_id('home')
    with open('temp/att.html', 'w') as t:
        t.write('<table>' + att.get_attribute('innerHTML') + '</table>')
    gen("att",186,35)

def getdata():

    p = driver.find_element_by_xpath("//*[text()[contains(., 'General')]]")
    driver.execute_script(p.get_attribute('onclick'))
    time.sleep(2)
    prof = driver.find_element_by_id('home')
    with open('temp/prof.html','w') as t:
        t.write('<table>'+prof.get_attribute('innerHTML')+'</table>')
    gen('prof',138,4)


def getdatatp():

    t = driver.find_element_by_xpath("//*[text()[contains(., 'Test performance')]]")
    driver.execute_script(t.get_attribute('onclick'))
    time.sleep(2)
    tp = driver.find_element_by_id('home')
    with open('temp/tp.html','w') as t:
        t.write('<table>'+tp.get_attribute('innerHTML')+'</table>')
    gen("tp",147,13)

def getdatatt():

    tt = driver.find_element_by_xpath("//*[text()[contains(., 'Time table')]]")
    driver.execute_script(tt.get_attribute('onclick'))
    time.sleep(2)
    timt = driver.find_element_by_id('home')
    with open('templates/tt.html','w') as t:
        t.write('<table>'+timt.get_attribute('innerHTML')+'</table>')


def getdatasem():
    sem = driver.find_element_by_xpath("//*[text()[contains(., 'Credit/marks')]]")
    driver.execute_script(sem.get_attribute('onclick'))
    time.sleep(2)
    seme = driver.find_element_by_id('home')
    with open('temp/sem.html','w') as t:
        t.write('<table>'+seme.get_attribute('innerHTML')+'</table>')
    gen("sem", 147, 25)


def getdatasub():
    sl = driver.find_element_by_xpath("//*[text()[contains(., 'Student Subject List')]]")
    driver.execute_script(sl.get_attribute('onclick'))
    time.sleep(2)
    sub = driver.find_element_by_id('home')
    with open('temp/sub.html','w') as t:
        t.write('<table>'+sub.get_attribute('innerHTML')+'</table>')
    gen('sub',141,14)