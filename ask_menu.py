def ask_menu(YMD = "20231006"):
    import json

    with open(f"./json_file/{YMD}.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    kcal = 0
    carbo = 0
    sugar = 0
    fat = 0
    protein = 0
    Ca = 0
    P = 0
    Na = 0
    K = 0
    Mg = 0
    Fe = 0
    Zn = 0
    cholesterol = 0
    trans_fat = 0

    max_kcal = 2600
    max_carbo = round(324 * max_kcal / 2000, 2)
    max_sugar = round(100 * max_kcal / 2000, 2)
    max_fat = round(54 * max_kcal / 2000, 2)
    max_protein = round(55 * max_kcal / 2000, 2)
    max_Ca = round(700 * max_kcal / 2000, 2)
    max_P = round(700 * max_kcal / 2000, 2)
    max_Na = round(2000 * max_kcal / 2000, 2)
    max_K = round(3500 * max_kcal / 2000, 2)
    max_Mg = round(315 * max_kcal / 2000, 2)
    max_Fe = round(12 * max_kcal / 2000, 2)
    max_Zn = round(8.5 * max_kcal / 2000, 2)
    max_cholesterol = round(300 * max_kcal / 2000, 2)
    max_trans_fat = round(15 * max_kcal / 2000, 2)

    for d in data:
        print(list(d.keys())[0])
        d_list = list(d.values())[0]
        for food in d_list:
            ans = input(f"{food['Food']} (y / n)")
            if ans == "y":
                f = food['Nutri']
                if len(f) != 0:
                    kcal += f['kcal']
                    carbo += f['carbo']
                    sugar += f['sugar']
                    fat += f['fat']
                    protein += f['protein']
                    Ca += f['Ca']
                    P += f['P']
                    Na += f['Na']
                    K += f['K']
                    Mg += f['Mg']
                    Fe += f['Fe']
                    Zn += f['Zn']
                    cholesterol += f['cholesterol']
                    trans_fat += f['trans_fat']

            elif ans == "n":
                continue
            else:
                pass
    
    return {
        "kcal" : round(kcal - max_kcal, 2),
        "carbo ": round(carbo - max_carbo, 2),
        "sugar" : round(sugar - max_sugar, 2),
        "fat" : round(fat - max_fat, 2),
        "protein" : round(protein - max_protein, 2),
        "Ca" : round(Ca - max_Ca, 2),
        "P" : round(P - max_P, 2),
        "Na" : round(Na - max_Na, 2),
        "K" : round(K - max_K, 2),
        "Mg" : round(Mg - max_Mg, 2),
        "Fe" : round(Fe - max_Fe, 2),
        "Zn" : round(Zn - max_Zn, 2),
        "cholesterol" : round(cholesterol - max_cholesterol, 2),
        "trans_fat" : round(trans_fat - max_trans_fat, 2),
    }
    
