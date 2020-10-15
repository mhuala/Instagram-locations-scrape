from selenium import webdriver
import requests
import time
import json

country_name = str(input("What country do you want to scrape ? : "))

with open(country_name+'.json', encoding='utf-8') as data_file:
    json_data = data_file.read()

country_data = json.loads(json_data)

time.sleep(10)

def start_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('private')
    options.add_argument('--log-level=3')
    driver = webdriver.Opera(executable_path='operadriver.exe', options=options)
    return driver

def scrape_all_cities(data,driver,country_name):
    for i in range(len(data)):
        links_cities = []
        link = data[i]["link"]
        city_name = data[i]["name"]
        page_number=0
        has_next_page = True
        time.sleep(3)
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
                    with open(str(country_name)+'-'+str(city_name)+'.json', 'w' , encoding='utf-8') as outfile:
                        print("Scrape Done !"+str(country_name)+'-'+str(city_name)+'json was created')
                        json.dump(links_cities,outfile)
                        time.sleep(3)

            else:
                has_next_page = False
                with open(str(country_name)+'-'+str(city_name)+'.json', 'w',  encoding='utf-8') as outfile:
                    print("Scrape Done !"+str(country_name)+'-'+str(city_name)+'json was created')
                    json.dump(links_cities,outfile)
                    time.sleep(3)
                   


def scrape_specific_city(data,driver,country_name):
    links_cities = []
    page_number=0
    has_next_page = True
    time.sleep(3)
    city_name = str(input("What city of "+str(country_name)+" do you want to scrape ? : "))
    link = next((city for city in data if city["name"] == str(city_name)))["link"]
    while(has_next_page):
        page_number+=1
        url=link+'?page='+str(page_number)
        print(url)
        request = requests.get(url, timeout=25)
        print(request.status_code)
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
                with open(str(country_name)+'-'+str(city_name)+'.json', 'w' , encoding='utf-8') as outfile:
                    print("Scrape Done !"+str(country_name)+'-'+str(city_name)+'json was created')
                    json.dump(links_cities,outfile)
                    time.sleep(3)
                    driver.quit()
        else:
            has_next_page = False
            with open(str(country_name)+'-'+str(city_name)+'.json', 'w',  encoding='utf-8') as outfile:
                print("Scrape Done !"+str(country_name)+'-'+str(city_name)+'json was created')
                json.dump(links_cities,outfile)
                time.sleep(3)
                driver.quit()

if __name__ == "__main__":
    opt = str(input("Do you want scrape all cities of "+str(country_name)+" ? (Y/N) : "))
    if opt == 'N':
        driver = start_driver()
        time.sleep(5)
        scrape_specific_city(country_data,driver,country_name)
    else:
        driver = start_driver()
        time.sleep(5)
        scrape_all_cities(country_data,driver,country_name)