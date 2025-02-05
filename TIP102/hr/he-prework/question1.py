
def solution(A):
    count = 1
    record = [A[0]]
    for _ in A[1:]:
        if _ < min(record): continue
        elif _ >= max(record): 
            record.append(_)
            count += 1
        else:
            record.append(_)
            sorted_record = sorted(record)
            record.pop(sorted_record.index(_))
    return count

