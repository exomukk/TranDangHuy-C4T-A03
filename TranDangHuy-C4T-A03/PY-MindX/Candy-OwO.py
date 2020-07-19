# money = int(input("Input money you have:"))
# price = int(input("Price 1 candy:"))
# shell = int(input("How many shell to exchange 1 candy:"))
# candy = money//price    
# candy2 = candy//shell  
# candy4 = candy%shell    
# candy5 = (candy2 + candy4)//shell
# candy6 = candy + candy2 + candy5
# candy7 = (candy5+candy2)%shell
# print("Candy to eat:",candy6)
# print("Shell left:",candy7)


def candy(choc, wrap):
    if (choc < wrap):
        return 0
    
    new_choc = choc // wrap
    return new_choc + count_remain(new_choc + choc % wrap, wrap)

def count_max(money, price, wrap):
    choc = money // price 

    return choc + candy(choc, wrap)