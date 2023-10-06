def get_food_data(food : str):
    #음식 데이터 불러오기
    import pandas as pd

    data = pd.read_csv("./csv_file/DB.csv", encoding="UTF-8")

    data_food_name = list(data["음 식 명"])

    #데이터 토크나이저
    import os
    os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-11\bin\server'

    from konlpy.tag import Okt
    okt = Okt()

    text = food
    text_split = okt.morphs(text)

    high_score = 0
    high_data = 0

    #데이터 유사도 확인하지
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
        return {
            "Food" : food,
            "Nutri" : {}
        }
    else:
        food_data = data[data['음 식 명'] == high_data]
        col = list(food_data.columns)
        if "밥" in food:
            old_weight = float(str(food_data[col[1]].values[0]).replace("-", "0"))
            rice_weight = 200
            return {
                "Food" : food,
                "Nutri" :{
                    "weight" : rice_weight,
                    "kcal" : float(str(food_data[col[2]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "carbo ": float(str(food_data[col[3]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "sugar" : float(str(food_data[col[4]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "fat" : float(str(food_data[col[5]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "protein" : float(str(food_data[col[6]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "Ca" : float(str(food_data[col[7]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "P" : float(str(food_data[col[8]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "Na" : float(str(food_data[col[9]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "K" : float(str(food_data[col[10]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "Mg" : float(str(food_data[col[11]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "Fe" : float(str(food_data[col[12]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "Zn" : float(str(food_data[col[13]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "cholesterol" : float(str(food_data[col[14]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    "trans_fat" : float(str(food_data[col[15]].values[0]).replace("-", "0")) / old_weight * rice_weight,
                    }
                }

        else:
            old_weight = float(str(food_data[col[1]].values[0]).replace("-", "0"))
            side_weight = 100
            return {
                "Food" : food,
                "Nutri" :{
                    "weight" : old_weight,
                    "kcal" : float(str(food_data[col[2]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "carbo ": float(str(food_data[col[3]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "sugar" : float(str(food_data[col[4]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "fat" : float(str(food_data[col[5]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "protein" : float(str(food_data[col[6]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "Ca" : float(str(food_data[col[7]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "P" : float(str(food_data[col[8]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "Na" : float(str(food_data[col[9]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "K" : float(str(food_data[col[10]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "Mg" : float(str(food_data[col[11]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "Fe" : float(str(food_data[col[12]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "Zn" : float(str(food_data[col[13]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "cholesterol" : float(str(food_data[col[14]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    "trans_fat" : float(str(food_data[col[15]].values[0]).replace("-", "0")) / old_weight * side_weight,
                    }
                }

def get_not_food_data(food : str):
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
        "carbo ": nutri[2],
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
    import pandas as pd
    foods = list(pd.read_csv("./csv_file/DB_not_food.csv")["음 식 명"])

    if food in foods:
        detail = get_not_food_data(food)
    else:
        detail = get_food_data(food)
    
    return detail
