# maze_generator_2.2.1_passage_algorithm

При тестировании различных алгоритмов прохождения и поиска кратчайшего пути возникает весьма существенная проблема – Создание поля для тренировки. 
При большом количестве экспериментов, человеку трудно создать различные макеты и ситуации, которые помогут отладить и найти недостатки в алгоритмах прохождения. 
Решением стало создание программного обеспечения по генерации Лабиринтов, написанное на языке программирования Python 

Программа способна строить многосвязные лабиринты, содержащие отдельные тупиковые маршруты и отдельно стоящие стенки.
Алгоритм, применяемый в программе по генерации лабиринтов основан на достаточно простом методе, создающий идеальный и разряженный лабиринт.

Первым шагом пользователь на поле ставит точки старта и финиша, нажатием левой кнопки мыши
1.	Программа начинает построение маршрута от точки старта к выходу
2.	В зависимости от сложности лабиринта, указанной в поле программы level программа начинает усложнять данный маршрут перекрестками и поворотами. При этом число поворотов и перекрестков равно указанной сложности.
3.	В результате в графическом интерфейсе появляется лабиринт, а в консоли информация о нем, включающая в себя общую длину маршрутов и времени генерации

Реализована гибкая настройка включающая размеры поля в пикселях и сложность, характеризующая количество развилок и тупиков на маршруте от старта к финишу. 
Так же от сложности зависит о общая протяженность лабиринта. 

