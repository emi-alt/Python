country_code = {
    "India": '0019',
    "Australia": '0025',
    "Nepal" : '00977'
}
print("Country code for India: ")
print(country_code.get("India", "NA"))

print("Country code for Japan: ")
print(country_code.get("Japan", "NA"))