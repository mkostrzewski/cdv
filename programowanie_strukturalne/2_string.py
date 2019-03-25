text = "Anna, paweł, JulIA"

lista = text.split(", ")

print(text)
print(lista)
print(type(lista))

imie1 = lista[0] #Anna
print(imie1)

print("Twoje imie: " + imie1)


imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower()
print(imieMale)

print(imie1)


#sprawdzanie zawartościallable
nazwisko = input("Podaj swoje nazwisko: ")
zawartosc = nazwisko.isalpha()
print(zawartosc)
#sprawdzic dlaczego przy lczbach jest False

nazwisko = ""

print(nazwisko.isalpha())

text1 = "\nJulia \n"
text2 = "Nowak"

print(text1 + text2)

text1 = text1.rstrip()

print(text1 + " " + text2)

#wyswietlanie lancucha znakow


#wszystkie wersje pythona


text = "%s , Java i  %s " % ("PHP", "Python")

print(text)


#nowsze


text = "{1}, Java i {0}".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)


#wypisanie danych


rok = 2019
miesiac = "marzec"
dzien = 25
print("Data: " , end="")
print(dzien, miesiac, rok)


print("Data: " , end="")
print(dzien, miesiac, rok, sep='-')








print()
