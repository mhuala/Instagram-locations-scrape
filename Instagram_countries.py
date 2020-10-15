from selenium import webdriver
import time
import requests
import json

def start_driver():
    # Declaramos las opciones con las que iniciará nuestro navegadr
    options = webdriver.ChromeOptions()
    options.add_argument('private')
    options.add_argument('--log-level=3')
    #Instanciamos un Driver del navegador seleccionado, con las opciones que declaramos
    driver = webdriver.Opera(executable_path='operadriver.exe', options=options)
    return driver


# ################################### COUNTRIES ########################################
def scrape_countries(driver):
    links_countries=[]
    for i in range(3):
        url = 'https://www.instagram.com/explore/locations/?page={}'.format(i+1)
        driver.get(url)
        time.sleep(1)
        countries_list = driver.find_elements_by_class_name("aMwHK")
        for country in countries_list:
            links_countries.append({
                "name":country.text, "link":country.get_attribute('href')
                })

    with open('countries.json', 'w') as outfile:
        json.dump(links_countries,outfile)
    print("Scrape done! , countries.json created")
    time.sleep(5)
    driver.quit()


def scrape_cities(driver):
    with open('countries.json', 'r') as data_file:
        json_data = data_file.read()
    data = json.loads(json_data)
    time.sleep(5)
    country_name = str(input("What country do you want to scrape ? : "))
    link = next((country for country in data if country["name"] == str(country_name)))["link"]
    time.sleep(2)
    links_cities=[]
    page_number=0
    has_next_page = True
    while(has_next_page):
        page_number+=1
        url=link+'?page='+str(page_number)
        print(url)
        request = requests.get(url, timeout=25)
        if request.status_code == 200 :
            driver.get(url)
            time.sleep(5)
            cities_list = driver.find_elements_by_class_name("aMwHK")
            if len(cities_list)>1:
                for city in cities_list:  
                    links_cities.append({
                        "name":str(city.text),
                        "link":city.get_attribute('href')
                        })   
                    has_next_page = True
            else:
                has_next_page = False
                with open(str(country_name)+'.json', 'w' , encoding='utf-8') as outfile:
                    print("Scrape done! " + str(country_name) +".json was created")
                    json.dump(links_cities,outfile)
                    time.sleep(3)
                    driver.quit()
        else:
            has_next_page = False
            with open(str(country_name)+'.json', 'w',  encoding='utf-8') as outfile:
                print("Scrape done! " + str(country_name) +".json was created")
                json.dump(links_cities,outfile)
                time.sleep(3)
                driver.quit()

if __name__ == '__main__':
    OPT = str(input("Do you have all the countries links (countries.json) ? Y/N :  "))
    if OPT == 'N':
        driver = start_driver()
        scrape_countries(driver)
    elif OPT == 'Y':
        driver = start_driver()
        scrape_cities(driver)