
a =input("Started the game press any key\n")
while(a!="end"):
    choise_field= int(input("For add press 1:\nFor update press 2:\n"))
    li=[]
    n = int(input("How many input you want to add in list\n"))
    if choise_field==1:
        for i in range(n):
         n1 = input()
         li.append(n1)

    print(li)

    choise_field= int(input("For add press 1:\n For update press 2:\n"))
    if choise_field==2:
        index = int(input("given index for update\n"))
        value = (input("set a value\n"))
        li[index] = value

    print(li)



