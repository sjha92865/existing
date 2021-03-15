from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
#selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# Create your views here.
def todolist(request):
    
    return render(request,'index.html',{})





# Create your views here.
def index(request):
    return  render(request,'deactivation.html')

def deactivate(request):
    u_id=request.POST['user_id']
    u_pass=request.POST['user_password']
    print(u_id,u_pass)

    # Selenium Coding
    driver=webdriver.Chrome(executable_path="/home/shubhamjha/Downloads/chromedriver")
    driver.get("https://www.instagram.com/")
    user_ele=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
    user_ele.send_keys(u_id)


    pwd_ele=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))
    pwd_ele.send_keys(u_pass)

    loginbutton=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    loginbutton.click()
    
    messages.success(request,("User Deleted!"))



    #selenium coding ends
    return  render(request,'index.html')
     
     
     
     
   
     

