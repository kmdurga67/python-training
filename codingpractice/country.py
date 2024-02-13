# Importing the required module.
from countryinfo import CountryInfo

# Getting a country name from the user.
count = input("Please enter your country name: ")
country = CountryInfo(count)

# print(country.info()) # It returns the object with all the info about the country.

# Different APIs to get the data as per the requirements.
print("Others names : ", country.alt_spellings())
print("Capital is : ", country.capital())
print("Currencies is :", country.currencies())
print("Lanuage is : ", country.languages())
print("Borders are : ", country.borders())
