########## Read a file containing integers and calculate their sum ###############

with open("Num.txt","r") as file:
    Num = file.readlines()
    Num = list(map(int, Num))
    result = sum(Num)
    print(result)
