class Pizza:
    def __init__(self):
        self.ingredients = []

    def get_ingredients(self):
        print(f"Pizza ingredients: {", ".join(self.ingredients)}")

class PizzaBuilder:

    def __init__(self):
        self.pizza = Pizza()

    def add_size(self):
        self.pizza.ingredients.append("30sm")

    def add_cheese(self):
        self.pizza.ingredients.append("cheese")

    def add_pepperoni(self):
        self.pizza.ingredients.append("pepperoni")

    def add_mushrooms(self):
        self.pizza.ingredients.append("mushrooms")

    def add_onions(self):
        self.pizza.ingredients.append("onions")

    def add_bacon(self):
        self.pizza.ingredients.append("bacon")

class PizzaDirector:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> PizzaBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: PizzaBuilder) -> None:
        self._builder = builder

    def make_pizza(self):
        self.builder.add_size()
        self.builder.add_bacon()
        self.builder.add_cheese()
        self.builder.add_onions()
        self.builder.add_mushrooms()
        self.builder.add_pepperoni()

pizza_builder = PizzaBuilder()
director = PizzaDirector()

director.builder = pizza_builder

director.make_pizza()

pizza_builder.pizza.get_ingredients()
    
