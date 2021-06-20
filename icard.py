import requests
import json


class iCard:

    shopID = 10

    def __init__(self,CardNo, apiToken, env_type):

        self.CardNo = CardNo
        self.apiToken = apiToken

        if env_type == "production":
            self.baseURL_icard = "http://icardsysp1.azurewebsites.net"
        elif env_type == "testing":
            self.baseURL_icard = "https://icardtestapp.azurewebsites.net"
        else:
            raise ValueError("type can only be 'production' or 'testing'")

    # Gets List of brands and cats
    def getBrands(self, package):
        path = "/Fulllist"
        reqURL = self.baseURL_icard + path

        reqHeaders = {"all": "true",
                      "pack": package}

        req = requests.get(reqURL, headers=reqHeaders)
        if req.status_code == 200:
            res = json.loads(req.text)
            for i in res:
                print(f"Brand ID: {i['id']} \nBrand Name: {i['nameEn']}")
                for j in i["cats"]:
                    print(f"Cat ID: {j['id']}")
                print("_____________")
            return res

    def retrieveCards(self, confirmCode):
        path = "/Retrieve"
        reqURL = self.baseURL_icard + path

        reqParams = {"cc": confirmCode,
                     "icashno": self.CardNo}
        req = requests.get(reqURL, params=reqParams)
        if req.status_code == 200:
            res = json.loads(req.text)
            return res

    def purchaseCards(self,items,paymentCode):
        path = "/apiPay"
        reqURL = self.baseURL_icard + path

        cart = []

        for k, v in items.items():
            cart.append({"id": k, "quantity": v})

        reqParams = {"confirmcode": paymentCode,
                     "items": cart,
                     "cardno": self.cardNo}
        reqHeaders = {"apitoken":self.apiToken}

        req = requests.post(reqURL, params=reqParams, headers=reqHeaders)

        if req.status_code == 200:
            res = json.loads(req.text)

"""
Example
icard_client = iCard("7120117557","production")
print(icard_client.getBrands("7120117545"))
icard_client.retrieveCards("7120118549", "123456")
icard_client.purchaseCards({1:3, 4:5, 6:9}, "1234567")
"""