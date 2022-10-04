from tinydb import TinyDB,Query 
import json
from pprint import pprint

db=TinyDB('db.json')

class DB:
    def __init__(self, filename):
        self.db = TinyDB(filename)
        self.query = Query()
        self.table = None
        self.mobel = None

    def company(self, company):
        query = Query()
        self.db.default_table_name = company
        self.table = company
        data = self.db.search(query.company.search(company))
        return data

    def company_name(self,company):
        query=Query()
        self.db.default_table_name=company
        self.table = company
        name = self.db.search(query.company.search(company))
        arr_name = []
        for i in name:
            arr_name.append(i["name"])
        return arr_name

    def company_mobil_imeg(self, mobil_name:str) -> str:
        query=Query()
        self.db.default_table_name = self.table
        data = self.db.search((self.query.name == mobil_name))
        return data

    # def company_img(self, company):
    #     query = Query()
    #     self.db.default_table_name = company
    #     data = self.db.search(query.company.search(company))
    #     arr_caption =[]
    #     for i in data:
    #         caption= "name :"+ i['name']+ " color : " + i["color"]+ " price : "+str(i['price'])+'$'+" Ram : "+i['RAM']+" memory : "+i["memory"]
    #         arr_caption.append({["name"]:i['img_url'],"caption":caption})
    #     return arr_caption


# x = DB('db.json')
# pprint(x.company_mobil('Redmi')) 








