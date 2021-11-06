word = input("Proszę podać słowo do sprawdzenia. ")
list_A = []
list_B = []

#Pobiera litery ze zmiennej word i dodaje te litery do obu list

for letter in word:
    list_A.append(letter)

for letter in word:
    list_B.append(letter)

# Odwraca zawartość listy_B

list_B.reverse()

# Porównuje czy obie listy są równoważne

if list_A == list_B:
    print(bool(1))
    print("Podane słowo jest palindromem.")
else:
    print(bool(0))
    print("Podane słowo NIE jest palindromem")