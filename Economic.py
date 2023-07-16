from dataclasses import dataclass


@dataclass
class EconomicData:
    date: int
    population: int
    pop_growth: float
    sold: int
    ready_cons: int
    cons: int
    cons_per: float
    outfit: int
    outfit_cost: int
    money: int
    min_money: int
    money_cost: float
    more_money: int
    fuel: int
    fuel_factory: int
    fuel_produce: int
    fuel_cost: float
    products: int
    products_factory: int
    products_produce: int
    products_cost: float

    def population_f(self):
        if self.cons_per >= (self.sold + self.cons + self.ready_cons) / self.population:
            self.population = int((self.population * self.pop_growth) - (self.population * (self.cons_per -
                                                                                            (
                                                                                                    self.sold + self.cons + self.ready_cons) / self.population)))
        else:
            self.population = int(self.population * self.pop_growth)
        return self.population

    def pop_growth_f(self):
        self.pop_growth = 1.1 + self.money_cost * 0.01 - int(
            (self.fuel_cost + self.products_cost) * 0.01 * self.money_cost)
        return self.pop_growth

    def money_f(self):
        self.money = int(self.money + (self.population * ((1 / self.money_cost) / 20)) - (
                self.sold + self.cons + self.ready_cons) * (4 / self.money_cost))
        return self.money

    def min_money_f(self):
        self.min_money = int((self.population * 5 / self.money_cost) + (10 / self.money_cost) * (
                self.sold + self.cons + self.ready_cons))
        return self.min_money

    def money_cost_f(self):
        self.money_cost = self.min_money / (self.money + self.more_money)
        return self.money_cost

    def fuel_f(self):
        self.fuel += self.fuel_produce
        return self.fuel

    def fuel_produce_f(self):
        self.fuel_produce = self.fuel_factory * 10000 - 4 * (self.sold + self.cons + self.ready_cons) - self.population
        return self.fuel_produce

    def fuel_cost_f(self):
        if self.fuel_produce < 0:
            if self.fuel / self.fuel_produce >= 60:
                self.fuel_cost = 5 / self.money_cost
            else:
                self.fuel_cost = 6 / self.money_cost
        elif self.fuel_produce == 0:
            self.fuel_cost = 4 / self.money_cost
        else:
            if self.fuel_produce / (4 * (self.sold + self.cons + self.ready_cons) + self.population) >= 2:
                self.fuel_cost = 2 / self.money_cost
            else:
                self.fuel_cost = 3 / self.money_cost
        return self.fuel_cost

    def products_f(self):
        self.products += self.products_produce
        return self.products

    def products_produce_f(self):
        self.products_produce = self.products_factory * 10000 - (self.sold + self.cons + self.ready_cons) - \
                                (2 * self.population)
        return self.products_produce

    def products_cost_f(self):
        if self.products_produce < 0:
            if self.products / self.products_produce >= 60:
                self.products_cost = 3 / self.money_cost
            else:
                self.products_cost = 4 / self.money_cost
        elif self.products_produce == 0:
            self.products_cost = 2 / self.money_cost
        else:
            if self.products_produce / ((self.sold + self.cons + self.ready_cons) + 2 * self.population) >= 2:
                self.products_cost = 2 / self.money_cost
            else:
                self.products_cost = 1 / self.money_cost
        return self.products_cost


date, population, pop_growth, sold, ready_cons, cons, cons_per, outfit, outfit_cost, money, min_money, money_cost, \
    more_money, fuel, fuel_factory, fuel_produce, fuel_cost, products, products_factory, products_produce, \
    products_cost = 1, 100000, 1.1, 100, 5, 20, 0.01, 8000, 5, 10000, 501250, 1, 0, 10000, 10, 100000, 3, 150000, \
    20, 200000, 3
td = EconomicData(data, population, pop_growth, sold, ready_cons, cons, cons_per, outfit, outfit_cost, money, min_money,
                  money_cost, more_money, fuel, fuel_factory, fuel_produce, fuel_cost, products, products_factory,
                  products_produce, products_cost)
