# from menu import get_data, write_csv

# data = get_data()

# print(len(data))

# drink = [
# "망고에이드",
# "유자에이드",
# "아몬드우유",
# "레몬에이드",
# "청포도에이드",
# "딸기에이드",
# "자두에이드",
# "오미자에이드",
# "파워에이드",
# "블루레몬에이드",
# "청귤에이드",
# "체리에이드",
# "배쥬스",
# "사과쥬스",
# "복숭아아이스티",
# "오미자쥬스",
# "블루베리쥬스",
# "알로에쥬스",
# "캐플쥬스",
# "토마토쥬스",
# "요거풋풋사과쥬스",
# "복숭아쥬스",
# "청귤쥬스",
# "감귤쥬스",
# "요거상큼복숭아쥬스",
# "파인쥬스",
# "포도쥬스",
# "오렌지쥬스",
# "샤인머스캣쥬스",
# "석류쥬스",
# "갈아만든배쥬스",
# "파인애플쥬스",
# "매실쥬스",
# "복분자쥬스",
# "망고쥬스",
# "자몽쥬스",
# "청포도쥬스",
# "게토레이",
# "이프로",
# "보리차",
# "수정과",
# "유자민트아이스티",
# "초코우유",
# "우유",
# "블루베리스무디",
# "레몬아이스티",
# "갈아만든배",
# "아몬드브리즈",
# "포카리스웨트",
# "요구르트"
# ]
# salad = []
# serial = [
#     "오레오오즈",
#     "그래놀라카카오",
#     "초코첵스",
#     "그래놀라코코아호두",
#     "그래놀라",
#     "그래놀라코코",
#     "아몬드콘후레이크",
#     "초코크런치",
#     "그래놀라다이제",
#     "초코후레이크",
#     "후르트링",
#     "후르츠링",
#     "허니오즈",
#     "코코볼",
#     "오레오즈",
#     "우리쌀링"
# ]

# print(len(drink))

# data = [x for x in data if x not in drink]

# for d in data:
#     if "샐러드" in d:
#         salad.append(d)

# print(len(salad))

# data = [x for x in data if x not in salad]

# data = [x for x in data if x not in serial]

# print(len(data))

# write_csv(data, "menu_new2")

import openai

openai.api_key = ""

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role":"user", 
        "content":""
        
    }],
    temperature = 0,
    max_tokens = 100,
)

print(completion.choices[0].message.content)