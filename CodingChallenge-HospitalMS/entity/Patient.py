class Patient:
    def __init__(self, patientId=None, firstName=None, lastName=None, dateOfBirth=None, gender=None, contactNumber=None, address=None):
        self.patientId = patientId
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.contactNumber = contactNumber
        self.address = address
    def getPatientId(self):
        return self.patientId
    def setPatientId(self, patientId):
        self.patientId = patientId

    def getFirstName(self):
        return self.firstName
    def setFirstName(self, firstName):
        self.firstName = firstName
    def getLastName(self):
        return self.lastName
    def setLastName(self, lastName):
        self.lastName = lastName
    def getDateOfBirth(self):
        return self.dateOfBirth
    def setDateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth
    def getGender(self):
        return self.gender
    def setGender(self, gender):
        self.gender = gender
    def getContactNumber(self):
        return self.contactNumber
    def setContactNumber(self, contactNumber):
        self.contactNumber = contactNumber
    def getAddress(self):
        return self.address
    def setAddress(self, address):
        self.address = address
    def __str__(self):
        return f"Patient ID: {self.patientId}, Name: {self.firstName} {self.lastName}, DOB: {self.dateOfBirth}, Gender: {self.gender}, Contact: {self.contactNumber}, Address: {self.address}"
