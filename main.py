from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import datetime
def automateActual(fullName, houseColor, number):
    driver = webdriver.Firefox()
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfhtB4b2tvB_ib_Zch7ReZRaSJOyRq_hHZE7QdW5zU77VveTA/viewform")
    name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(fullName)
    houseColorNumber = 9
    if houseColor == 'Orange':
        houseColorNumber += 3
    elif houseColor == 'Yellow':
        houseColorNumber += 6
    elif houseColor == 'Green':
        houseColorNumber += 9
    elif houseColor == 'Blue':
        houseColorNumber += 12
    elif houseColor == 'Purple':
        houseColorNumber += 15
    elif houseColor == 'Indigo':
        houseColorNumber += 18
    driver.find_element(By.XPATH, f'//*[@id="i{houseColorNumber}"]/div[3]/div').click()
    numberInput = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    numberInput.send_keys(number)
    currentlyExperiencing = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div').click()
    nextButton = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div').click()
    symptoms = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div').click()
    nextButton = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span').click()
    testing = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div').click()
    nextButton = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
    closeContacts = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div').click()
    nextButton = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
    publicHealth = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div').click()
    nextButton = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()

    submitButton = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
    time.sleep(1)
    driver.close()
    driver.quit()
#data
elliot = {
    "Name": "Elliott Chaplin",
    "House": "Indigo",
    "Number": "55"
}
waseem = {
    "Name": "Waseem Saad",
    "House": "Violet",
    "Number": "35"
}
edison = {
    "Name" : "Edison Qu",
    "House" : "Red",
    "Number" : "36"
}
myles = {
    "Name": "Myles Odlozinski",
    "House": "Red",
    "Number": "43"
}
gurdy = {
    "Name": "Gurtej Singh",
    "House": "Orange",
    "Number": "44"
}
rishi = {
    "Name": "Rishi Jarajapu",
    "House": "Blue",
    "Number": "47"
}
ishan = {
    "Name": "Ishan Sur",
    "House": "Blue",
    "Number": "56"
}
jessica = {
    "Name": "Jessica Wei",
    "House": "Blue",
    "Number": "26"
}
ellen = {
    "Name": "Ellen Brisley",
    "House": "Orange",
    "Number": "30"
}

nout = {
    "Name": "Nout Geurts",
    "House": "Blue",
    "Number": "40"
}

lucas = {
    "Name": "Lucas Kim",
    "House": "Green",
    "Number": "39"
}

allenna = {
    "Name": "Allenna Tang",
    "House": "Yellow",
    "Number": "24"
}

elisa = {
    "Name": "Elisa Xue",
    "House": "Red",
    "Number": "32"
}

lulu = {
    "Name": "Lulu DeLuca",
    "House": "Yellow",
    "Number": "17"
}

listOfShads = []
listOfShads.append(edison)
listOfShads.append(myles)
listOfShads.append(nout)
listOfShads.append(lucas)
listOfShads.append(allenna)
listOfShads.append(lulu)
listOfShads.append(jessica)
listOfShads.append(gurdy)
listOfShads.append(rishi)
listOfShads.append(waseem)
listOfShads.append(ishan)
listOfShads.append(elliot)
listOfShads.append(ellen)


totalNumOfShads = len(listOfShads)
counter = 0
for shad in listOfShads:
    counter+=1
    print("Currently doing " + shad.get("Name"))
    automateActual(shad.get("Name"), shad.get("House"),shad.get("Number"))
    if counter == totalNumOfShads:
        print("submitted all")
    print("Finished "+ str(counter)+ "/" + str(totalNumOfShads))
    print(datetime.datetime.now())































