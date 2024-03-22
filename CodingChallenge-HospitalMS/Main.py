import sys
import os
# Add parent directory of 'dao' to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you should be able to import 'dao'
from entity.HospitalManagementSystem_service_impl import HospitalManagementSystemServiceImpl
from entity.patientException import PatientNumberNotFoundException
from entity.Appointment import Appointment
class MainModule:
    def __init__(self):
        self.HospitalManagementSystem_service = HospitalManagementSystemServiceImpl()
    def display_menu(self):
        print("\nHospitalManagementSystem Management System Menu:")
        print("1. Get Appointment by ID")
        print("2. Get Appointments for Patient")
        print("3. Get Appointments for Doctor")
        print("4. Schedule Appointment")
        print("5. Update Appointment")
        print("6. Cancel Appointment")
        print("7. Exit")
    def get_input(self, prompt):
        return input(prompt)
    def main(self):
        try:
            while True:
                self.display_menu()
                choice = int(self.get_input("\nEnter your choice: "))

                if choice == 1:
                    appointment_id = int(self.get_input("Enter appointment ID: "))
                    appointment = self.HospitalManagementSystem_service.getAppointmentById(appointment_id)
                    print("Appointment details:")
                    print(appointment)

                elif choice == 2:
                    patient_id = int(self.get_input("Enter patient ID: "))
                    appointments = self.HospitalManagementSystem_service.getAppointmentsForPatient(patient_id)
                    print("Appointments for patient:")
                    for appointment in appointments:
                        print(appointment)

                elif choice == 3:
                    doctor_id = int(self.get_input("Enter doctor ID: "))
                    appointments = self.HospitalManagementSystem_service.getAppointmentsForDoctor(doctor_id)
                    print("Appointments for doctor:")
                    for appointment in appointments:
                        print(appointment)

                elif choice == 4:
                    appointment_id = int(self.get_input("Enter appointment ID: "))
                    patient_id = int(self.get_input("Enter patient ID: "))
                    doctor_id = int(self.get_input("Enter doctor ID: "))
                    appointment_date = self.get_input("Enter appointment date (YYYY-MM-DD): ")
                    description = self.get_input("Enter appointment description: ")
                    new_appointment = Appointment(appointment_id, patient_id, doctor_id, appointment_date, description)
                    success = self.HospitalManagementSystem_service.scheduleAppointment(new_appointment)
                    if success:
                        print("Appointment scheduled successfully.")
                    else:
                        print("Failed to schedule appointment.")
                elif choice == 5:
                    appointment_id = int(self.get_input("Enter appointment ID: "))
                    patient_id = int(self.get_input("Enter patient ID: "))
                    doctor_id = int(self.get_input("Enter doctor ID: "))
                    appointment_date = self.get_input("Enter updated appointment date (YYYY-MM-DD): ")
                    description = self.get_input("Enter updated appointment description: ")
                    updated_appointment = Appointment(appointment_id, patient_id, doctor_id, appointment_date, description)
                    success = self.HospitalManagementSystem_service.updateAppointment(updated_appointment)
                    if success:
                        print("Appointment updated successfully.")
                    else:
                        print("Failed to update appointment.")
                elif choice == 6:
                    appointment_id = int(self.get_input("Enter appointment ID to cancel: "))
                    success = self.HospitalManagementSystem_service.cancelAppointment(appointment_id)
                    if success:
                        print("Appointment cancelled successfully.")
                    else:
                        print("Failed to cancel appointment.")
                elif choice == 7:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
        except PatientNumberNotFoundException as e:
            print("Patient number not found in the database:", e)
    def new_method(self):
        return HospitalManagementSystemServiceImpl()
if __name__ == "__main__":
    main_module = MainModule()
    main_module.main()
