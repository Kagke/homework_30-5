united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]["capital"]="Cardiff"
print(united_kingdom[1]["capital"])
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
nothern_ireland={"name" : "Nothern Ireland",
    "population": 1811000,
    "capital": "Belfast"}
united_kingdom.append(nothern_ireland)
print(united_kingdom)

# 3. Use a loop to print the names of all the countries in the UK.

# for x in united_kingdom["names"] :
#     print(united_kingdom[x]["name"])


# 4. Use a loop to find the total population of the UK.
# total_population=0
# x=0
# for x in united_kingdom[x]str(["population"]):
#     total_population = total_population + united_kingdom[x]str(["population"])
#     x+=1
# print(total_population)    
