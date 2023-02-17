def split_num(num):
    lst=[]
    for i in str(num):
        lst.append(int(i))
    return sorted(lst)

def list_tonum(lst):
    num=""
    for i in lst:
        num+=str(i)
    return int(num)

def biggest_string_order_bigger(n):
    lst=split_num(n)
    print(lst.reverse())
    num=list_tonum(lst)
    return num


print(biggest_string_order_bigger(254))
