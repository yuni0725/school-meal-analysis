def get_food_data(food : str):
    #사전에 조사된 음식 데이터 불러오기
    import pandas as pd

    data = pd.read_csv("./csv_file/DB.csv", encoding="UTF-8")

    data_food_name = list(data["음 식 명"])

    #데이터 토크나이저(명사 단위로 자르기)
    import os
    os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-11\bin\server'

    from konlpy.tag import Okt
    okt = Okt()

    text = food
    text_split = okt.morphs(text)

    high_score = 0
    high_data = 0

    #자카드 유사도를 활용하여 유사도 비교하기
    from modules import jaccard_similarity

    for d in data_food_name:
        d_split = okt.morphs(d)
        score = jaccard_similarity(d_split, text_split)
        if score > high_score:
            high_score = score
            high_data = d
        else:
            continue

    if high_data == 0:
        #유사한 데이터가 없으면...빈 데이터 반환하기
        return {
            "Food" : food,
            "Nutri" : {}
        }
    else:
        #유사한 데이터가 존재한다면...음식의 영양소를 반환하기
        food_data = data[data['음 식 명'] == high_data]
        col = list(food_data.columns)

        #밥이라는 단어가 존재 여부를 체크
        if "밥" in food:
            old_weight = float(str(food_data[col[1]].values[0]).replace("-", "0"))
            rice_weight = 183
            return {
                "Food" : food,
                "Nutri" :{
                    "weight" : rice_weight,
                    "kcal" : round(float(str(food_data[col[2]].values[0])) / old_weight * rice_weight, 2),
                    "carbo": round(float(str(food_data[col[3]].values[0])) / old_weight * rice_weight, 2),
                    "sugar" : round(float(str(food_data[col[4]].values[0])) / old_weight * rice_weight, 2),
                    "fat" : round(float(str(food_data[col[5]].values[0])) / old_weight * rice_weight, 2),
                    "protein" : round(float(str(food_data[col[6]].values[0])) / old_weight * rice_weight, 2),
                    "Ca" : round(float(str(food_data[col[7]].values[0])) / old_weight * rice_weight, 2),
                    "P" : round(float(str(food_data[col[8]].values[0])) / old_weight * rice_weight, 2),
                    "Na" : round(float(str(food_data[col[9]].values[0])) / old_weight * rice_weight, 2),
                    "K" : round(float(str(food_data[col[10]].values[0])) / old_weight * rice_weight, 2),
                    "Mg" : round(float(str(food_data[col[11]].values[0])) / old_weight * rice_weight, 2),
                    "Fe" : round(float(str(food_data[col[12]].values[0])) / old_weight * rice_weight, 2),
                    "Zn" : round(float(str(food_data[col[13]].values[0])) / old_weight * rice_weight, 2),
                    "cholesterol" : round(float(str(food_data[col[14]].values[0])) / old_weight * rice_weight, 2),
                    "trans_fat" : round(float(str(food_data[col[15]].values[0])) / old_weight * rice_weight, 2),
                    }
                }

        else:
            #밥이라는 단어가 포함되어있지 않으면 모두 반찬으로 간주
            old_weight = float(str(food_data[col[1]].values[0]))
            side_weight = 70
            return {
                "Food" : food,
                "Nutri" :{
                    "weight" : side_weight,
                    "kcal" : round(float(str(food_data[col[2]].values[0])) / old_weight * side_weight, 2),
                    "carbo": round(float(str(food_data[col[3]].values[0])) / old_weight * side_weight, 2),
                    "sugar" : round(float(str(food_data[col[4]].values[0])) / old_weight * side_weight, 2),
                    "fat" : round(float(str(food_data[col[5]].values[0])) / old_weight * side_weight, 2),
                    "protein" : round(float(str(food_data[col[6]].values[0])) / old_weight * side_weight, 2),
                    "Ca" : round(float(str(food_data[col[7]].values[0])) / old_weight * side_weight, 2),
                    "P" : round(float(str(food_data[col[8]].values[0])) / old_weight * side_weight, 2),
                    "Na" : round(float(str(food_data[col[9]].values[0])) / old_weight * side_weight, 2),
                    "K" : round(float(str(food_data[col[10]].values[0])) / old_weight * side_weight, 2),
                    "Mg" : round(float(str(food_data[col[11]].values[0])) / old_weight * side_weight, 2),
                    "Fe" : round(float(str(food_data[col[12]].values[0])) / old_weight * side_weight, 2),
                    "Zn" : round(float(str(food_data[col[13]].values[0])) / old_weight * side_weight, 2),
                    "cholesterol" : round(float(str(food_data[col[14]].values[0])) / old_weight * side_weight, 2),
                    "trans_fat" : round(float(str(food_data[col[15]].values[0])) / old_weight * side_weight, 2),
                    }
                }

def get_not_food_data(food : str):
    #음료, 시리얼, 과일과 같은 반복되는 데이터라면 사전에 조사된 데이터를 그대로 반환
    import pandas as pd
    not_food = pd.read_csv("./csv_file/DB_not_food.csv")

    food_detail = not_food[not_food['음 식 명'] == food]
    food_detail = list(food_detail.values[0])

    name = food_detail[0]
    nutri = food_detail[1:]

    return {
    "Food" : name,
    "Nutri" :{
        "weight" : nutri[0],
        "kcal" : nutri[1],
        "carbo": nutri[2],
        "sugar" : nutri[3],
        "fat" : nutri[4],
        "protein" : nutri[5],
        "Ca" : nutri[6],
        "P" : nutri[7],
        "Na" : nutri[8],
        "K" : nutri[9],
        "Mg" : nutri[10],
        "Fe" : nutri[11],
        "Zn" : nutri[12],
        "cholesterol" : nutri[13],
        "trans_fat" : nutri[14],
        }
    }

def check_food(food : str):
    #음료, 샐러드, 시리얼 등 반복되는 음식인지 판단
    import pandas as pd
    foods = list(pd.read_csv("./csv_file/DB_not_food.csv")["음 식 명"])

    if food in foods:
        detail = get_not_food_data(food)
    else:
        detail = get_food_data(food)
    
    return detail
