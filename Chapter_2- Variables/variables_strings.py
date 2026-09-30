# Using variables in strings.
first_name = "peter"
last_name = "muigai"
full_name = f"{first_name} {last_name}"  # introduce f-strings
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"  # use a variable and f-string
print(message)