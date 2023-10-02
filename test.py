from bs4 import BeautifulSoup
import requests

num = 1312

drinks = [
    ["음 식 명", "중량(g)" ,"에너지(kcal)","탄수화물(g)","당류(g)","지방(g)",'단백질(g)','칼슘(mg)','인(mg)','나트륨(mg)','칼륨(mg)','마그네슘(mg)','철(mg)','아연(mg)','콜레스테롤(mg)','트랜스지방(g)']
]

for i in range(0, 7):
    URL = f"https://theliter.net/board_cCpL21/category/{num + i}"

    res = requests.get(URL)

    if res.status_code != 200:
        print(res.status_code)
    else:
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        divs = soup.find_all("div", "subject")
        for div in divs:
            title = div.text
            print(title)
            uls = div.parent.parent.parent.find_all("ul", 'info g-0')
            for ul in uls:
                lis = ul.find_all("li")
                name = lis[0].text
                size = name.split(" ")[0]
                if size == "ML":
                    weight = "680"
                elif size == "L":
                    weight = "907"
                kcal = lis[1].text.split(")")[1].replace(" ", "").replace("\t", "")
                carbo = lis[2].text.split(")")[1].replace(" ", "").replace("\t", "")
                sugar = lis[3].text.split(")")[1].replace(" ", "").replace("\t", "")
                protein = lis[4].text.split(")")[1].replace(" ", "").replace("\t", "")
                fat = lis[5].text.split(")")[1].replace(" ", "").replace("\t", "")
                na = lis[6].text.split(")")[1].replace(" ", "").replace("\t", "")
                if kcal == "-" and carbo == "-" and sugar == "-" and protein == "-" and fat == "-" and na == "-":
                    pass
                else:
                    drink = [title + " " + name, weight.replace("-", "0"), kcal.replace("-", "0"), carbo.replace("-", "0"), sugar.replace("-", "0"), fat.replace("-", "0"), protein.replace("-", "0"), 0, 0, na.replace("-", "0"), 0, 0, 0, 0, 0, 0]
                    drinks.append(drink)


import csv

f = open("DB_drink_litter.csv", "w", newline="")
writer = csv.writer(f)

for d in drinks:
    writer.writerow(d)
f.close