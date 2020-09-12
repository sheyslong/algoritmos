list_ = input().split()

def bubble(list_):
    index = 0
    while index < len(list_)-1:
        index_ = 0 
        while index_ < len(list_)-1:
            current = list_[index_]
            next_ = list_[index_+1]
            if next_ < current:
                list_[index_+1] = current
                list_[index_] = next_
            
            index_+=1

        index+=1

def response(list_):
    string = ""
    for el in list_:
        string += el + " "
    return string

bubble(list_)
res =  response(list_)
print(res)