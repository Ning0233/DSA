def arrange_attendees_by_priority(attendees, priority):
    less_p = []
    more_p = []
    and_p = []
    for i in attendees:
        if i == priority: and_p.append(i)
        if i < priority: less_p.append(i)
        if i > priority: more_p.append(i)
    return less_p + and_p + more_p

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 