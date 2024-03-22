import sys
import os
# Add parent directory of 'dao' to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from abc import ABC, abstractmethod
from Appointment import Appointment
from typing import List
class IHospitalManagementSystemService(ABC):
    @abstractmethod
    def getAppointmentById(self, appointment_id):
        pass
    @abstractmethod
    def getAppointmentsForPatient(self, patient_id):
        pass
    @abstractmethod
    def getAppointmentsForDoctor(self, doctor_id):
        pass
    @abstractmethod
    def scheduleAppointment(self, appointment):
        pass
    @abstractmethod
    def updateAppointment(self, appointment):
        pass
    @abstractmethod
    def cancelAppointment(self, appointment_id):
        pass
