class Car:

    def __init__(self, model: str, VIN: int, numbers: str):
        self.model = model
        if self.__is_valid_vin(VIN):
            self.__vin = VIN
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
        print(f'Модель "{model}" успешно создан!')

    def __is_valid_vin(self, vin_number):
        if not type(vin_number) == int:
            raise IncorrectVinNumber(message='ОШИБКА: Некорректный тип VIN, должен быть int!')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber(message='ОШИБКА: Неверный диапазон для VIN номера!')
        return True

    def __is_valid_numbers(self, numbers):
        if not type(numbers) == str:
            raise IncorrectCarNumbers(message='ОШИБКА: Некорректный тип номера, должен быть str!')
        if not len(numbers) == 6:
            raise IncorrectCarNumbers(message='ОШИБКА: Неверная длина номера, должна быть 6!')
        return True
class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message



class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car(IncorrectVinNumber):
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        else:
            self.__vin = None

        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
        else:
            self.__numbers = None

    def __is_valid_vin(self, vin):
        if isinstance(vin, int):
            if 1000000 <= vin <= 9999999:
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
            else:
                return str
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')