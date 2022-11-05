import random
import logging
while True:
    logging.basicConfig(filename="ex.log", level=logging.INFO)
    logging.info("Programm started")
    try:
        n = int(input("Сколько бочонков необходимо вытянуть из мешка?"))
        logging.info(f"Users nuber is {n}")
    except ValueError:
        print("Ошибка ввода. Введите число от 1 до N")
        logging.error("ValueError.")
        continue
    if n <= 0:
        print("Ошибка ввода. Введите число от 1 до N")
        logging.error("ValueError.")
        continue

