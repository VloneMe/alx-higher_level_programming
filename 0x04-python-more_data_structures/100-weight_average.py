#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple
    """
    if len(my_list) == 0:
        return 0

    scores = [score * weight for (score, weight) in my_list]
    total_score = sum(scores)
    total_weight = sum(weight for (_, weight) in my_list)

    return (total_score / total_weight)
