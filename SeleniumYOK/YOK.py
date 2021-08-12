from selenium import webdriver
import time
from math import floor
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
url = "https://yokatlas.yok.gov.tr/lisans-anasayfa.php"

driver.get(url)



def bolumBilgiAl2020():

    print ("************** Genel Bilgiler *********************")
    solGenel=[]
    sagGenel=[]


    myBtn = driver.find_element_by_css_selector("#headingOne > a:nth-child(1) > h4:nth-child(2)")
    myBtn.click()
    time.sleep(3)


    elementsRight = driver.find_elements_by_css_selector('.vert-align')
    for elementRight in elementsRight:
       sagGenel.append(elementRight.text)

    elementsLeft = driver.find_elements_by_css_selector('.text-left')
    for elementLeft in elementsLeft:
       solGenel.append(elementLeft.text)


    print("sag liste: "+str(len(sagGenel)))
    print("sol liste: "+str(len(solGenel)))

    genelBilgiler = dict(zip(solGenel, sagGenel))

    print ("Genel Bilgiler:")
    for key, value in genelBilgiler.items():
        print(key, ' : ', value)

    myBtn.click()
    """
    print ("************** Kontenjan İstatistikleri *********************") #hangi veriler lazım?

    solKontenjan=[]
    sagKontenjan=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[3]/div")
    myBtn.click()
    time.sleep(1)

    elementLeft = driver.find_element_by_css_selector('th.thb:nth-child(2)')
    solKontenjan.append(elementLeft.text)
    elementLeft = driver.find_element_by_css_selector('th.thb:nth-child(4)')
    solKontenjan.append(elementLeft.text)

    elementRight = driver.find_element_by_css_selector('#icerik_1000_2 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')
    sagKontenjan.append(elementRight.text)
    elementRight = driver.find_element_by_css_selector('td.text-center:nth-child(4)')
    sagKontenjan.append(elementRight.text)
    print("sol liste: "+str(len(solKontenjan)))
    print("sag liste: "+str(len(sagKontenjan)))

    kontenjanDict = dict(zip(solKontenjan, sagKontenjan))

    print ("Kontenjan İstatistikleri:")
    for key, value in kontenjanDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print ("************** Cinsiyet İstatistikleri *********************") #hangi veriler lazım?

    solCinsiyet=[]
    sagCinsiyet=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[4]/div")
    myBtn.click()
    time.sleep(1)


    elementLeft = driver.find_element_by_css_selector('#icerik_1010 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)')
    solCinsiyet.append(elementLeft.text)
    elementLeft = driver.find_element_by_css_selector('#icerik_1010 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1)')
    solCinsiyet.append(elementLeft.text)

    elementRight = driver.find_element_by_css_selector('#icerik_1010 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')
    sagCinsiyet.append(elementRight.text)
    elementRight = driver.find_element_by_css_selector('#icerik_1010 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(3)')
    sagCinsiyet.append(elementRight.text)

    print("sol liste: "+str(len(solCinsiyet)))
    print("sag liste: "+str(len(sagCinsiyet)))

    cinsiyetDict = dict(zip(solCinsiyet, sagCinsiyet))

    print ("Cinsiyet İstatistikleri:")
    for key, value in cinsiyetDict.items():
        print(key, ' : ', value)

    myBtn.click()

    print ("************** Coğrafi Bölge İstatistikleri *********************") #hangi veriler lazım?

    solBolge=[]
    sagBolge=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[5]/div")
    myBtn.click()
    time.sleep(1)


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


    print("sol liste: "+str(len(solBolge)))
    print("sag liste: "+str(len(sagBolge)))

    bolgeDict = dict(zip(solBolge, sagBolge))

    print ("Bölge İstatistikleri:")
    for key, value in bolgeDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print ("************** Öğrenim Durumu İstatistikleri *********************") #hangi veriler lazım?

    solOgrenim=[]
    sagOgrenim=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[7]/div")
    myBtn.click()
    time.sleep(1)

    for i in [2,3,4,5,6]:
        elementsLeft = driver.find_elements_by_css_selector("#icerik_1030a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solOgrenim.append(elementLeft.text)

    for i in [2,3,4,5,6]:
        elementsRight = driver.find_elements_by_css_selector("#icerik_1030a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagOgrenim.append(elementRight.text)

    print("sol liste: "+str(len(solOgrenim)))
    print("sag liste: "+str(len(sagOgrenim)))

    ogrenimDict = dict(zip(solOgrenim, sagOgrenim))

    print ("Öğreneme Durumu İstatistikleri:")
    for key, value in ogrenimDict.items():
        print(key, ' : ', value)

    myBtn.click()

    print ("************** Mezuniyet Yılı İstatistikleri *********************") #hangi veriler lazım?

    solMezYil=[]
    sagMezYil=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[8]/div")
    myBtn.click()
    time.sleep(1)

    for i in [2,3,4,5,6,7]:
        elementsLeft = driver.find_elements_by_css_selector("#icerik_1030b > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solMezYil.append(elementLeft.text)

    for i in [2,3,4,5,6,7]:
        elementsRight = driver.find_elements_by_css_selector("#icerik_1030b > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagMezYil.append(elementRight.text)

    print("sol liste: "+str(len(solMezYil)))
    print("sag liste: "+str(len(sagMezYil)))

    mezYilDict = dict(zip(solMezYil, sagMezYil))

    print ("Mezuniyet Yılı İstatistikleri:")
    for key, value in mezYilDict.items():
        print(key, ' : ', value)

    myBtn.click()

    print ("************** Lise Alanı İstatistikleri *********************") #hangi veriler lazım?

    solLiseAlan=[]
    sagLiseAlan=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[9]/div")
    myBtn.click()
    time.sleep(2)


    elementsLeftNum = driver.find_elements_by_class_name("text-left")
    print(len(list(elementsLeftNum)))

    for i in list(range(2,len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[1]")
        for elementLeft in elementsLeft:
            solLiseAlan.append(elementLeft.text)

    for i in list(range(2,len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr["+str(i)+"]/td[2]")
        for elementRight in elementsRight:
            sagLiseAlan.append(elementRight.text)

    print("sol liste: "+str(len(solLiseAlan)))
    print("sag liste: "+str(len(sagLiseAlan)))

    liseAlanDict = dict(zip(solLiseAlan, sagLiseAlan))

    print ("Lise Alanı İstatistikleri:")
    for key, value in liseAlanDict.items():
        print(key, ' : ', value)

    myBtn.click()

    print ("************** Lise Grubu İstatistikleri *********************") #hangi veriler lazım?

    solLiseGrup=[]
    sagLiseGrup=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[10]/div")
    myBtn.click()
    time.sleep(1)


    elementsLeftNum = driver.find_elements_by_class_name("vert-align")

    for i in list(range(1,len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_css_selector("table.table:nth-child(4) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solLiseGrup.append(elementLeft.text)

    for i in list(range(1,len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector("table.table:nth-child(4) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagLiseGrup.append(elementRight.text)

    for i in list(range(1,len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_css_selector("table.table:nth-child(5) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solLiseGrup.append(elementLeft.text)

    for i in list(range(1,len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector("table.table:nth-child(5) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagLiseGrup.append(elementRight.text)

    print("sol liste: "+str(len(solLiseGrup)))
    print("sag liste: "+str(len(sagLiseGrup)))

    liseGrupDict = dict(zip(solLiseGrup, sagLiseGrup))

    print ("Lise Grubu İstatistikleri:")
    for key, value in liseGrupDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print ("************** Taban Puan ve Başarı Sırası *********************") #hangi veriler lazım?

    solPuan=[]
    sagPuan=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[13]/div")
    myBtn.click()
    time.sleep(2)

    elementsLeftNum = driver.find_elements_by_class_name("text-left")

    for i in list(range(1,len(list(elementsLeftNum)))):  #icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)
        elementsLeft1 = driver.find_elements_by_css_selector("#icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        elementsLeft2 = driver.find_element_by_css_selector("#icerik_1000_3 > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(4)")
        for elementLeft1 in elementsLeft1:
            solPuan.append(elementLeft1.text+elementsLeft2.text)

    for i in list(range(1,len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector("#icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(4)")
        for elementRight in elementsRight:
            sagPuan.append(elementRight.text)

    print("sol liste: "+str(len(solPuan)))
    print("sag liste: "+str(len(sagPuan)))

    liseGrupDict = dict(zip(solPuan, sagPuan))

    print ("Taban Puanı ve Başarı Sıralaması:")
    for key, value in liseGrupDict.items():
        print(key, ' : ', value)

    myBtn.click()

    print ("************** Net Ortalamaları *********************") #hangi veriler lazım?

    solNet=[]
    sagNet=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[2]/div[1]/a/h4")
    driver.execute_script("arguments[0].click();", myBtn)
    time.sleep(3)
    elementsLeftNum = driver.find_elements_by_class_name("text-left")

    for i in list(range(3,len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solNet.append(elementLeft.text)

    for i in list(range(3,len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector("#icerik_1210a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagNet.append(elementRight.text)

    print("sol liste: "+str(len(solNet)))
    print("sag liste: "+str(len(sagNet)))


    netDict = dict(zip(solNet, sagNet))

    print ("Net İstatistikleri:")
    for key, value in netDict.items():
        print(key, ' : ', value)
    driver.execute_script("arguments[0].click();", myBtn)

    print ("************** Tercih Edilme İstatistikleri *********************") #hangi veriler lazım?

    solTercih=[]
    sagTercih=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[5]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

    for i in list(range(1,7)):
        elementsLeft = driver.find_elements_by_xpath("./html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr["+str(i)+"]/td[1]")
        for elementLeft in elementsLeft:
            solTercih.append(elementLeft.text)

    for i in list(range(1,11)):
        elementsLeft = driver.find_elements_by_xpath("./html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/tbody/tr["+str(i)+"]/td[1]")
        for elementLeft in elementsLeft:
            solTercih.append(elementLeft.text)

    for i in list(range(1,17)):
        elementsRight = driver.find_elements_by_css_selector("#icerik_1080 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagTercih.append(elementRight.text)

    for i in list(range(1,11)):
        elementsRight = driver.find_elements_by_css_selector("table.table:nth-child(3) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
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

    driver.execute_script("arguments[0].click();", myBtn)

    print ("************** Yerleşenlerin Tercih Sıraları *********************") #hangi veriler lazım?

    solTercihSıra=[]
    sagTercihSıra=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[6]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

    for i in list(range(1,13)):
        elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[2]/tbody/tr/td[1]/table/tbody/tr["+str(i)+"]/td[1]")
        for elementLeft in elementsLeft:
            solTercihSıra.append(elementLeft.text)
    for i in list(range(1,13)):
        elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr["+str(i)+"]/td[1]")
        for elementLeft in elementsLeft:
            solTercihSıra.append(elementLeft.text)

    for i in list(range(1,13)):
        elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[2]/tbody/tr/td[1]/table/tbody/tr["+str(i)+"]/td[2]")
        for elementRight in elementsRight:
            sagTercihSıra.append(elementRight.text)
    for i in list(range(1,13)):
        elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr["+str(i)+"]/td[2]")
        for elementRight in elementsRight:
            sagTercihSıra.append(elementRight.text)

    print("sol liste: "+str(len(solTercihSıra)))
    print("sag liste: "+str(len(sagTercihSıra)))


    tercihSıraDict = dict(zip(solTercihSıra, sagTercihSıra))

    print ("Yerleşenlerin Tercih Sıraları:")
    for key, value in tercihSıraDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print ("************** Yerleşenlerin Tercih Eğilimleri *********************") #hangi veriler lazım?

    solEgilim=[]
    sagEgilim=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[7]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

    for i in list(range(1,6)):
        elementsLeft = driver.find_elements_by_css_selector("table.table:nth-child(2) > tbody:nth-child(1) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solEgilim.append(elementLeft.text)

    for i in list(range(1,6)):
        elementsRight = driver.find_elements_by_css_selector("table.table:nth-child(2) > tbody:nth-child(1) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagEgilim.append(elementRight.text)

    print("sol liste: "+str(len(solEgilim)))
    print("sag liste: "+str(len(sagEgilim)))

    egilimDict = dict(zip(solEgilim, sagEgilim))

    print ("Yerleşenlerin Tercih Eğilimleri:")
    for key, value in egilimDict.items():
        print(key, ' : ', value)
    myBtn.click()


    print("************** Yerleşenlerin Tercih Eğilimleri-Üni Türleri *********************")  # hangi veriler lazım?

    solEgilimTur = []
    sagEgilimTur = []

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[8]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

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
    myBtn.click()

    print("************** Yerleşenlerin Tercih Eğilimleri-İller *********************")  # hangi veriler lazım?

    solEgilimIl = []
    sagEgilimIl = []

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[10]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

    elementsLeftNum = driver.find_elements_by_class_name("text-center")

    for i in list(range(1, len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_css_selector(
            "#icerik_1330 > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solEgilimIl.append(elementLeft.text)

    for i in list(range(1, len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector(
            "#icerik_1330 > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagEgilimIl.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimIl)))
    print("sag liste: " + str(len(sagEgilimIl)))

    egilimTurDict = dict(zip(solEgilimIl, sagEgilimIl))

    print("Yerleşenlerin Tercih Eğilimleri-Üni Türleri:")
    for key, value in egilimTurDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print("************** Yerleşenlerin Tercih Eğilimleri-Farklı Program *********************")  # hangi veriler lazım?

    solEgilimIl = []
    sagEgilimIl = []

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[11]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

    for i in list(range(1, 6)):
        elementsLeft = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]")
        for elementLeft in elementsLeft:
            solEgilimIl.append(elementLeft.text)

    for i in list(range(1, 6)):
        elementsRight = driver.find_elements_by_xpath(
            "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[2]")
        for elementRight in elementsRight:
            sagEgilimIl.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimIl)))
    print("sag liste: " + str(len(sagEgilimIl)))

    egilimIlDict = dict(zip(solEgilimIl, sagEgilimIl))

    print("Yerleşenlerin Tercih Eğilimleri-Üni Türleri:")
    for key, value in egilimIlDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print("************** Yerleşenlerin Tercih Programlar *********************")  # hangi veriler lazım?

    solProgram = []
    sagProgram = []

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[12]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

    elementsLeftNum = driver.find_elements_by_class_name("text-center")
    print(len(list(elementsLeftNum)))

    for i in list(range(1, len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_css_selector(
            ".table > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(1) ")
        for elementLeft in elementsLeft:
            solProgram.append(elementLeft.text)

    for i in list(range(1, len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector(
            ".table > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(2) ")
        for elementRight in elementsRight:
            sagProgram.append(elementRight.text)

    print("sol liste: " + str(len(solProgram)))
    print("sag liste: " + str(len(sagProgram)))

    programDict = dict(zip(solProgram, sagProgram))

    print("Yerleşenlerin Tercih Ettiği Programlar:")
    for key, value in programDict.items():
        print(key, ' : ', value)
    myBtn.click()
"""
def bolumBilgiAl2019():

    print ("************** Genel Bilgiler *********************")
    solGenel=[]
    sagGenel=[]
    try:
        myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[1]/div[1]/a/h4")
        driver.execute_script("arguments[0].click();",myBtn)
        time.sleep(2)

    except NoSuchElementException:
        pass


    elementsRight = driver.find_elements_by_css_selector('.vert-align')
    for elementRight in elementsRight:
       sagGenel.append(elementRight.text)

    elementsLeft = driver.find_elements_by_css_selector('.text-left')
    for elementLeft in elementsLeft:
       solGenel.append(elementLeft.text)


    print("sag liste: "+str(len(sagGenel)))
    print("sol liste: "+str(len(solGenel)))

    genelBilgiler = dict(zip(solGenel, sagGenel))
    print ("Genel Bilgiler:")

    for key, value in genelBilgiler.items():
        print(key, ' : ', value)

    """
    print ("************** Kontenjan İstatistikleri *********************") #hangi veriler lazım?

    solKontenjan=[]
    sagKontenjan=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[2]/div")
    myBtn.click()
    time.sleep(1)

    elementLeft = driver.find_element_by_css_selector('th.thb:nth-child(4)')
    solKontenjan.append(elementLeft.text)

    elementRight = driver.find_element_by_css_selector('td.text-center:nth-child(4)')
    sagKontenjan.append(elementRight.text)
    print("sol liste: "+str(len(solKontenjan)))
    print("sag liste: "+str(len(sagKontenjan)))

    kontenjanDict = dict(zip(solKontenjan, sagKontenjan))

    print ("Kontenjan İstatistikleri:")
    for key, value in kontenjanDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print ("************** Cinsiyet İstatistikleri *********************") #hangi veriler lazım?

    solCinsiyet=[]
    sagCinsiyet=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[3]/div")
    myBtn.click()
    time.sleep(1)


    elementLeft = driver.find_element_by_css_selector('#icerik_1010 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)')
    solCinsiyet.append(elementLeft.text)
    elementLeft = driver.find_element_by_css_selector('#icerik_1010 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1)')
    solCinsiyet.append(elementLeft.text)

    elementRight = driver.find_element_by_css_selector('#icerik_1010 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')
    sagCinsiyet.append(elementRight.text)
    elementRight = driver.find_element_by_css_selector('#icerik_1010 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(3)')
    sagCinsiyet.append(elementRight.text)

    print("sol liste: "+str(len(solCinsiyet)))
    print("sag liste: "+str(len(sagCinsiyet)))

    cinsiyetDict = dict(zip(solCinsiyet, sagCinsiyet))

    print ("Cinsiyet İstatistikleri:")
    for key, value in cinsiyetDict.items():
        print(key, ' : ', value)

    myBtn.click()

    print ("************** Coğrafi Bölge İstatistikleri *********************") #hangi veriler lazım?

    solBolge=[]
    sagBolge=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[4]/div")
    myBtn.click()
    time.sleep(1)


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


    print("sol liste: "+str(len(solBolge)))
    print("sag liste: "+str(len(sagBolge)))

    bolgeDict = dict(zip(solBolge, sagBolge))

    print ("Bölge İstatistikleri:")
    for key, value in bolgeDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print ("************** Öğrenim Durumu İstatistikleri *********************") #hangi veriler lazım?

    solOgrenim=[]
    sagOgrenim=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[6]/div")
    myBtn.click()
    time.sleep(1)

    for i in [2,3,4,5,6]:
        elementsLeft = driver.find_elements_by_css_selector("#icerik_1030a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solOgrenim.append(elementLeft.text)

    for i in [2,3,4,5,6]:
        elementsRight = driver.find_elements_by_css_selector("#icerik_1030a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagOgrenim.append(elementRight.text)

    print("sol liste: "+str(len(solOgrenim)))
    print("sag liste: "+str(len(sagOgrenim)))

    ogrenimDict = dict(zip(solOgrenim, sagOgrenim))

    print ("Öğreneme Durumu İstatistikleri:")
    for key, value in ogrenimDict.items():
        print(key, ' : ', value)

    myBtn.click()

    print ("************** Mezuniyet Yılı İstatistikleri *********************") #hangi veriler lazım?

    solMezYil=[]
    sagMezYil=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[7]/div")
    myBtn.click()
    time.sleep(1)

    for i in [2,3,4,5,6,7]:
        elementsLeft = driver.find_elements_by_css_selector("#icerik_1030b > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solMezYil.append(elementLeft.text)

    for i in [2,3,4,5,6,7]:
        elementsRight = driver.find_elements_by_css_selector("#icerik_1030b > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagMezYil.append(elementRight.text)

    print("sol liste: "+str(len(solMezYil)))
    print("sag liste: "+str(len(sagMezYil)))

    mezYilDict = dict(zip(solMezYil, sagMezYil))

    print ("Mezuniyet Yılı İstatistikleri:")
    for key, value in mezYilDict.items():
        print(key, ' : ', value)

    myBtn.click()

    print ("************** Lise Alanı İstatistikleri *********************") #hangi veriler lazım?

    solLiseAlan=[]
    sagLiseAlan=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[8]/div")
    myBtn.click()
    time.sleep(1)


    elementsLeftNum = driver.find_elements_by_class_name("text-left")

    for i in list(range(2,len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_css_selector("#icerik_1050b > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solLiseAlan.append(elementLeft.text)

    for i in list(range(2,len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector("#icerik_1050b > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagLiseAlan.append(elementRight.text)

    print("sol liste: "+str(len(solLiseAlan)))
    print("sag liste: "+str(len(sagLiseAlan)))

    liseAlanDict = dict(zip(solLiseAlan, sagLiseAlan))

    print ("Lise Alanı İstatistikleri:")
    for key, value in liseAlanDict.items():
        print(key, ' : ', value)

    myBtn.click()

    print ("************** Lise Grubu İstatistikleri *********************") #hangi veriler lazım?

    solLiseGrup=[]
    sagLiseGrup=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[9]/div")
    myBtn.click()
    time.sleep(1)


    elementsLeftNum = driver.find_elements_by_class_name("vert-align")

    for i in list(range(1,len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_css_selector("table.table:nth-child(4) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solLiseGrup.append(elementLeft.text)

    for i in list(range(1,len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector("table.table:nth-child(4) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagLiseGrup.append(elementRight.text)

    for i in list(range(1,len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_css_selector("table.table:nth-child(5) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solLiseGrup.append(elementLeft.text)

    for i in list(range(1,len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector("table.table:nth-child(5) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagLiseGrup.append(elementRight.text)

    print("sol liste: "+str(len(solLiseGrup)))
    print("sag liste: "+str(len(sagLiseGrup)))

    liseGrupDict = dict(zip(solLiseGrup, sagLiseGrup))

    print ("Lise Grubu İstatistikleri:")
    for key, value in liseGrupDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print ("************** Taban Puan ve Başarı Sırası *********************") #hangi veriler lazım?

    solPuan=[]
    sagPuan=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[7]/div/div[12]/div")
    myBtn.click()
    time.sleep(1)

    elementsLeftNum = driver.find_elements_by_class_name("text-left")

    for i in list(range(1,len(list(elementsLeftNum)))):  #icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)
        elementsLeft1 = driver.find_elements_by_css_selector("#icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        elementsLeft2 = driver.find_element_by_css_selector("#icerik_1000_3 > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(4)")
        for elementLeft1 in elementsLeft1:
            solPuan.append(elementLeft1.text+elementsLeft2.text)

    for i in list(range(1,len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector("#icerik_1000_3 > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(4)")
        for elementRight in elementsRight:
            sagPuan.append(elementRight.text)

    print("sol liste: "+str(len(solPuan)))
    print("sag liste: "+str(len(sagPuan)))

    liseGrupDict = dict(zip(solPuan, sagPuan))

    print ("Taban Puanı ve Başarı Sıralaması:")
    for key, value in liseGrupDict.items():
        print(key, ' : ', value)

    myBtn.click()

    print ("************** Net Ortalamaları *********************") #hangi veriler lazım?

    solNet=[]
    sagNet=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[1]/div[1]/a/h4")
    myBtn.click()
    time.sleep(2)

    elementsLeftNum = driver.find_elements_by_class_name("text-left")

    for i in list(range(3,len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_css_selector("#icerik_1210a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solNet.append(elementLeft.text)

    for i in list(range(3,len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector("#icerik_1210a > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagNet.append(elementRight.text)

    print("sol liste: "+str(len(solNet)))
    print("sag liste: "+str(len(sagNet)))

    netDict = dict(zip(solNet, sagNet))

    print ("Net İstatistikleri:")
    for key, value in netDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print ("************** Tercih Edilme İstatistikleri *********************") #hangi veriler lazım?

    solTercih=[]
    sagTercih=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[4]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

    for i in list(range(1,7)):
        elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table[1]/tbody/tr["+str(i)+"]/td[1]")
        for elementLeft in elementsLeft:
            solTercih.append(elementLeft.text)

    for i in list(range(1,11)):
        elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/tbody/tr["+str(i)+"]/td[1]")
        for elementLeft in elementsLeft:
            solTercih.append(elementLeft.text)

    for i in list(range(1,17)):
        elementsRight = driver.find_elements_by_css_selector("#icerik_1080 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagTercih.append(elementRight.text)

    for i in list(range(1,11)):
        elementsRight = driver.find_elements_by_css_selector("table.table:nth-child(3) > tbody:nth-child(2) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagTercih.append(elementRight.text)

    print("sol liste: "+str(len(solTercih)))
    print("sag liste: "+str(len(sagTercih)))


    tercihEdilmeDict = dict(zip(solTercih, sagTercih))

    print ("Tercih Edilme İstatistikleri:")
    for key, value in tercihEdilmeDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print ("************** Yerleşenlerin Tercih Sıraları *********************") #hangi veriler lazım?

    solTercihSıra=[]
    sagTercihSıra=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[5]/div[1]/a/h4")
    myBtn.click()
    time.sleep(2)

    for i in list(range(1,13)):
        elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/tbody/tr/td[1]/table/tbody/tr["+str(i)+"]/td[1]")
        for elementLeft in elementsLeft:
            solTercihSıra.append(elementLeft.text)
    for i in list(range(1,13)):
        elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr["+str(i)+"]/td[1]")
        for elementLeft in elementsLeft:
            solTercihSıra.append(elementLeft.text)

    for i in list(range(1,13)):
        elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/tbody/tr/td[1]/table/tbody/tr["+str(i)+"]/td[2]")
        for elementRight in elementsRight:
            sagTercihSıra.append(elementRight.text)
    for i in list(range(1,13)):
        elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/tbody/tr/td[2]/table/tbody/tr["+str(i)+"]/td[2]")
        for elementRight in elementsRight:
            sagTercihSıra.append(elementRight.text)

    print("sol liste: "+str(len(solTercihSıra)))
    print("sag liste: "+str(len(sagTercihSıra)))


    tercihSıraDict = dict(zip(solTercihSıra, sagTercihSıra))

    print ("Yerleşenlerin Tercih Sıraları:")
    for key, value in tercihSıraDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print ("************** Yerleşenlerin Tercih Eğilimleri *********************") #hangi veriler lazım?

    solEgilim=[]
    sagEgilim=[]

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[6]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

    for i in list(range(1,6)):
        elementsLeft = driver.find_elements_by_css_selector("#icerik_1300 > table.table:nth-child(2) > tbody:nth-child(1) > tr:nth-child("+str(i)+") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solEgilim.append(elementLeft.text)

    for i in list(range(1,6)):
        elementsRight = driver.find_elements_by_css_selector("#icerik_1300 > table.table:nth-child(2) > tbody:nth-child(1) > tr:nth-child("+str(i)+") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagEgilim.append(elementRight.text)

    print("sol liste: "+str(len(solEgilim)))
    print("sag liste: "+str(len(sagEgilim)))

    egilimDict = dict(zip(solEgilim, sagEgilim))

    print ("Yerleşenlerin Tercih Eğilimleri:")
    for key, value in egilimDict.items():
        print(key, ' : ', value)
    myBtn.click()


    print("************** Yerleşenlerin Tercih Eğilimleri-Üni Türleri *********************")  # hangi veriler lazım?

    solEgilimTur = []
    sagEgilimTur = []

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[7]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

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
    myBtn.click()

    print("************** Yerleşenlerin Tercih Eğilimleri-İller *********************")  # hangi veriler lazım?

    solEgilimIl = []
    sagEgilimIl = []

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[9]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

    elementsLeftNum = driver.find_elements_by_class_name("text-center")

    for i in list(range(1, len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_css_selector(
            "#icerik_1330 > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(1)")
        for elementLeft in elementsLeft:
            solEgilimIl.append(elementLeft.text)

    for i in list(range(1, len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector(
            "#icerik_1330 > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(2)")
        for elementRight in elementsRight:
            sagEgilimIl.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimIl)))
    print("sag liste: " + str(len(sagEgilimIl)))

    egilimTurDict = dict(zip(solEgilimIl, sagEgilimIl))

    print("Yerleşenlerin Tercih Eğilimleri-Üni Türleri:")
    for key, value in egilimTurDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print("************** Yerleşenlerin Tercih Eğilimleri-Farklı Program *********************")  # hangi veriler lazım?

    solEgilimIl = []
    sagEgilimIl = []

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[10]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

    for i in list(range(1, 6)):
        elementsLeft = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]")
        for elementLeft in elementsLeft:
            solEgilimIl.append(elementLeft.text)

    for i in list(range(1, 6)):
        elementsRight = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[2]")
        for elementRight in elementsRight:
            sagEgilimIl.append(elementRight.text)

    print("sol liste: " + str(len(solEgilimIl)))
    print("sag liste: " + str(len(sagEgilimIl)))

    egilimIlDict = dict(zip(solEgilimIl, sagEgilimIl))

    print("Yerleşenlerin Tercih Eğilimleri-Üni Türleri:")
    for key, value in egilimIlDict.items():
        print(key, ' : ', value)
    myBtn.click()

    print("************** Yerleşenlerin Tercih Programlar *********************")  # hangi veriler lazım?

    solProgram = []
    sagProgram = []

    myBtn = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]/div/div[11]/div[1]/a/h4")
    myBtn.click()
    time.sleep(1)

    elementsLeftNum = driver.find_elements_by_class_name("text-center")
    print(len(list(elementsLeftNum)))

    for i in list(range(1, len(list(elementsLeftNum)))):
        elementsLeft = driver.find_elements_by_css_selector(
            ".table > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(1) ")
        for elementLeft in elementsLeft:
            solProgram.append(elementLeft.text)

    for i in list(range(1, len(list(elementsLeftNum)))):
        elementsRight = driver.find_elements_by_css_selector(
            ".table > tbody:nth-child(2) > tr:nth-child(" + str(i) + ") > td:nth-child(2) ")
        for elementRight in elementsRight:
            sagProgram.append(elementRight.text)

    print("sol liste: " + str(len(solProgram)))
    print("sag liste: " + str(len(sagProgram)))

    programDict = dict(zip(solProgram, sagProgram))

    print("Yerleşenlerin Tercih Ettiği Programlar:")
    for key, value in programDict.items():
        print(key, ' : ', value)
    myBtn.click()
"""
btn1 = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[1]/div/form/div/div/div/button")
btn1.click()
time.sleep(1)

btn2 = driver.find_element_by_class_name("opt")
uniName = btn2.text
btn2.click()
time.sleep(1)

btn3Num = len(list(driver.find_elements_by_class_name("btn")))
print(floor(int((btn3Num)/2+1)))
print(list(range(1, floor(int((btn3Num)/2+1)))))

#sayfanın solu
# for i in list(range(1, floor(int((btn3Num)/2+1)))):
#     btn3 = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[1]/div/div["+str(i)+"]/div/h4/a/div")
#     bolumName = btn3.text
#     driver.execute_script("arguments[0].click();", btn3)
#     time.sleep(2)
#     for i in [3,2,1]:
#         btn2020 = driver.find_element_by_css_selector("a.label:nth-child("+str(i)+") > font:nth-child(1)")
#         yil = btn2020.text
#         print(uniName+" "+" "+bolumName+" "+" "+yil)
#         driver.execute_script("arguments[0].click();", btn2020)
#         time.sleep(2)
#         if i == 3:
#             bolumBilgiAl2020()
#             time.sleep(2)
#
#         else:
#             bolumBilgiAl2019()
#             time.sleep(2)
#
#     driver.execute_script("window.history.go(-3)")
#     time.sleep(2)

print(floor(int((btn3Num)/2+1)))
print(list(range(1, floor(int((btn3Num)/2+1)))))

#sayfanın sağı
for i in list(range(5, floor(int((btn3Num)/2+1)))):
    btn3 = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div/div["+str(i)+"]/div/h4/a/div")
    bolumName = btn3.text
    driver.execute_script("arguments[0].click();", btn3)
    time.sleep(2)
    exeptionExist = False
    for i in [3,2,1]:
        try:
            btn2020 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[6]/div[2]/h2/strong/a[" + str(i) + "]")
            yil = btn2020.text
            print(uniName + " " + " " + bolumName + " " + " " + yil)
            driver.execute_script("arguments[0].click();", btn2020)
            time.sleep(2)

        except NoSuchElementException:
            exeptionExist = True
            pass


        # btn2020 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[6]/div[2]/h2/strong/a[" + str(i) + "]")
        # yil = btn2020.text
        # print(uniName+" "+" "+bolumName+" "+" "+yil)
        # driver.execute_script("arguments[0].click();", btn2020)
        # time.sleep(2)
        if i == 3:
            bolumBilgiAl2020()
            time.sleep(2)
        else:
            bolumBilgiAl2019()
            time.sleep(2)
    if exeptionExist == True:
        driver.execute_script("window.history.go(-2)")
        time.sleep(2)
    else:
        driver.execute_script("window.history.go(-3)")
driver.execute_script("window.history.go(-1)")

















