first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]

second_result = [(x1,x2) for x2 in second_strings for x1 in first_strings if len(x2) == len(x1)]

third_result = {x: len(x) for x in second_strings + first_strings if len(x) % 2 == 0}


# Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)
