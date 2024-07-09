import random

block_0 = ["Могучие", "Боевые", "Стальные"]
block_1 = input("Введите любой город: ")
block_2 = input("Введите кличку животного: ")

print(f"Название группы: {block_0[random.randint(0,2)]} {block_1}ие {block_2}ы")