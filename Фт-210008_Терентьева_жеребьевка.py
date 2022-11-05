import random
import logging
while True:
    logging.basicConfig(filename="ex.log", level=logging.INFO)
    logging.info("Programm started")
    try:
        n = int(input("Сколько бочонков необходимо вытянуть из мешка?"))
        logging.info(f"Users nuber is {n}")

