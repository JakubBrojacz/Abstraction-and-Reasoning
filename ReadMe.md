# Konkurs

## Wizualizacja

### Lokalnie

``` python
python .\src\visualize.py
```

### Na necie

[kaggle](https://www.kaggle.com/boliu0/visualizing-all-task-pairs-with-gridlines?fbclid=IwAR3xoxK6-Z9iBFBAczOPPXIusU79gSy1is15Wo-cRNeSZB8HuIoUzXyEa94)

## Plan

0. Czarny i inny kolor
1. Tylko zadania 2-kolorowe
2. Tylko zadania 3-kolorowe
3. Próba uogulnienia zadania dowolnego do 2/3 kolorowego (?)

## Ideas

1. Rozdzielić obraz na obiekt / obiekty i tło
2. Obiekty wybierać na kilka sposobów:
    - obszar 4 lub 8-spójny jednokolorowy
    - obszar 4 lub 8-spójny wielokolorowy na jednokolorowym tle
    - obszar niespójny jednokolorowy
    - obszar niespójny wielokolorowy na jednokolorowym tle
    - sterowanie punktem rysującym
3. Aby ogarnąć który sposób jest dobry w danym zadaniu trzeba porównać wyniki ze wszystkich danych treningowych, czy dane obiekty występują na nich.
4. Tak samo dla wyników z danych treningowych.
5. Sposób generowania wyniku to pewne (proste?) przekształcenie obiektów i tła.
6. W obiekcie mogą istnieć wewnętrzna obiekty, można spróbować je znaleźć. Na przykład 00d62c1b.json - wypełnienie obiektu, które jest obiuektem wewnętrznym, zmienia kolor z czarnego na źółty.
7. Trzeba próbować robnić pewnego rodzaju transformacje:
    - rotacje
    - symetrie
    - przesunięcia z nakładaniem się, czy obiekt/tło jest cykliczne
    - powiększenie / pomniejszenie
8. Transformacje na współrzęnych i znajdowanie zależności równości między współrzędnymi różnych obiektów
9. Podział całego obrazka na poszczególne plansze
10. Szukanie początkowych obektów w wynikowym obrazku
