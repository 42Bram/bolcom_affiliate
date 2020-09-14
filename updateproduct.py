from config import categories
import loadjson
import wordpress
import getjson

## Run full script for every category in config file ##
for category in categories:

    ## Get JSON file from Bol.com server ##
    getjson.get(category)

    ## Load JSON file ##
    products = loadjson.openjson(category)
    print(str(len(products)) + " producten gevonden")

    ## Loop through all the products in JSON ##
    for details in products:

        ## Get attributes per product ##
        data = loadjson.parser(details, category)

        ## Upload to wordpress ##
        wordpress.api(data)





