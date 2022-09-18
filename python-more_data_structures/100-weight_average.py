#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return None
    if my_list == []:
        return 0
    scores = map(lambda x: x[0] * x[1], my_list)
    total_score = 0
    for i in scores:
        total_score += i
    weights = map(lambda x: x[1], my_list)
    total_weight = 0
    for j in weights:
        total_weight += j
    return (total_score / total_weight)
