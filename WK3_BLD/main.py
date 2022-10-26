import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

csv_data = pandas.read_csv("Pokemon.csv")
csv_data
'''which pokemon has the most defense?'''
csv_data.sort_values("Defense", ascending=False)