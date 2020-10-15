from selenium import webdriver
import time
import json
from datetime import date

def start_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('private')
    options.add_argument('--log-level=3')
    driver = webdriver.Opera(executable_path='operadriver.exe', options=options)
    return driver

def scrape_places(data,driver,city_name):
    today = date.today()
    today_d = today.strftime("%b-%d-%Y")
    places_list=[]
    for i in range(len(data)):
        loc_id=data[i]["link"].split('locations/',1)[1].split('/',1)[0]
        loc_name=data[i]["name"]
        driver.get(data[i]["link"])
        time.sleep(1.5)
        #exist = driver.find_element_by_class_name("VnYfv")
        elements = driver.find_elements_by_xpath("//script[@type = 'text/javascript']")
        script_info = elements[6].get_attribute("innerHTML")
        try:
            count=script_info.split('"count":',1)[1].split(',',1)[0]
            lat =script_info.split('"lat":',1)[1].split(',',1)[0]
            lng =script_info.split('"lng":',1)[1].split(',',1)[0]
            print({"location": str(loc_name) , "id": int(loc_id), "lat": str(lat), "lng": str(lng) , today_d: str(count)})
            places_list.append({"location": str(loc_name) , "id": int(loc_id), "lat": float(lat), "lng": float(lng) ,  today_d: float(count)})
        except IndexError:
            places_list.append({"location": str(loc_name) , "id": int(loc_id) , "lat": None , "lng": None , today_d: None})

    with open(city_name+'_places_data.json', 'w') as outfile:
        print("Scrape done ! " +str(city_name)+'_places_data.json was created')
        json.dump(places_list,outfile)
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":

        country_name = str(input("What country do you want to scrape? : "))
        city_name = str(input("What city do you want to scrape ? : "))

        with open(str(country_name)+'-'+str(city_name)+'.json', encoding='utf-8') as data_file:
            json_data = data_file.read()
            data = json.loads(json_data)
        
        driver=start_driver()
        scrape_places(data,driver,city_name)