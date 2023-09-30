def get_nutri_data(food_name):
    #음식 데이터 불러오기
    import pandas as pd

    data = pd.read_csv("DB.csv", encoding="UTF-8")

    data_food_name = list(data["음 식 명"])

    #데이터 토크나이저
    import os
    os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-11\bin\server'

    from konlpy.tag import Okt
    okt = Okt()

    text = food_name
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
            "Food" : food_name,
            "Nutri" : {}
        }
    else:
        food_data = data[data['음 식 명'] == high_data]
        col = list(food_data.columns)
        return {
            "Food" : food_name,
            "Nutri" :{
                "weight" : float(str(food_data[col[1]].values[0]).replace("-", "0")),
                "kcal" : float(str(food_data[col[2]].values[0]).replace("-", "0")),
                "carbo ": float(str(food_data[col[3]].values[0]).replace("-", "0")),
                "sugar" : float(str(food_data[col[4]].values[0]).replace("-", "0")),
                "fat" : float(str(food_data[col[5]].values[0]).replace("-", "0")),
                "protein" : float(str(food_data[col[6]].values[0]).replace("-", "0")),
                "Ca" : float(str(food_data[col[7]].values[0]).replace("-", "0")),
                "P" : float(str(food_data[col[8]].values[0]).replace("-", "0")),
                "Na" : float(str(food_data[col[9]].values[0]).replace("-", "0")),
                "K" : float(str(food_data[col[10]].values[0]).replace("-", "0")),
                "Mg" : float(str(food_data[col[11]].values[0]).replace("-", "0")),
                "Fe" : float(str(food_data[col[12]].values[0]).replace("-", "0")),
                "Zn" : float(str(food_data[col[13]].values[0]).replace("-", "0")),
                "cholesterol" : float(str(food_data[col[14]].values[0]).replace("-", "0")),
                "trans_fat" : float(str(food_data[col[15]].values[0]).replace("-", "0")),
                }
            }
    