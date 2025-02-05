def find_missing_clues(clues, lower, upper): 
    clue_set = set(clues)
    list_range =  []
    for clue in clue_set:
        pre_clue = clue - 1
        after_clue = clue + 1
        if (lower <= pre_clue <= upper) and (pre_clue not in clue_set):
            list_range.append(pre_clue)
        if (lower <= after_clue <= upper) and (after_clue not in clue_set):
            list_range.append(after_clue)
    if not lower in clue_set:
        list_range.insert(0,lower)
    if not upper in clue_set:
        list_range.append(upper)
    print( [list_range[i: i+2] for i in range(0, len(list_range), 2)])
    

            


if __name__ == "__main__": 
    clues = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    find_missing_clues(clues, lower, upper)

    clues = [-1]
    lower = -1
    upper = -1
    find_missing_clues(clues, lower, upper)
