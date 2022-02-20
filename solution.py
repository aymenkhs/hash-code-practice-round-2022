

def solve(clients):
    return naive_solution(clients)

def naive_solution(clients):

    ingredients = set()
    not_included_ingredients = set()

    for client in clients:
        # we first check that the ingredients in the pizza don't bother the client
        disliked = False
        for ingredient in ingredients:
            if ingredient in client.disliked_ingredients:
                disliked = True
                break

        if not disliked:
            # we check that we can add the ingredients he like
            liked = True
            for ingredient in client.liked_ingredients:
                if ingredient in not_included_ingredients:
                    liked = False

            if liked:
                ingredients = ingredients.union(set(client.liked_ingredients))
                not_included_ingredients = not_included_ingredients.union(set(client.disliked_ingredients))


    return ingredients
