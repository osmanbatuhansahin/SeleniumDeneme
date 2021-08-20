import pandas as pd
from selenium import webdriver
import time
from math import floor
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os
import itertools
from collections import defaultdict
import pymysql
from sqlalchemy import create_engine


connection = pymysql.connect(
  host="localhost",
  user="username",
  password="password",
database="dbname",
charset='utf8'
)

engine = create_engine('mysql+pymysql://username:password@localhost/dbname')

cursor = connection.cursor()


programKodu = []
osym = []

sagGenel = []
solGenel = []

solKontenjan = []
sagKontenjan = []

solCinsiyet = []
sagCinsiyet = []

solBolge = []
sagBolge = []

bolgeDict = {}

myDict = defaultdict()

xl = []


driver = webdriver.Firefox()

df = pd.read_csv('osymveri.csv') # can also index sheet by name or fetch all sheets
listKod = df['AAA'].tolist()


def bolumBilgiAl2020():


    try:
        myBtn = driver.find_element_by_class_name("featherlight-close-icon")
        myBtn.click()
        time.sleep(1)
    except NoSuchElementException:
        pass



    #myBtn = driver.find_element_by_css_selector("#headingOne > a:nth-child(1) > h4:nth-child(2)")
    try:
        myBtns = WebDriverWait(driver, 12).until( \
    EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "glyphicon-arrow-down")))
        for i in myBtns:
            driver.execute_script("arguments[0].click();", i)
        time.sleep(1)
    except TimeoutException:
        pass



    print ("************** Genel Bilgiler *********************")


    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
       sagGenel.append(elementRight.text)

    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
       solGenel.append(elementLeft.text)

    programKodu.append(driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[2]").text)
    osym.append(driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[1]").text)



    print ("************** Kontenjan İstatistikleri *********************") #hangi veriler lazım?



    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[3]/div/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solKontenjan.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[3]/div/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagKontenjan.append(elementRight.text)
    # print("sol liste: "+str(len(solKontenjan)))
    # print("sag liste: "+str(len(sagKontenjan)))
    #
    # kontenjanDict = dict(zip(solKontenjan, sagKontenjan))
    #
    # print ("Kontenjan İstatistikleri:")
    # for key, value in kontenjanDict.items():
    #     print(key, ' : ', value)


    print ("************** Cinsiyet İstatistikleri *********************") #hangi veriler lazım?


    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solCinsiyet.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagCinsiyet.append(elementRight.text)

    # print("sol liste: "+str(len(solCinsiyet)))
    # print("sag liste: "+str(len(sagCinsiyet)))
    #
    # cinsiyetDict = dict(zip(solCinsiyet, sagCinsiyet))
    #
    # print ("Cinsiyet İstatistikleri:")
    # for key, value in cinsiyetDict.items():
    #     print(key, ' : ', value)


    print ("************** Coğrafi Bölge İstatistikleri *********************") #hangi veriler lazım?

    solBolgeLocal =[]
    sagBolgeLocal = []
    for i in [2,3]:
        elementsLeft = driver.find_elements_by_css_selector("#icerik_1020ab > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solBolgeLocal.append(elementLeft.text)
    for i in [2,3]:
        elementsRight = driver.find_elements_by_css_selector('#icerik_1020ab > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child('+str(i)+') > td:nth-child(2)')
        for elementRight in elementsRight:
            sagBolgeLocal.append(elementRight.text)

    for i in [2,3,4,5,6,7,8]:
        elementsLeft = driver.find_elements_by_css_selector("table.table:nth-child(6) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solBolgeLocal.append(elementLeft.text)

    for i in [2,3,4,5,6,7,8]:
        elementsRight = driver.find_elements_by_css_selector("table.table:nth-child(6) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagBolgeLocal.append(elementRight.text)

    sagBolge.append(sagBolgeLocal)
    solBolge.append(solBolgeLocal)


    #
    # print("sol liste: "+str(len(solBolge)))
    # print("sag liste: "+str(len(sagBolge)))
    #
    # bolgeDict = dict(zip(solBolge, sagBolge))
    #
    # print ("Bölge İstatistikleri:")
    # for key, value in bolgeDict.items():
    #     print(key, ' : ', value)

    """
    print ("************** Öğrenim Durumu İstatistikleri *********************") #hangi veriler lazım?

    for i in [2,3,4,5,6]:
        elementsLeft = driver.find_elements_by_css_selector("#icerik_1030a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solGenel.append(elementLeft.text)

    for i in [2,3,4,5,6]:
        elementsRight = driver.find_elements_by_css_selector("#icerik_1030a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagList.append(elementRight.text)

    # print("sol liste: "+str(len(solOgrenim)))
    # print("sag liste: "+str(len(sagOgrenim)))
    #
    # ogrenimDict = dict(zip(solOgrenim, sagOgrenim))

    print ("Öğrenim Durumu İstatistikleri:")
    for key, value in ogrenimDict.items():
        print(key, ' : ', value)



    print ("************** Mezuniyet Yılı İstatistikleri *********************") #hangi veriler lazım?

    solMezYil=[]
    sagMezYil=[]

    elementList = driver.find_elements_by_xpath("/ html / body / div[2] / div[1] / div[7] / div / div[8] / div[2] / div / div / table / tbody / tr / td[1]")
    elementListNum = (len(list((elementList))))

    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solMezYil.append(elementLeft.text)


    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagMezYil.append(elementRight.text)

    print("sol liste: "+str(len(solMezYil)))
    print("sag liste: "+str(len(sagMezYil)))

    mezYilDict = dict(zip(solMezYil, sagMezYil))

    print ("Mezuniyet Yılı İstatistikleri:")
    for key, value in mezYilDict.items():
        print(key, ' : ', value)


    print ("************** Lise Alanı İstatistikleri *********************") #hangi veriler lazım?

    solLiseAlan=[]
    sagLiseAlan=[]


    elementsLeftNum = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr/td[1]")
    print(len(list(elementsLeftNum)))

    for i in list(range(2,len(list(elementsLeftNum))+1)):
        elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[1]")
        for elementLeft in elementsLeft:
            solLiseAlan.append(elementLeft.text)

    for i in list(range(2,len(list(elementsLeftNum))+1)):
        elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[2]")
        for elementRight in elementsRight:
            sagLiseAlan.append(elementRight.text)

    print("sol liste: "+str(len(solLiseAlan)))
    print("sag liste: "+str(len(sagLiseAlan)))

    liseAlanDict = dict(zip(solLiseAlan, sagLiseAlan))

    print ("Lise Alanı İstatistikleri:")
    for key, value in liseAlanDict.items():
        print(key, ' : ', value)


    print ("************** Lise Grubu İstatistikleri *********************") #hangi veriler lazım?

    solLiseGrup=[]
    sagLiseGrup=[]


    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solLiseGrup.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
            sagLiseGrup.append(elementRight.text)


    print("sol liste: "+str(len(solLiseGrup)))
    print("sag liste: "+str(len(sagLiseGrup)))

    liseGrupDict = dict(zip(solLiseGrup, sagLiseGrup))

    print ("Lise Grubu İstatistikleri:")
    for key, value in liseGrupDict.items():
        print(key, ' : ', value)


    print ("************** Taban Puan ve Başarı Sırası *********************") #hangi veriler lazım?

    solPuan=[]
    sagPuan=[]

    for i in [1,2]:
        elementsLeft1 = driver.find_elements_by_css_selector("#icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        elementsLeft2 = driver.find_element_by_css_selector("#icerik_1000_3 > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(4)")
        for elementLeft1 in elementsLeft1:
            solPuan.append(elementLeft1.text+elementsLeft2.text)

    for i in [1,2]:
        elementsRight = driver.find_elements_by_css_selector("#icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(4)")
        for elementRight in elementsRight:
            sagPuan.append(elementRight.text)
    #bottom table
    for i in [1,2]:
        elementsLeft1 = driver.find_elements_by_css_selector("#icerik_1000_3 > table:nth-child(3) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        elementsLeft2 = driver.find_element_by_css_selector("#icerik_1000_3 > table:nth-child(3) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(2)")
        for elementLeft1 in elementsLeft1:
            solPuan.append(elementLeft1.text+elementsLeft2.text)

    for i in [1,2]:
        elementsRight = driver.find_elements_by_css_selector("#icerik_1000_3 > table:nth-child(3) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(4)")
        for elementRight in elementsRight:
            sagPuan.append(elementRight.text)

    print("sol liste: "+str(len(solPuan)))
    print("sag liste: "+str(len(sagPuan)))

    puanDict = dict(zip(solPuan, sagPuan))

    print ("Taban Puanı ve Başarı Sıralaması:")
    for key, value in puanDict.items():
        print(key, ' : ', value)



    print ("************** Net Ortalamaları *********************") #hangi veriler lazım?

    solNet=[]
    sagNet=[]


    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solNet.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagNet.append(elementRight.text)

    print("sol liste: "+str(len(solNet)))
    print("sag liste: "+str(len(sagNet)))


    netDict = dict(zip(solNet, sagNet))

    print ("Net İstatistikleri:")
    for key, value in netDict.items():
        print(key, ' : ', value)


    print ("************** Tercih Edilme İstatistikleri *********************") #hangi veriler lazım?

    solTercih=[]
    sagTercih=[]


    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solTercih.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagTercih.append(elementRight.text)

    print("sol liste: "+str(len(solTercih)))
    print("sag liste: "+str(len(sagTercih)))
    print(sagTercih)
    print(solTercih)


    tercihEdilmeDict = dict(zip(solTercih, sagTercih))

    print ("Tercih Edilme İstatistikleri:")
    for key, value in tercihEdilmeDict.items():
        print(key, ' : ', value)



    print ("************** Yerleşenlerin Tercih Sıraları *********************") #hangi veriler lazım?

    solTercihSira=[]
    sagTercihSira=[]

    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solTercihSira.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagTercihSira.append(elementRight.text)

    print("sol liste: "+str(len(solTercihSira)))
    print("sag liste: "+str(len(sagTercihSira)))


    tercihSiraDict = dict(zip(solTercihSira, sagTercihSira))

    print ("Yerleşenlerin Tercih Sıraları:")
    for key, value in tercihSiraDict.items():
        print(key, ' : ', value)


    print ("************** Yerleşenlerin Tercih Eğilimleri *********************") #hangi veriler lazım?

    solEgilim=[]
    sagEgilim=[]


    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[7]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilim.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[7]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilim.append(elementRight.text)

    print("sol liste: "+str(len(solEgilim)))
    print("sag liste: "+str(len(sagEgilim)))

    egilimDict = dict(zip(solEgilim, sagEgilim))

    print ("Yerleşenlerin Tercih Eğilimleri:")
    for key, value in egilimDict.items():
        print(key, ' : ', value)


    print("************** Yerleşenlerin Tercih Eğilimleri-Üni Türleri *********************")  # hangi veriler lazım?

    solEgilimTur = []
    sagEgilimTur = []

    for i in list(range(1, 6)):
        elementsLeft = driver.find_elements_by_css_selector(
            "#icerik_1310 > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(" + str(i) + ") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solEgilimTur.append(elementLeft.text)

    for i in list(range(1, 6)):
        elementsRight = driver.find_elements_by_css_selector(
            "#icerik_1310 > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(" + str(i) + ") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagEgilimTur.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimTur)))
    print("sag liste: " + str(len(sagEgilimTur)))

    egilimTurDict = dict(zip(solEgilimTur, sagEgilimTur))

    print("Yerleşenlerin Tercih Eğilimleri-Üni Türleri:")
    for key, value in egilimTurDict.items():
        print(key, ' : ', value)


    print("************** Yerleşenlerin Tercih Eğilimleri-Üniler *********************")  # hangi veriler lazım?

    solEgilimUni = []
    sagEgilimUni = []

    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilimUni.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilimUni.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimUni)))
    print("sag liste: " + str(len(sagEgilimUni)))

    egilimUniDict = dict(zip(solEgilimUni, sagEgilimUni))

    print("Yerleşenlerin Tercih Eğilimleri-Üniler:")
    for key, value in egilimUniDict.items():
        print(key, ' : ', value)


    print("************** Yerleşenlerin Tercih Eğilimleri-İller *********************")  # hangi veriler lazım?

    solEgilimIl = []
    sagEgilimIl = []


    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilimIl.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilimIl.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimIl)))
    print("sag liste: " + str(len(sagEgilimIl)))

    egilimTurDict = dict(zip(solEgilimIl, sagEgilimIl))

    print("Yerleşenlerin Tercih Eğilimleri-İller:")
    for key, value in egilimTurDict.items():
        print(key, ' : ', value)


    print("************** Yerleşenlerin Tercih Eğilimleri-Farklı Program *********************")  # hangi veriler lazım?

    solEgilimIl = []
    sagEgilimIl = []



    elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilimIl.append(elementLeft.text)


    elementsRight = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilimIl.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimIl)))
    print("sag liste: " + str(len(sagEgilimIl)))

    egilimIlDict = dict(zip(solEgilimIl, sagEgilimIl))

    print("Yerleşenlerin Tercih Eğilimleri-Üni Türleri:")
    for key, value in egilimIlDict.items():
        print(key, ' : ', value)


    print("************** Yerleşenlerin Tercih Programlar *********************")  # hangi veriler lazım?

    solProgram = []
    sagProgram = []


    elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[8]/div/div[12]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solProgram.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[8]/div/div[12]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagProgram.append(elementRight.text)

    print("sol liste: " + str(len(solProgram)))
    print("sag liste: " + str(len(sagProgram)))

    programDict = dict(zip(solProgram, sagProgram))

    print("Yerleşenlerin Tercih Ettiği Programlar:")
    for key, value in programDict.items():
        print(key, ' : ', value)

"""

def bolumBilgiAl2019():

    try:
        myBtn = driver.find_element_by_class_name("featherlight-close-icon")
        myBtn.click()
        time.sleep(1)
    except NoSuchElementException:
        pass

    # myBtn = driver.find_element_by_css_selector("#headingOne > a:nth-child(1) > h4:nth-child(2)")
    try:
        myBtns = WebDriverWait(driver, 12).until( \
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "glyphicon-arrow-down")))
        for i in myBtns:
            driver.execute_script("arguments[0].click();", i)
        time.sleep(1)
    except TimeoutException:
        pass

    print("************** Genel Bilgiler *********************")

    solGenel = []
    sagGenel = []

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagGenel.append(elementRight.text)

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solGenel.append(elementLeft.text)

    print("sag liste: " + str(len(sagGenel)))
    print("sol liste: " + str(len(solGenel)))

    genelBilgiler = dict(zip(solGenel, sagGenel))

    print("Genel Bilgiler:")
    for key, value in genelBilgiler.items():
        print(key, ' : ', value)




    print("************** Kontenjan İstatistikleri *********************")  # hangi veriler lazım?

    solKontenjan = []
    sagKontenjan = []


    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solKontenjan.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagKontenjan.append(elementRight.text)
    print("sol liste: " + str(len(solKontenjan)))
    print("sag liste: " + str(len(sagKontenjan)))

    kontenjanDict = dict(zip(solKontenjan, sagKontenjan))

    print("Kontenjan İstatistikleri:")
    for key, value in kontenjanDict.items():
        print(key, ' : ', value)

    print("************** Cinsiyet İstatistikleri *********************")  # hangi veriler lazım?

    solCinsiyet = []
    sagCinsiyet = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solCinsiyet.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagCinsiyet.append(elementRight.text)

    print("sol liste: " + str(len(solCinsiyet)))
    print("sag liste: " + str(len(sagCinsiyet)))

    cinsiyetDict = dict(zip(solCinsiyet, sagCinsiyet))

    print("Cinsiyet İstatistikleri:")
    for key, value in cinsiyetDict.items():
        print(key, ' : ', value)

    print("************** Coğrafi Bölge İstatistikleri *********************")  # hangi veriler lazım?

    solBolge = []
    sagBolge = []

    for i in [2, 3]:
        elementsLeft = driver.find_elements_by_css_selector(
            "#icerik_1020ab > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solBolge.append(elementLeft.text)
    for i in [2, 3]:
        elementsRight = driver.find_elements_by_css_selector(
            '#icerik_1020ab > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(' + str(i) + ') > td:nth-child(2)')
        for elementRight in elementsRight:
            sagBolge.append(elementRight.text)

    for i in [2, 3, 4, 5, 6, 7, 8]:
        elementsLeft = driver.find_elements_by_css_selector(
            "table.table:nth-child(6) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solBolge.append(elementLeft.text)

    for i in [2, 3, 4, 5, 6, 7, 8]:
        elementsRight = driver.find_elements_by_css_selector(
            "table.table:nth-child(6) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagBolge.append(elementRight.text)

    print("sol liste: " + str(len(solBolge)))
    print("sag liste: " + str(len(sagBolge)))

    bolgeDict = dict(zip(solBolge, sagBolge))

    print("Bölge İstatistikleri:")
    for key, value in bolgeDict.items():
        print(key, ' : ', value)

    print("************** Öğrenim Durumu İstatistikleri *********************")  # hangi veriler lazım?

    solOgrenim = []
    sagOgrenim = []

    for i in [2, 3, 4, 5, 6]:
        elementsLeft = driver.find_elements_by_css_selector(
            "#icerik_1030a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solOgrenim.append(elementLeft.text)

    for i in [2, 3, 4, 5, 6]:
        elementsRight = driver.find_elements_by_css_selector(
            "#icerik_1030a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagOgrenim.append(elementRight.text)

    print("sol liste: " + str(len(solOgrenim)))
    print("sag liste: " + str(len(sagOgrenim)))

    ogrenimDict = dict(zip(solOgrenim, sagOgrenim))

    print("Öğrenim Durumu İstatistikleri:")
    for key, value in ogrenimDict.items():
        print(key, ' : ', value)

    print("************** Mezuniyet Yılı İstatistikleri *********************")  # hangi veriler lazım?

    solMezYil = []
    sagMezYil = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solMezYil.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagMezYil.append(elementRight.text)

    print("sol liste: " + str(len(solMezYil)))
    print("sag liste: " + str(len(sagMezYil)))

    mezYilDict = dict(zip(solMezYil, sagMezYil))

    print("Mezuniyet Yılı İstatistikleri:")
    for key, value in mezYilDict.items():
        print(key, ' : ', value)

    print("************** Lise Alanı İstatistikleri *********************")  # hangi veriler lazım?

    solLiseAlan = []
    sagLiseAlan = []

    elementsLeftNum = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr/td[1]")
    print(len(list(elementsLeftNum)))

    for i in list(range(2, len(list(elementsLeftNum))+1)):
        elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]")
        for elementLeft in elementsLeft:
            solLiseAlan.append(elementLeft.text)

    for i in list(range(2, len(list(elementsLeftNum))+1)):
        elementsRight = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[2]")
        for elementRight in elementsRight:
            sagLiseAlan.append(elementRight.text)

    print("sol liste: " + str(len(solLiseAlan)))
    print("sag liste: " + str(len(sagLiseAlan)))

    liseAlanDict = dict(zip(solLiseAlan, sagLiseAlan))

    print("Lise Alanı İstatistikleri:")
    for key, value in liseAlanDict.items():
        print(key, ' : ', value)

    print("************** Lise Grubu İstatistikleri *********************")  # hangi veriler lazım?

    solLiseGrup = []
    sagLiseGrup = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solLiseGrup.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagLiseGrup.append(elementRight.text)

    print("sol liste: " + str(len(solLiseGrup)))
    print("sag liste: " + str(len(sagLiseGrup)))

    liseGrupDict = dict(zip(solLiseGrup, sagLiseGrup))

    print("Lise Grubu İstatistikleri:")
    for key, value in liseGrupDict.items():
        print(key, ' : ', value)

    print("************** Taban Puan ve Başarı Sırası *********************")  # hangi veriler lazım?

    solPuan = []
    sagPuan = []

    for i in [1, 2]:
        elementsLeft1 = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table[1]/tbody/tr["+str(i)+"]/td[1]")
        elementsLeft2 = driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table[1]/thead/tr/th[4]")
        for elementLeft1 in elementsLeft1:
            solPuan.append(elementLeft1.text + elementsLeft2.text)

    for i in [1, 2]:
        elementsRight = driver.find_elements_by_css_selector(
            "#icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(4)")
        for elementRight in elementsRight:
            sagPuan.append(elementRight.text)
    # bottom table
    for i in [1, 2]:
        elementsLeft1 = driver.find_elements_by_css_selector(
            "#icerik_1000_3 > table:nth-child(3) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(1)")
        elementsLeft2 = driver.find_element_by_css_selector(
            "#icerik_1000_3 > table:nth-child(3) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(2)")
        for elementLeft1 in elementsLeft1:
            solPuan.append(elementLeft1.text + elementsLeft2.text)

    for i in [1, 2]:
        elementsRight = driver.find_elements_by_css_selector(
            "#icerik_1000_3 > table:nth-child(3) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(4)")
        for elementRight in elementsRight:
            sagPuan.append(elementRight.text)

    print("sol liste: " + str(len(solPuan)))
    print("sag liste: " + str(len(sagPuan)))

    puanDict = dict(zip(solPuan, sagPuan))

    print("Taban Puanı ve Başarı Sıralaması:")
    for key, value in puanDict.items():
        print(key, ' : ', value)

    print("************** Net Ortalamaları *********************")  # hangi veriler lazım?

    solNet = []
    sagNet = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[1]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solNet.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[1]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagNet.append(elementRight.text)

    print("sol liste: " + str(len(solNet)))
    print("sag liste: " + str(len(sagNet)))

    netDict = dict(zip(solNet, sagNet))

    print("Net İstatistikleri:")
    for key, value in netDict.items():
        print(key, ' : ', value)

    print("************** Tercih Edilme İstatistikleri *********************")  # hangi veriler lazım?

    solTercih = []
    sagTercih = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solTercih.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagTercih.append(elementRight.text)

    print("sol liste: " + str(len(solTercih)))
    print("sag liste: " + str(len(sagTercih)))
    print(sagTercih)
    print(solTercih)

    tercihEdilmeDict = dict(zip(solTercih, sagTercih))

    print("Tercih Edilme İstatistikleri:")
    for key, value in tercihEdilmeDict.items():
        print(key, ' : ', value)

    print("************** Yerleşenlerin Tercih Sıraları *********************")  # hangi veriler lazım?

    solTercihSira = []
    sagTercihSira = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solTercihSira.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagTercihSira.append(elementRight.text)

    print("sol liste: " + str(len(solTercihSira)))
    print("sag liste: " + str(len(sagTercihSira)))

    tercihSiraDict = dict(zip(solTercihSira, sagTercihSira))

    print("Yerleşenlerin Tercih Sıraları:")
    for key, value in tercihSiraDict.items():
        print(key, ' : ', value)

    print("************** Yerleşenlerin Tercih Eğilimleri *********************")  # hangi veriler lazım?

    solEgilim = []
    sagEgilim = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilim.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilim.append(elementRight.text)

    print("sol liste: " + str(len(solEgilim)))
    print("sag liste: " + str(len(sagEgilim)))

    egilimDict = dict(zip(solEgilim, sagEgilim))

    print("Yerleşenlerin Tercih Eğilimleri:")
    for key, value in egilimDict.items():
        print(key, ' : ', value)


    print("************** Yerleşenlerin Tercih Eğilimleri-Üniler *********************")  # hangi veriler lazım?

    solEgilimUni = []
    sagEgilimUni = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[8]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilimUni.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[8]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilimUni.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimUni)))
    print("sag liste: " + str(len(sagEgilimUni)))

    egilimUniDict = dict(zip(solEgilimUni, sagEgilimUni))

    print("Yerleşenlerin Tercih Eğilimleri-Üni Türleri:")
    for key, value in egilimUniDict.items():
        print(key, ' : ', value)

    print("************** Yerleşenlerin Tercih Eğilimleri-İller *********************")  # hangi veriler lazım?

    solEgilimIl = []
    sagEgilimIl = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilimIl.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilimIl.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimIl)))
    print("sag liste: " + str(len(sagEgilimIl)))

    egilimTurDict = dict(zip(solEgilimIl, sagEgilimIl))

    print("Yerleşenlerin Tercih Eğilimleri-İller:")
    for key, value in egilimTurDict.items():
        print(key, ' : ', value)

    print("************** Yerleşenlerin Tercih Eğilimleri-Farklı Program *********************")  # hangi veriler lazım?

    solEgilimIl = []
    sagEgilimIl = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilimIl.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilimIl.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimIl)))
    print("sag liste: " + str(len(sagEgilimIl)))

    egilimIlDict = dict(zip(solEgilimIl, sagEgilimIl))

    print("Yerleşenlerin Tercih Eğilimleri-Üni Türleri:")
    for key, value in egilimIlDict.items():
        print(key, ' : ', value)

    print("************** Yerleşenlerin Tercih Programlar *********************")  # hangi veriler lazım?

    solProgram = []
    sagProgram = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solProgram.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagProgram.append(elementRight.text)

    print("sol liste: " + str(len(solProgram)))
    print("sag liste: " + str(len(sagProgram)))

    programDict = dict(zip(solProgram, sagProgram))

    print("Yerleşenlerin Tercih Ettiği Programlar:")
    for key, value in programDict.items():
        print(key, ' : ', value)


for kod in listKod[:3]:

    url = "https://yokatlas.yok.gov.tr/lisans.php?y=" + str(kod) + ""

    try:
        driver.get(url)
        divSayiBtns = driver.find_elements_by_class_name("panel-default")
        divSayi = len(list(divSayiBtns))
        time.sleep(1)
        if (divSayi == 27):
            time.sleep(1)
            bolumBilgiAl2020()
            time.sleep(1)

        else:
            print("girdi")
            time.sleep(1)
            bolumBilgiAl2019()
            time.sleep(1)



        # print("sag liste: " + str(len(sagGenel)))
        # print("sol liste: " + str(len(solGenel)))
        #
        # genelBilgiler = dict(zip(solGenel, sagGenel))
        #
        # print(genelBilgiler)
        #
        # print("Genel Bilgiler:")
        # for key, value in genelBilgiler.items():
        #     print(key, ' : ', value)




    except NoSuchElementException:
        time.sleep(1)
        print("Exception exist")
        pass

# abc = pd.DataFrame(sagGenel, solGenel)
#
# abc2 = abc.to_dict()
#
# df2 = pd.DataFrame.from_dict(abc2, orient='index')
# print(df2)
# print(sagGenel)
# print(solGenel)

listGenel = list(zip(solGenel, sagGenel))
dGenel = defaultdict(list)

# print(solGenel)
# print(sagGenel)
#
# print(d1)
#
# data_pairs = zip(data[::2],data[1::2])
#
# for x in data_pairs:
#     myDict.setdefault(x[0],[]).append(x[1])
#
# print("****************************")
# print(myDict)


"""
for k, v in listGenel:
    dGenel[k].append(v)

d = dict((k, tuple(v)) for k, v in dGenel.items())
print(d)
#({k:pd.Series(v) for k, v in d.items()})
df2 = pd.DataFrame.from_dict({k:pd.Series(v) for k, v in d.items()})
#df2.columns = listKod[:3]
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(df2)
df2.to_sql(con=engine, name='2020genel', if_exists='replace')
"""
solKontenjan.extend(osym)
sagKontenjan.extend(programKodu)
listKontenjan = list(zip(solKontenjan, sagKontenjan))
dKontenjan = defaultdict(list)
for k, v in listKontenjan:
    dKontenjan[k].append(v)

d = dict((k, tuple(v)) for k, v in dKontenjan.items())
df2 = pd.DataFrame.from_dict({k: pd.Series(v) for k, v in d.items()})
df2.to_sql(con=engine, name='2020kontenjan', if_exists='replace')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
     print(df2)

listCinsiyet = list(zip(solCinsiyet, sagCinsiyet))
dCinsiyet = defaultdict(list)
for k, v in listCinsiyet:
    dCinsiyet[k].append(v)

d = dict((k, tuple(v)) for k, v in dCinsiyet.items())

df2 = pd.DataFrame.from_dict({k: pd.Series(v) for k, v in d.items()})
df2.to_sql(con=engine, name='2020cinsiyet', if_exists='replace')

# solBolge.extend(osym)
# sagBolge.extend(programKodu)
# listBolge = list(zip(solBolge, sagBolge))
# dBolge = defaultdict(list)
# for k, v in listBolge:
#     dBolge[k].append(v)
# print("****************************dBolge")
#
# print(dBolge)
#
# d = dict((k, tuple(v)) for k, v in dBolge.items())
# print(d)
# df2 = pd.DataFrame.from_dict({k: pd.Series(v) for k, v in d.items()})
# df2.to_sql(con=engine, name='2020cografibolge', if_exists='replace')

print(solBolge)
print(sagBolge)

for i in list(range(0,len(solBolge))):
    for j in list(range(0, len(solBolge[i]))):
        sagBolge[i][j] = ""+str(solBolge[i][j])+" : "+str(sagBolge[i][j])+""
print(solBolge)
dBolge = defaultdict(list)
# dictBolge = dict(zip(solBolge, sagBolge))
# print(dictBolge)

listBolge = list(zip(programKodu, sagBolge))
for k, v in listBolge:
    dBolge[k].extend(v)
print(dBolge)

d = dict((k, tuple(v)) for k, v in dBolge.items())
print(d)
# for j in list(range(0, len(solBolge))):
#     for i in list(range(0, len(solBolge[2]))):
#         print(solBolge[i])
#         print(pd.Series(v))

df2 = pd.DataFrame.from_dict({k: pd.Series(v) for k, v in d.items()},orient="columns")

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df2)

df2.to_sql(con=engine, name='2020cografibolge', if_exists='replace')
# print(len(solBolge))
# for j in list(range(0, len(solBolge))):
#     for i in list(range(0, len(solBolge[0]))):
#         df2 = pd.DataFrame(sagBolge[j][i],index=solBolge[j][i])
#         with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#             print(df2)




# table_name = "2020deneme"
# cursor.execute("""CREATE TABLE IF NOT EXISTS """ + table_name + " (" + " VARCHAR(250),".join(solGenel) + " VARCHAR(250))")
# connection.commit()
#
# cols = "`,`".join([str(i) for i in df2.columns.tolist()])
#
# for i,row in df2.iterrows():
#     sql = "INSERT INTO `2020deneme` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
#     cursor.execute(sql, tuple(row))
#
#     connection.commit()
#
# sql = "SELECT * FROM `2020deneme`"
# cursor.execute(sql)
#
# # Fetch all the records
# result = cursor.fetchall()
# for i in result:
#     print(i)









for kod in listKod:

    url = "https://yokatlas.yok.gov.tr/2018/lisans.php?y=" + str(kod) + ""

    try:
        driver.get(url)
        divSayiBtns = driver.find_elements_by_class_name("panel-default")
        divSayi = len(list(divSayiBtns))
        time.sleep(1)
        if (divSayi == 27):
            time.sleep(1)
            bolumBilgiAl2020()
            time.sleep(1)
        else:
            print("girdi")
            time.sleep(1)
            bolumBilgiAl2019()
            time.sleep(1)
    except NoSuchElementException:
        time.sleep(1)
        print("Exception exist")
        pass


for kod in listKod:

    url = "https://yokatlas.yok.gov.tr/2019/lisans.php?y=" + str(kod) + ""

    try:
        driver.get(url)
        divSayiBtns = driver.find_elements_by_class_name("panel-default")
        divSayi = len(list(divSayiBtns))
        time.sleep(1)
        if (divSayi == 27):
            time.sleep(1)
            bolumBilgiAl2020()
            time.sleep(1)
        else:
            print("girdi")
            time.sleep(1)
            bolumBilgiAl2019()
            time.sleep(1)
    except NoSuchElementException:
        time.sleep(1)
        print("Exception exist")
        pass


