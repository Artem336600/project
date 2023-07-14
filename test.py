class Economy:
    def __init__(self, money, money_cost, goods, extra_money):
        self.money = money
        self.money_cost = money_cost
        self.goods = goods
        self.extra_money = extra_money

    def more_money(self, n):
        self.money_cost = (self.money / (self.money + n))
        return f'цена денег теперь {self.money_cost} от изначальной стоимости'

    def eat(self, n):
        self.goods = (self.goods - n)
        return f'На складах осталось {self.goods} товаров'

    def factories(self, n):
        self.goods = (self.goods + n * 10)
        return f'Фабрики поработали и на складах осталось {self.goods} товаров'


def main():
    money, money_cost, factory, extra_money = 1000, 1, 2, 0
    cd = Economy(money, money_cost, factory, extra_money)
    for i in range(20):
        extra_money = int(input('Сколько Денег вы хотите напечатать?'))
        print(cd.more_money(extra_money))
        print(cd.eat(5))
        print(cd.factories(factory))


main()
