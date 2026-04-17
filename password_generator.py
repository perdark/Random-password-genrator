import random
import string
import time

name = ["Ali", "Mustafa"]
year = ["1990"]
football = ["Messi"]
car = ["Nissan"]
cat = ["Siri"]
son = ["Ahmed"]

special_chars = ["@", "#", "_", "!", "$"]
start_time = time.time()
passwords = set()

def random_number():
    return str(random.randint(0, 9999))

def random_case(word):
    return ''.join(
        c.upper() if random.random() > 0.5 else c.lower()
        for c in word
    )

while len(passwords) < 100000:
    
    n = random.choice(name)
    y = random.choice(year)
    f = random.choice(football)
    c = random.choice(car)
    ca = random.choice(cat)
    s = random.choice(son)
    sp = random.choice(special_chars)

    # -------------------

    passwords.add(n + y)
    passwords.add(f + sp + y)
    passwords.add(c + "_" + s)
    passwords.add(ca + random_number() + sp)
    passwords.add(random_case(n) + random_number())
    passwords.add(s + sp + f + random_number())
    passwords.add(c + sp + random_case(n))
    passwords.add(f + "_" + random_number())

passwords = list(passwords)[:100000]

with open("passwords.txt", "w") as file:
    for p in passwords:
        file.write(p + "\n")

end_time = time.time()

print("Done generate 100000 passwords!")
print("Saved to: passwords.txt")
print(f"Time elapsed: {end_time - start_time:.2f} seconds")
