from classes import AddressBook, Record, Name, Phone, Field


def parser_commands(command: str):
    command = command.strip().lower().split(' ')
    return command


if __name__ == '__main__':
    book = AddressBook()
    print('Commands: add contact, add phone, change phone, delete phone\n'
          'Enter: COMMAND(two words) NAME +- NUMBER(two numbers for change number)')

    while True:
        command = parser_commands(input('Enter your command:'))
        if len(command) == 5 or len(command) == 4:
            if ' '.join(command[0:2]) == 'add contact':
                book.add_contact(
                    name=Name(value=command[2]), phone=Phone(value=command[3]))

            elif ' '.join(command[0:2]) == 'add phone':
                a = Record(name=Name(value=command[2]))
                if a.name.value in book:
                    book.get(
                        Record(name=Name(value=command[2])).name.value).add_phone(Phone(value=command[3]))
                else:
                    print(f'Name {command[2].capitalize()} does not exist')
            elif ' '.join(command[0:2]) == 'change phone':
                a = Record(name=Name(value=command[2]))
                if a.name.value in book:
                    try:
                        book.get(
                            Record(name=Name(value=command[2])).name.value).change_phone(command[3], Phone(value=command[4]))
                    except IndexError:
                        print('Enter two numbers, not one')
            elif ' '.join(command[0:2]) == 'delete phone':
                a = Record(name=Name(value=command[2]))
                if a.name.value in book:
                    book.get(
                        Record(name=Name(value=command[2])).name.value).delete_phone(command[3])
        elif len(command) == 3 and ' '.join(command[0:2]) == 'add contact':
            book.add_contact(
                name=Name(value=command[2]))

        else:
            print('Enter-string is not correct')
        print(f'Your addressbook:{book}')
