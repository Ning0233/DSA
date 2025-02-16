def counting_pirates_action_minutes(logs, k):
    dp = [0] * k
    hash = {}
    for i in logs:
            hash[i[0]] = hash.get(i[0], []) + [i[1]] 
    #print(hash)
    for key in hash:
        PAM = len(set(hash[key]))
        dp[PAM-1] += 1
    return dp

    
    

logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4

print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))