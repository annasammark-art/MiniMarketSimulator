print("Добро пожаловать в MiniMarketSimulator!")
while True:
    try:
        money = int(input("Введите стартовый капитал:  "))
        if 1000 <= money <= 10000:
            print("Замечательная сумма!")
            break
        elif 0 > money > 1000:
            print("Боюсь, этого количества не хватит. Минимальная сумма - 1.000 руб.)")
        elif money > 10000:
            print("Столько средств иметь нечестно, выберите сумму до 10.000 руб.")
        else:
            print("Капитал должен быть больше нуля.")
    except ValueError:
        print("Пожалуйста, введите целое число.")
while True:
    try:
        max_days = int(input("Введите количество игровых дней:  "))
        if 1 <= max_days <= 7:
            break
        else:
            print("Можно выбрать от 1 до 7 дней")
    except ValueError:
        print("Пожалуйста, введите целое число.")
day = 1
print("Игра начинается!")
print("День", day, "из", max_days)
print("Деньги магазина:", money, "рублей")


products = {
    "Бананы": {
        "purchase_price": 40,
        "stock": 0
    },
    "Апельсины": {
        "purchase_price": 50,
        "stock": 0
    },
    "Яблоки": {
        "purchase_price": 30,
        "stock": 0
    },
    "Мука": {
        "purchase_price": 35,
        "stock": 0
    },
    "Яйца": {
        "purchase_price": 70,
        "stock": 0
    },
    "Творог": {
        "purchase_price": 60,
        "stock": 0
    },
    "Сыр": {
        "purchase_price": 30,
        "stock": 0
    },
    "Свинина": {
        "purchase_price": 150,
        "stock": 0
    },
    "Курица": {
        "purchase_price": 110,
        "stock": 0
    },
    "Говядина": {
        "purchase_price": 160,
        "stock": 0
    },
    "Огурцы": {
        "purchase_price": 65,
        "stock": 0
    },
    "Помидоры": {
        "purchase_price": 65,
        "stock": 0
    },
    "Картофель": {
        "purchase_price": 33,
        "stock": 0
    },
    "Гречка": {
        "purchase_price": 30,
        "stock": 0
    },
    "Рис": {
        "purchase_price": 30,
        "stock": 0
    },
    "Пшено": {
        "purchase_price": 40,
        "stock": 0
    },
    "Вода": {
        "purchase_price": 65,
        "stock": 0
    },
    "Сок": {
        "purchase_price": 30,
        "stock": 0
    },
     "Печенье": {
        "purchase_price": 65,
        "stock": 0
    },
    "Шоколад": {
        "purchase_price": 30,
        "stock": 0
    },
}

print("\nТовары нашего магазина:")

for name, info in products.items():
    print(
        name,
        "- Цена закупки:", info["purchase_price"],
        "руб. | Остаток:", info["stock"]
    )





