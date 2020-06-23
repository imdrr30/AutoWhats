from flask import Flask, request, redirect, render_template
import evarsity
import time
import os
import random
from threading import *
app = Flask(__name__)

class getinfobg(Thread):
    def run(self):
        time.sleep(1)
        print("Getting Test Performance Status")
        evarsity.getdatatp()
        time.sleep(1)
        print("Getting sem Status")
        evarsity.getdatasem()
        time.sleep(1)
        print("Getting Profile Status")
        evarsity.getdata()
        time.sleep(1)
        print("Getting Subject Status")
        evarsity.getdatasub()
        evarsity.driver.execute_script("LogOut()")
        okk = evarsity.driver.find_element_by_id("okay")
        okk.click()

fetcher = getinfobg()

class closer(Thread):
    def run(self):
        exit()

close= closer()

class autologout(Thread):
    def run(self):
        time.sleep(450)
        exit()

alo = autologout()


def errorcheck():
    try:
        time.sleep(1)
        try:
            err = evarsity.driver.find_elements_by_xpath('//font[@color = "red"]')
            if err!=[]:
                return True
        except:
            try:
                err2 = evarsity.driver.find_element_by_xpath('//input[@value = "Force login"]')
                evarsity.driver.execute_script("loginform(1)")
            except:
                return False
    except:
        return False

@app.route("/")
def hello():

    cins = evarsity.loadcp()

    return render_template('loginpage.html',capins=cins,rval=random.randint(11111,22222))

@app.route('/signup', methods = ['POST'])
def signup():
    username = request.form['us']
    password = request.form['ps']
    captacha = request.form['cp']
    try:
        evarsity.login(username,password,captacha)
        time.sleep(4)
        if errorcheck():
            print("Checking Credential Status")
            return render_template('loginpage.html',log="Invalid Login Info",rval=random.randint(11111,22222))
        else:
            try:
                print("Checking Session Status")
                evarsity.driver.execute_script("loginform(1)")
            except:
                pass
            time.sleep(1)
            print("Getting Attendance Status")
            evarsity.getdataatt()
            print("Getting Avathar Status")
            evarsity.loadava()
            fetcher.start()
            alo.start()
    except:
        print("reached exception")
        pass
    return redirect('/att?id={}'.format(random.randint(11111,33333)))

@app.route("/att")
def load():
    #evarsity.getdataatt()
    return render_template('att.html',rval=random.randint(11111,22222))

@app.route("/prof")
def loadprof():
    #evarsity.getdata()
    return render_template('prof.html',rval=random.randint(11111,22222))

@app.route("/sem")
def loadsem():
    #evarsity.getdatasem()
    return render_template('sem.html',rval=random.randint(11111,22222))

@app.route("/sub")
def loadsub():
    #evarsity.getdatasub()
    return render_template('sub.html',rval=random.randint(11111,22222))

@app.route("/tp")
def loadtp():
    #evarsity.getdatatp()
    return render_template('tp.html',rval=random.randint(11111,22222))

@app.route("/tt")
def loadtt():
    evarsity.getdatatt()
    return render_template('tt.html',rval=random.randint(11111,22222))

@app.route("/logout")
def logout():
    """evarsity.driver.execute_script("LogOut()")
    okk = evarsity.driver.find_element_by_id("okay")
    okk.click()"""
    tempp = ['sub.html','prof.html','att.html','sem.html','tp.html']
    for i in tempp:
        try:
            os.remove("./temp/{}".format(i))
            os.remove("./templates/{}".format(i))
            os.remove("./static/avatar.png")
        except:
            pass
    try:
        os.remove("./static/captcha.png")
    except:
        pass
    close.start()
    return 'Service Ended'