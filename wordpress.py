from config import wcapi3

def api(data):
    result = wcapi3.post("products", data).json()
    print(result)
    print(data)
    if 'product_invalid_sku' in result.values():
        print("Product bestaat al.. checking for updates")
        x = (wcapi3.get("products", params={"sku": data['sku']}).json())
        x = x[0]
        queryid = str(x['id'])
        wcapi3.put("products/" + queryid, data).json()
        print("Product bijgewerkt")
    else:
        print("Product toegevoegd:")
        print(data)
