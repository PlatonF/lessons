
def input_list(param):
    input_list = input(f"Input your favorite {param} separetad by spaces_ ")
    l = input_list.split(" ")
    l = [x for x in l if x !='']
    return l


games = input_list("activites")
food = input_list("food")
favorites = games + food
print(favorites)
