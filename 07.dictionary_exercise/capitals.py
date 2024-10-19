countries = input().split(", ")
capitals = input().split(", ")

information = {countries[index]: capitals[index] for index in range(len(countries))}
for country, capital in information.items():
    print(f"{country} -> {capital}")
