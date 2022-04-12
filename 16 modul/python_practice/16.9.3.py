class Clients:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    def show_me_your_money_petrov(self):
        return f"{self.name}, Ваш баланс {self.wallet} руб."

client_1 = Clients("Иван Петров", 50)
print(client_1.show_me_your_money_petrov())