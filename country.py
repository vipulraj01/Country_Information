# Creates a CountryInfo from a countryinfo import.
from countryinfo import CountryInfo

# Enter the name of your country
count = input("Enter the name of your country : ")

# Sets the country info.
country = CountryInfo(count)

# Prints a description of the country capital.
print("Capital is : " , country.capital())

# Prints out information about the currency.
print("Currency is : " , country.currencies())

# Prints a warning if the border is a country.
print("Border is : " , country.borders())

# Prints a description of the language.
print("Language is : ", country.languages())

# Prints information about the Other name.
print("Other name is : ", country.alt_spellings())
