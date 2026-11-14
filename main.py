print("Добро пожаловать в MiniMarketSimulator!")
import tkinter as tk
from tkinter import simpledialog, messagebox
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
    "Бананы (500 г)": {
        "purchase_price": 55,
        "sell_price": 80,
        "competitor_price": 80,
        "stock": 0
    },
    "Апельсины (500 г)": {
        "purchase_price": 75,
        "sell_price": 110,
        "competitor_price": 110,
        "stock": 0
    },
    "Яблоки (500 г)": {
        "purchase_price": 50,
        "sell_price": 75,
        "competitor_price": 75,
        "stock": 0
    },
    "Мука (1 кг)": {
        "purchase_price": 60,
        "sell_price": 85,
        "competitor_price": 85,
        "stock": 0
    },
    "Яйца (10 шт.)": {
        "purchase_price": 85,
        "sell_price": 120,
        "competitor_price": 120,
        "stock": 0
    },
    "Творог (180 г)": {
        "purchase_price": 90,
        "sell_price": 125,
        "competitor_price": 125,
        "stock": 0
    },
    "Сыр (200 г)": {
        "purchase_price": 135,
        "sell_price": 195,
        "competitor_price": 195,
        "stock": 0
    },
    "Свинина (500 г)": {
        "purchase_price": 170,
        "sell_price": 235,
        "competitor_price": 235,
        "stock": 0
    },
    "Курица (500 г)": {
        "purchase_price": 105,
        "sell_price": 145,
        "competitor_price": 145,
        "stock": 0
    },
    "Говядина (300 г)": {
        "purchase_price": 190,
        "sell_price": 255,
        "competitor_price": 255,
        "stock": 0
    },
    "Огурцы (500 г)": {
        "purchase_price": 55,
        "sell_price": 80,
        "competitor_price": 80,
        "stock": 0
    },
    "Помидоры (500 г)": {
        "purchase_price": 80,
        "sell_price": 110,
        "competitor_price": 110,
        "stock": 0
    },
    "Картофель (1 кг)": {
        "purchase_price": 40,
        "sell_price": 60,
        "competitor_price": 60,
        "stock": 0
    },
    "Гречка (800 г)": {
        "purchase_price": 65,
        "sell_price": 95,
        "competitor_price": 95,
        "stock": 0
    },
    "Рис (800 г)": {
        "purchase_price": 80,
        "sell_price": 110,
        "competitor_price": 110,
        "stock": 0
    },
    "Пшено (800 г)": {
        "purchase_price": 45,
        "sell_price": 70,
        "competitor_price": 70,
        "stock": 0
    },
    "Вода (1,5 л)": {
        "purchase_price": 30,
        "sell_price": 50,
        "competitor_price": 50,
        "stock": 0
    },
    "Сок (1 л)": {
        "purchase_price": 80,
        "sell_price": 115,
        "competitor_price": 115,
        "stock": 0
    },
    "Печенье (200 г)": {
        "purchase_price": 60,
        "sell_price": 85,
        "competitor_price": 85,
        "stock": 0
    },
    "Шоколад (90 г)": {
        "purchase_price": 75,
        "sell_price": 105,
        "competitor_price": 105,
        "stock": 0
    }
}

print("\nТовары нашего магазина:")

for name, info in products.items():
    print(
        name,
        "- Цена закупки:", info["purchase_price"],
        "руб. | Остаток:", info["stock"]
    )
def buy_product(product_name: str, quantity: int) -> tuple[bool, str]:
    global money
    if product_name not in products:
        return False, "Такого товара нет."
    elif quantity <= 0:
        return False, "Пожалуйста, введите число больше нуля."
    else:
        product = products[product_name]
        total_cost = product["purchase_price"] * quantity
        if total_cost <= money:
            money = money - total_cost
            product["stock"] = product["stock"] + quantity
            print("Покупка успешна!")
            print("Потрачено:", total_cost, "рублей")
            print("Осталось денег:", money, "рублей")
            print("Количество товара на складе:", product["stock"])

            return True, "Покупка успешна!"

        else:
            print("Недостаточно денег для покупки!")

window = tk.Tk()
window.title("MiniMarketSimulator")
window.geometry("1000*600")
def selected_product(product_name: str) -> None:
    selected_label.config(text = "Вы выбрали: "+ product_name)
    quantity = simpledialog.askinteger("Закупка товара", "Сколько упаковок хотите закупить?", minvalue = 1 )
    if quantity is None:
        return
    success, message = buy_product(product_name, quantity)
    if success:
        messagebox.showinfo( "Результат", f"Покупка успешна!/n"
                            f"Товар: {product_name}/n"
                            f"Куплено упаковок: {quantity}"
                            f("Осталось денег: {money}/n"
                            f"Всего упаковок на складе: {products[product_name]["stock"]}"
                            )
    else:
        messagebox.showerror("Ошибка", message)
selected_label = tk.Label(window, text = "Выберите товар для закупки", font = ("Arial, 16") )
selected_label.pack(pady = 20)
buttons_frame = tk.Frame(window)
buttons_frame.pack()
for number, product_name in enumerate(products):
    button = tk.Button(buttons_frame, text = product_name, width = 23, height = 2,
                        command = lambda name = product_name: selected_product(name)) 
    #Каждая кнопка запоминает своё название товара и передаёт его в функцию select_product()
    button.grid(row = number // 4, column = number % 4, padx = 5, pady = 5)
window.mainloop()





        









