try:
    a1 = int(input("Massivni sonini kiriting: "))
    tr = False
    i = 1
    lis = []
    lis1 = []
    while i <=a1:
        a = (input("Soni kiriting: "))

        if len(a.split()) > a1:
            print("Kop son kiritildi!!")
        elif len(a.split()) == a1:
            print(222)
            lis.append(a.split())
            i+=1
        elif len(a) == a1:
            print("1")
            lis1.append(a)
            i+=1
        else:
            print("Kam son kiritildi!!")
    print(lis)
    print(lis1)

    # print(siii)
    # print(len(siii))
    # lis1 = len(lis) // a1
    # if len(siii) == 1:
    #     print("2 2 3")

    # elif lis1 == a1:
    #     print(lis)

    # if lis1 == 1:
    #     print(lis[0])
    # print(a1)
    # print(lis)
    # print(lis1)
    # print(len(lis))
    # print(lis)
    # print("Sonlarni kiriting: ")  
    # a2 = (input())
    # a3 = (input())
    # a4 = (input())
    # print("-----------------------")
    # if len(a1) == 4:
    #     print(f"{a1[0]} {a1[1]} {a1[2]} {a1[3]}\n    {a2[-2]} {a2[-1]}\n      {a3[-1]}")
    # elif len(a1) == 7:
    #     a11 = a1.split()
    #     a22 = a2.split()
    #     a33 = a3.split()
    #     a44 = a4.split()
    #     print(f"{a11[0]} {a11[1]} {a11[2]} {a11[3]}\n    {a22[-2]} {a22[-1]}\n      {a33[-1]}")
    # else:
    #     print("Xato normanli kiriting")

except IndexError as err:
    print("IndexError raqam togri kiriting kiriting")

