class Doctor:
    def __init__(self, doctorId=None, firstName=None, lastName=None, specialization=None, contactNumber=None):
        self.doctorId = doctorId
        self.firstName = firstName
        self.lastName = lastName
        self.specialization = specialization
        self.contactNumber = contactNumber
    def getDoctorId(self):
        return self.doctorId
    def setDoctorId(self, doctorId):
        self.doctorId = doctorId
    def getFirstName(self):
        return self.firstName
    def setFirstName(self, firstName):
        self.firstName = firstName
    def getLastName(self):
        return self.lastName
    def setLastName(self, lastName):
        self.lastName = lastName
    def getSpecialization(self):
        return self.specialization
    def setSpecialization(self, specialization):
        self.specialization = specialization
    def getContactNumber(self):
        return self.contactNumber
    def setContactNumber(self, contactNumber):
        self.contactNumber = contactNumber
    def __str__(self):
        return f"Doctor ID: {self.doctorId}, Name: {self.firstName} {self.lastName}, Specialization: {self.specialization}, Contact: {self.contactNumber}"
