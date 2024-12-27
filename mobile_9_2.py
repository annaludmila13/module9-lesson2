# Исходные списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Первый результат: список длин строк из первого списка, если их длина >= 5
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Второй результат: список кортежей, содержащих слова одинаковой длины из обоих списков
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# Третий результат: словарь, где ключами являются строки с четной длиной, а значениями - их длины
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Вывод результатов
print("Первый результат:", first_result)
print("Второй результат:", second_result)
print("Третий результат:", third_result)
