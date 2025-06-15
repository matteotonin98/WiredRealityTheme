# esempio.py - File di esempio Python per il tema Electric Violet Dark

import math # Importazione di un modulo standard

# Definizione di una variabile globale e una costante
GLOBAL_MESSAGE = "Questo è un messaggio globale!"
PI_VALUE = 3.1415926535

"""
Questa è una docstring multilinea
per la funzione `calculate_area`.
Calcola l'area di un cerchio dato il raggio.
"""
def calculate_area(radius):
    if not isinstance(radius, (int, float)) or radius < 0:
        raise ValueError("Il raggio deve essere un numero positivo.")
        
    # Uso di una variabile locale e una costante
    area = PI_VALUE * (radius ** 2)
    return area

# Definizione di una classe di esempio
class Animal:
    def __init__(self, name, species):
        self.name = name # Attributo della classe
        self.species = species
        self._private_attribute = "valore_privato" # Convenzione per attributo privato

    def describe(self):
        # Stampa una stringa formattata (f-string)
        print(f"Nome: {self.name}, Specie: {self.species}")

    def _internal_method(self):
        # Un metodo "privato"
        print("Metodo interno chiamato.")

# Funzione per dimostrare cicli e condizioni
def process_list(data_list):
    print("\nElaborazione della lista:")
    for index, item in enumerate(data_list): # Ciclo for con enumerate
        if isinstance(item, str): # Condizione if-elif-else
            print(f"Elemento {index}: '{item}' (Stringa)")
        elif isinstance(item, (int, float)):
            if item % 2 == 0:
                print(f"Elemento {index}: {item} (Numero Pari)")
            else:
                print(f"Elemento {index}: {item} (Numero Dispari)")
        else:
            print(f"Elemento {index}: {item} (Tipo Sconosciuto)") 

# Blocco principale del programma
if __name__ == "__main__":
    print(GLOBAL_MESSAGE)

    # Chiamata a funzione
    try:
        circle_radius = 5.0
        area_result = calculate_area(circle_radius)
        print(f"L'area di un cerchio con raggio {circle_radius} è: {area_result}")

        # Test per un raggio negativo
        # calculate_area(-2) # Questa riga causerebbe un errore
    except ValueError as e:
        print(f"Errore: {e}")

    # Creazione di oggetti e chiamata a 
    dog = Animal("Fido", "Cane")
    cat = Animal("Romeo", "Gatto")
    dog.describe()
    cat.describe()
    dog._internal_method() # Chiamata al metodo "privato"

    # Esempio di lista con vari tipi di dati
    mixed_data = ["Test", 123, "Python", 45.67, True, None, "Highlighting", 88]
    process_list(mixed_data)

    # Uso di un set e un dizionario
    my_set = {"apple", "banana", "cherry"}
    my_dict = {"key1": "value1", "key2": 123, "key3": [1, 2]}

    print(f"\nSet: {my_set}")
    print(f"Dizionario: {my_dict}")

    print("\nProgramma Python terminato.")