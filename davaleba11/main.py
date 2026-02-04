# 1
# youngest_age = None
# youngest_name = ""
# with open("oscars.txt","r") as oscars:
#     for line in oscars:
#         fields = line.strip().split(",")
#
#         age = int(fields[2])
#         name = fields[3]
#
#         if youngest_age is None or age < youngest_age:
#             youngest_age = age
#             youngest_name = name
# print(youngest_age)
# print(youngest_name)

# 2
# year_input = input("Enter year: ")
# with open("oscars.txt","r") as oscars:
#     found = False
#     for line in oscars:
#         fields = line.strip().split(",")
#         year = fields[0]
#         name = fields[3]
#
#         if year == year_input:
#             print(name)
#             found = True
#     if not found:
#         print("Oscar not found")
