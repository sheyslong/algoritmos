list_ = input().split()
element = int(input())
def binary_search(el, list_, l, r):
    if r > -1 and l < len(list_):
        if l == r:
            if int(list_[r]) == el:
                return True
            return False
        mid = (l+r)//2
        if el == int(list_[mid]):
            return True
        if int(list_[mid]) < el:
            return binary_search(el, list_, mid+1, r)
        return binary_search(el, list_, l, mid-1)
        

bs = binary_search(element, list_, 0, len(list_)-1)
if bs:
    print("Exist")
else:
    print("Not Exist")