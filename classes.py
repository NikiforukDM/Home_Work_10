from collections import UserDict
import email
from typing import Union


class Field:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class AddressBook(UserDict):
    def add_contact(self, name: Name, phone: Phone = None):
        contact = Record(name=name, phone=phone)
        self.data[name.value] = contact

    def add_record(self, record: "Record"):
        self.data[record.name.value] = record

    def find_by_name(self, name):
        try:
            return self.data[name]
        except KeyError:
            return None

    def find_by_phone(self, phone: str):
        for record in self.data.values():  # type:Record
            if phone in [number.value for number in record.phones]:
                return record
            return None


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name: Name = name
        self.phones: list[Phone] = [phone] if phone is not None else []

    def __repr__(self):
        return f'{self.name.value} : {" ".join(phone.value for phone in self.phones)}'

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, old_number: str, new_number: Phone):
        try:
            # self.phones.append(old_number)
            # self.phones.append(new_number)
            for ph in self.phones:
                if ph.value == old_number:
                    self.phones.remove(ph)
                else:
                    print(f'Phone {old_number} does not exists')
                self.phones.append(new_number)
        except ValueError:
            print(f'{old_number} does not exists')

    def delete_phone(self, phone: Phone):

        # try:
        for ph in self.phones:
            if ph.value == phone:
                self.phones.remove(ph)
            else:
                print(f'Number {phone} does not exists')

        # except ValueError:
        #     print(f'{phone} does not exists')
