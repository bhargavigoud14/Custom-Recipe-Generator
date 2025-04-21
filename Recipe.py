import random

class RecipeGenerator:
    def __init__(self):
        self.cooking_methods = ["saute", "fry", "boil", "steam", "grill", "bake"]
        self.spices = ["turmeric", "red chili powder", "cumin seeds", "garam masala", "coriander powder", "black pepper"]
        self.herbs = ["coriander leaves", "mint", "basil"]
        self.oils = ["sunflower oil", "mustard oil", "olive oil"]
        self.styles = ["Spicy", "Creamy", "Tandoori", "Desi Delight", "Hearty", "Home-Style", "Zesty", "Street-Style"]

    def welcome_message(self):
        print("👋 Welcome to the AI-Powered Recipe Generator!")
        print("Give me the ingredients you have, and I’ll create a delicious recipe just for you!\n")

    def get_ingredients(self):
        ingredients = input("👉 Enter your ingredients (separated by commas): ")
        return [item.strip().capitalize() for item in ingredients.split(",") if item.strip()]

    def generate_recipe_name(self, ingredients):
        if len(ingredients) >= 2:
            main = f"{ingredients[0]} & {ingredients[1]}"
        else:
            main = ingredients[0]
        return f"{random.choice(self.styles)} {main} Curry"

    def generate_recipe_steps(self, ingredients):
        method = random.choice(self.cooking_methods)
        spice = random.sample(self.spices, 2)
        herb = random.choice(self.herbs)
        oil = random.choice(self.oils)

        steps = f"""
🧑‍🍳 Let's prepare your dish using: {', '.join(ingredients)}!

🔪 Preparation:
- Finely chop the {', '.join(ingredients[:-1])} and keep them aside.
- If you're using {ingredients[-1]}, slice or dice it as needed.
- Heat 2 tablespoons of {oil} in a pan over medium heat.

🍳 Cooking:
1. Add 1 teaspoon of cumin seeds and let them crackle.
2. Add chopped onions (if included) and sauté until golden brown.
3. Add the rest of the chopped ingredients and cook for 5 minutes.
4. Add 1/2 tsp of {spice[0]} and 1/2 tsp of {spice[1]} with a pinch of salt.
5. Cook everything together for another 10–15 minutes, stirring occasionally.
6. Sprinkle some {herb} on top for added freshness and aroma.

🍽️ Final Touch:
- Serve hot with rice, chapati, or naan.
- You can also add lemon juice or yogurt for a tangy twist.

💡 Tip: Add a little butter or cream to make it richer, especially for special occasions!
"""
        return steps

    def run(self):
        self.welcome_message()
        ingredients = self.get_ingredients()

        if not ingredients:
            print("⚠️ Please enter at least one ingredient to proceed.")
            return

        recipe_name = self.generate_recipe_name(ingredients)
        recipe_steps = self.generate_recipe_steps(ingredients)

        print(f"\n🍽️ Your Custom Recipe: {recipe_name}\n")
        print(recipe_steps)


# Run the tool
if __name__ == "__main__":
    generator = RecipeGenerator()
    generator.run()
