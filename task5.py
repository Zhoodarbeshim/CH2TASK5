def desks_for_students(desk1, desk2, desk3):
    list_=[]
    if desk1 == 10:
        list_.append(desk1)

    if desk2 == 11:
        list_.append(desk2)

    if desk3 == 11:
        list_.append(desk3)
    
    return sum(list_)

print(desks_for_students(10, 11, 11))