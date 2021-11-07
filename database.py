#importing modules
from modules import *



def CommonDetailEntry(ID,Name, AddressID, ContactNo, gender, DOB):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        print(ID, Name, AddressID, ContactNo, gender, DOB)
        try:
                Database.execute(f"""INSERT INTO CommonDetails
                                VALUES ('{ ID }', '{ Name }', '{ AddressID }', '{ ContactNo }', '{ gender }', '{ DOB }')
                """)
        except:
                pass
        HosDB.commit()
        return


def AddressesEntry(ID,LineNo1,city,pincode,state):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        try:
                Database.execute(f""" INSERT INTO Addresses
                        VALUES ('{ID}', '{LineNo1}', '{city}', {pincode}, '{state}') """)
        except:
                pass
        HosDB.commit()
        return


def DoctorsEntry(ID,grade,wardNo,specialization,salary,workingSince):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO Doctors
                        VALUES ('{ID}', '{grade}', '{wardNo}', '{specialization}', '{salary}', '{workingSince}')
                """)
        except:
                pass
        HosDB.commit()
        return


def PatientEntry(ID,prescription,diagnosis):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO Patient
                        VALUES ('{ID}', '{prescription}', '{diagnosis}')
                """)
        except:
                try:
                        Database.execute(f"""
                                UPDATE 
                                        Patient
                                SET 
                                        prescription = '{prescription}',
                                        diagnosis = '{diagnosis}'
                                WHERE 
                                        ID='{ID}'
                        """)
                except:
                        pass
        HosDB.commit()  
        return  


def wardsEntry(No,Name):        
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO wards
                        VALUES ({No}, '{Name}')
                """)
        except:
                pass
        HosDB.commit()
        return


def RoomsEntry(RoomNo):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO Rooms
                        VALUES ({RoomNo})
                """)
        except:
                pass
        HosDB.commit()
        return

def workersEntry(ID,wardNo,position,salary,workingSince):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO workers
                        VALUES ('{ID}', '{wardNo}', '{position}', '{salary}', '{workingSince}')
                """)
        except:
                pass
        HosDB.commit()
        return

def visitedByEntry(patientID,visitorID):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO visitedBy
                        VALUES ('{patientID}', '{visitorID}')
                """)
        except:
                pass
        HosDB.commit()
        return 

def visitorEntry(visitorID,Name,ContactNo,relation,VisitedDate,VisitedTime):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO visitor
                        VALUES ('{visitorID}', '{Name}', '{ContactNo}', '{relation}', '{VisitedDate}', '{VisitedTime}')
                """)
        except:
                pass
        HosDB.commit()
        return 

def ReceiptEntry(ID,DoctorID,Problem):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        Date = date.today()
        Time = datetime.now()
        try:
                Database.execute(f"""
                        INSERT INTO Receipt
                        VALUES ('{ID}', '{Date}', '{Time}', '{DoctorID}', '{Problem}')
                """)
        except:
                pass
        HosDB.commit()
        return

def PaymentsEntry(patientID,chargesID):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO Payments
                        VALUES ('{patientID}', '{chargesID}')
                """)
        except:
                pass
        HosDB.commit()
        return 

def AdmitedPatientEntry(patientID,wardNo,roomNo,FromDate):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO AdmitedPatients (patientID,wardNo,roomNo,FromDate)
                        VALUES ('{patientID}', '{wardNo}', '{roomNo}', '{FromDate}')
                """)
        except:
                pass
        HosDB.commit()
        return 

def TreatedEntry(patientID,doctorID,Date):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO Treated
                        VALUES ('{patientID}', '{doctorID}', '{Date}')
                """)
        except:
                pass
        HosDB.commit()
        return 

def Transaction(chargesID,Date,Amount):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO Transaction
                        VALUES ('{chargesID}', '{Date}',{Amount})
                """)
        except:
                pass
        HosDB.commit()
        return 

def WorkerAttendance(ID,Day):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO WorkerAttendance
                        VALUES ('{ID}', '{Day}')
                """)
        except:
                pass
        HosDB.commit()
        return 

def DoctorToDoctor(DoctorID,patientID,NextDoctorID):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO DoctorT0Doctor
                        VALUES ('{DoctorID}', '{patientID}', '{NextDoctorID}')
                """)
        except:
                pass
        HosDB.commit()
        return 
