import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

csv_data = pandas.read_csv("Pokemon.csv")
csv_data
'''which type of pokemon has the highest ATK'''
csv_data.groupby("Type 1")["Attack"].mean().sort_values(ascending=False)
'''which dragon pokemons have the most attack from highest to lowest'''
csv_data[csv_data["Type 1"] == "Dragon"].sort_values(by="Attack", ascending=False)
'''which generation has the most amount of legendaries'''
csv_data.groupby("Generation")["Legendary"].sum().sort_values(ascending=False)
'''which generation of pokemon has the highest average speed'''
csv_data.groupby("Generation")["Speed"].mean().sort_values(ascending=False)