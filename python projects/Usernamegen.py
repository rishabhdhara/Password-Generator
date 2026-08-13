import random

adjectives = ["Black", "Silent", "Fallen", "Clever", "Mighty", "Cosmic", "Shadow", "Blazing", "Frozen", "Rapid"]
nouns = ["wings", "Falcon", "Angel", "Phoenix", "Uriel", "Dragon", "Panther", "Comet", "Raven", "Storm"]

def generate_username(include_number=True):
    username = random.choice(adjectives) + random.choice(nouns)
    if include_number:
        username += str(random.randint(1, 999))
    return username


for _ in range(7):
    print(generate_username())