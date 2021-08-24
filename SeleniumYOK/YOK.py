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
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="batuhan",
    password="batuhan12",
    charset='utf8',
    database="yokdeneme2"
)

mycursor = mydb.cursor()

mycursor.execute("SET SQL_SAFE_UPDATES = 0;")

# mycursor.execute("DROP TABLE 2020genelbilgiler")
# mycursor.execute("DROP TABLE 2020kontenjan")
# mycursor.execute("DROP TABLE 2020cinsiyet;")
# mycursor.execute("DROP TABLE 2020bolge;")
# mycursor.execute("DROP TABLE 2020ogrenim")
# mycursor.execute("DROP TABLE 2020mezuniyetyillari")
# mycursor.execute("DROP TABLE 2020lisealanlari")
# mycursor.execute("DROP TABLE 2020lisegruplari")
# mycursor.execute("DROP TABLE 2020tabanpuan")
# mycursor.execute("DROP TABLE 2020net")
# mycursor.execute("DROP TABLE 2020tercihedilme")
# mycursor.execute("DROP TABLE 2020tercihegilim")
# mycursor.execute("DROP TABLE 2020tercihegilimtur")
# mycursor.execute("DROP TABLE 2020tercihegilimuni")
# mycursor.execute("DROP TABLE 2020tercihegilimil")
# mycursor.execute("DROP TABLE 2020tercihegilimaynifarkli")
# mycursor.execute("DROP TABLE 2020tercihegilimprogram")



# mycursor.execute("DROP TABLE 2019genelbilgiler")
# mycursor.execute("DROP TABLE 2019kontenjan")
# mycursor.execute("DROP TABLE 2019cinsiyet")
# mycursor.execute("DROP TABLE 2019bolge")
# mycursor.execute("DROP TABLE 2019ogrenim")
# mycursor.execute("DROP TABLE 2019lisealanlari")
# mycursor.execute("DROP TABLE 2019mezuniyetyillari")
# mycursor.execute("DROP TABLE 2019lisegruplari")
# mycursor.execute("DROP TABLE 2019tabanpuan")
# mycursor.execute("DROP TABLE 2019net")
# mycursor.execute("DROP TABLE 2019tercihedilme")
# mycursor.execute("DROP TABLE 2019tercihegilim")
# mycursor.execute("DROP TABLE 2019tercihegilimuni")
# mycursor.execute("DROP TABLE 2019tercihegilimil")
# mycursor.execute("DROP TABLE 2019tercihegilimaynifarkli")
# mycursor.execute("DROP TABLE 2019tercihegilimprogram")




mycursor.execute("CREATE TABLE 2020kontenjan (programkodu INT, genelkontenjan SMALLINT, tubitakkontenjani SMALLINT, engellikontenjani SMALLINT, okulbirincisikontenjani SMALLINT, toplamkontenjan SMALLINT)")
mycursor.execute("CREATE TABLE 2020cinsiyet (programkodu INT, cinsiyet VARCHAR(255), adet SMALLINT)")
mycursor.execute("CREATE TABLE 2020bolge (programkodu INT, bolge VARCHAR(255), adet SMALLINT)")
mycursor.execute("CREATE TABLE 2020genelbilgiler (programkodu INT, universiteturu VARCHAR(255), universite VARCHAR(255),"
                 " fakulte VARCHAR(255), puanturu VARCHAR(255), bursturu VARCHAR(255),genelkontenjan SMALLINT,"
                 " okulbirincisikontenjani SMALLINT, toplamkontenjan SMALLINT,genelkontenjanyerlesen SMALLINT,"
                 " okulbirincisikontenjaniyerlesen SMALLINT, toplamkontenjanyerlesen SMALLINT, boskontenjan SMALLINT,"
                 " ilkyerlesmeorani VARCHAR(255), yerlesipkayityaptirmayan SMALLINT, ekyerlesen SMALLINT,"
                 " 012katsayiileyerlesensonkisininpuani float,012arti006katsayiileyerlesensonkisininpuani float,"
                 " 012katsayiileyerlesensonkisininbasarisirasi INT, 012arti006katsayiileyerlesensonkisininbasarisirasi INT,"
                 " 2020tavanpuan float,2020tavanbasarisirasi INT, 2019dayerlesip2020deobpsikirilarakyerlesensayısi INT,"
                 " yerlesenlerinortalamaobpsi float, yerlesenlerinortalamadiplomanotu float)")

mycursor.execute("CREATE TABLE 2020ogrenim (programkodu INT, ogrenimdurumu VARCHAR(255), yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE 2020mezuniyetyillari (programkodu INT, mezuniyetyili YEAR, yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE 2020lisealanlari (programkodu INT, lisealani VARCHAR(255), yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE 2020lisegruplari (programkodu INT, lisegrubu VARCHAR(255), yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE 2020tabanpuan (programkodu INT, genelkontenjanyerlesensonkisininpuani float,okulbirincisikontenjaniyerlesensonkisininpuani float, "
                 "genelkontenjanyerlesensonkisininbasarisirasi int, okulbirincisikontenjaniyerlesensonkisininbasarisirasi int)")
mycursor.execute("CREATE TABLE 2020net (programkodu INT, test VARCHAR(255), net float)")
mycursor.execute("CREATE TABLE 2020tercihedilme (programkodu INT, tercihedensayisi INT, birkontenjanatalipsayisi float,"
               " ortalamatercihsirasi float, birincisiratercihedensayisi INT, ilkucsiratercihedensayisi INT, ilkdokuzsiratercihedensayisi INT)")
mycursor.execute("CREATE TABLE 2020tercihegilim (programkodu INT, genelkontenjanayerlesensayisi INT, yerlesenlerintoplamtercihhakki INT,"
                 " kullanilantercih INT, bosbirakilantercih INT, yerlesenlerortalamatercihsayisi INT)")
mycursor.execute("CREATE TABLE `2020tercihegilimtur`(programkodu INT, devlet INT, vakif INT, kibris INT, yabanci INT)")
mycursor.execute("CREATE TABLE `2020tercihegilimuni`(programkodu INT, universite VARCHAR(255), tercihsayisi INT)")
mycursor.execute("CREATE TABLE 2020tercihegilimil (programkodu INT, il VARCHAR(255), tercihsayisi SMALLINT)")
mycursor.execute("CREATE TABLE `2020tercihegilimaynifarkli`(programkodu INT, ayniprogram INT, farkliprogram INT, kibristercihleri INT, onlisanstercihleri INT, yabancitercihleri INT)")
mycursor.execute("CREATE TABLE `2020tercihegilimprogram`(programkodu INT, program VARCHAR(255), tercihsayisi INT)")


mycursor.execute("CREATE TABLE 2019genelbilgiler (programkodu INT, universiteturu VARCHAR(255), universite VARCHAR(255),"
                 " fakulte VARCHAR(255), puanturu VARCHAR(255), bursturu VARCHAR(255),genelkontenjan SMALLINT,"
                 " okulbirincisikontenjani SMALLINT, toplamkontenjan SMALLINT,genelkontenjanyerlesen SMALLINT,"
                 " okulbirincisikontenjaniyerlesen SMALLINT, toplamkontenjanyerlesen SMALLINT, boskontenjan SMALLINT,"
                 " ilkyerlesmeorani VARCHAR(255), yerlesipkayityaptirmayan SMALLINT, ekyerlesen SMALLINT,"
                 " 012katsayiileyerlesensonkisininpuani float,012arti006katsayiileyerlesensonkisininpuani float,"
                 " 012katsayiileyerlesensonkisininbasarisirasi INT, 012arti006katsayiileyerlesensonkisininbasarisirasi INT,"
                 " 2020tavanpuan float,2020tavanbasarisirasi INT, 2019dayerlesip2020deobpsikirilarakyerlesensayısi INT,"
                 " yerlesenlerinortalamaobpsi float, yerlesenlerinortalamadiplomanotu float)")

mycursor.execute("CREATE TABLE 2019kontenjan (programkodu INT, genelkontenjan SMALLINT, tubitakkontenjani SMALLINT, engellikontenjani SMALLINT, okulbirincisikontenjani SMALLINT, toplamkontenjan SMALLINT)")
mycursor.execute("CREATE TABLE 2019cinsiyet (programkodu INT, cinsiyet VARCHAR(255), adet SMALLINT)")
mycursor.execute("CREATE TABLE 2019bolge (programkodu INT, bolge VARCHAR(255), adet SMALLINT)")
mycursor.execute("CREATE TABLE 2019ogrenim (programkodu INT, ogrenimdurumu VARCHAR(255), yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE 2019mezuniyetyillari (programkodu INT, mezuniyetyili YEAR, yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE 2019lisealanlari (programkodu INT, lisealani VARCHAR(255), yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE 2019lisegruplari (programkodu INT, lisegrubu VARCHAR(255), yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE 2019tabanpuan (programkodu INT, genelkontenjanyerlesensonkisininpuani float,okulbirincisikontenjaniyerlesensonkisininpuani float, "
                 "genelkontenjanyerlesensonkisininbasarisirasi INT, okulbirincisikontenjaniyerlesensonkisininbasarisirasi INT)")
mycursor.execute("CREATE TABLE 2019net (programkodu INT, test VARCHAR(255), net float)")
mycursor.execute("CREATE TABLE 2019tercihedilme (programkodu INT, tercihedensayisi INT, birkontenjanatalipsayisi float,"
               " ortalamatercihsirasi float, birincisiratercihedensayisi INT, ilkucsiratercihedensayisi INT, ilkdokuzsiratercihedensayisi INT)")
mycursor.execute("CREATE TABLE 2019tercihegilim (programkodu INT, genelkontenjanayerlesensayisi INT, yerlesenlerintoplamtercihhakki INT,"
                 " kullanilantercih INT, bosbirakilantercih INT, yerlesenlerortalamatercihsayisi INT)")
mycursor.execute("CREATE TABLE `2019tercihegilimuni`(programkodu INT, universite VARCHAR(255), tercihsayisi INT)")
mycursor.execute("CREATE TABLE 2019tercihegilimil (programkodu INT, il VARCHAR(255), tercihsayisi SMALLINT)")
mycursor.execute("CREATE TABLE `2019tercihegilimaynifarkli`(programkodu INT, ayniprogram INT, farkliprogram INT, kibristercihleri INT, onlisanstercihleri INT, yabancitercihleri INT)")
mycursor.execute("CREATE TABLE `2019tercihegilimprogram`(programkodu INT, program VARCHAR(255), tercihsayisi INT)")



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

    osym = []
    programKodu = []
    sagGenel = []
    solGenel = []

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
       if elementRight.text == "---":
           sagGenel.append(0)
       else:
           a = elementRight.text.replace(".", "")
           b = a.replace(",", ".")
           sagGenel.append(b)

    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
       solGenel.append(elementLeft.text)
    print(sagGenel)
    programKodu.append(driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[2]").text)
    # osym.append(driver.find_element_by_xpath(
    #     "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[1]").text)

    my_insert_query = u"""INSERT INTO `2020genelbilgiler`(`programkodu`,`universiteturu`,`universite`,`fakulte`,`puanturu`,
    `bursturu`,`genelkontenjan`,`okulbirincisikontenjani`,`toplamkontenjan`,`genelkontenjanyerlesen`,
    `okulbirincisikontenjaniyerlesen`,`toplamkontenjanyerlesen`,`boskontenjan`,`ilkyerlesmeorani`,`yerlesipkayityaptirmayan`,
    `ekyerlesen`,`012katsayiileyerlesensonkisininpuani`,`012arti006katsayiileyerlesensonkisininpuani`,`012katsayiileyerlesensonkisininbasarisirasi`,
    `012arti006katsayiileyerlesensonkisininbasarisirasi`,`2020tavanpuan`,`2020tavanbasarisirasi`,`2019dayerlesip2020deobpsikirilarakyerlesensayısi`,
    `yerlesenlerinortalamaobpsi`,`yerlesenlerinortalamadiplomanotu`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(my_insert_query,sagGenel)
    mydb.commit()



    print ("************** Kontenjan İstatistikleri *********************") #hangi veriler lazım?

    solKontenjan = []
    sagKontenjan = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[3]/div/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solKontenjan.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[3]/div/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagKontenjan.append(0)
        else:
            sagKontenjan.append(elementRight.text)


    a = []
    a.extend(programKodu)
    a.extend(sagKontenjan)

    my_insert_query = u"""INSERT INTO `2020kontenjan`(`programkodu`,`genelkontenjan`,`tubitakkontenjani`,`engellikontenjani`,`okulbirincisikontenjani`,`toplamkontenjan`) VALUES (%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query,a)
    mydb.commit()



    print ("************** Cinsiyet İstatistikleri *********************") #hangi veriler lazım?
    solCinsiyet = []
    sagCinsiyet = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solCinsiyet.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagCinsiyet.append(elementRight.text)

    osymCinsiyet = programKodu * len(solCinsiyet)

    mySql_insert_query = u"""INSERT INTO `2020cinsiyet`(`programkodu`,`cinsiyet`,`adet`) VALUES (%s,%s,%s)"""
    for elem in zip(osymCinsiyet,solCinsiyet,sagCinsiyet):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()




    print ("************** Coğrafi Bölge İstatistikleri *********************") #hangi veriler lazım?

    solBolge =[]
    sagBolge = []
    for i in [2,3]:
        elementsLeft = driver.find_elements_by_css_selector("#icerik_1020ab > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solBolge.append(elementLeft.text)
    for i in [2,3]:
        elementsRight = driver.find_elements_by_css_selector('#icerik_1020ab > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child('+str(i)+') > td:nth-child(2)')
        for elementRight in elementsRight:
            sagBolge.append(elementRight.text)

    for i in [2,3,4,5,6,7,8]:
        elementsLeft = driver.find_elements_by_css_selector("table.table:nth-child(6) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solBolge.append(elementLeft.text)

    for i in [2,3,4,5,6,7,8]:
        elementsRight = driver.find_elements_by_css_selector("table.table:nth-child(6) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagBolge.append(elementRight.text)

    osymBolge = programKodu * len(solBolge)


    mySql_insert_query = u"""INSERT INTO `2020bolge`(`programkodu`,`bolge`,`adet`) VALUES (%s,%s,%s)"""
    for elem in zip(osymBolge,solBolge,sagBolge):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()


    print ("************** Öğrenim Durumu İstatistikleri *********************") #hangi veriler lazım?

    solOgrenim =[]
    sagOgrenim =[]

    for i in [2,3,4,5,6]:
        elementsLeft = driver.find_elements_by_css_selector("#icerik_1030a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solOgrenim.append(elementLeft.text)

    for i in [2,3,4,5,6]:
        elementsRight = driver.find_elements_by_css_selector("#icerik_1030a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            if elementRight.text == "---":
                sagOgrenim.append(0)
            else:
                sagOgrenim.append(elementRight.text)

    osymOgrenim = programKodu * len(solOgrenim)


    mySql_insert_query = u"""INSERT INTO `2020ogrenim`(`programkodu`,`ogrenimdurumu`,`yerlesensayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymOgrenim,solOgrenim,sagOgrenim):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()


    print ("************** Mezuniyet Yılı İstatistikleri *********************") #hangi veriler lazım?

    solMezYil=[]
    sagMezYil=[]

    elementsLeftLen = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr/td[1]")
    for i in [*range(2,len(elementsLeftLen))]: #did not add +1 ro range because elementsLeftLen have 1 more el.
        elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[1]")
        for elementLeft in elementsLeft:
            solMezYil.append(elementLeft.text)


    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagMezYil.append(elementRight.text)

    osymMezYil = programKodu * len(solMezYil)

    mySql_insert_query = u"""INSERT INTO `2020mezuniyetyillari`(`programkodu`,`mezuniyetyili`,`yerlesensayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymMezYil,solMezYil,sagMezYil):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()

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

    osymLiseAlan = programKodu * len(solLiseAlan)


    mySql_insert_query = u"""INSERT INTO `2020lisealanlari`(`programkodu`,`lisealani`,`yerlesensayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymLiseAlan,solLiseAlan,sagLiseAlan):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()


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

    osymLiseGrup = programKodu * len(solLiseGrup)

    mySql_insert_query = u"""INSERT INTO `2020lisegruplari`(`programkodu`,`lisegrubu`,`yerlesensayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymLiseGrup,solLiseGrup,sagLiseGrup):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()


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
            if elementRight.text == "---":
                sagPuan.append(0)
            else:
                a = elementRight.text.replace(",", ".")
                sagPuan.append(a)
    #bottom table
    for i in [1,2]:
        elementsLeft1 = driver.find_elements_by_css_selector("#icerik_1000_3 > table:nth-child(3) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        elementsLeft2 = driver.find_element_by_css_selector("#icerik_1000_3 > table:nth-child(3) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(2)")
        for elementLeft1 in elementsLeft1:
            solPuan.append(elementLeft1.text+elementsLeft2.text)

    for i in [1,2]:
        elementsRight = driver.find_elements_by_css_selector("#icerik_1000_3 > table:nth-child(3) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(4)")
        for elementRight in elementsRight:
            if elementRight.text == "---":
                sagPuan.append(0)
            else:
                a = elementRight.text.replace(".","")
                sagPuan.append(a)
    a = []
    a.extend(programKodu)
    a.extend(sagPuan)

    my_insert_query = u"""INSERT INTO `2020tabanpuan`(`programkodu`,`genelkontenjanyerlesensonkisininpuani`,
    `okulbirincisikontenjaniyerlesensonkisininpuani`,`genelkontenjanyerlesensonkisininbasarisirasi`,
    `okulbirincisikontenjaniyerlesensonkisininbasarisirasi`) VALUES (%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query,a)
    mydb.commit()


    print ("************** Net Ortalamaları *********************") #hangi veriler lazım?

    solNet=[]
    sagNet=[]


    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solNet.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        a = elementRight.text.replace(",",".")
        sagNet.append(a)

    print("sol liste: "+str(len(solNet)))
    print("sag liste: "+str(len(sagNet)))


    osymNet = programKodu * len(solNet)

    mySql_insert_query = u"""INSERT INTO `2020net`(`programkodu`,`test`,`net`) VALUES (%s,%s,%s)"""
    for elem in zip(osymNet,solNet,sagNet):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()


    print ("************** Tercih Edilme İstatistikleri *********************") #hangi veriler lazım?

    solTercih=[]
    sagTercih=[]


    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solTercih.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr/td[2]")
    for elementRight in elementsRight:
        a = elementRight.text.replace(",",".")
        sagTercih.append(a)

    a = []
    a.extend(programKodu)
    a.extend(sagTercih)
    print(a)

    my_insert_query = u"""INSERT INTO `2020tercihedilme`(`programkodu`,`tercihedensayisi`,
    `birkontenjanatalipsayisi`,`ortalamatercihsirasi`,
    `birincisiratercihedensayisi`,`ilkucsiratercihedensayisi`,`ilkdokuzsiratercihedensayisi`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query,a)
    mydb.commit()




    print ("************** Yerleşenlerin Tercih Sıraları *********************") #hangi veriler lazım?

    solTercihSira=[]
    sagTercihSira=[]

    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solTercihSira.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagTercihSira.append(elementRight.text)


    print ("************** Yerleşenlerin Tercih Eğilimleri *********************") #hangi veriler lazım?

    solEgilim=[]
    sagEgilim=[]


    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[7]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilim.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[7]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilim.append(elementRight.text)

    a = []
    a.extend(programKodu)
    a.extend(sagEgilim)

    my_insert_query = u"""INSERT INTO `2020tercihegilim`(`programkodu`,`genelkontenjanayerlesensayisi`,
    `yerlesenlerintoplamtercihhakki`,`kullanilantercih`,
    `bosbirakilantercih`,`yerlesenlerortalamatercihsayisi`) VALUES (%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query,a)
    mydb.commit()


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
            if elementRight.text == "---":
                sagEgilimTur.append(0)
            else:
                sagEgilimTur.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimTur)))
    print("sag liste: " + str(len(sagEgilimTur)))

    a = []
    a.extend(programKodu)
    a.extend(sagEgilimTur)

    my_insert_query = u"""INSERT INTO `2020tercihegilimtur`(`programkodu`,`devlet`,
    `vakif`,`kibris`, `yabanci`) VALUES (%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query,a)
    mydb.commit()



    print("************** Yerleşenlerin Tercih Eğilimleri-Üniler *********************")  # hangi veriler lazım?

    solEgilimUni = []
    sagEgilimUni = []

    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilimUni.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilimUni.append(elementRight.text)

    osymUni = programKodu * len(solEgilimUni)

    mySql_insert_query = u"""INSERT INTO `2020tercihegilimuni`(`programkodu`,`universite`,`tercihsayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymUni,solEgilimUni,sagEgilimUni):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()


    print("************** Yerleşenlerin Tercih Eğilimleri-İller *********************")  # hangi veriler lazım?

    solEgilimIl = []
    sagEgilimIl = []


    elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilimIl.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilimIl.append(elementRight.text)


    osymIl = programKodu * len(solEgilimIl)

    mySql_insert_query = u"""INSERT INTO `2020tercihegilimil`(`programkodu`,`il`,`tercihsayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymIl,solEgilimIl,sagEgilimIl):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()


    print("************** Yerleşenlerin Tercih Eğilimleri-Farklı Program *********************")  # hangi veriler lazım?

    solEgilimAyniFarkli = []
    sagEgilimAyniFarkli = []



    elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilimAyniFarkli.append(elementLeft.text)


    elementsRight = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagEgilimAyniFarkli.append(0)
        else:
            sagEgilimAyniFarkli.append(elementRight.text)

    a = []
    a.extend(programKodu)
    a.extend(sagEgilimAyniFarkli)

    my_insert_query = u"""INSERT INTO `2020tercihegilimaynifarkli`(`programkodu`,`ayniprogram`,`farkliprogram`,
    `kibristercihleri`,`onlisanstercihleri`, `yabancitercihleri`) VALUES (%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query,a)
    mydb.commit()



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

    osymProgram = programKodu * len(solProgram)

    mySql_insert_query = u"""INSERT INTO `2020tercihegilimprogram`(`programkodu`,`program`,`tercihsayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymProgram,solProgram,sagProgram):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()

def bolumBilgiAl2019():
    print(url)
    print(type(url))
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


    programKodu = []
    solGenel = []
    sagGenel = []

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagGenel.append(0)
        else:
            a = elementRight.text.replace(".", "")
            b = a.replace(",", ".")
            sagGenel.append(b)
    print(sagGenel)

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solGenel.append(elementLeft.text)

    programKodu.append(driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[2]").text)


    my_insert_query = u"""INSERT INTO `2019genelbilgiler`(`programkodu`,`universiteturu`,`universite`,`fakulte`,`puanturu`,
    `bursturu`,`genelkontenjan`,`okulbirincisikontenjani`,`toplamkontenjan`,`genelkontenjanyerlesen`,
    `okulbirincisikontenjaniyerlesen`,`toplamkontenjanyerlesen`,`boskontenjan`,`ilkyerlesmeorani`,`yerlesipkayityaptirmayan`,
    `ekyerlesen`,`012katsayiileyerlesensonkisininpuani`,`012arti006katsayiileyerlesensonkisininpuani`,`012katsayiileyerlesensonkisininbasarisirasi`,
    `012arti006katsayiileyerlesensonkisininbasarisirasi`,`2020tavanpuan`,`2020tavanbasarisirasi`,`2019dayerlesip2020deobpsikirilarakyerlesensayısi`,
    `yerlesenlerinortalamaobpsi`,`yerlesenlerinortalamadiplomanotu`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(my_insert_query,sagGenel)
    mydb.commit()



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
        if elementRight.text == "---":
            sagKontenjan.append(0)
        else:
            elementRight.text.replace(",", ".")
            sagKontenjan.append(elementRight.text)


    a = []
    a.extend(programKodu)
    a.extend(sagKontenjan)

    my_insert_query = u"""INSERT INTO `2019kontenjan`(`programkodu`,`genelkontenjan`,`tubitakkontenjani`,`engellikontenjani`,`okulbirincisikontenjani`,`toplamkontenjan`) VALUES (%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query,a)
    mydb.commit()




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
    osymCinsiyet = programKodu * len(solCinsiyet)

    mySql_insert_query = u"""INSERT INTO `2019cinsiyet`(`programkodu`,`cinsiyet`,`adet`) VALUES (%s,%s,%s)"""
    for elem in zip(osymCinsiyet,solCinsiyet,sagCinsiyet):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()



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

    osymBolge = programKodu * len(solBolge)

    mySql_insert_query = u"""INSERT INTO `2019bolge`(`programkodu`,`bolge`,`adet`) VALUES (%s,%s,%s)"""
    for elem in zip(osymBolge,solBolge,sagBolge):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()

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
            if elementRight.text == "---":
                sagOgrenim.append(0)
            else:
                sagOgrenim.append(elementRight.text)

    osymOgrenim = programKodu * len(solOgrenim)

    mySql_insert_query = u"""INSERT INTO `2019ogrenim`(`programkodu`,`ogrenimdurumu`,`yerlesensayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymOgrenim,solOgrenim,sagOgrenim):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()

    print("************** Mezuniyet Yılı İstatistikleri *********************")  # hangi veriler lazım?

    solMezYil = []
    sagMezYil = []

    elementsLeftLen = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr/td[1]")
    for i in [*range(2,len(elementsLeftLen))]: #did not add +1 ro range because elementsLeftLen have 1 more el.
        elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[1]")
    for elementLeft in elementsLeft:
        solMezYil.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagMezYil.append(elementRight.text)

    osymMezYil = programKodu * len(solMezYil)

    mySql_insert_query = u"""INSERT INTO `2019mezuniyetyillari`(`programkodu`,`mezuniyetyili`,`yerlesensayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymMezYil,solMezYil,sagMezYil):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()


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

    osymLiseAlan = programKodu * len(solLiseAlan)

    mySql_insert_query = u"""INSERT INTO `2019lisealanlari`(`programkodu`,`lisealani`,`yerlesensayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymLiseAlan,solLiseAlan,sagLiseAlan):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()


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

    osymLiseGrup = programKodu * len(solLiseGrup)

    mySql_insert_query = u"""INSERT INTO `2019lisegruplari`(`programkodu`,`lisegrubu`,`yerlesensayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymLiseGrup,solLiseGrup,sagLiseGrup):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()
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
            if elementRight.text == "---":
                sagPuan.append(0)
            else:
                a = elementRight.text.replace(",", ".")
                sagPuan.append(a)
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
            if elementRight.text == "---":
                sagPuan.append(0)
            else:
                a = elementRight.text.replace(".","")
                sagPuan.append(a)
        print(sagPuan)


    a = []
    a.extend(programKodu)
    a.extend(sagPuan)

    my_insert_query = u"""INSERT INTO `2019tabanpuan`(`programkodu`,`genelkontenjanyerlesensonkisininpuani`,
    `okulbirincisikontenjaniyerlesensonkisininpuani`,`genelkontenjanyerlesensonkisininbasarisirasi`,
    `okulbirincisikontenjaniyerlesensonkisininbasarisirasi`) VALUES (%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query,a)
    mydb.commit()

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
        a = elementRight.text.replace(",",".")
        sagNet.append(a)

    osymNet = programKodu * len(solNet)

    mySql_insert_query = u"""INSERT INTO `2019net`(`programkodu`,`test`,`net`) VALUES (%s,%s,%s)"""
    for elem in zip(osymNet,solNet,sagNet):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()

    print("************** Tercih Edilme İstatistikleri *********************")  # hangi veriler lazım?

    solTercih = []
    sagTercih = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table[1]/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solTercih.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table[1] /tbody/tr/td[2]")
    for elementRight in elementsRight:
        a = elementRight.text.replace(",", ".")
        sagTercih.append(a)


    a = []
    a.extend(programKodu)
    a.extend(sagTercih)

    my_insert_query = u"""INSERT INTO `2019tercihedilme`(`programkodu`,`tercihedensayisi`,
    `birkontenjanatalipsayisi`,`ortalamatercihsirasi`,
    `birincisiratercihedensayisi`,`ilkucsiratercihedensayisi`,`ilkdokuzsiratercihedensayisi`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query,a)
    mydb.commit()

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

    a = []
    a.extend(programKodu)
    a.extend(sagEgilim)

    my_insert_query = u"""INSERT INTO `2019tercihegilim`(`programkodu`,`genelkontenjanayerlesensayisi`,
    `yerlesenlerintoplamtercihhakki`,`kullanilantercih`,
    `bosbirakilantercih`,`yerlesenlerortalamatercihsayisi`) VALUES (%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query,a)
    mydb.commit()


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

    osymUni = programKodu * len(solEgilimUni)

    mySql_insert_query = u"""INSERT INTO `2019tercihegilimuni`(`programkodu`,`universite`,`tercihsayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymUni,solEgilimUni,sagEgilimUni):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()



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

    osymIl = programKodu * len(solEgilimIl)

    mySql_insert_query = u"""INSERT INTO `2019tercihegilimil`(`programkodu`,`il`,`tercihsayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymIl,solEgilimIl,sagEgilimIl):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()


    print("************** Yerleşenlerin Tercih Eğilimleri-Farklı Program *********************")  # hangi veriler lazım?

    solEgilimAyniFarkli = []
    sagEgilimAyniFarkli = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilimAyniFarkli.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagEgilimAyniFarkli.append(0)
        else:
            sagEgilimAyniFarkli.append(elementRight.text)

    a = []
    a.extend(programKodu)
    a.extend(sagEgilimAyniFarkli)

    my_insert_query = u"""INSERT INTO `2019tercihegilimaynifarkli`(`programkodu`,`ayniprogram`,`farkliprogram`,
    `kibristercihleri`,`onlisanstercihleri`, `yabancitercihleri`) VALUES (%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query,a)
    mydb.commit()


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

    osymProgram = programKodu * len(solProgram)

    mySql_insert_query = u"""INSERT INTO `2019tercihegilimprogram`(`programkodu`,`program`,`tercihsayisi`) VALUES (%s,%s,%s)"""
    for elem in zip(osymProgram,solProgram,sagProgram):

        mycursor.execute(mySql_insert_query,elem)
        mydb.commit()



for kod in listKod[3:6]:

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


for kod in listKod[3:6]:

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

    except NoSuchElementException:
        time.sleep(1)
        print("Exception exist")
        pass



for kod in listKod[3:6]:

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



