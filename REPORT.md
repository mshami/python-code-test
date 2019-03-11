OSTMODERN Solution Report
====


## Data Modeling:


#### There are two models `Starship` and `Listing`


** `Starship object`, fields are starship_class, starship_class_slug, manufacturer, length,
 hyperdrive_rating, cargo_capacity, crew, passengers
 
** `Listing object`, fields are name, ship_type, enabled, created, price


## Importer:


**  there is a management command to read, process and store the data from `https://swapi.co/api/starships/`

*** `read_process_data()` , It uses `requests` to download data and store them in db using `djano ORM`

* It covers follwing section of requirments:

````
We need to be able to import all existing
  [Starships](https://swapi.co/documentation#starships) to the provided Starship
  Model
````  


## Views:


#### 'StarshipListingSerializer'

* It is a `ModelSerializer`
* It gets all the `Listing` and `Starship` data and serialize them. There is a ForeignKey 
from Listing object to Starship object

#### 'StarshipListing'

* It is a `ListAPIView`
* It gets all Listing data/serialize
* It adds some filters for `price` and `created`

* It covers following section of requirements:

````
* A potential buyer can browse all Starships
* A potential buyer can sort listings by price or time of listing
````  
* Testing URLs:

`http://localhost:8000/shiptrader/listing/`
`http://localhost:8000/shiptrader/listing/?ordering=price`
`http://localhost:8000/shiptrader/listing/?ordering=created`


#### 'StarshipClassListing'

* It is a `APIView`
* It gets listing for a specific `starship_class` by using `starship_class_slug`
* It creates response 

* It covers following section of requirements:

````
* A potential buyer can browse all the listings for a given `starship_class`
````
* Testing URL:

`http://localhost:8000/shiptrader/starship-class/corvette`

#### 'StarshipDetails'

* It is a `generics.RetrieveUpdateAPIView`
* It gets a specific `listing` object by using `object_id`
* It allows user to update `name`, `price` and `enabled`

* It covers following section of requirements:

````
* To list a Starship as for sale, the user should supply the Starship name and
  list price
* A seller can deactivate and reactivate their listing
````
* Testing URL:

`http://localhost:8000/shiptrader/details/36`

## Tests:

#### `TestAPI`

* It covers models and views.

## Admin:

* It covers `Listing` and `Starship` objects.

## Setting up and testing:


* In order to set it up locally, Please refer to README.md file
* In order to populate the database, Python run `python manage.py importer`
* To get listing of all starships object -> `http://localhost:8000/shiptrader/listing/`
* To get sorted listing by `price` and `created` ->
`http://localhost:8000/shiptrader/listing/?ordering=price`
`http://localhost:8000/shiptrader/listing/?ordering=created`

* To supply the Starship name, list price and also deactivate, reactivate their listing ->
`http://localhost:8000/shiptrader/details/36` 36 is object_id it can be changed

* To browse all the listings for a given `starship_class` ->
`http://localhost:8000/shiptrader/starship-class/corvette` corvette is starship_class_slug it can be changed