#games = input("What are your favorite activites?")
def input_list(param):
    input_list = input(f"Input your favorite {param} separetad by spaces_ ")
    processed_list = input_list.split(" ")
    processed_list = filter(lambda x:  x != '', processed_list)
    return list(processed_list)



games = input_list("activites")
food = input_list("food")
favorites = games + food
print(favorites)
