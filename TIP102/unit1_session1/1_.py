def linear_search(lst, t):
    count = 0
    for _ in lst:
        if _ == t:
            return count        
        count += 1

    return -1





if __name__ == "__main__": 
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    print(linear_search(items, target))

    items = ['bed', 'blue jacket', 'red shirt', 'hunny']
    target = 'red balloon'
    print(linear_search(items, target))

"""
https://docs.google.com/forms/d/e/1FAIpQLSfcXQx910yu3dmEfIoeZ_kBtkSiNpoJAH9nYkwQYi9gQzpHlw/viewform
"""



