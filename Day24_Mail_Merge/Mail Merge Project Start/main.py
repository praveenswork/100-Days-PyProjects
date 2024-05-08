with open('./Input/Names/invited_names.txt') as name_file:
    names = name_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_content = letter_file.read()
    for name in names:
        striped_names = name.strip()
        new_letter = letter_content.replace('[name]', striped_names)
        with open(f'./Output/ReadyToSend/letter_for_{striped_names}.txt', mode='r') as completed_letter:
            completed_letter.write(new_letter)
