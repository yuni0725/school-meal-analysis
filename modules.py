def write_csv(menu, name):
    import csv

    f = open(f"./csv_file/{name}.csv", 'w', newline="", encoding="UTF-8")
    writer = csv.writer(f)
    for food in menu:
        writer.writerow([food])

    f.close()

def get_csv_to_list(name):
    import pandas as pd

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    data = pd.read_csv(f"./csv_file/{name}.csv", encoding='UTF-8', usecols=['food'])

    data = data.food.tolist()

    data_new = []

    for d in data:
        data_new.append(d)
    
    return data_new

def write_split_data(data):
    import os
    os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-11\bin\server'

    from konlpy.tag import Okt
    okt = Okt()

    data_new = []

    for d in data:
        data_new.append(okt.morphs(d))

    write_csv(data_new, "menu_split")

def jaccard_similarity(A, B):
    A = set(A)
    B = set(B)

    union = A.union(B)
    intersection = A.intersection(B)

    jaccard_similarity = len(intersection) / len(union)

    return jaccard_similarity