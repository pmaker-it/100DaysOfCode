print("Калькулятор чаевых приветствует вас!")
total_bill = float(input("Общий счет (руб.): "))
tip_percent = int(input("Сколько оставите на чай? (%) [10, 12, 15]: "))
peoples_count = int(input("Сколько вас всего ?: "))

each_part = round((total_bill + .01 * tip_percent) / peoples_count, 1)

print(f"Каждый должен заплатить {each_part} ")
