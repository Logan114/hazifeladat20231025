szoveg = "Szép nap van!"

print('1. karakter' ,szoveg[0])
print('2. karakter' ,szoveg[1])
print('szoveg hossza:' ,len(szoveg))
utolso:int = int(len(szoveg))
utolso -= 1
print ('Az utolso karakter', szoveg[utolso])
n = 0

while n < len(szoveg):
    print(szoveg[n])
    n += 1
def szovegkezeles():
    szoveg = "ez egy teszt szöveg"
    print (szoveg)
    print("nagybetűvel", end=": ")
    print (szoveg.upper())
    if "teszt" in szoveg:
        print ("szerepel a teszt szó")
    teszt2 = szoveg.replace("teszt", "proba")
    print("'TESZT kicserélve PRÓBAra", end=": ")
    print (teszt2)
    print("Első betű nagybetű", end=": ")
    print(szoveg.title())
    print(szoveg.index("s"),". helyen szerepel az S")
szoveg = "ez egy teszt szöveg"


szovegkezeles()
def szoveg_visszafele(szoveg):
    print (f"a(z)'{szoveg}' visszafelé", end=": ")
    print(szoveg[::-1])

def a_betuk_szama(szoveg):
    print(f"Hányszor szerepel az A betű az alábbi szövegben:'{szoveg}'", end=": ")
    print(szoveg.count("a"))
    i:int = 0
    a_szam:int = 0
    while i!<len(szoveg):
        if szoveg[i] == 'a':
            a_szam += 1
        i+=1
    print('A betuk szama', a_szam)

szoveg_visszafele("Ez egy teszt szöveg")
a_betuk_szama("The quick brown fox jumps over the lazy dog")