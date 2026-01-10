class Pizza:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __str__(self):
        return f'Pizza with: {", ".join(self.ingredients)}'

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.add_ingredient('cheese')
        return self

    def add_pepperoni(self):
        self.pizza.add_ingredient('pepperoni')
        return self

    def add_veggies(self):
        self.pizza.add_ingredient('veggies')
        return self

    def build(self):
        return self.pizza

if __name__ == '__main__':
    pizza = PizzaBuilder().add_cheese().add_pepperoni().build()
    print(pizza)
