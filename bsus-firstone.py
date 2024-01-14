#games = input("What are your favorite activites?")
def input_list(param):
    input_list = input(f"Input your favorite {param} separetad by spaces")
    input_list.split(" ")


games = ["Minecraft", "luyfiyff"]
food = ["pizza", "azzip"]
favorites = games + food
print(favorites)
