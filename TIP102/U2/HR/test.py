def grouped_anagrams(strs):
    print(strs)
    # Write your code here
    if len(strs) <=1: 
        return [strs]
    hashm = {}
    memo = {}
    result = []
    
    for _ in range(len(strs)):
        memo[_] = sorted(list(strs[_]))
    print(memo)
    for key, item in memo.items():
        s = "".join(item)
        if s not in hashm: 
            hashm[s] = [strs[key]]
        else: 
            hashm[s].append(strs[key])
    print("hashm")
    print(hashm)
print(grouped_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
