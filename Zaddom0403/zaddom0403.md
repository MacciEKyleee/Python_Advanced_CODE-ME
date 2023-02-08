# Zadanie domowe 0403

W tym zadaniu należy stworzyć context manager, który umożliwi policzenie czasu wykonania kodu zawartego w jego wnętrzu.

## Etap 1

W pliku `zaddom0403_e1_szablon.py` znajdziesz funkcję `generate_and_sort`, której czas działania wykonania chcemy zmierzyć. Napisz klasę `Timed`, która będzie context managerem i zmierz za jej pomocą czas wykonania funkcji `generate_and_sort`. Przy wyjściu z context managera, na ekranie ma pojawić się linia ze zmierzonym czasem w standardowym formacie: np. `0:00:00.095467`. Przykładowy kod mierzący czas wykonania znajdziesz w pliku `measure_time.py`.

## Etap 2

W tym etapie należy dodać do klasy `Timed` możliwość zwrócenia czasu, jaki minął od startu również wewnątrz bloku context managera.

Aby to osiągnąć:
- dodaj do context managera zwracanie obiektu, w tym przypadku siebie samego.
- dodaj do context managera metodę `elapsed`, która obliczy i wydrukuje na ekran czas, który upłynął od rozpoczęcia działania context managera.
- aby przetestować jej działanie, wywołaj tę metodę po każdym wywołaniu funkcji `generate_and_sort`

## Etap 3 (rozszerzenie) 

To rozszerzenie proszę umieścić w pliku `zaddom0403_e3.py`, gdyż zaburzy on działanie testów do poprzednich etapów.

Dodaj do klasy `Timed` metodę `elapsed_since_last`, która zwróci czas, który minął od ostatniego zawołania tej metody, lub, jeśli nie była nigdy zawołana, to od początku.
W tym etapie czasy nie powinny być wypisywane na bieżąco na ekran, lecz wydrukowane po wyjściu z context managera. 