
dolnaGranica = 10
gornaGranica = 100
#dolnaGranica = int(input("Dolny zakres to: "))
#gornaGranica = int(input("Gorny zakres to: "))
def liczbyPierwsze(dolnaGranica, gornaGranica)

    print("Liczby pierwsze od ",dolnaGranica," do",gornaGranica,"to:")
    for liczba in range(dolnaGranica,gornaGranica + 1):
       # prime numbers are greater than 1
       if liczba > 1:
           for i in range(2,liczba):
               if (liczba % i) == 0:
                   break
           else:
               print(liczba)

def main():
    dolnaGranica =int  (input ('Dolny zakres liczb'))
    gornaGranica = int (input ('Gorny zakres liczb'))

    print (liczbyPierwsze(10,100))

main()
