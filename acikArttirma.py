# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:41:29 2023
@author: musta
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException

import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


maxTeklif=21000
def wait_for_element(driver,by, value, timeout):
    try:
        return WebDriverWait(driver, timeout, ignored_exceptions=(StaleElementReferenceException,)).until(EC.presence_of_element_located((by, value)))
    except TimeoutException:
        print("TimeoutException: Element with XPath '{}' not found within {} seconds.".format(value, timeout))
        return None
def wait_for_elements(driver,by, value, timeout):
    try:
        return WebDriverWait(driver, timeout, ignored_exceptions=(StaleElementReferenceException,)).until(EC.presence_of_all_elements_located((by, value)))
    except TimeoutException:
        print("TimeoutException: Element with XPath '{}' not found within {} seconds.".format(value, timeout))
        return None
    
def currTime2():
    now = datetime.datetime.now() 
    second=int(now.second)
    micro=second*1000000+now.microsecond
    return micro
def currTime(str):
   now = datetime.datetime.now() 
   current_time = now.strftime('%H:%M:%S')
   print(str,current_time,":",now.microsecond)

def findElement(id):
    driver.get(url)
    ilanlar=wait_for_element(driver, By.XPATH, '//div[@class="esatis-anasayfa-products"]', timeout)
    innerhtml=ilanlar.get_attribute("innerHTML")
    dataSoup=BeautifulSoup(innerhtml,'html.parser')
    all_tags = [tag for tag in dataSoup.find_all('div')]
    for tag in all_tags:
        try:
            element = driver.find_element(By.ID,id)
            print(element.text)
            if element is not None:
                break
        except NoSuchElementException:
            pass
        
def muhammelBedeli():
    
        check = wait_for_element(driver, By.XPATH, '//label[@for="muhammenBedelUstuTeklif"]', 5)
        if not check.is_selected():
            check.click()
            time.sleep(0.1)
    
        
    
    
def confirm():
    currTime('BEKLEMEDEN ÖNCE')
    btn= WebDriverWait(driver, 3, ignored_exceptions=(StaleElementReferenceException,)).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-bb-handler="confirm"]')))
    btn.click()
    currTime('BEKLEMEDEN SORNA')
    second = wait_for_element(driver, By.ID, 'second', timeout)
    print('DONE',second.text)
    currTime('SON')
    
def accept(second,myOffer,lastPrice):
    #myOfferN=int(myOffer.text.split(',')[0].replace(".",""))
    myOfferN=20000
    lastPriceN=int(lastPrice.text.split(',')[0].replace(".",""))
    boolean=int(second.text)<3 and int(second.text)>0 and myOfferN <lastPriceN
    now = datetime.datetime.now()
    totalMicro=now.second*1000+int(now.microsecond/1000)
    while boolean and totalMicro <59000:
        time.sleep(0.01)
        now = datetime.datetime.now()
        totalMicro=now.second*1000+int(now.microsecond/1000) 
    return boolean
        
 
def accept2(baslangic,micro,myOffer,lastPrice):
    kalan = (time.time()*1000)-baslangic
    kalanZaman = micro-kalan
    temp=123301000
    myOfferN=2000
    lastPriceN=int(lastPrice.text.split(',')[0].replace(".",""))
    return kalanZaman<temp and kalanZaman>temp-1000 and myOfferN <lastPriceN
    
timeout=180  
driver = webdriver.Chrome()
url='https://esatis.uyap.gov.tr/main/esatis/index.jsp'
buyUrl='https://esatis.uyap.gov.tr/main/jsp/esatis/index.jsp?menuId=21772&kayitId=12427572463'
def counter():
    flag=False
    
    while True:
        currentMillis_value = driver.execute_script('return currentMillis;')
        clock =int(currentMillis_value/1000)
        day=int(clock/86400)
        hour=int((clock%86400)/3600)
        minute=int((clock%3600)/60)
        second=int(clock%60)
        micro = currentMillis_value%1000
        flag=True
        #print("GUN: ",day," HOUR: ", hour, " Minute: ",minute, " second: ",second,"Micro: ",micro)
        #print('milli:  ',currentMillis_value)
        return day,hour,minute,second,micro
def runCode():
    id=buyUrl[-11:]
    print(id)
    driver.get(url)
    #WebDriverWait(driver, 100).until(EC.url_changes('https://esatis.uyap.gov.tr/main/jsp/esatis/index.jsp?menuId=21772&kayitId=12316663722'))

    try:
        element=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH,'//div[@id="anaSayfaSorguContainer"]')))
        print(driver.current_url)
    except TimeoutException:
        print('Belirlenen Sürede Giriş Yapılamadı veya Ana sayfaya girelemedi! Lütfen Tekrar Başlatın')

    try:
        driver.get(buyUrl)
        print('İlan Tespiti Başarılı')
    except TimeoutException:
        print('Belirlenen Sürede İlan Sayfasına Ulaşılamadı lütfen tekrar giriş yapınız')
        
    try:
        element=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH,'//ul[@class="product-info-list"]')))
        print('iland  fiyatları')
    except:
        print('kudurma')
        

    zaman=wait_for_element(driver, By.XPATH, '//div[@id="kalanSureAck"]', 45)
    time.sleep(3)
    
    
    
    
    try:
        day1,hour1,minute1,second1,micro1=counter()
        currTime('MICRO BEKLEEM ÖNCE')
        time.sleep((1000-micro1)/1000)
        currTime('MICRO BEKLEEM SONRA')
        print("KADAR BEKLENDİ", (1000-micro1)/1000)
    except TypeError:
        print('Type Error')
        pass
    
    day =wait_for_element(driver, By.ID, 'day', timeout)
    hour =wait_for_element(driver, By.ID, 'hour', timeout)
    minute =wait_for_element(driver, By.ID, 'minute', timeout)
    second=wait_for_element(driver, By.ID, 'second', timeout)
    
    lastPrice =wait_for_element(driver, By.ID, 'ihaleSonTeklif', timeout)
    plusBtn =wait_for_element(driver, By.ID, 'minArtir', timeout)
    myOffer =wait_for_element(driver, By.ID, 'kullaniciMaxTeklifDiv', timeout)#HATAAAA! BENIM SON TEKLİFİM OLMALI
    muhammelBedel =wait_for_element(driver, By.ID, 'muhammenBedeli', timeout)
    muhammelFlag=False
    while(True):
        bas=currTime2()
        minArt=driver.find_element(By.ID, 'minArtir')
        fiyatGir= driver.find_element(By.XPATH,'//input[@type="text"][@placeholder="Teklif Miktarı"]')
        button = driver.find_element(By.XPATH, '//a[@class="btn btn-lg esatis-green" and @onclick="IlanDetayi.teklifEkle();"]')
        #driver.execute_script("return document.getElementById('kullaniciMaxTeklifDiv').innerText;")
        print("Teklif: ",lastPrice.text," Benim Teklif: ",myOffer.text, " Gün: ", day.text, " Saat: ", hour.text, " Dakika: ", minute.text, " Saniye: ", second.text)
        if second and day and minute and hour:
            currTime('Teklif')
            while accept(second,myOffer,lastPrice):
                currTime('ilk')
                last = int(lastPrice.text.split(',')[0].replace(".",""))
                muham= int(muhammelBedel.text.split(',')[0].replace(".","").replace(":",""))
                flag=False
                if muham<last+muham/1000 or muham<last+100:
                    if not muhammelFlag:
                        muhammelBedeli()
                        muhammelFlag=True
                #if int(myOffer.text.split(',')[0].replace(".",""))<int(lastPrice.text.split(',')[0].replace(".","")):
                if int('20000'.replace(".",""))<int(lastPrice.text.split(',')[0].replace(".","")):#BURAYA DİKKAT LAST PRİCE KOYULCAK ŞİMDİLİK SAYI VAR
                    try:
                        currentTeklif= driver.find_element(By.ID, 'teklifMiktari')
                        if currentTeklif.text ==''and int(lastPrice.text.split(',')[0].replace(".",""))+int(minArt.text.split(',')[0].replace(".",""))<maxTeklif:
                            plusBtn.click()
                        elif currentTeklif.text !='' and int(currentTeklif.text)+minArt<maxTeklif:
                            plusBtn.click()
                        currentTeklif= driver.find_element(By.ID, 'teklifMiktari')
                        if currentTeklif.text !='' and int(currentTeklif.text)+minArt<maxTeklif:
                            plusBtn.click()
                        
                    except ElementClickInterceptedException:
                        print('plusa basmadı')
                        pass
                    try:
                        driver.find_element(By.XPATH,'//a[@class="btn btn-lg esatis-green"]').click()
                        flag=True
                    except ElementClickInterceptedException:
                        pass
                    if flag:
                        confirm()
                        currTime('SON')
                        break
                    continue
                
        else:
            print('hata')
        son=currTime2()
        print(son)
        if bas-son>59000000 and son/1000000<1:
            bas=bas-59000000
        delay=(son-bas)/1000000
        print(1-delay)
        if delay<1:
            time.sleep(1-delay)
    print('Kalan zaman Tespit Edildi!')
    """""
    day = wait_for_element(driver, By.XPATH, '//span[@id="day"][@class="count"]', 15)
    hour= wait_for_element(driver, By.XPATH, '//span[@id="hour"][@class="count"]', 15)
    minute = wait_for_element(driver, By.XPATH, '//span[@id="minute"][@class="count"]', 15)
    second = wait_for_element(driver, By.XPATH, '//span[@id="second"][@class="count"]', 15)

    day = driver.execute_script("return document.getElementById('day').innerText;")
    hour= driver.execute_script("return document.getElementById('hour').innerText;")
    minute = driver.execute_script("return document.getElementById('minute').innerText;")
    second = driver.execute_script("return document.getElementById('second').innerText;")
    lastPrice= driver.execute_script("return document.getElementById('ihaleSonTeklif').innerText;")
    plusBtn = driver.execute_script("return document.getElementById('minArtir')")
    myOffer =driver.execute_script("return document.getElementById('kullaniciMaxTeklifDiv').innerText;")
        muhammelBedel=driver.execute_script("return document.getElementById('muhammenBedeli').innerText;")
    """

def deneme(url):
    driver.get(url)
    #WebDriverWait(driver, 100).until(EC.url_changes('https://esatis.uyap.gov.tr/main/jsp/esatis/index.jsp?menuId=21772&kayitId=12316663722'))

    try:
        element=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH,'//div[@id="anaSayfaSorguContainer"]')))
        print(driver.current_url)
    except TimeoutException:
        print('Belirlenen Sürede Giriş Yapılamadı veya Ana sayfaya girelemedi! Lütfen Tekrar Başlatın')

    try:
        driver.get(buyUrl)
        print('İlan Tespiti Başarılı')
    except TimeoutException:
        print('Belirlenen Sürede İlan Sayfasına Ulaşılamadı lütfen tekrar giriş yapınız')
        
    try:
        element=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH,'//ul[@class="product-info-list"]')))
        print('iland  fiyatları')
    except:
        print('kudurma')
        

    zaman=wait_for_element(driver, By.XPATH, '//div[@id="kalanSureAck"]', 45)
    time.sleep(5)
    
    currentMillis_value = driver.execute_script('return currentMillis;')
    baslangic=time.time()*1000
    
    
    lastPrice =wait_for_element(driver, By.ID, 'ihaleSonTeklif', timeout)
    plusBtn =wait_for_element(driver, By.ID, 'minArtir', timeout)
    myOffer =wait_for_element(driver, By.ID, 'kullaniciMaxTeklifDiv', timeout)#HATAAAA! BENIM SON TEKLİFİM OLMALI
    muhammelBedel =wait_for_element(driver, By.ID, 'muhammenBedeli', timeout)
    muhammelFlag=False
    while(True):
        bas=currTime2()
        fiyatGir= driver.find_element(By.XPATH,'//input[@type="text"][@placeholder="Teklif Miktarı"]')
        button = driver.find_element(By.XPATH, '//a[@class="btn btn-lg esatis-green" and @onclick="IlanDetayi.teklifEkle();"]')
        #driver.execute_script("return document.getElementById('kullaniciMaxTeklifDiv').innerText;")
        if True:
            while accept2(baslangic,currentMillis_value,myOffer,lastPrice):
                currTime('ilk')
                last = int(lastPrice.text.split(',')[0].replace(".",""))
                muham= int(muhammelBedel.text.split(',')[0].replace(".","").replace(":",""))
                flag=False
                if muham<last+muham/1000 or muham<last+100:
                    if not muhammelFlag:
                        muhammelBedeli()
                        muhammelFlag=True
                #if int(myOffer.text.split(',')[0].replace(".",""))<int(lastPrice.text.split(',')[0].replace(".","")):
                if int('2000'.split(',')[0].replace(".",""))<int(lastPrice.text.split(',')[0].replace(".","")):
                    try:
                        plusBtn.click()
                    except ElementClickInterceptedException:
                        print('plusa basmadı')
                        pass
                    try:
                        driver.find_element(By.XPATH,'//a[@class="btn btn-lg esatis-green"]').click()
                        flag=True
                    except ElementClickInterceptedException:
                        pass
                    if flag:
                        confirm()
                        currTime('Son')
                    continue
                
        else:
            print('hata')
        son=currTime2()
        if bas-son>59000000 and son/1000000<1:
            bas=bas-59000000
        
    
   
runCode()