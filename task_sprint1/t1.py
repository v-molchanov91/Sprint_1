def get_days_in_month(m):
    month_days = {
        "январь": 31,
        "февраль": 28,
        "март": 31,
        "апрель": 30,
        "май": 31,
        "июнь": 30,
        "июль": 31,
        "август": 31,
        "сентябрь": 30,
        "октябрь": 31,
        "ноябрь": 30,
        "декабрь": 31,
    }

    if not isinstance(m, str):
        return "неверный формат"

    m = m.strip().lower()
    return month_days.get(m, "неверный месяц")


for i in range(5):
    user_input = input("Введите месяц (или 'Отмена' для выхода): ")
    if user_input.strip().lower() == "отмена":
        print("Ввод отменён.")
        break
    print(get_days_in_month(user_input))
