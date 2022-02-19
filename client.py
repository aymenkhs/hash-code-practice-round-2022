
class Client:

    def __init__(self, liked_ingredients, disliked_ingredients):
        self.liked_ingredients = liked_ingredients
        self.disliked_ingredients =  disliked_ingredients

    def __str__(self):
        return 'Client liked ingredients : {} disliked ingredients : {}\n'.format(self.liked_ingredients, self.disliked_ingredients)

    def __repr__(self):
        return str(self)

    def check_pizza(self, pizza):
        """
        method that check if a pizza is conform with the preferances of a client

        Args:
            pizza : a list discribing the ingredients of a pizza

        Return:
            True if the pizza matches with the client preferances and False if the pizza doesn't match with it's preferances
        """

        for ingredient in pizza:
            if ingredient in self.disliked_ingredients:
                return False

        for ingredient in self.liked_ingredients:
            if ingredient not in pizza:
                return False

        return True
