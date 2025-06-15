% esempio.m - File di esempio MATLAB per il tema Electric Violet Dark

%% Sezione 1: Dichiarazione Variabili e Costanti
% Questo è un commento su più righe
% per dimostrare la colorazione dei commenti

clc;        % Pulisce la finestra di comando
clear all;  % Rimuove tutte le variabili dal workspace
close all;  % Chiude tutte le finestre delle figure

% Dichiarazione di variabili numeriche
a = 10; 
b = 2.5;
c = a * b; % Operazione numerica

% Dichiarazione di una stringa
myString = 'Ciao, questo è un esempio di stringa in MATLAB!';

% Dichiarazione di un array (vettore riga)
myArray = [1, 2, 3, 4, 5];

% Array di celle
myCellArray = {'Apple', 'Banana', 123, true};

%% Sezione 2: Cicli e Condizioni
disp('Inizio ciclo for...'); % Stampa a console

for i = 1:length(myArray) % Ciclo for
    if mod(myArray(i), 2) == 0 % Condizione if-else
        fprintf('L''elemento %d è pari.\n', myArray(i));
    else
        fprintf('L''elemento %d è dispari.\n', myArray(i));
    end
end

disp('Fine ciclo for.');

% Ciclo while
counter = 5;
while counter > 0
    fprintf('Contatore: %d\n', counter);
    counter = counter - 1;
end

%% Sezione 3: Definizione e Chiamata Funzioni
% Definizione di una funzione locale (in genere in file separati)
function result = calculateProduct(x, y)
    % Questa funzione calcola il prodotto di due numeri
    result = x * y;
end

% Chiamata alla funzione
productResult = calculateProduct(a, b);
fprintf('Il prodotto di %f e %f è: %f\n', a, b, productResult);

% Funzione anonima
square = @(n) n.^2;
squaredValue = square(7);
fprintf('Il quadrato di 7 è: %d\n', squaredValue);

%% Sezione 4: Plotting (solo un accenno)
% MATLAB è famoso per i suoi strumenti di plotting
x_vals = 0:0.1:2*pi; % Vettore di valori
y_vals = sin(x_vals); % Funzione trigonometrica

% plot(x_vals, y_vals); % Commentato per evitare l'apertura di finestre
% title('Grafico della Funzione Seno');
% xlabel('Valore X');
% ylabel('Valore Y');
% legend('Seno');

%% Sezione 5: Costanti e valori speciali
TRUE_VALUE = true;
FALSE_VALUE = false;
NAN_VALUE = NaN;
INF_VALUE = Inf;

% Esempio di utilizzo di valori logici
if TRUE_VALUE && (NAN_VALUE ~= NAN_VALUE)
    disp('Questa riga non verrà eseguita.');
end
