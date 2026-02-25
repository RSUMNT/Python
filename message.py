sent_message =" I want to crack Netflix so badly, that I want in"
unsent_message = "I want to crack Netflix so badly, that I want i by June"

with open("sent_message.txt", "w") as file:
    file.write(sent_message)

with open("sent_message.txt", "r+") as file:
    read_message = file.read()
    file.seek(0)
    file.write(unsent_message)
    print(f"Sent Message: {read_message}")
    print(f"Unsent Message: {unsent_message}")