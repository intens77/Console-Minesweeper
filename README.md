# Console-Minesweeper
## Console version of the Minesweeper game
### Запуск
Игра запускается из директории с файлами игры с помощью команды python3 main.py.
### Описание игрового процесса
Формат для ввода параметров игры:  
width height mines_count. 3 игровых параметра вводятся в одну строчку через пробел. Пример: 6 7 8 - поле размером 6X7 с 8 минами.  
Формат для ввода игровой тройки:   
x y action. 3 параметра команды вводятся в одну строчку через пробел. Пример: 1 3 flag - поставить флаг на клетку, находящуюся в 1 столбце и 3 строке; 2 5 open - открыть клетку, находящуюся во 2 столбце и 5 строке. Action имеет 2 возможных значения: flag - поставить флаг, open - открыть клетку. Также помимо ввода игровой тройки возможно использование команды restart, которая запускает новую игру.  
### Дополнительная информация
В игре работает функция сохранения игрового поля в запароленный архив. Пароль от архива:  
26092021

