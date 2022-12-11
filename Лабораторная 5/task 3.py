from random import randint

def get_unique_list_numbers(a, b, c) -> list[int]:
    list = []
    while (len(list)<c):
        uni = randint(a,b)
        if uni in list:
            continue
        else:
            list.append(uni)
    return(list)

print(get_unique_list_numbers(-10,10,15))

