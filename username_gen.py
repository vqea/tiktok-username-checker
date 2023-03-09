import random, string

output_file = "usernames.txt"
amount = int(input("amount of strings: "))
character_amount = int(input("how many characters: "))

for i in range(amount):
    generated = ("").join(random.choices(string.ascii_letters + string.digits, k = character_amount))
    print(generated)
    with open(output_file, "a") as f:
        f.write(generated + "\n")
input()
