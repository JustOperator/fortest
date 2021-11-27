class PhoneContact():
    def __init__(self, name, contactNumber, note):
        self.name = name
        self.contactNumber = contactNumber
        self.note = note
    def convert(self):
        name = str(self.name)
        contactNumber = str(self.contactNumber)
        note = str(self.note)
        return name, contactNumber, note
