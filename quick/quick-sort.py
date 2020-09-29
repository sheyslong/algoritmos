def quickSort(list_, init, fin):
    if fin > init:
        pivot = partition(list_, init, fin)
        quickSort(list_, init, pivot-1)
        quickSort(list_, pivot+1, fin)

def partition(list_, init, fin):
    pivo = list_[init]
    i = init
    j = fin
    
    while i < j:
        while i < fin and int(list_[i]) <= int(pivo):
            i+=1
        while j > init and int(list_[j]) >= int(pivo):
            j-=1
            
        if i < j:
            aux = list_[i]
            list_[i] = list_[j] 
            list_[j] = aux
        
    list_[init] = list_[j]
    list_[j] = pivo
    return j

def response(list_):
    string = ""
    for el in list_:
        string += el + " "
    return string

list_ = input().split()
quickSort(list_, 0, len(list_)-1)
res =  response(list_)
print(res)