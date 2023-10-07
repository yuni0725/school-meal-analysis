def write_csv(menu : list, name : str):
    #csv 파일을 쓰기
    import csv

    f = open(f"./csv_file/{name}.csv", 'w', newline="", encoding="UTF-8")
    writer = csv.writer(f)
    for food in menu:
        writer.writerow([food])

    f.close()

def get_csv_to_list(name : str):
    #csv파일 데이터를 리스트로 변환하기
    import pandas as pd

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    data = pd.read_csv(f"./csv_file/{name}.csv", encoding='UTF-8', usecols=['food'])

    data = data.food.tolist()

    data_new = []

    for d in data:
        data_new.append(d)
    
    return data_new

def write_split_data(data : list):
    import os
    os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-11\bin\server'

    from konlpy.tag import Okt
    okt = Okt()

    data_new = []

    for d in data:
        data_new.append(okt.morphs(d))

    write_csv(data_new, "menu_split")

def jaccard_similarity(A : list, B : list):
    #자카드 유사도 구하기(교집합 / 합집합)
    A = set(A)
    B = set(B)

    union = A.union(B)
    intersection = A.intersection(B)

    jaccard_similarity = len(intersection) / len(union)

    return jaccard_similarity