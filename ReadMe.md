# Abstraction and Reasoning

[Strona konkursu na kaggle](https://www.kaggle.com/boliu0/visualizing-all-task-pairs-with-gridlines?fbclid=IwAR3xoxK6-Z9iBFBAczOPPXIusU79gSy1is15Wo-cRNeSZB8HuIoUzXyEa94)

Program rozwiązuje zadania ze zbioru data/training i sprawdza poprawność wyników

## Uruchomienie programu

``` python
python .\src\main.py
```

## Wizualizacja zadań

``` python
python .\src\main.py -v
```

## Parametry uruchomienia programu


-  -h, --help       show this help message and exit
-  --filter, -f     Filter input tasks to only contains tasks with black background 
-  --visualize, -v  Visualize tasks
-  --time, -t       Measure execution time

Dodatkowe parametry można ustalać w pliku `scr/config.py`.