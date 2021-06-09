while True:
    x= int(input("Please enter a decimal number:"))
    r = 0;
    Rs = [];
    while(x != 0):
        r = x% 2
        x = x//2
        Rs = [r]+Rs
    for i in range(0,len(Rs)):   
        print(Rs[i],end='')
    print()
