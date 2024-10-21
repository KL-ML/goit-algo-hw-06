## goit-algo-hw-06

**Опис:**
Для цієї роботи була побудована структура молекули кофеїну у вигляді графу.
![graf_coffein.png](https://github.com/KL-ML/goit-algo-hw-06/blob/main/graf_coffein.png)

# Отримано наступні результати:

# Завдання 1:

Виводимо кількість вершин та ребер у вигляді підрахунку кількості атомів і звʼязків між ними:
Кількість атомів: 24
Кількість звʼязків: 29

Знайдено валентність елементів за допомогою підрахунку ступені кожної вершини
Валентність елементів:
Натрій: 3, Вуглець: 4, Кисень: 2, Водень: 1

Отримаємо найбільш середній елемент за методом посередництва вузла
('C3', 0.021739130434782608)

# Завдання 2:

Будемо відштовхуватися від найбільш середнього елементу, виявленого раніше і пройдемо по кожному елементу графу двома алгоритмами.

Отриманий шлях використовуючи алгоритм `DFS`:<br>
C3 C4 O1 N4 C7 N3 C5 N1 C1 H1 N2 C2 H2 H3 H4 C6 H5 H6 H7 O2 C8 H8 H9 H10<br>

Отриманий шлях використовуючи рекурсивний алгоритм `BFS`:<br>
C3 C4 C5 N2 N4 O1 N1 N3 C2 C1 C7 C8 C6 H3 H4 H2 H1 O2 H10 H9 H8 H6 H5 H7<br>

## Aлгоритм BFS (Breadth-first search):
За результатами виконання алгоритму BFS ми бачимо, що він працює очікувано та коректно. Тобто спочатку алгоритм бере вершини які з'єднані з нашою "початковою" вершиною ребрами - "найближчі" вершини, а потім алгоритм переходить до вершин пов'язаних ребрами вже з "найближчими" вершинами, і так далі поки не пройде всі вершини.

## Aлгоритм DFS (Depth-first search):
За результатами виконання алгоритму DFS ми бачимо, що він працює очікувано та коректно. Тобто спочатку алгоритм йде по вершинам до самої глибини, поки є зв'язок ребрами між вершинами, коли таких вершин більше нема, алгоритм починає з початку шукати які вершини він ще не пройшов.

# Завдання 3:

Найкоротші шляхи від `C1`: {'C1': 0, 'H1': 1, 'N1': 3, 'N2': 3, 'C2': 6, 'H2': 7, 'H3': 7, 'H4': 7, 'C3': 6, 'C4': 10, 'C5': 6, 'O1': 12, 'N3': 9, 'C6': 12, 'C7': 12, 'H5': 13, 'H6': 13, 'H7': 13, 'O2': 14, 'N4': 13, 'C8': 16, 'H8': 17, 'H9': 17, 'H10': 17}<br>
Найкоротші шляхи від `H1`: {'C1': 1, 'H1': 0, 'N1': 4, 'N2': 4, 'C2': 7, 'H2': 8, 'H3': 8, 'H4': 8, 'C3': 7, 'C4': 11, 'C5': 7, 'O1': 13, 'N3': 10, 'C6': 13, 'C7': 13, 'H5': 14, 'H6': 14, 'H7': 14, 'O2': 15, 'N4': 14, 'C8': 17, 'H8': 18, 'H9': 18, 'H10': 18}<br>
Найкоротші шляхи від `N1`: {'C1': 3, 'H1': 4, 'N1': 0, 'N2': 6, 'C2': 9, 'H2': 10, 'H3': 10, 'H4': 10, 'C3': 7, 'C4': 11, 'C5': 3, 'O1': 13, 'N3': 6, 'C6': 9, 'C7': 9, 'H5': 10, 'H6': 10, 'H7': 10, 'O2': 11, 'N4': 12, 'C8': 15, 'H8': 16, 'H9': 16, 'H10': 16}<br>
Найкоротші шляхи від `N2`: {'C1': 3, 'H1': 4, 'N1': 6, 'N2': 0, 'C2': 3, 'H2': 4, 'H3': 4, 'H4': 4, 'C3': 3, 'C4': 7, 'C5': 7, 'O1': 9, 'N3': 10, 'C6': 13, 'C7': 13, 'H5': 14, 'H6': 14, 'H7': 14, 'O2': 15, 'N4': 10, 'C8': 13, 'H8': 14, 'H9': 14, 'H10': 14}<br>
Найкоротші шляхи від `C2`: {'C1': 6, 'H1': 7, 'N1': 9, 'N2': 3, 'C2': 0, 'H2': 1, 'H3': 1, 'H4': 1, 'C3': 6, 'C4': 10, 'C5': 10, 'O1': 12, 'N3': 13, 'C6': 16, 'C7': 16, 'H5': 17, 'H6': 17, 'H7': 17, 'O2': 18, 'N4': 13, 'C8': 16, 'H8': 17, 'H9': 17, 'H10': 17}<br>
Найкоротші шляхи від `H2`: {'C1': 7, 'H1': 8, 'N1': 10, 'N2': 4, 'C2': 1, 'H2': 0, 'H3': 2, 'H4': 2, 'C3': 7, 'C4': 11, 'C5': 11, 'O1': 13, 'N3': 14, 'C6': 17, 'C7': 17, 'H5': 18, 'H6': 18, 'H7': 18, 'O2': 19, 'N4': 14, 'C8': 17, 'H8': 18, 'H9': 18, 'H10': 18}<br>
Найкоротші шляхи від `H3`: {'C1': 7, 'H1': 8, 'N1': 10, 'N2': 4, 'C2': 1, 'H2': 2, 'H3': 0, 'H4': 2, 'C3': 7, 'C4': 11, 'C5': 11, 'O1': 13, 'N3': 14, 'C6': 17, 'C7': 17, 'H5': 18, 'H6': 18, 'H7': 18, 'O2': 19, 'N4': 14, 'C8': 17, 'H8': 18, 'H9': 18, 'H10': 18}<br>
Найкоротші шляхи від `H4`: {'C1': 7, 'H1': 8, 'N1': 10, 'N2': 4, 'C2': 1, 'H2': 2, 'H3': 2, 'H4': 0, 'C3': 7, 'C4': 11, 'C5': 11, 'O1': 13, 'N3': 14, 'C6': 17, 'C7': 17, 'H5': 18, 'H6': 18, 'H7': 18, 'O2': 19, 'N4': 14, 'C8': 17, 'H8': 18, 'H9': 18, 'H10': 18}<br>
Найкоротші шляхи від `C3`: {'C1': 6, 'H1': 7, 'N1': 7, 'N2': 3, 'C2': 6, 'H2': 7, 'H3': 7, 'H4': 7, 'C3': 0, 'C4': 4, 'C5': 4, 'O1': 6, 'N3': 7, 'C6': 10, 'C7': 10, 'H5': 11, 'H6': 11, 'H7': 11, 'O2': 12, 'N4': 7, 'C8': 10, 'H8': 11, 'H9': 11, 'H10': 11}<br>
Найкоротші шляхи від `C4`: {'C1': 10, 'H1': 11, 'N1': 11, 'N2': 7, 'C2': 10, 'H2': 11, 'H3': 11, 'H4': 11, 'C3': 4, 'C4': 0, 'C5': 8, 'O1': 2, 'N3': 9, 'C6': 12, 'C7': 6, 'H5': 13, 'H6': 13, 'H7': 13, 'O2': 8, 'N4': 3, 'C8': 6, 'H8': 7, 'H9': 7, 'H10': 7}<br>
Найкоротші шляхи від `C5`: {'C1': 6, 'H1': 7, 'N1': 3, 'N2': 7, 'C2': 10, 'H2': 11, 'H3': 11, 'H4': 11, 'C3': 4, 'C4': 8, 'C5': 0, 'O1': 10, 'N3': 3, 'C6': 6, 'C7': 6, 'H5': 7, 'H6': 7, 'H7': 7, 'O2': 8, 'N4': 9, 'C8': 12, 'H8': 13, 'H9': 13, 'H10': 13}<br>
Найкоротші шляхи від `O1`: {'C1': 12, 'H1': 13, 'N1': 13, 'N2': 9, 'C2': 12, 'H2': 13, 'H3': 13, 'H4': 13, 'C3': 6, 'C4': 2, 'C5': 10, 'O1': 0, 'N3': 11, 'C6': 14, 'C7': 8, 'H5': 15, 'H6': 15, 'H7': 15, 'O2': 10, 'N4': 5, 'C8': 8, 'H8': 9, 'H9': 9, 'H10': 9}<br>
Найкоротші шляхи від `N3`: {'C1': 9, 'H1': 10, 'N1': 6, 'N2': 10, 'C2': 13, 'H2': 14, 'H3': 14, 'H4': 14, 'C3': 7, 'C4': 9, 'C5': 3, 'O1': 11, 'N3': 0, 'C6': 3, 'C7': 3, 'H5': 4, 'H6': 4, 'H7': 4, 'O2': 5, 'N4': 6, 'C8': 9, 'H8': 10, 'H9': 10, 'H10': 10}<br>
Найкоротші шляхи від `C6`: {'C1': 12, 'H1': 13, 'N1': 9, 'N2': 13, 'C2': 16, 'H2': 17, 'H3': 17, 'H4': 17, 'C3': 10, 'C4': 12, 'C5': 6, 'O1': 14, 'N3': 3, 'C6': 0, 'C7': 6, 'H5': 1, 'H6': 1, 'H7': 1, 'O2': 8, 'N4': 9, 'C8': 12, 'H8': 13, 'H9': 13, 'H10': 13}<br>
Найкоротші шляхи від `C7`: {'C1': 12, 'H1': 13, 'N1': 9, 'N2': 13, 'C2': 16, 'H2': 17, 'H3': 17, 'H4': 17, 'C3': 10, 'C4': 6, 'C5': 6, 'O1': 8, 'N3': 3, 'C6': 6, 'C7': 0, 'H5': 7, 'H6': 7, 'H7': 7, 'O2': 2, 'N4': 3, 'C8': 6, 'H8': 7, 'H9': 7, 'H10': 7}<br>
Найкоротші шляхи від `H5`: {'C1': 13, 'H1': 14, 'N1': 10, 'N2': 14, 'C2': 17, 'H2': 18, 'H3': 18, 'H4': 18, 'C3': 11, 'C4': 13, 'C5': 7, 'O1': 15, 'N3': 4, 'C6': 1, 'C7': 7, 'H5': 0, 'H6': 2, 'H7': 2, 'O2': 9, 'N4': 10, 'C8': 13, 'H8': 14, 'H9': 14, 'H10': 14}<br>
Найкоротші шляхи від `H6`: {'C1': 13, 'H1': 14, 'N1': 10, 'N2': 14, 'C2': 17, 'H2': 18, 'H3': 18, 'H4': 18, 'C3': 11, 'C4': 13, 'C5': 7, 'O1': 15, 'N3': 4, 'C6': 1, 'C7': 7, 'H5': 2, 'H6': 0, 'H7': 2, 'O2': 9, 'N4': 10, 'C8': 13, 'H8': 14, 'H9': 14, 'H10': 14}<br>
Найкоротші шляхи від `H7`: {'C1': 13, 'H1': 14, 'N1': 10, 'N2': 14, 'C2': 17, 'H2': 18, 'H3': 18, 'H4': 18, 'C3': 11, 'C4': 13, 'C5': 7, 'O1': 15, 'N3': 4, 'C6': 1, 'C7': 7, 'H5': 2, 'H6': 2, 'H7': 0, 'O2': 9, 'N4': 10, 'C8': 13, 'H8': 14, 'H9': 14, 'H10': 14}<br>
Найкоротші шляхи від `O2`: {'C1': 14, 'H1': 15, 'N1': 11, 'N2': 15, 'C2': 18, 'H2': 19, 'H3': 19, 'H4': 19, 'C3': 12, 'C4': 8, 'C5': 8, 'O1': 10, 'N3': 5, 'C6': 8, 'C7': 2, 'H5': 9, 'H6': 9, 'H7': 9, 'O2': 0, 'N4': 5, 'C8': 8, 'H8': 9, 'H9': 9, 'H10': 9}<br>
Найкоротші шляхи від `N4`: {'C1': 13, 'H1': 14, 'N1': 12, 'N2': 10, 'C2': 13, 'H2': 14, 'H3': 14, 'H4': 14, 'C3': 7, 'C4': 3, 'C5': 9, 'O1': 5, 'N3': 6, 'C6': 9, 'C7': 3, 'H5': 10, 'H6': 10, 'H7': 10, 'O2': 5, 'N4': 0, 'C8': 3, 'H8': 4, 'H9': 4, 'H10': 4}<br>
Найкоротші шляхи від `C8`: {'C1': 16, 'H1': 17, 'N1': 15, 'N2': 13, 'C2': 16, 'H2': 17, 'H3': 17, 'H4': 17, 'C3': 10, 'C4': 6, 'C5': 12, 'O1': 8, 'N3': 9, 'C6': 12, 'C7': 6, 'H5': 13, 'H6': 13, 'H7': 13, 'O2': 8, 'N4': 3, 'C8': 0, 'H8': 1, 'H9': 1, 'H10': 1}<br>
Найкоротші шляхи від `H8`: {'C1': 17, 'H1': 18, 'N1': 16, 'N2': 14, 'C2': 17, 'H2': 18, 'H3': 18, 'H4': 18, 'C3': 11, 'C4': 7, 'C5': 13, 'O1': 9, 'N3': 10, 'C6': 13, 'C7': 7, 'H5': 14, 'H6': 14, 'H7': 14, 'O2': 9, 'N4': 4, 'C8': 1, 'H8': 0, 'H9': 2, 'H10': 2}<br>
Найкоротші шляхи від `H9`: {'C1': 17, 'H1': 18, 'N1': 16, 'N2': 14, 'C2': 17, 'H2': 18, 'H3': 18, 'H4': 18, 'C3': 11, 'C4': 7, 'C5': 13, 'O1': 9, 'N3': 10, 'C6': 13, 'C7': 7, 'H5': 14, 'H6': 14, 'H7': 14, 'O2': 9, 'N4': 4, 'C8': 1, 'H8': 2, 'H9': 0, 'H10': 2}<br>
Найкоротші шляхи від `H10`: {'C1': 17, 'H1': 18, 'N1': 16, 'N2': 14, 'C2': 17, 'H2': 18, 'H3': 18, 'H4': 18, 'C3': 11, 'C4': 7, 'C5': 13, 'O1': 9, 'N3': 10, 'C6': 13, 'C7': 7, 'H5': 14, 'H6': 14, 'H7': 14, 'O2': 9, 'N4': 4, 'C8': 1, 'H8': 2, 'H9': 2, 'H10': 0}<br>
