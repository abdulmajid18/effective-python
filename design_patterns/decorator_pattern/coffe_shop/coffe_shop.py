# Step 1: Define the Component Interface
class Coffee:
    def cost(self):
        pass

    def description(self):
        pass


# Step 2: Define the ConcreteComponent
class SimpleCoffee(Coffee):
    def cost(self):
        return 5  # Base cost of simple coffee

    def description(self):
        return "Simple Coffee"


# Step 3: Define the Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


# Step 4: Define ConcreteDecorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2  # Adding cost of milk

    def description(self):
        return self._coffee.description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # Adding cost of sugar

    def description(self):
        return self._coffee.description() + ", Sugar"


class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3  # Adding cost of whipped cream

    def description(self):
        return self._coffee.description() + ", Whipped Cream"


# Step 5: Client Code
if __name__ == "__main__":
    # Create a simple coffee
    coffee = SimpleCoffee()
    print(f"Cost: ${coffee.cost()}, Description: {coffee.description()}")

    # Add milk to the coffee
    coffee_with_milk = MilkDecorator(coffee)
    print(f"Cost: ${coffee_with_milk.cost()}, Description: {coffee_with_milk.description()}")

    # Add sugar to the coffee with milk
    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print(f"Cost: ${coffee_with_milk_and_sugar.cost()}, Description: {coffee_with_milk_and_sugar.description()}")

    # Add whipped cream to the coffee with milk and sugar
    coffee_with_all = WhippedCreamDecorator(coffee_with_milk_and_sugar)
    print(f"Cost: ${coffee_with_all.cost()}, Description: {coffee_with_all.description()}")