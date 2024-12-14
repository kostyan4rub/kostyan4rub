import threading
import time
import random
from threading import Thread, Lock


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        counter = 0
        while counter <= 100:
            bk = random.randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += bk
                print(f'Пополнение: {bk}. Баланс: {self.balance}\n')
            finally:
                self.lock.release()
            time.sleep(0.01)
            counter += 1

    def take(self):
        counter = 0
        while counter <= 100:
            bk = random.randint(50, 500)
            print(f'Запрос на {bk}')
            self.lock.acquire()
            try:
                if bk <= self.balance:
                    self.balance -= bk
                    print(f'Снятие: {bk}. Баланс: {self.balance}\n')
                else:
                    print('Запрос отклонён, недостаточно средств')
            finally:
                self.lock.release()
            time.sleep(0.001)
            counter += 1


bk = Bank() 

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')




