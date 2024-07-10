w = float(input("Ваш вес(кг.): "))
h = float(input("Ваш рост(м.): "))

bmi = round(w / h ** 2, 2)

print(f"BMI : {bmi}")