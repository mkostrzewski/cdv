print("CDV")
print(2)
print()

#potega
potega = 2 ** 10
print(potega)

#pobieranie danych z klawiatury

imie = input("Podaj imie: ")

#konkatenacja +
print("Twoje imię podane z klawiatury: " + imie)

nazwisko = input("Podaj nazwisko: ")

print("Twoje imię: " + imie + ", Twoje nazwisko: " + nazwisko)

dlugosc = len(nazwisko)

print("Długość nazwiska: " , dlugosc)

print("Długość nazwiska: " + str(dlugosc))


#uzytkownik podaje z klawiatury swoj wiek
# print("cos ", end="") usuwa endl
# type(zmienna) sprawdza jakiego jest typu

wiek = input("Podaj swój wiek: ")

print("Twój wiek: " , wiek , " lat")


nazwisko = "Kowalski"

pierwszyZnak = nazwisko[0]

print(pierwszyZnak)

ostatniZnak = nazwisko[len(nazwisko) - 1]

print(ostatniZnak)

ostatniZnak = nazwisko[-1]

print(ostatniZnak)


x = "5"
print(type(x)) #str

x = int(x)

print(type(x)) #int


text = "Jan" * 2

print(text)

print(type(text))

y = 6

print(type(y)) #int

y = y / 2

print(type(y)) #float
print(y) # 3.0


wiek = 21

print("Twój wiek:" , wiek)

print("Twój wiek: " + str(wiek))



nazwisko = "Jankowski"

print(nazwisko[:3])

print(nazwisko[-2])

print(nazwisko[-2:])

print(nazwisko[:-2])

print(nazwisko[:-2:2]) #Jnos

print(nazwisko[::2])
