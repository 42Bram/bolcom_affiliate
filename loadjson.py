import json
from config import bolid, reportname, subid

def openjson(categorytype):
    with open('JSON/' + categorytype[0] + '.json', encoding="utf-8") as f:
        data = json.load(f)
        products = data['products']
        return products

def parser(details, category):
    ## Get attributes ##
    ean = details['ean']
    productid = details['id']
    title = details['title']
    description = details['longDescription']
    shortdescription = details['shortDescription']
    url = "http://partnerprogramma.bol.com/click/click?&s=" + bolid +"&t=p&f=PF&pid=" + productid + "&name=" + reportname +"&subid=" + subid
    image = ""
    try:
        for x in details['images']:
            if "XL" in x.values():
                image = x['url']
    except:
        pass
    price = str(details['offerData']['offers'][0]['price'])

    ## Create product in Woocommerce
    data = {
        "name": title,
        "type": "external",
        "sku": ean,
        "regular_price": price,
        "description": description,
        "short_description": (shortdescription[0:650] + "..."),
        "external_url": url,
        "button_text": "Koop op bol.com",
        "categories": [
            {
                "id": category[2]
            },
        ],
        "images": [
            {
                "src": image
            },

        ]
    }
    return data
