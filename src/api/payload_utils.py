from random import randint


def generate_user_data(faker):
    name = faker.name()
    data = {"username": name,
            "password": str(randint(1000, 1000000)),
            "email": f'{name.replace(" ", "_").lower()}@gmail.com'}
    return data

