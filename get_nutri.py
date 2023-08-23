import requests
from bs4 import BeautifulSoup

menus = []

key = "JKAjWtJPpVy75MU5wvCtXa76wUc1yuqYSyRTrDJDUpZihoQ1fl5NQGJUATNEjYwVAapsTOPRsX0cVWcEjSbeqg=="

URL_CODE = "http://apis.data.go.kr/1390802/AgriFood/MzenFoodCode/getKoreanFoodList"

URL_NUT = "http://apis.data.go.kr/1390802/AgriFood/MzenFoodNutri/getKoreanFoodIdntList"

def get_info(menu):
    params = {
    "serviceKey": key,
    "Page_Size" : 50,
    "food_Name" : f"{menu}"
    }

    res = requests.get(URL_CODE, params=params, verify=False)

    xml_obj = BeautifulSoup(res.text, 'lxml-xml')
    rows = xml_obj.findAll("item")

    if rows:
        for i in range(0, len(rows)):
            text = rows[i].text.strip().split("\n")
            name = text[3]
            code = text[0]
            get_nutri(name, code)

    else:
        menu = get_formal_menu(menu)
        get_info(menu)

def get_nutri(menu, code):
    print(code)
    params = {
        'serviceKey' : key,
        'food_Code' : code,
    }

    res = requests.get(URL_NUT, params=params, verify=False)

    xml_obj = BeautifulSoup(res.text, 'lxml-xml')
    rows = xml_obj.findAll("idnt_List")

    weight = 0 #식품 무게
    prot = 0 #단백질
    carbo = 0 #탄수화물
    fafref = 0 #지방산
    ptss = 0 #칼륨
    clci = 0 #칼슘
    mg = 0 #마그네슘
    na = 0 #나트륨
    irn = 0 #철
    zn = 0 #아연
    vitE = 0 #비타민 E
    vitD = 0 #비타민 D
    sugar = 0 #당
    fiber = 0 #식이섬유

    for row in rows:
        weight += float(row.find("food_Weight").text)
        prot += float(row.find("prot_Qy").text)
        carbo += float(row.find("carbohydrate_Qy").text)
        fafref += float(row.find("fafref_Qy").text)
        ptss += float(row.find("ptss_Qy").text)
        clci += float(row.find("clci_Qy").text)
        mg += float(row.find("mg_Qy").text)
        na += float(row.find("na_Qy").text)
        irn += float(row.find("irn_Qy").text)
        zn += float(row.find("zn_Qy").text)
        vitE += float(row.find("vite_Qy").text)
        vitD += float(row.find("vitd_Qy").text)
        sugar += float(row.find("sugar_Qy").text)
        fiber += float(row.find("fibtg_Qy").text)

    nutri = {
        "Weight" : round(weight, 2),
        "Protin" : round(prot, 2),
        "Carbohydrate" : round(carbo, 2),
        "Fafref" : round(fafref, 2),
        "Ptss" : round(ptss, 2),
        "Clci" : round(clci, 2),
        "Mg" : round(mg, 2),
        "Na" : round(na, 2),
        "Iron" : round(irn, 2),
        "Zn" : round(zn, 2),
        "VitE" : round(vitE, 2),
        "VitD" : round(vitD, 2),
        "Sugar" : round(sugar, 2),
        "Fiber" : round(fiber, 2),
    }

    menus.append({
        menu : nutri,
    })

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


for menu in ["오리주물럭", "감자조림"]:
    get_info(menu)

print(menus)





