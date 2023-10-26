def harommaloszthato(b):
    a:int = 1
    while a <= b:
        a  +=1
        if a % 3:
            print (f"A(z) {a} osztható hárommal", end=",")

def csokkeno(a):
    print("csokkeno szamok:")
    while a>1:
        a-=1
        print(a, end=";")
        


def otteloszthato():
    ot = False
    while ot == False:
        szam:int = int(input("Írjon be egy öttel oszthato szamot"))
        oszthato = szam % 5
        if oszthato == 0:
            ot = True

