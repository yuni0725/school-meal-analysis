import requests
from bs4 import BeautifulSoup

menus = []

key = "JKAjWtJPpVy75MU5wvCtXa76wUc1yuqYSyRTrDJDUpZihoQ1fl5NQGJUATNEjYwVAapsTOPRsX0cVWcEjSbeqg=="

URL = "http://apis.data.go.kr/1390802/AgriFood/MzenFoodCode/getKoreanFoodList"

def get_nutri(menu):
    params = {
    "serviceKey": key,
    "Page_Size" : 50,
    "food_Name" : f"{menu}"
    }

    res = requests.get(URL, params=params, verify=False)

    xml_obj = BeautifulSoup(res.text, 'lxml-xml')
    rows = xml_obj.findAll("item")

    if rows:
        for i in range(0, len(rows)):
            text = rows[i].text.strip().split("\n")
            name = text[3]
            code = text[0]
            print(f"Name : {name}")
            print(f"Code : {code}")
    else:
        menu = get_formal_menu(menu)
        get_nutri(menu)
               
def get_formal_menu(menu):
    import openai

    openai.api_key = "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"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":"user", 
            "content":f"{menu}의 가장 중요한 재료 하나만 말해주고 따움표로 강조해줘",
            
        }],
        temperature = 0,
        max_tokens = 100,
    )

    return completion.choices[0].message.content.split("'")[1]

get_nutri('오리주물럭')





