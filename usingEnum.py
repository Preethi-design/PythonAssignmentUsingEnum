import enum
# Using enum class create enumerations
class country(enum.Enum):
    Afghanistan = 93 
    Albania = 355
    Algeria = 213 
    Andorra = 376
    Angola = 244
    Antarctica = 672

Member_name=country.Albania.name
Member_value=country.Albania.value
print("Member name:{first} Member Value:{second}".format(first=Member_name,second=Member_value))
