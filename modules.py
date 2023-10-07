def jaccard_similarity(A : list, B : list):
    #자카드 유사도 구하기(교집합 / 합집합)
    A = set(A)
    B = set(B)

    union = A.union(B)
    intersection = A.intersection(B)

    jaccard_similarity = len(intersection) / len(union)

    return jaccard_similarity