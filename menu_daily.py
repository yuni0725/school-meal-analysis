# This File gets menu from website and export by csv
def get_data():
    import requests
    from bs4 import BeautifulSoup

    import datetime

    date = datetime.datetime.now()
    YMD = date.strftime('%Y%m%d')

    menu = []

    url = f"https://school.jbedu.kr/sangsan/MABAGAEAD/list?ymd={YMD}"
    res = requests.get(url)

    if res.status_code != 200:
        print(res.status_code)
    else:
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        new_menu = []

        real_menu = []

        wraps = soup.find_all("li", "tch-lnc-wrap")
        if wraps:
            #메뉴 찾아서 리스트에 집어 넣기
            for wrap in wraps:
                new_menu = []
                real_menu = []

                title = wrap.find("dt").string
                for menus in wrap.find("dd", "tch-lnc").find_all("li"):
                    menus = menus.text.replace("\r", "")
                    if "/" in menus:
                        menus = menus.split("/")
                        for i in menus:
                            new_menu.append(i)
                    else:
                        new_menu.append(menus)
            
                for food in make_data_regular(new_menu):
                    real_menu.append(food)
            
                menu.append({
                    title : real_menu
                })
        else:
            pass

    return {"food" : menu }, YMD

def add_date(YMD):
    import datetime

    date = datetime.datetime.strptime(YMD, '%Y%m%d')
    new = date + datetime.timedelta(days=1)
    YMD = new.strftime('%Y%m%d')

    return YMD

def make_data_regular(list):
    import re
    pattern =  r'[^a-zA-Z가-힣]'
    menu = []
    for i in list:
        s = re.sub(pattern=pattern, repl='', string=i)
        menu.append(s)
    return menu