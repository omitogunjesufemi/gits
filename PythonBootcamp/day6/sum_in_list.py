def my_list(a,b,c,d,e):
    my_list = [a,b,c,d,e]
    return my_list

def main():
    total = 0
    for i in my_list(8,3,2,0,7):
        total = total + i
    print(total)

    
main()
