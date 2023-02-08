# Zadanie domowe 0401

W plikach `zaddom0401_*.py` znajdziesz funkcję `example_function()`, która drukuje pewien tekst na ekran.

## Etap 1

Napisz funkcję `three_times`, która jako argument przyjmuje inną funkcję. Po wywołaniu funkcji `three_times`, funkcja
przekazana jej w parametrze ma zostać wywołana trzy razy.

## Etap 2

Napisz dekorator `three_times`, który spowoduje, że gdy odekorowana przez niego funkcja zostanie wywołana, w
rzeczywistości funkcja ta wywoła się trzy razy. Odekoruj funkcję `example_function` tym dekoratorem. Uzyskany efekt ma
być identyczny z tym w etapie 1.

## Etap 3

W tym etapie funkcja `example_function` przyjmuje jeden parametr. Zmodyfikuj kod tak, żeby po odekorowaniu
funkcji `example_function` dekoratorem `three_times` można było nadal przekazać funkcji parametr (pozycyjny, oraz za
pomocą nazwy).

## Etap 4 (rozszerzenie)

Na podstawie dekoratora `three_times` napisz dekorator `many_times`, któremu podczas dekorowania będzie można przekazać
w parametrze, ile razy dekorowana funkcja ma zostać wywołana. Odekoruj funkcję `example_function`
dekoratorem `many_times` tak, aby funkcja ta została wywołana pięć razy. Dekorowana funkcja nadal ma przyjmować
parametry tak jak w etapie 3. 
