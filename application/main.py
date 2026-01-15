from get_nutri import check_food
from menu_daily import get_daily_menu
from ask_menu import ask_menu

import json

menu = []

data, YMD = get_daily_menu()

for food in data['food']:
    food_list = []
    food_key = list(food.keys())[0] #조식 -> 중식 -> 석식 순으로 메뉴 데이터 생성
    foods = food[food_key]
    for f in foods:
        if "샐러드" in f:
            f = "샐러드"

        food_list.append(check_food(f))
    menu.append({food_key : food_list})

with open(f"./json_file/{YMD}.json", 'w', encoding='utf-8') as file:
    json.dump(menu, file, indent="\t", ensure_ascii=False)

print(ask_menu(YMD))