# Prospecting LA's Backyard Houses with Machine Learning

This project looks at how to influence housing in Los Angeles 
(because I really would like to rent/buy a house soon) with a 
tool powered by data science.  Many LA Homeowners have the 
question: Should I build a backyard house?  Backyard houses are 
typically rentals and are often for family members. However, some 
are rented out as passive income especially for young families or 
aging elderly. I want to find out where these houses will make a 
good amount of money.

## Objective

I wanted to create a tool that determines: 1. the potential income of a backyard house, 
2. its feasibility in the homeowner's backyard

## Data Sources

I have divided the data sources into the two parts of my project:

### Part 1 Datasets: Predict Nightly Income 

I first looked at the Inside AirBnB dataset on Los Angeles 
to get a proxy for rental income.  Inside AirBnB is an AirBnB watchdog
that aims to keep the platform honest and identify illegal rentals.  
I used the detailed listings data from March 13, 2020, available here
under the creative commons license:

*[Inside AirBnB LA](http://data.insideairbnb.com/united-states/ca/los-angeles/2020-03-13/data/listings.csv.gz)

I augmented this data with geographical datasets available from Los Angeles' geohub, 
as well as scraping neighborhood sales price data.  These datasets 
can be obtained here:

* [LA's geohub](http://geohub.lacity.org/)
This site has a plethora of useful datasets of which I only used a fraction I thought
most relevant. Each property had a feature that took into account the proximity of each of these amenities:

* [Parks and Gardens](http://geohub.lacity.org/datasets/lacounty::parks-and-gardens) - recreation
* [Metro](http://geohub.lacity.org/datasets/lacounty::metro-stations) - public transit
* [Freeway](http://geohub.lacity.org/datasets/lacounty::freeway-exits) - private transit
* [Museums and Aquariums](http://geohub.lacity.org/datasets/lacounty::museums-and-aquariums) - culture for family
* [Cultural and Performing Arts](http://geohub.lacity.org/datasets/lacounty::cultural-and-performing-arts-centers-1) - culture for adults
* [Walkability Index Score](http://geohub.lacity.org/datasets/ladot::walkability-index-score-2012) - residential
* [Property Shark's Median Home Sales Price by Neighborhood](https://public.tableau.com/profile/property.shark#!/vizhome/LATopNhoods2018/Dashboard1) - neighborhood value

### Part 2 Datasets: Determine feasibility in homeowner's backyard

I used two datasets to assess the lot feasibility.
These datasets gave me the lot address, location, size, zoning, and existing house area.
* [Assessor Parcels Data - 2016-2019](https://data.lacounty.gov/Parcel-/Assessor-Parcels-Data-2016/7rjj-f2pv)
* [Parcels](http://data-lahub.opendata.arcgis.com/datasets/lacounty::parcels/data)

Backyard House Zoning Regulations as well as basic floor areas, plans, and capacity of backyard houses 
was sourced from the very handy pamphlet out of UCLA's CityLab:

* [ADU Guidebook - CityLab](https://citylab.ucla.edu/adu-guidebook) - zoning+ from UCLA

## Methodology: Transfer Learning

To make this prediction, I first built an XGBoost Regressor model that predicted the income 
of a property. I then built a database of properties that could feasibly accommodate a backyard house 
of any size. I then used transfer learning to plug my backyard house database into my 
price prediction model to obtain each property’s predicted nightly income of their potential 
backyard house.

## Conclusions

For an individual in a high value neighborhood with space to accommodate a large unit, the 
gains for renting out your backyard will be higher. For an individual in a less desire-able 
neighborhood with less space, your gains will be lower. However, there will still be 
quantifiable gains.

Using our backyard house database and visualizing it over LA with Tableau, we can identify 
three distinct segments of the potential backyard house market — high, medium, and low value. 

This machine-learning powered database is a useful tool for both the ADU start-up as well as 
the home-owner. I also see a potentials from a planning perspective. The city is capable of 
tuning its incentives for different populations in different areas of the city.

You can see the complete project, as well as a Map of the Backyard House Segments of LA at my medium blog:
* [Prospecting LA's Backyard Houses](https://medium.com/@anupamagarla/prospecting-las-backyard-houses-with-machine-learning-8fdc191e1cf)



## Author

* **Anupama Garla** - [Pamaland1](https://github.com/Pamaland1)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thank you to COVER's [Jemuel Joseph](https://www.buildcover.com/) - for taking time to talk to me about his company and provide an Assessor's dataset.
* Thanks for those who came before and studied AirBnB datasets both through mapping and modelling:
* [Graciela Carrillo](https://towardsdatascience.com/predicting-airbnb-prices-with-machine-learning-and-location-data-5c1e033d0a5a) - mapping
* [Laura Lewis](https://towardsdatascience.com/predicting-airbnb-prices-with-machine-learning-and-deep-learning-f46d44afb8a6) - modelling
* and to my husband, Jesung Park, for supporting me in new endeavors even though its tough
* [METIS](https://www.thisismetis.com/live-online-data-science-bootcamp) teachers for also supporting, assisting, and teaching me mad data science skills.

