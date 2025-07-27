# Empty list to store all the names from the file
names = []

# Open the invited_names.txt file in read mode
with open("Input/Names/invited_names.txt", "r") as file:
    for line in file:
        name = line.strip()  # Remove leading/trailing whitespace and newline characters
        if name:             # Skip any empty lines
            names.append(name)  # Add the cleaned name to the list

# Open the letter template file and read its content
with open("Input/Letters/starting_letter.txt") as f:
    letter_template = f.read()  # Store the entire letter template as a string

# Loop through each name and create a personalized letter
for name in names:
    # Replace [name] placeholder with the actual name
    final_letter = letter_template.replace("[name]", name)

    # Set the output file path where the personalized letter will be saved
    file_address = f"Output/ReadyToSend/{name}.txt"

    # Write the personalized letter to the output file
    with open(file_address, "w") as file:
        file.write(final_letter)
