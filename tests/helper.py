
import random
from faker import Faker

def generate_password():
    simbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.sample(simbols, random.randint(6, 12)))
    yield password

def generate_email():
    simbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    domain = random.choice(["gmail.com", "yandex.ru", "mail.ru"])
    mail = ''.join(random.sample(simbols, random.randint(5, 64)))
    return mail + "@" + domain

print(generate_email())

