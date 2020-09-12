list_ = input().split() 

def selection(list_):
    for i in range(len(list_)):
        index_min = i
        for j in range(i, len(list_)):
            if list_[j] < list_[index_min]:
                index_min = j

        aux = list_[i]
        list_[i] = list_[index_min]
        list_[index_min] = aux

def response(list_):
    string = ""
    for el in list_:
        string += el + " "
    return string

selection(list_)
res =  response(list_)
print(res)