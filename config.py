from woocommerce import API

# Enter your Bol.com API key here
bolapi = ""

# Enter your bol.com affiliate ID here. This ID will be used to create affiliate links automatically
bolid = ""

# Enter your bol.com affiliate account id
reportname = ""

# Enter subid here for reporting in the bol.com dashboard, or leave empty
subid = ""

# Enter your Woocommerce consumer_key here
woo_consumer = ""

# Enter your Woocommerce secret_key here
woo_secret = ""

# Enter the category description, the Bol.com category ID, and the Woocommerce category ID
categories = [
    ("Nintendo Switch Games","38906", "103"),
    # ("Nintendo 3D Games", "38908", "106"),
    # ("Nintendo Wii Games", cat=3135, wordpress=107))
    #("Nintendo Switch Consoles", "38912", "108"),
    # ("Nintendo DS Consoles", "38923", "108")
]

wcapi3 = API(
    url="https://www.yourwebsite.com",
    consumer_key= woo_consumer,
    consumer_secret= woo_secret,
    version="wc/v3",
    query_string_auth=True,
    timeout=20
)
