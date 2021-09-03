import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="dbname",
    charset='utf8'
)

mycursor = mydb.cursor()

#creating tables

mycursor.execute("CREATE TABLE bolumbilgi (yil YEAR, programadi VARCHAR(255),programkodu INT,  universiteturu VARCHAR(255), "
                 "universite VARCHAR(255), fakulte VARCHAR(255),  puanturu VARCHAR(255), bursturu VARCHAR(255))")

mycursor.execute("CREATE TABLE kontenjan (yil YEAR, programkodu INT, genelkontenjan SMALLINT, tubitakkontenjani SMALLINT, engellikontenjani SMALLINT, okulbirincisikontenjani SMALLINT, toplamkontenjan SMALLINT)")
mycursor.execute("CREATE TABLE cinsiyet (yil YEAR, programkodu INT, cinsiyet VARCHAR(255), adet SMALLINT)")
mycursor.execute("CREATE TABLE bolge (yil YEAR, programkodu INT, bolge VARCHAR(255), adet SMALLINT)")
mycursor.execute("CREATE TABLE genelbilgiler (yil YEAR, programkodu INT, universiteturu VARCHAR(255), universite VARCHAR(255),"
                 " fakulte VARCHAR(255), puanturu VARCHAR(255), bursturu VARCHAR(255),genelkontenjan SMALLINT,"
                 " okulbirincisikontenjani SMALLINT, toplamkontenjan SMALLINT,genelkontenjanyerlesen SMALLINT,"
                 " okulbirincisikontenjaniyerlesen SMALLINT, toplamkontenjanyerlesen SMALLINT, boskontenjan SMALLINT,"
                 " ilkyerlesmeorani VARCHAR(255), yerlesipkayityaptirmayan SMALLINT, ekyerlesen SMALLINT,"
                 " 012katsayiileyerlesensonkisininpuani float,012arti006katsayiileyerlesensonkisininpuani float,"
                 " 012katsayiileyerlesensonkisininbasarisirasi INT, 012arti006katsayiileyerlesensonkisininbasarisirasi INT,"
                 " 2020tavanpuan float,2020tavanbasarisirasi INT, 2019dayerlesip2020deobpsikirilarakyerlesensayısi INT,"
                 " yerlesenlerinortalamaobpsi float, yerlesenlerinortalamadiplomanotu float)")
mycursor.execute("CREATE TABLE geldikleriiller (yil YEAR, programkodu INT, geldikleriil VARCHAR(255), yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE ogrenim (yil YEAR, programkodu INT, ogrenimdurumu VARCHAR(255), yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE mezuniyetyillari (yil YEAR, programkodu INT, mezuniyetyili YEAR, yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE lisealanlari (yil YEAR, programkodu INT, lisealani VARCHAR(255), yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE lisegruplari (yil YEAR, programkodu INT, lisegrubu VARCHAR(255), yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE liseler (yil YEAR, programkodu INT, lise VARCHAR(255), yerlesensayisi SMALLINT)")
mycursor.execute("CREATE TABLE tabanpuan (yil YEAR, programkodu INT, genelkontenjanyerlesensonkisininpuani float,okulbirincisikontenjaniyerlesensonkisininpuani float, "
                 "genelkontenjanyerlesensonkisininbasarisirasi int, okulbirincisikontenjaniyerlesensonkisininbasarisirasi int)")
mycursor.execute("CREATE TABLE net (yil YEAR, programkodu INT, test VARCHAR(255), net float)")
mycursor.execute("CREATE TABLE `puansiralama`(yil YEAR, programkodu INT, ortalamaobp float, ortalamatytpuan float,"
                 " endusukobp float, endusuktytpuan float, ortalamatytsiralama INT, endusuktytsiralama INT)")
mycursor.execute("CREATE TABLE tercihedilme (yil YEAR, programkodu INT, tercihedensayisi INT, birkontenjanatalipsayisi float,"
               " ortalamatercihsirasi float, birincisiratercihedensayisi INT, ilkucsiratercihedensayisi INT, ilkdokuzsiratercihedensayisi INT)")
mycursor.execute("CREATE TABLE tercihyerlesme (yil YEAR, programkodu INT, yerlesensayisi INT, birincitercihyerlesen INT,"
               " ilkuctercihyerlesen INT, ilkontercihyerlesen INT, yerlesenortalamasira float)")
mycursor.execute("CREATE TABLE tercihegilim (yil YEAR, programkodu INT, genelkontenjanayerlesensayisi INT, yerlesenlerintoplamtercihhakki INT,"
                 " kullanilantercih INT, bosbirakilantercih INT, yerlesenlerortalamatercihsayisi INT)")
mycursor.execute("CREATE TABLE `tercihegilimtur`(yil YEAR, programkodu INT, devlet INT, vakif INT, kibris INT, yabanci INT)")
mycursor.execute("CREATE TABLE `tercihegilimuni`(yil YEAR, programkodu INT, universite VARCHAR(255), tercihsayisi INT)")
mycursor.execute("CREATE TABLE tercihegilimil (yil YEAR, programkodu INT, il VARCHAR(255), tercihsayisi SMALLINT)")
mycursor.execute("CREATE TABLE `tercihegilimaynifarkli`(yil YEAR, programkodu INT, ayniprogram INT, farkliprogram INT, kibristercihleri INT, onlisanstercihleri INT, yabancitercihleri INT)")
mycursor.execute("CREATE TABLE `tercihegilimprogram`(yil YEAR, programkodu INT, program VARCHAR(255), tercihsayisi INT)")
mycursor.execute("CREATE TABLE `yerlesmekosullari`(yil YEAR, programkodu INT, kosulno SMALLINT)")

#webdriver
driver = webdriver.Firefox()

#reading csv and adding to a list
df = pd.read_csv('osymveri.csv')
listKod = df['AAA'].tolist()

#some pages have 1 more div that named "Akademik Kadro". I used this func for them.
def bolumBilgiAlCokDiv():

    url2019 = "/2019/"
    url2018 = "/2018/"
    strUrl = str(url)

    if url2018 in strUrl:
        print("2018 yılı")
        yil = 2018
    elif url2019 in strUrl:
        print("2019 yılı")
        yil = 2019
    else:
        print("2020 yılı")
        yil = 2020

#close pop ups
    try:
        myBtn = driver.find_element_by_class_name("featherlight-close-icon")
        driver.execute_script("arguments[0].click();", myBtn)
        myBtn = driver.find_element_by_class_name("featherlight-close-icon")
        driver.execute_script("arguments[0].click();", myBtn)

    except NoSuchElementException:
        pass

#clicking buttons for get data
    try:
        myBtns = WebDriverWait(driver, 3).until( \
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "glyphicon-arrow-down")))
        for i in myBtns:
            driver.execute_script("arguments[0].click();", i)

    except TimeoutException:
        pass
    WebDriverWait(driver, 4).until( \
        EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/div/table/tbody/tr/td")))

#getting datas and inserting to tables
    # print("************** Bolum Bilgiler *********************")
    programKodu = []
    sagBolum = []
    yilList = []

    programKodu.append(str(kod))
    yilList.append(str(yil))

    WebDriverWait(driver, 4).until( \
        EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[1]/thead/tr/th")))
    bolumAdi = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[1]/thead/tr/th")
    sagBolum.append(bolumAdi.text)

    print(sagBolum)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[1]/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagBolum.append(None)
        elif elementRight.text == "Dolmadı":
            sagBolum.append(None)
        elif elementRight.text == "":
            sagBolum.append(0)
        else:
            a = elementRight.text.replace(".", "")
            b = a.replace(",", ".")
            sagBolum.append(b)

    a = []
    a.append(str(yil))
    a.extend(sagBolum)

    my_insert_query = u"""INSERT INTO `bolumbilgi`(`yil`,`programadi`,`programkodu`,`universiteturu`,`universite`,`fakulte`,`puanturu`,`bursturu`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Genel Bilgiler *********************")

    sagGenel = []

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagGenel.append(None)
        elif elementRight.text == "Dolmadı":
            sagGenel.append(None)
        elif elementRight.text == "":
            sagGenel.append(0)
        else:
            a = elementRight.text.replace(".", "")
            b = a.replace(",", ".")
            sagGenel.append(b)


    a = []
    a.append(yil)
    a.extend(sagGenel)


    my_insert_query = u"""INSERT INTO `genelbilgiler`(`yil`,`programkodu`,`universiteturu`,`universite`,`fakulte`,`puanturu`,
            `bursturu`,`genelkontenjan`,`okulbirincisikontenjani`,`toplamkontenjan`,`genelkontenjanyerlesen`,
            `okulbirincisikontenjaniyerlesen`,`toplamkontenjanyerlesen`,`boskontenjan`,`ilkyerlesmeorani`,`yerlesipkayityaptirmayan`,
            `ekyerlesen`,`012katsayiileyerlesensonkisininpuani`,`012arti006katsayiileyerlesensonkisininpuani`,`012katsayiileyerlesensonkisininbasarisirasi`,
            `012arti006katsayiileyerlesensonkisininbasarisirasi`,`2020tavanpuan`,`2020tavanbasarisirasi`,`2019dayerlesip2020deobpsikirilarakyerlesensayısi`,
            `yerlesenlerinortalamaobpsi`,`yerlesenlerinortalamadiplomanotu`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Kontenjan İstatistikleri *********************")

    sagKontenjan = []

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[3]/div/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagKontenjan.append(0)
        else:
            elementRight.text.replace(",", ".")
            sagKontenjan.append(elementRight.text)

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagKontenjan)


    my_insert_query = u"""INSERT INTO `kontenjan`(`yil`,`programkodu`,`genelkontenjan`,`tubitakkontenjani`,`engellikontenjani`,`okulbirincisikontenjani`,`toplamkontenjan`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Cinsiyet İstatistikleri *********************")
    solCinsiyet = []
    sagCinsiyet = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solCinsiyet.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "":
            sagCinsiyet.append(0)
        else:
            sagCinsiyet.append(elementRight.text)

    osymCinsiyet = programKodu * len(solCinsiyet)
    yilCinsiyet = yilList * len(solCinsiyet)


    mySql_insert_query = u"""INSERT INTO `cinsiyet`(`yil`,`programkodu`,`cinsiyet`,`adet`) VALUES (%s,%s,%s,%s)"""
    for elem in zip(yilCinsiyet,osymCinsiyet, solCinsiyet, sagCinsiyet):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Coğrafi Bölge İstatistikleri *********************")

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
            if elementRight.text == "---":
                sagBolge.append(0)
            else:
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
            if elementRight.text == "---":
                sagBolge.append(0)
            else:
                sagBolge.append(elementRight.text)

    osymBolge = programKodu * len(solBolge)
    yilBolge = yilList * len(solBolge)

    mySql_insert_query = u"""INSERT INTO `bolge`(`yil`,`programkodu`,`bolge`,`adet`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilBolge,osymBolge, solBolge, sagBolge):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Geldikleri İller *********************")

    solGeldikleriIller = []
    sagGeldikleriIller = []

    elementsLeftLen = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr/td[1]")
    for i in [*range(2, len(elementsLeftLen))]:  # did not add +1 ro range because elementsLeftLen have 1 more el.
        elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]")
        for elementLeft in elementsLeft:
            if elementLeft.text == "Diğer":
                solGeldikleriIller.append(None)
            else:
                solGeldikleriIller.append(elementLeft.text)
    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagGeldikleriIller.append(elementRight.text)

    osymGeldikleriIller = programKodu * len(solGeldikleriIller)
    yilGeldikleriIller = yilList * len(solGeldikleriIller)

    mySql_insert_query = u"""INSERT INTO `geldikleriiller`(`yil`,`programkodu`,`geldikleriil`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""
    for elem in zip(yilGeldikleriIller, osymGeldikleriIller, solGeldikleriIller, sagGeldikleriIller):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Öğrenim Durumu İstatistikleri *********************")

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
    yilOgrenim = yilList * len(solOgrenim)


    mySql_insert_query = u"""INSERT INTO `ogrenim`(`yil`,`programkodu`,`ogrenimdurumu`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""
    for elem in zip(yilOgrenim,osymOgrenim, solOgrenim, sagOgrenim):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Mezuniyet Yılı İstatistikleri *********************")

    solMezYil = []
    sagMezYil = []

    elementsLeftLen = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr/td[1]")
    for i in [*range(2, len(elementsLeftLen))]:  # did not add +1 ro range because elementsLeftLen have 1 more el.
        elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]")
        for elementLeft in elementsLeft:
            if elementLeft.text == "Diğer":
                solMezYil.append(None)
            else:
                solMezYil.append(elementLeft.text)
    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagMezYil.append(elementRight.text)

    osymMezYil = programKodu * len(solMezYil)
    yilMezYil = yilList * len(solMezYil)

    mySql_insert_query = u"""INSERT INTO `mezuniyetyillari`(`yil`,`programkodu`,`mezuniyetyili`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""
    for elem in zip(yilMezYil, osymMezYil, solMezYil, sagMezYil):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Lise Alanı İstatistikleri *********************")

    solLiseAlan = []
    sagLiseAlan = []

    elementsLeftNum = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr/td[1]")

    for i in list(range(2, len(list(elementsLeftNum)) + 1)):
        elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]")
        for elementLeft in elementsLeft:
            solLiseAlan.append(elementLeft.text)

    for i in list(range(2, len(list(elementsLeftNum)) + 1)):
        elementsRight = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[2]")
        for elementRight in elementsRight:
            sagLiseAlan.append(elementRight.text)

    osymLiseAlan = programKodu * len(solLiseAlan)
    yilLiseAlan = yilList * len(solLiseAlan)

    mySql_insert_query = u"""INSERT INTO `lisealanlari`(`yil`,`programkodu`,`lisealani`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilLiseAlan, osymLiseAlan, solLiseAlan, sagLiseAlan):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Lise Grubu İstatistikleri *********************")

    solLiseGrup = []
    sagLiseGrup = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solLiseGrup.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagLiseGrup.append(elementRight.text)

    osymLiseGrup = programKodu * len(solLiseGrup)
    yilLiseGrup = yilList * len(solLiseGrup)

    mySql_insert_query = u"""INSERT INTO `lisegruplari`(`yil`,`programkodu`,`lisegrubu`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""
    for elem in zip(yilLiseGrup, osymLiseGrup, solLiseGrup, sagLiseGrup):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Liseler *********************")

    solLiseler = []
    sagLiseler = []

    elementsLeftLen = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/tbody/tr/td[1]")
    for i in [*range(2, len(elementsLeftLen))]:  # did not add +1 ro range because elementsLeftLen have 1 more el.
        elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]")
        for elementLeft in elementsLeft:
            if elementLeft.text == "Diğer":
                solLiseler.append(None)
            else:
                solLiseler.append(elementLeft.text)
    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagLiseler.append(elementRight.text)

    osymLiseler = programKodu * len(solLiseler)
    yilLiseler = yilList * len(solLiseler)

    mySql_insert_query = u"""INSERT INTO `liseler`(`yil`,`programkodu`,`lise`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""
    for elem in zip(yilLiseler, osymLiseler, solGeldikleriIller, sagGeldikleriIller):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Taban Puan ve Başarı Sırası *********************")

    solPuan = []
    sagPuan = []

    for i in [1, 2]:
        elementsLeft1 = driver.find_elements_by_css_selector(
            "#icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(1)")
        elementsLeft2 = driver.find_element_by_css_selector(
            "#icerik_1000_3 > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(4)")
        for elementLeft1 in elementsLeft1:
            solPuan.append(elementLeft1.text + elementsLeft2.text)

    for i in [1, 2]:
        elementsRight = driver.find_elements_by_css_selector(
            "#icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(4)")
        for elementRight in elementsRight:
            if elementRight.text == "---":
                sagPuan.append(None)
            elif elementRight.text == '':
                sagPuan.append(None)
            elif elementRight.text == "Dolmadı":
                sagPuan.append(None)
            else:
                a = elementRight.text.replace(".", "")
                b = a.replace(",", ".")
                sagPuan.append(b)
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
                sagPuan.append(None)
            elif elementRight.text == '':
                sagPuan.append(None)
            elif elementRight.text == "Dolmadı":
                sagPuan.append(None)
            else:
                a = elementRight.text.replace(".", "")
                b = a.replace(",", ".")
                sagPuan.append(b)
    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagPuan)

    my_insert_query = u"""INSERT INTO `tabanpuan`(`yil`,`programkodu`,`genelkontenjanyerlesensonkisininpuani`,
        `okulbirincisikontenjaniyerlesensonkisininpuani`,`genelkontenjanyerlesensonkisininbasarisirasi`,
        `okulbirincisikontenjaniyerlesensonkisininbasarisirasi`) VALUES (%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Net Ortalamaları *********************")

    solNet = []
    sagNet = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        if elementLeft.text == "---":
            solNet.append(None)
        else:
            solNet.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagNet.append(None)
        else:
            a = elementRight.text.replace(",", ".")
            sagNet.append(a)

    osymNet = programKodu * len(solNet)
    yilNet = yilList * len(solNet)

    mySql_insert_query = u"""INSERT INTO `net`(`yil`,`programkodu`,`test`,`net`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilNet,osymNet, solNet, sagNet):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** YKS Puan ve Başarı Sırası *********************")

    puanBasari = []

    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/table/tbody/tr[2]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/table/tbody/tr[3]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/div[2]/table/tbody/tr[3]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table/tbody/tr[2]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(puanBasari)

    my_insert_query = u"""INSERT INTO `puansiralama`(`yil`,`programkodu`,`ortalamaobp`,
        `ortalamatytpuan`,`endusukobp`,`endusuktytpuan`,`ortalamatytsiralama`,`endusuktytsiralama`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Tercih Edilme İstatistikleri *********************")

    sagTercih = []

    elementsRight = WebDriverWait(driver, 3).until( \
                EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr/td[2]")))
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagTercih.append(0)
        elif elementRight.text == "":
            sagTercih.append(0)
        else:
            a = elementRight.text.replace(",", ".")
            sagTercih.append(a)

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagTercih)

    my_insert_query = u"""INSERT INTO `tercihedilme`(`yil`,`programkodu`,`tercihedensayisi`,
        `birkontenjanatalipsayisi`,`ortalamatercihsirasi`,
        `birincisiratercihedensayisi`,`ilkucsiratercihedensayisi`,`ilkdokuzsiratercihedensayisi`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Tercih Yerleşme İstatistikleri *********************")

    sagTercihYerlesme = []

    elementsRight = WebDriverWait(driver, 3).until( \
        EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[1]/tbody/tr/td[2]")))
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagTercihYerlesme.append(0)
        elif elementRight.text == "":
            sagTercihYerlesme.append(0)
        else:
            a = elementRight.text.replace(",", ".")
            sagTercihYerlesme.append(a)

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagTercihYerlesme)

    my_insert_query = u"""INSERT INTO `tercihyerlesme`(`yil`,`programkodu`,`yerlesensayisi`,
            `birincitercihyerlesen`,`ilkuctercihyerlesen`,
            `ilkontercihyerlesen`,`yerlesenortalamasira`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Yerleşenlerin Tercih Eğilimleri *********************")

    sagEgilim = []

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[7]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "":
            sagEgilim.append(0)
        elif elementRight.text == "---":
            sagEgilim.append(0)
        else:
            sagEgilim.append(elementRight.text)

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagEgilim)

    my_insert_query = u"""INSERT INTO `tercihegilim`(`yil`,`programkodu`,`genelkontenjanayerlesensayisi`,
        `yerlesenlerintoplamtercihhakki`,`kullanilantercih`,
        `bosbirakilantercih`,`yerlesenlerortalamatercihsayisi`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Yerleşenlerin Tercih Eğilimleri-Üni Türleri *********************")

    sagEgilimTur = []

    for i in list(range(1, 6)):
        elementsRight = driver.find_elements_by_css_selector(
            "#icerik_1310 > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(" + str(i) + ") > td:nth-child(2)")
        for elementRight in elementsRight:
            if elementRight.text == "---":
                sagEgilimTur.append(0)
            else:
                sagEgilimTur.append(elementRight.text)
        if not sagEgilimTur:
            sagEgilimTur = [0,0,0,0]

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagEgilimTur)

    my_insert_query = u"""INSERT INTO `tercihegilimtur`(`yil`,`programkodu`,`devlet`,
        `vakif`,`kibris`, `yabanci`) VALUES (%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Yerleşenlerin Tercih Eğilimleri-Üniler *********************")

    solEgilimUni = []
    sagEgilimUni = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solEgilimUni.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagEgilimUni.append(elementRight.text)

    osymUni = programKodu * len(solEgilimUni)
    yilUni = yilList * len(solEgilimUni)

    mySql_insert_query = u"""INSERT INTO `tercihegilimuni`(`yil`,`programkodu`,`universite`,`tercihsayisi`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilUni,osymUni, solEgilimUni, sagEgilimUni):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Yerleşenlerin Tercih Eğilimleri-İller *********************")

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

    osymIl = programKodu * len(solEgilimIl)
    yilIl = yilList * len(solEgilimIl)

    mySql_insert_query = u"""INSERT INTO `tercihegilimil`(`yil`,`programkodu`,`il`,`tercihsayisi`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilIl, osymIl, solEgilimIl, sagEgilimIl):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Yerleşenlerin Tercih Eğilimleri-Farklı Program *********************")

    sagEgilimAyniFarkli = []

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagEgilimAyniFarkli.append(0)
        elif elementRight.text == None:
            sagEgilimAyniFarkli.append(0)
        else:
            sagEgilimAyniFarkli.append(elementRight.text)
    if not sagEgilimAyniFarkli:
        sagEgilimAyniFarkli = [0,0,0,0,0]

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagEgilimAyniFarkli)

    my_insert_query = u"""INSERT INTO `tercihegilimaynifarkli`(`yil`,`programkodu`,`ayniprogram`,`farkliprogram`,
        `kibristercihleri`,`onlisanstercihleri`, `yabancitercihleri`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Yerleşenlerin Tercih Programlar *********************")

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

    osymProgram = programKodu * len(solProgram)
    yilProgram = yilList * len(solProgram)

    mySql_insert_query = u"""INSERT INTO `tercihegilimprogram`(`yil`,`programkodu`,`program`,`tercihsayisi`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilProgram, osymProgram, solProgram, sagProgram):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Yerleşme Koşulları *********************")

    kosulNo = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[13]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        kosulNo.append(elementLeft.text)


    osymKosul = programKodu * len(kosulNo)
    yilKosul = yilList * len(kosulNo)

    mySql_insert_query = u"""INSERT INTO `yerlesmekosullari`(`yil`,`programkodu`,`kosulno`) VALUES (%s,%s,%s)"""

    for elem in zip(yilKosul,osymKosul, kosulNo):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

def bolumBilgiAlAzDiv():

    url2019 = "/2019/"
    url2018 = "/2018/"
    strUrl = str(url)

    if url2018 in strUrl:
        print("2018 yılı")
        yil = "2018"
    elif url2019 in strUrl:
        print("2019 yılı")
        yil = "2019"
    else:
        print("2020 yılı")
        yil = "2020"

    try:
        myBtn = driver.find_element_by_class_name("featherlight-close-icon")
        driver.execute_script("arguments[0].click();", myBtn)
        myBtn = driver.find_element_by_class_name("featherlight-close-icon")
        driver.execute_script("arguments[0].click();", myBtn)

    except NoSuchElementException:
        pass
    try:
        myBtns = WebDriverWait(driver, 4).until( \
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "glyphicon-arrow-down")))
        for i in myBtns:
            driver.execute_script("arguments[0].click();", i)
    except TimeoutException:
        pass
    try:
        WebDriverWait(driver, 4).until( \
            EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/div/table")))
    except NoSuchElementException:
        pass
    WebDriverWait(driver, 4).until( \
        EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/div/table/tbody/tr/td")))


    # print("************** Bolum Bilgiler *********************")
    programKodu = []
    sagBolum = []
    yilList = []


    programKodu.append(str(kod))
    yilList.append(str(yil))

    WebDriverWait(driver, 4).until( \
        EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div/table[1]/thead/tr/th")))
    bolumAdi = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div/table[1]/thead/tr/th")
    sagBolum.append(bolumAdi.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div/table[1]/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagBolum.append(None)
        elif elementRight.text == "Dolmadı":
            sagBolum.append(None)
        elif elementRight.text == "":
            sagBolum.append(0)
        else:
            a = elementRight.text.replace(".", "")
            b = a.replace(",", ".")
            sagBolum.append(b)

    print(sagBolum)

    a = []
    a.append(str(yil))
    a.extend(sagBolum)

    my_insert_query = u"""INSERT INTO `bolumbilgi`(`yil`,`programadi`,`programkodu`,`universiteturu`,`universite`,`fakulte`,`puanturu`,`bursturu`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Genel Bilgiler *********************")

    sagGenel = []

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[1]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagGenel.append(None)
        elif elementRight.text == "Dolmadı":
            sagGenel.append(None)
        elif elementRight.text == "":
            sagGenel.append(0)
        else:
            a = elementRight.text.replace(".", "")
            b = a.replace(",", ".")
            sagGenel.append(b)

    a = []
    a.append(yil)
    a.extend(sagGenel)
    my_insert_query = u"""INSERT INTO `genelbilgiler`(`yil`,`programkodu`,`universiteturu`,`universite`,`fakulte`,`puanturu`,
            `bursturu`,`genelkontenjan`,`okulbirincisikontenjani`,`toplamkontenjan`,`genelkontenjanyerlesen`,
            `okulbirincisikontenjaniyerlesen`,`toplamkontenjanyerlesen`,`boskontenjan`,`ilkyerlesmeorani`,`yerlesipkayityaptirmayan`,
            `ekyerlesen`,`012katsayiileyerlesensonkisininpuani`,`012arti006katsayiileyerlesensonkisininpuani`,`012katsayiileyerlesensonkisininbasarisirasi`,
            `012arti006katsayiileyerlesensonkisininbasarisirasi`,`2020tavanpuan`,`2020tavanbasarisirasi`,`2019dayerlesip2020deobpsikirilarakyerlesensayısi`,
            `yerlesenlerinortalamaobpsi`,`yerlesenlerinortalamadiplomanotu`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(my_insert_query, a)
    mydb.commit()


    # print("************** Kontenjan İstatistikleri *********************")

    sagKontenjan = []

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagKontenjan.append(0)
        else:
            elementRight.text.replace(",", ".")
            sagKontenjan.append(elementRight.text)

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagKontenjan)

    my_insert_query = u"""INSERT INTO `kontenjan`(`yil`,`programkodu`,`genelkontenjan`,`tubitakkontenjani`,`engellikontenjani`,`okulbirincisikontenjani`,`toplamkontenjan`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Cinsiyet İstatistikleri *********************")

    solCinsiyet = []
    sagCinsiyet = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        solCinsiyet.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "":
            sagCinsiyet.append(0)
        else:
            sagCinsiyet.append(elementRight.text)

    osymCinsiyet = programKodu * len(solCinsiyet)
    yilCinsiyet = yilList * len(solCinsiyet)


    mySql_insert_query = u"""INSERT INTO `cinsiyet`(`yil`,`programkodu`,`cinsiyet`,`adet`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilCinsiyet,osymCinsiyet, solCinsiyet, sagCinsiyet):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Coğrafi Bölge İstatistikleri *********************")

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
            if elementRight.text == "---":
                sagBolge.append(0)
            else:
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
            if elementRight.text == "---":
                sagBolge.append(0)
            else:
                sagBolge.append(elementRight.text)


    osymBolge = programKodu * len(solBolge)
    yilBolge = yilList * len(solBolge)

    mySql_insert_query = u"""INSERT INTO `bolge`(`yil`,`programkodu`,`bolge`,`adet`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilBolge,osymBolge, solBolge, sagBolge):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Geldikleri İller *********************")

    solGeldikleriIller = []
    sagGeldikleriIller = []

    elementsLeftLen = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table/tbody/tr/td[1]")
    for i in [*range(2, len(elementsLeftLen))]:  # did not add +1 ro range because elementsLeftLen have 1 more el.
        elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]")
        for elementLeft in elementsLeft:
            if elementLeft.text == "Diğer":
                solGeldikleriIller.append(None)
            else:
                solGeldikleriIller.append(elementLeft.text)
    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagGeldikleriIller.append(elementRight.text)

    osymGeldikleriIller = programKodu * len(solGeldikleriIller)
    yilGeldikleriIller = yilList * len(solGeldikleriIller)

    mySql_insert_query = u"""INSERT INTO `geldikleriiller`(`yil`,`programkodu`,`geldikleriil`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""
    for elem in zip(yilGeldikleriIller, osymGeldikleriIller, solGeldikleriIller, sagGeldikleriIller):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Öğrenim Durumu İstatistikleri *********************")

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
    yilOgrenim = yilList * len(solOgrenim)

    mySql_insert_query = u"""INSERT INTO `ogrenim`(`yil`,`programkodu`,`ogrenimdurumu`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilOgrenim, osymOgrenim, solOgrenim, sagOgrenim):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Mezuniyet Yılı İstatistikleri *********************")

    solMezYil = []
    sagMezYil = []

    elementsLeftLen = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr/td[1]")
    for i in [*range(2, len(elementsLeftLen))]:  # did not add +1 ro range because elementsLeftLen have 1 more el.
        elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]")
    for elementLeft in elementsLeft:
        if elementLeft.text == "Diğer":
            solMezYil.append(None)
        else:
            solMezYil.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagMezYil.append(elementRight.text)

    osymMezYil = programKodu * len(solMezYil)
    yilMezYil = yilList * len(solMezYil)

    mySql_insert_query = u"""INSERT INTO `mezuniyetyillari`(`yil`,`programkodu`,`mezuniyetyili`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilMezYil, osymMezYil, solMezYil, sagMezYil):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Lise Alanı İstatistikleri *********************")

    solLiseAlan = []
    sagLiseAlan = []

    elementsLeftNum = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr/td[1]")

    for i in list(range(2, len(list(elementsLeftNum)) + 1)):
        elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]")
        for elementLeft in elementsLeft:
            solLiseAlan.append(elementLeft.text)

    for i in list(range(2, len(list(elementsLeftNum)) + 1)):
        elementsRight = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[2]")
        for elementRight in elementsRight:
            sagLiseAlan.append(elementRight.text)

    osymLiseAlan = programKodu * len(solLiseAlan)
    yilLiseAlan = yilList * len(solLiseAlan)

    mySql_insert_query = u"""INSERT INTO `lisealanlari`(`yil`,`programkodu`,`lisealani`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilLiseAlan, osymLiseAlan, solLiseAlan, sagLiseAlan):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Lise Grubu İstatistikleri *********************")

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
    yilLiseGrup = yilList * len(solLiseGrup)

    mySql_insert_query = u"""INSERT INTO `lisegruplari`(`yil`,`programkodu`,`lisegrubu`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilLiseGrup, osymLiseGrup, solLiseGrup, sagLiseGrup):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Liseler *********************")
    solLiseler = []
    sagLiseler = []

    elementsLeftLen = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr/td[1]")
    for i in [*range(2, len(elementsLeftLen))]:  # did not add +1 ro range because elementsLeftLen have 1 more el.
        elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]")
        for elementLeft in elementsLeft:
            if elementLeft.text == "Diğer":
                solLiseler.append(None)
            else:
                solLiseler.append(elementLeft.text)
    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        sagLiseler.append(elementRight.text)

    osymLiseler = programKodu * len(solLiseler)
    yilLiseler = yilList * len(solLiseler)

    mySql_insert_query = u"""INSERT INTO `liseler`(`yil`,`programkodu`,`lise`,`yerlesensayisi`) VALUES (%s,%s,%s,%s)"""
    for elem in zip(yilLiseler, osymLiseler, solGeldikleriIller, sagGeldikleriIller):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Taban Puan ve Başarı Sırası *********************")

    solPuan = []
    sagPuan = []

    for i in [1, 2]:
        elementsLeft1 = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table[1]/tbody/tr[" + str(i) + "]/td[1]")
        elementsLeft2 = driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table[1]/thead/tr/th[4]")
        for elementLeft1 in elementsLeft1:
            solPuan.append(elementLeft1.text + elementsLeft2.text)

    for i in [1, 2]:
        elementsRight = driver.find_elements_by_css_selector(
            "#icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(4)")
        for elementRight in elementsRight:
            if elementRight.text == "---":
                sagPuan.append(None)
            elif elementRight.text == '':
                sagPuan.append(None)
            elif elementRight.text == "Dolmadı":
                sagPuan.append(None)
            else:
                a = elementRight.text.replace(".", "")
                b = a.replace(",", ".")
                sagPuan.append(b)
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
                sagPuan.append(None)
            elif elementRight.text == '':
                sagPuan.append(None)
            elif elementRight.text == "Dolmadı":
                sagPuan.append(None)
            else:
                a = elementRight.text.replace(".", "")
                b = a.replace(",", ".")
                sagPuan.append(b)

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagPuan)

    my_insert_query = u"""INSERT INTO `tabanpuan`(`yil`,`programkodu`,`genelkontenjanyerlesensonkisininpuani`,
        `okulbirincisikontenjaniyerlesensonkisininpuani`,`genelkontenjanyerlesensonkisininbasarisirasi`,
        `okulbirincisikontenjaniyerlesensonkisininbasarisirasi`) VALUES (%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Net Ortalamaları *********************")

    solNet = []
    sagNet = []

    elementsLeft = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[1]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        if elementLeft.text == "---":
            solNet.append(None)
        else:
            solNet.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[1]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagNet.append(None)
        else:
            a = elementRight.text.replace(",", ".")
            sagNet.append(a)

    osymNet = programKodu * len(solNet)
    yilNet = yilList * len(solNet)

    mySql_insert_query = u"""INSERT INTO `net`(`yil`,`programkodu`,`test`,`net`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilNet,osymNet, solNet, sagNet):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** YKS Puan ve Başarı Sırası *********************")

    puanBasari = []

    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr[2]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr[3]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[3]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/table/tbody/tr[2]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)
    element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[2]")
    if element.text == "---":
        sagPuan.append(None)
    elif element.text == '':
        sagPuan.append(None)
    elif element.text == "Dolmadı":
        sagPuan.append(None)
    else:
        a = element.text.replace(".", "")
        b = a.replace(",", ".")
        puanBasari.append(b)

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(puanBasari)

    my_insert_query = u"""INSERT INTO `puansiralama`(`yil`,`programkodu`,`ortalamaobp`,
        `ortalamatytpuan`,`endusukobp`,`endusuktytpuan`,`ortalamatytsiralama`,`endusuktytsiralama`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Tercih Edilme İstatistikleri *********************")

    # solTercih = []
    sagTercih = []

    # elementsLeft = driver.find_elements_by_xpath(
    #     "/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table[1]/tbody/tr/td[1]")
    # for elementLeft in elementsLeft:
    #     solTercih.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table[1] /tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagTercih.append(0)
        elif elementRight.text == "":
            sagTercih.append(0)
        else:
            a = elementRight.text.replace(",", ".")
            sagTercih.append(a)

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagTercih)

    my_insert_query = u"""INSERT INTO `tercihedilme`(`yil`,`programkodu`,`tercihedensayisi`,
        `birkontenjanatalipsayisi`,`ortalamatercihsirasi`,
        `birincisiratercihedensayisi`,`ilkucsiratercihedensayisi`,`ilkdokuzsiratercihedensayisi`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Tercih Yerleşme İstatistikleri *********************")

    sagTercihYerlesme = []

    elementsRight = WebDriverWait(driver, 3).until( \
        EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr/td[2]")))
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagTercihYerlesme.append(0)
        elif elementRight.text == "":
            sagTercihYerlesme.append(0)
        else:
            a = elementRight.text.replace(",", ".")
            sagTercihYerlesme.append(a)

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagTercihYerlesme)

    my_insert_query = u"""INSERT INTO `tercihyerlesme`(`yil`,`programkodu`,`yerlesensayisi`,
            `birincitercihyerlesen`,`ilkuctercihyerlesen`,
            `ilkontercihyerlesen`,`yerlesenortalamasira`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Yerleşenlerin Tercih Sıraları *********************")
    #
    # solTercihSira = []
    # sagTercihSira = []
    #
    # elementsLeft = driver.find_elements_by_xpath(
    #     "/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[1]")
    # for elementLeft in elementsLeft:
    #     solTercihSira.append(elementLeft.text)
    #
    # elementsRight = driver.find_elements_by_xpath(
    #     "/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[2]")
    # for elementRight in elementsRight:
    #     sagTercihSira.append(elementRight.text)

    # print("************** Yerleşenlerin Tercih Eğilimleri *********************")

    # solEgilim = []
    sagEgilim = []

    # elementsLeft = driver.find_elements_by_xpath(
    #     "/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table/tbody/tr/td[1]")
    # for elementLeft in elementsLeft:
    #     solEgilim.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "":
            sagEgilim.append(0)
        elif elementRight.text == "---":
            sagEgilim.append(0)
        else:
            sagEgilim.append(elementRight.text)

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagEgilim)

    my_insert_query = u"""INSERT INTO `tercihegilim`(`yil`,`programkodu`,`genelkontenjanayerlesensayisi`,
        `yerlesenlerintoplamtercihhakki`,`kullanilantercih`,
        `bosbirakilantercih`,`yerlesenlerortalamatercihsayisi`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Yerleşenlerin Tercih Eğilimleri-Üni Türleri *********************")

    # solEgilimTur = []
    sagEgilimTur = []

    # for i in list(range(1, 6)):
    #     elementsLeft = driver.find_elements_by_css_selector(
    #         "#icerik_1310 > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(" + str(i) + ") > td:nth-child(1)")
    #     for elementLeft in elementsLeft:
    #         solEgilimTur.append(elementLeft.text)

    for i in list(range(1, 6)):
        elementsRight = driver.find_elements_by_css_selector(
            "#icerik_1310 > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(" + str(i) + ") > td:nth-child(2)")
        for elementRight in elementsRight:
            if elementRight.text == "---":
                sagEgilimTur.append(0)
            else:
                sagEgilimTur.append(elementRight.text)
        if not sagEgilimTur:
            sagEgilimTur = [0,0,0,0]

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagEgilimTur)

    my_insert_query = u"""INSERT INTO `tercihegilimtur`(`yil`,`programkodu`,`devlet`,
        `vakif`,`kibris`, `yabanci`) VALUES (%s,%s,%s,%s,%s,%s)"""

    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Yerleşenlerin Tercih Eğilimleri-Üniler *********************")

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
    yilUni = yilList * len(solEgilimUni)

    mySql_insert_query = u"""INSERT INTO `tercihegilimuni`(`yil`,`programkodu`,`universite`,`tercihsayisi`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilUni,osymUni, solEgilimUni, sagEgilimUni):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Yerleşenlerin Tercih Eğilimleri-İller *********************")

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
    yilIl = yilList * len(solEgilimIl)

    mySql_insert_query = u"""INSERT INTO `tercihegilimil`(`yil`,`programkodu`,`il`,`tercihsayisi`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilIl, osymIl, solEgilimIl, sagEgilimIl):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

    # print("************** Yerleşenlerin Tercih Eğilimleri-Farklı Program *********************")

    # solEgilimAyniFarkli = []
    sagEgilimAyniFarkli = []

    # elementsLeft = driver.find_elements_by_xpath(
    #     "/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr/td[1]")
    # for elementLeft in elementsLeft:
    #     solEgilimAyniFarkli.append(elementLeft.text)

    elementsRight = driver.find_elements_by_xpath(
        "/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr/td[2]")
    for elementRight in elementsRight:
        if elementRight.text == "---":
            sagEgilimAyniFarkli.append(0)
        elif elementRight.text == None:
            sagEgilimAyniFarkli.append(0)
        else:
            sagEgilimAyniFarkli.append(elementRight.text)
    if not sagEgilimAyniFarkli:
        sagEgilimAyniFarkli = [0,0,0,0,0]

    a = []
    a.append(yil)
    a.extend(programKodu)
    a.extend(sagEgilimAyniFarkli)

    my_insert_query = u"""INSERT INTO `tercihegilimaynifarkli`(`yil`,`programkodu`,`ayniprogram`,`farkliprogram`,
        `kibristercihleri`,`onlisanstercihleri`, `yabancitercihleri`) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    mycursor.execute(my_insert_query, a)
    mydb.commit()

    # print("************** Yerleşenlerin Tercih Programlar *********************")

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
    yilProgram = yilList * len(solProgram)

    mySql_insert_query = u"""INSERT INTO `tercihegilimprogram`(`yil`,`programkodu`,`program`,`tercihsayisi`) VALUES (%s,%s,%s,%s)"""

    for elem in zip(yilProgram, osymProgram, solProgram, sagProgram):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

        # print("************** Yerleşme Koşulları *********************")

    kosulNo = []

    elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[8]/div/div[12]/div[2]/div/div/table/tbody/tr/td[1]")
    for elementLeft in elementsLeft:
        kosulNo.append(elementLeft.text)

    osymKosul = programKodu * len(kosulNo)
    yilKosul = yilList * len(kosulNo)

    mySql_insert_query = u"""INSERT INTO `yerlesmekosullari`(`yil`,`programkodu`,`kosulno`) VALUES (%s,%s,%s)"""

    for elem in zip(yilKosul, osymKosul, kosulNo):
        mycursor.execute(mySql_insert_query, elem)
        mydb.commit()

#2018
for kod in listKod:

    url = "https://yokatlas.yok.gov.tr/2018/lisans.php?y=" + str(kod) + ""

    try:
        driver.get(url)
        divSayiBtns = WebDriverWait(driver, 4).until( \
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "panel-default")))
        divSayi = len(list(divSayiBtns))
        if (divSayi == 27):
            bolumBilgiAlCokDiv()
        else:
            bolumBilgiAlAzDiv()
    except TimeoutException:
        print("Exception exist")
        pass

#2019
for kod in listKod:

    url = "https://yokatlas.yok.gov.tr/2019/lisans.php?y=" + str(kod) + ""

    try:
        driver.get(url)
        divSayiBtns = WebDriverWait(driver, 4).until( \
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "panel-default")))
        divSayi = len(list(divSayiBtns))
        if (divSayi == 27):
            print("cokdiv")
            bolumBilgiAlCokDiv()
        else:
            print("azdiv")
            bolumBilgiAlAzDiv()
    except TimeoutException:
        pass

#2020
for kod in listKod:

    url = "https://yokatlas.yok.gov.tr/lisans.php?y=" + str(kod) + ""

    try:
        driver.get(url)
        divSayiBtns = WebDriverWait(driver, 3).until( \
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "panel-default")))
        divSayi = len(list(divSayiBtns))
        if (divSayi == 27):
            print("cokdiv")
            bolumBilgiAlCokDiv()

        else:
            print("azdiv")
            bolumBilgiAlAzDiv()

    except TimeoutException:
        print("TimeoutException exist")
        pass




