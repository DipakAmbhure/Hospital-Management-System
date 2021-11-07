#To Handle Doctors
from database import *
from functionalities import *
from modules import *

def TellDoctor(patientID,DoctorID):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user="Hospital", 
                                passwd="Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO hastoTreat
                        VALUES ('{patientID}','{DoctorID}')
                """)
        except:
                pass
        HosDB.commit()
        return


def getDoctorData(ID):
        print(ID)
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user="Hospital", 
                                passwd="Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        SELECT patientID FROM hastoTreat
                        WHERE doctorID = '{ID}'
                """)
                PatientHasToTreat = Database.fetchall()
                Database.execute(f"""
                        SELECT wardNo,specialization,WorkingSince,salary,grade FROM Doctors
                        WHERE ID = '{ID}'
                """)
                data=Database.fetchall()
                WardNo=data[0][0]
                specialization = data[0][1]
                doj = data[0][2]
                salary = data[0][3]
                grade = data[0][4]
                Database.execute(f"""
                        SELECT Name FROM wards
                        WHERE No = {WardNo}
                """)
                WardName = Database.fetchall()[0][0]

                Database.execute(f"""
                        SELECT Name FROM CommonDetails
                        WHERE CommonDetails.ID='{ID}'
                """)
                Name = Database.fetchall()[0][0]

                Database.execute(f"""
                        SELECT patientID,ondate FROM Treated
                        WHERE doctorID = '{ID}'
                """)
                TreatedPatient = Database.fetchall()
        except:
                HosDB.commit()
                return (None,) * 9

        HosDB.commit()
        return Name, WardNo, PatientHasToTreat, TreatedPatient, specialization, salary, doj, WardName, grade

def EnterDoctor(Name, Address, ContactNo, gender, DOB, specialization, wardNo, salary, doj, grade):
        AID=getNextID(getLastId('address'))
        AddressesEntry(AID, Address[0], Address[1], Address[2], Address[3])
        ChangeLastIdTo(AID)
        DID=getNextID(getLastId('doctor'))
        CommonDetailEntry(DID, Name, AID, ContactNo, gender, str(DOB))
        ChangeLastIdTo(DID)
        DoctorsEntry(DID, grade, wardNo, specialization, salary, doj)
        return DID

def AssignNextDoctor(PID, DID, Ngrade):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user="Hospital", 
                                passwd="Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        SELECT ID from Doctors
                        where grade = '{ Ngrade }'
                """)
                data = Database.fetchall()
                NDID = data[random.randint(0,len(data)-1)][0]
        except:
                #no doctor with that grade
                HosDB.commit()
                return None
        DoctorToDoctor(DID, PID, NextDoctorID=NDID)
        TellDoctor(PID, NDID)
        HosDB.commit()
        return NDID

