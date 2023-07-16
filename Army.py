from dataclasses import dataclass


@dataclass
class Armydata:
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

    def sold_f(self):
        if self.date % 3 == 0:
            if self.outfit >= self.ready_cons:
                self.outfit = self.outfit - self.ready_cons
                self.sold = self.sold + self.ready_cons
                self.ready_cons = 0
            else:
                self.sold = self.outfit
                self.ready_cons = self.ready_cons - self.outfit
                self.outfit = 0
        return self.sold, self.ready_cons, self.outfit

    def ready_cons_f(self):
        if self.date % 7 == 0:
            self.ready_cons = self.ready_cons + self.cons
        return self.ready_cons

    def cons_f(self):
        if self.date % 10 == 0:
            if ((self.cons + self.ready_cons + self.sold) / self.population) < self.cons_per:
                self.cons += self.population * (self.cons_per - (self.sold + self.ready_cons + self.cons)
                                                / self.population)
