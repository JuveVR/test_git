# For this task send link to Pull Request
#
# Create 2 classes
#
# Every class should contain:
#
#  - at least two instance fields
#
#  - at least one class field
#
#  - at least two instance methods
#
# At least one class should contain
#
#  - one class method
#
#  - one static method
#
# Add docstrings to every method.
#
# Instance methods should NOT be just get/set some field. Imagine something more interesting (but you could add them if needed).
#
# Write code that creates several instances and shows their work

class Cocktail:
    available_alcohols = ["vodka", "rum", "gin", "whiskey", "tequila"]
    alcohol_tax = 0.1

    def __init__(self, name, price: float, ingredients: list):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def is_alcoholic(self):
        """Determine if a cocktail is alcoholic based on its ingredients."""
        return any(alcohol in self.ingredients for alcohol in Cocktail.available_alcohols)

    def list_ingredients(self):
        """List the ingredients of the cocktail."""
        return f"{self.name} contains: " + ", ".join(self.ingredients)

    def calculate_price_with_tax(self):
        """Calculates total price of a cocktail including taxes"""
        total_price = self.price + (self.price * Cocktail.alcohol_tax)
        return round(total_price, 2)

    @staticmethod
    def count_available_alcohol():
        """Calculates how many kinds of available alcohols are already in stock"""
        return len(Cocktail.available_alcohols)

    @classmethod
    def add_new_available_alcohol(cls, new_alcohol: str):
        """Adds new alcohol to the list of available alcohols in stock"""
        if new_alcohol not in cls.available_alcohols:
            print(f"Adding new alcohol to the storage: {new_alcohol}")
            cls.available_alcohols.append(new_alcohol)
            print(f"Now we have such list of available alcohols: {cls.available_alcohols}")
        else:
            print(f"{new_alcohol} is already in stock")


class Food:
    happy_hours_discount = 0.2

    def __init__(self, name: str, calories: int, price: float):
        """Initialize a new food item with a name and calorie count."""
        self.name = name
        self.price = price
        self.calories = calories

    def calorie_info(self):
        """Provide calorie information about the food item."""
        return f"{self.name} contains {self.calories} calories."

    def make_discount(self):
        """Calculates total price of a food item excluding happy hour discount"""
        print(f"The regular price for {self.name} is: {self.price}")
        happy_price = round((self.price - (self.price * Food.happy_hours_discount)), 2)
        print(f"But you are lucky, your happy ours price is: {happy_price}")


# Create instances of Cocktail
mohito = Cocktail("Mohito", 9.99, ["sugar", "sprite", "mint", "lime"])
cuba_libre = Cocktail("Cuba Libre", 8.50, ["rum", "cola", "lemon"])

print(cuba_libre.is_alcoholic())
print(mohito.is_alcoholic())

print(mohito.list_ingredients())

print(mohito.calculate_price_with_tax())

print(Cocktail.count_available_alcohol())

Cocktail.add_new_available_alcohol("samogon")
Cocktail.add_new_available_alcohol("rum")

print(Cocktail.count_available_alcohol())


# Create instances of Food
meat_dumplings = Food("Varenyky", 450, 59.99)
cabbage_rolls = Food("Golubci", 345, 65.00)

print(meat_dumplings.calorie_info())

cabbage_rolls.make_discount()

