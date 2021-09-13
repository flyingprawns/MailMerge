TEMPLATE_PATH = "./Input/Letters/starting_letter.txt"
NAMES_PATH = "./Input/Names/invited_names.txt"
DESTINATION_PATH = "./Output/ReadyToSend/"

# Get the letter template
with open(TEMPLATE_PATH, mode="r") as file:
    letter_template = file.read()

# Get recipient names
with open(NAMES_PATH, mode="r") as file:
    recipient_names = file.readlines()

for name in recipient_names:
    # Create a letter
    name = name.rstrip()
    final_letter = letter_template.replace("[name]", name, 1)
    # Save the letter to destination
    letter_destination = DESTINATION_PATH + name + ".txt"
    with open(letter_destination, mode="w") as file:
        file.write(final_letter)

# Exit program
print("Your letters have been successfully written. Find them in /Output/ReadyToSend !")