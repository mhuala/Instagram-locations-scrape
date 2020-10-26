# Instagram geo-tagged posts Scraper:

[![Contact](https://img.shields.io/badge/Email-%20Contact-yellow.svg)](mailto:manuelhuala@outlook.com)



## Requirements:
These Python packages are required for the proper functioning:

-beautifulSoup4
-datetime
-requests
-selenium

```sh
pip3 install -r requirements.txt
```
I used  [Opera WebDriver](https://github.com/operasoftware/operachromiumdriver/releases) to run these scripts.

---

## Before using

What can be obtained with these scripts ?

* **Instagram_countries.py**: All countries displayed in [explore locations](https://www.instagram.com/explore/locations/) section, and the 1000 most popular cities or locations (based on the ammount of geo-tagged Instagram posts)  from every country like [this example of Chile](https://www.instagram.com/explore/locations/CL/chile/).
<br> 


* **Instagram_cities.py**: The 1000 most popular places (based on the ammount of geo-tagged Instagram posts) of every city like [this example of Valdvia](https://www.instagram.com/explore/locations/c328920/valdivia-chile/), a chilean city.
<br> 

* **Instagram_places.py**: You will obtain more info about the links acquired with the previous script (*Instagram_cities.py*), like the latitude or longitude, the amount of total tagged publications of every place. This JSON filename have this format:

```sh
        {country_name}-{city_name}.json
```

And have this body format:

```sh
        { "location": LOCATION_NAME, "id": LOCATION_ID, "lat": LOCATION_LAT, "lng": LOCATION_LNG , {today_date} = POSTS_UNTIL_TODAY}
```

---


## Usage



### *Instagram_countries.py*
First of all you need the file *countries.json* created by *Instagram_countries.py* .

* **Obtain countries.json** :  To obtain this json file you need to run the script and type **N**.

![countries_list](https://user-images.githubusercontent.com/45650277/96024330-f746ea80-0e29-11eb-9c49-f3a37c43ab8a.gif)

**Obtain data of a specific country** : Once you have the *countries.json* file you can obtain the top 1000 cities or locations of any country, in order to do that you need run the script and type **Y** then put the country name in the same way that this appear in the file *countries.json*. This will generate a json file with the next filename:

```sh
{country_name}.json
```

**Helpful Tip:** May you need to activate the internal VPN of Opera when it starts, before the scrape process begin, in order to avoid problems with the petitions to the Instagram servers.

![cities_list](https://user-images.githubusercontent.com/45650277/96024110-b222b880-0e29-11eb-9946-c1182565a756.gif)

### *Instagram_cities.py*
Previous to run this script you will need the file *{country_name}.json* created by *Instagram_countries.py* in the previous step. Now having this json file of a country you can run this script.

* **Obtain a JSON of all the cities of a country** :  This option will return a json file for every city contained in *{country_name].json*, saving the name and the specific link of the 1000 most tagged places of every city, it will have the next filename:

```sh
{country_name}-{city_name}.json
```

To obtain a json file of all the cities of a country you need to run the script and put the name of the country exactly how it appears in your *{country_name}.json* file), then type "**Y**", finally accept the cookies of the web browser for Instagram.

**Helpful Tip:** May you need to activate the internal VPN of Opera when it starts, before the scrape process begin, in order to avoid problems with the petitions to the Instagram servers.

![places_all](https://user-images.githubusercontent.com/45650277/96042994-ae505f80-0e44-11eb-9ab5-a771267bb4fb.gif)

* **Obtain a JSON of a specific city of a country** : This option will return a json file for the selected city wich is contained in the *{country_name}.json*, it will save the name and the specific link of the 1000 most tagged places of this city, it will have the next filename:

```sh
{country_name}-{city_name}.json
```

To obtain this json file of a specific city of a country you need to run the script, put this name of the country *(the same of your {country_name}.json file)*, then type "**N**" and put the name of the selected city *(this have to be the same name contained in the ["name"] key of the {country_name}.json file)* , finally you need to accept the cookies of the web browser for Instagram

**Helpful Tip:** M May you need to activate the internal VPN of Opera when it starts, before the scrape process begin, in order to avoid problems with the petitions to the Instagram servers.

![places_list](https://user-images.githubusercontent.com/45650277/96037819-b3a9ac00-0e3c-11eb-80b0-992f4194c7a0.gif)


### *Instagram_places.py*
Finally we can get info of all these places obtained with the previous script, only we neeed to run this script and specify the country and the target city, with the same names that appear in the file *{country_name}-{city_name}.json* and wait for at least 70-90 minutes.

The json created with this script have the following filename:

```sh
{city_name}_places_data.json
```
This file will have the next content format with the following data:

```sh
{"location": LOCATION_NAME, "id": LOCATION_ID , "lat": LATITUDE ,"lng": LONGITUDE, TODAY_DATE : TOTAL_POSTS}
```




![all_places](https://user-images.githubusercontent.com/45650277/96074282-a7464300-0e7e-11eb-9b1d-7bae3487481b.gif)


---

## What you can do with this data ?

### *Scrape all the geo-tagged posts:*
You can use the final JSON file **{city_name}_places_data.json** and change its name to **locations.json** and move this file to the folder of this repository [Instagram Geo-tagged posts scraper](https://github.com/mhuala/Instagram-Geo-tagged-posts-scraper) then you will be able to have new locations in order to obtain public info of all the publications of a particular location/geo-tag like the next info:

* *user_id* : Numeric value that refers to the user unique id
* *date* : Numeric value that refers to the date in wich this post was publicated, have timestamp format.
* *shortcode* : Alpha-numeric value that refers to the post unique id.
* *post_text* : String wich contains the title text below the post.
* *post_reactions* : Numeric valor that refers to the ammount of likes of the post.
* *post_is_video* : Boolean value that is True if the publication is a video instead of a photo.

You only need to put all the content of this new **locations.json** inside of a dictionary with a single key called **"locations"** and you are ready to scrape one of these 1000 new places.

![places_to_scrape](https://user-images.githubusercontent.com/45650277/96075639-df02ba00-0e81-11eb-81d6-fb75215f7c6c.gif)


### *Make a geospatial analysis of the most popular places:*

You can also make a geospatial analysis of the most popular places with the JSON files obtained with the *Instagram_places.py* and applying different clustering techniques.
