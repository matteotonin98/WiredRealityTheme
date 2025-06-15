// esempio.cpp - File di esempio C++ per il tema Electric Violet Dark

#include <iostream> // Inclusione di libreria standard
#include <vector>   // Un'altra libreria comune

// Definizione di una costante
const double PI_VALUE = 3.1415926535;

/*
 * Questa è una funzione di esempio
 * che dimostra l'uso di variabili, cicli e condizioni.
 * @param count Il numero di iterazioni.
 * @return Un valore intero calcolato.
 */
int calculateSum(int count) {
    int totalSum = 0; // Dichiarazione e inizializzazione di una variabile

    for (int i = 0; i < count; ++i) { // Ciclo for
        if (i % 2 == 0) { // Condizione if-else
            totalSum += i; // Operatore di assegnazione con addizione
        } else {
            totalSum -= i;
        }
    }
    // Una stringa di esempio
    std::cout << "Calcolo completato. Somma parziale: " << totalSum << std::endl;
    return totalSum;
}

// Definizione di una classe di esempio
class MyClass {
public: // Specifier di accesso
    std::string name;
    int id;

    // Costruttore
    MyClass( std::string n, int i ) : name(n), id(i) {
        // Un commento TODO: Aggiungere logica di inizializzazione
    }

    // Metodo di classe
    void displayInfo() const {
        // Stampa le informazioni usando un metodo della libreria standard
        std::cout << "Nome: " << this->name << ", ID: " << id << std::endl;
    }
};

int main() {
    // Chiamata a funzione
    int result = calculateSum(10);
    std::cout << "Risultato finale: " << result << std::endl;

    // Creazione di un oggetto e chiamata a metodo
    MyClass obj("OggettoTest", 101);
    obj.displayInfo();
    
    // Uso di un puntatore (esempio breve)
    int* ptr = new int(2024);
    std::cout << "Anno corrente: " << *ptr << std::endl;
    delete ptr; // Deallocazione della memoria

    // Un'altra stringa con caratteri speciali: "Hello\nWorld!"
    const char* message = "Esempio di \"stringa\" con \\escape e numeri 123.";

    return 0; // Fine del programma
}