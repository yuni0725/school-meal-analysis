def get_daily_menu():
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
        #오늘 날짜의 급식 메뉴 불러오기
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        new_menu = []

        real_menu = []

        wraps = soup.find_all("li", "tch-lnc-wrap")
        if wraps:
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
            
                for food in make_data_clean(new_menu):
                    real_menu.append(food)
            
                menu.append({
                    title : real_menu
                })
        else:
            pass

    return {"food" : menu }, YMD

def add_date(YMD):
    #날짜를 더하는 함수
    import datetime

    date = datetime.datetime.strptime(YMD, '%Y%m%d')
    new = date + datetime.timedelta(days=1)
    YMD = new.strftime('%Y%m%d')

    return YMD

def make_data_clean(list):
    #정규식 표현을 이용한 데이터 정규화
    import re
    pattern =  r'[^a-zA-Z가-힣]'
    menu = []
    for i in list:
        s = re.sub(pattern=pattern, repl='', string=i)
        menu.append(s)
    return menu







