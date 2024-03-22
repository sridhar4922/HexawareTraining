import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
class PropertyUtil:
    @staticmethod
    def getPropertyString(self):
        server_name = "SRIDHAR/LOCALHOST"
        database_name = "HospitalManagementSystem"
        trusted_connection = "yes"
        self.cursor = self.connection.cursor()
        return f"Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection={trusted_connection};"
