def create_greeting(name):
    return f"Hello, {name}! Welcome to my AI engineering homelab!"

name = input("What is your name? ")
greeting = create_greeting(name)

print(greeting)
