import random                                                                                                  #импорт функций
import logging
while True:
    logging.basicConfig(filename="ex.log", level=logging.INFO)                                                       #вызов логгера
    logging.info("Programm started")
    try:
        n = int(input("Сколько бочонков необходимо вытянуть из мешка?")) 
        logging.info(f"Users nuber is {n}")
    except ValueError:                                                                                         #обработка ошибок
        print("Ошибка ввода. Введите число от 1 до N")                                         
        logging.error("ValueError.")
        continue
    if n <= 0:
        print("Ошибка ввода. Введите число от 1 до N")
        logging.error("ValueError.")
        continue
        numbers = []
    while len(numbers) != n:                                                                                           
        number = random.randint(1,n)                                                                             #добавление числа в список и проверка на уникальность
        if number not in numbers:
            print("Вам выпал бочонок под номером: ")
            numbers.append(number)
            print(number)
            logging.info(f"Program printed {number}")
            input('Для того, чтобы вытянуть бочонок нажмите "ENTER"')
             print("Все выпавшие бочонки за игру: ", numbers)                                                     #вывод номеров всех бочонков 
    logging.info(f"All nubers is: {numbers}")
    logging.info("Programms end")

