list_ = input().split()

def insertion(list_):
    for i in range(1, len(list_)):
        j = i
        k = j -1
        current = list_[j]
        while k >= 0:
            previous = list_[k]
            if current < previous:
                list_[k] = current
                list_[j] = previous        
            else:
                break
            j-=1
            k = j -1
            current = list_[j]

def response(list_):
    string = ""
    for el in list_:
        string += el + " "
    return string

insertion(list_)
res =  response(list_)
print(res)