from dataclasses import dataclass


class Thing:
    def __init__(self, population, population_growth, soldiers, conscript, conscript_percentage, ready_conscript,
                 outfit, outfit_cost, fuel, fuel_produce, fuel_cost, money, money_cost, more_money, products,
                 products_produce, products_cost):
        self.population = population
        self.ready_conscript = ready_conscript
        self.population_growth = population_growth
        self.products_produce = products_produce
        self.soldiers = soldiers
        self.conscript = conscript
        self.conscript_percentage = conscript_percentage
        self.outfit = outfit
        self.outfit_cost = outfit_cost
        self.fuel = fuel
        self.fuel_produce = fuel_produce
        self.fuel_cost = fuel_cost
        self.money = money
        self.more_money = more_money
        self.products = products
        self.products_produce = products_produce
        self.products_cost = products_cost
        self.money_cost = money_cost

    def people(self):
        p = self.population
        self.population *= self.population_growth
        self.population -= 1 * (self.conscript_percentage - (
                (self.soldiers + self.conscript + self.ready_conscript) / self.population))
        self.money_cost = ((self.population * 10 / self.money_cost) / (p * 10 / self.money_cost)) - (
                self.more_money / (self.more_money + self.money))
        return format(self.population, '.6g'), format(self.money_cost, '6g')

    def more_people(self):
        self.population_growth = 1.1 + self.money_cost * 0.01 - (self.fuel_cost + self.products_cost) * 0.01

    def reg_army(self):
        if self.outfit > self.ready_conscript:
            self.outfit += (self.outfit - self.ready_conscript) - self.outfit - self.ready_conscript
        else:
            self.outfit += (self.outfit - self.ready_conscript)

    def getting_ready(self):
        self.conscript += self.population * (self.conscript_percentage - (
                (self.soldiers + self.ready_conscript + self.conscript) / self.population))

    def outfit_price(self):
        self.outfit_cost /= self.money_cost

    def gas(self):
        self.fuel += self.fuel_produce

    def gas_produce(self):
        self.fuel_produce = self.fuel_cost - 2 * (
                self.soldiers + self.conscript + self.ready_conscript) - 1 * self.population

    def gas_price(self):
        if self.fuel_produce < 0:
            if self.fuel / self.fuel_produce >= 60:
                self.fuel_cost = 5 / self.money_cost
            else:
                self.fuel_cost = 6 / self.money_cost
        elif self.products_produce == 0:
            self.fuel_cost = 4 / self.money_cost
        else:
            if (self.fuel_produce / (
                    2 * (self.soldiers + self.conscript + self.ready_conscript) + 1 * self.population)) >= 2:
                self.fuel_cost = 2 / self.money_cost
            else:
                self.fuel_cost = 3 / self.money_cost

    def your_money(self):
        self.money = self.money + (self.population * (2 / self.money_cost)) - (
                (self.soldiers + self.conscript + self.ready_conscript) * (4 / self.money_cost))

    def eat(self):
        self.products -= self.products_produce

    def eat_produce(self):
        self.products_produce -= 1 * (self.soldiers + self.conscript + self.ready_conscript) - 2 * self.population

    def eat_price(self):
        if self.products_produce < 0:
            if self.products / self.products_produce >= 60:
                self.products_cost = 3 / self.money_cost
            else:
                self.products_cost = 4 / self.money_cost
        elif self.products_produce == 0:
            self.products_cost = 2 / self.money_cost
        else:
            if (self.fuel_produce / (
                    (self.soldiers + self.conscript + self.ready_conscript) + 2 * self.population)) >= 2:
                self.products_cost = 1 / self.money_cost
            else:
                self.products_cost = 2 / self.money_cost


# @dataclass
# class ThingData:
#     population: int  # население страны (мирное)
#     population_growth: float  # скорость роста населения(в процентах)
#     soldiers: int  # количество регулярных соладат страны
#     conscript: int  # количество призывников, которые в данный момент проходят службу
#     conscript_percentage: float  # процент призывников от общего насления
#     ready_conscript: int  # готовые призывники
#     outfit: int  # количество снаряжения для военных на складах
#     outfit_cost: int  # стоимость покупки снаряжения
#     fuel: int  # количество топлива на складах
#     fuel_produce: int  # Производство топлива в день
#     fuel_cost: int  # цена топлива
#     money: int  # количество денег у игрока
#     money_cost: int  # стоимость денег
#     more_money: int  # количество денег напечатанных игроком за раз
#     products: int  # количество продуктов на складах
#     products_produce: int  # производство продуктов
#     products_cost: int  # цена продуктов


# td = ThingData('Топор', 5, 8000)
# t = Thing('Питончик', 20, 10000)
# print(td)
# print(t)
population = 10000
pop_growth = 1.1
sold = 20
cons = 10
cons_per = 0.05
ready_cons = 5
outfit = 8000
outfit_cost = 5
fuel = 100000
fuel_produce = 50000
fuel_cost = 10
money = 1000000
money_cost = 1
more_money = 0
products = 10000
products_poduce = 100000
products_cost = 1
economy_status = {'population': 10000, 'pop_growth': 1.1, 'sold': 20, 'cons': 10, 'cons_per': 0.05, 'ready_cons': 5,
                  'outfit': 8000, 'outfit_cost': 5,
                  'fuel': 100000, 'fuel_produce': 50000, 'fuel_cost': 10, 'money': 1000000, 'money_cost': 1,
                  'more_money': 0, 'products': 10000, 'products_poduce': 100000, 'products_cost': 1}
while True:
    td = Thing(population, pop_growth, sold, cons, cons_per, ready_cons, outfit, outfit_cost, fuel, fuel_produce,
               fuel_cost, money, money_cost, more_money, products, products_poduce, products_cost)
    population, money_cost = td.people()
    pop_growth = td.more_people()
    sold = td.reg_army()
    cons = td.getting_ready()
    cons_per = 0
    print(td.people())
