#To Manage Patient
from functionalities import *
from database import *


#IDFormate : HP0000000

def RegisterPatient(Name,Address,ContactNo,gender,DOB,Problem):
        AID=getNextID(getLastId('address'))
        AddressesEntry(AID,Address[0],Address[1],Address[2],Address[3])
        ChangeLastIdTo(AID)
        PID=getNextID(getLastId('patient'))
        CommonDetailEntry(PID,Name,AID,ContactNo,gender,DOB)
        ChangeLastIdTo(PID)
        WardNo = getWardNo(Problem)
        DoctorID = getFirstDoctorID(WardNo)
        ReceiptEntry(PID,DoctorID,Problem)
        return (DoctorID,WardNo,PID)


                

def AdmitPatient(PID,DID):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        SELECT WardNo from Doctors
                        WHERE ID = '{ DID }'
                """)
                WardNo = Database.fetchall()[0][0]
                RoomNo = GetFreeRoom(WardNo)
                From = date.today()
                AdmitedPatientEntry(PID,WardNo,RoomNo,From)
        except:
                HosDB.commit()
                return -1,-1
        HosDB.commit()
        return WardNo,RoomNo


def GetPatientData(ID):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        CommonDetails = getCommonDetails(ID)
        
        
        Database.execute(f"""
                SELECT DoctorID,Name from Treated INNER JOIN CommonDetails
                ON Treated.DoctorID=CommonDetails.ID
                where PatientID = '{ID}'
        """)
        
        Doctors = Database.fetchall()
        Database.execute(f"""
                SELECT wardNo,roomNo,FromDate,Till FROM AdmitedPatients
                where PatientID = '{ID}'
        """)

        Admited = Database.fetchall()
        Database.execute(f"""
                SELECT Date,Amount from Payments INNER JOIN Transaction
                on Payments.chargesID = Transaction.chargesID
                where PatientID = '{ID}'
        """)

        Payments = Database.fetchall()
        Database.execute(f"""
                SELECT Date, time, Problem, Name, DoctorID From Receipt INNER JOIN CommonDetails
                ON Receipt.DoctorID = CommonDetails.ID
                where Receipt.ID = '{ID}'
        """)
        Receipt = Database.fetchall()[0]

        Database.execute(f"""
                SELECT prescription, diagnosis FROM Patient
                WHERE ID = '{ID}'
        """)
        Treatment = Database.fetchall()
        try:
                prescription=Treatment[0][0]
                dignosis = Treatment[0][1]
        except:
                prescription=None
                dignosis=None
        return Doctors,Admited,CommonDetails,Payments,Receipt,prescription,dignosis

def DoNotExists(PID):
        print("here")
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        Database.execute(f"""
                select * from Patient
                where ID = '{PID}'
        """)
        try:
                R = Database.fetchall()[0][0]
                print("r",R)
                return False
        except:
                return True

def SaveRecord(PID,amount):
        CID=getNextID(getLastId('charges'))
        print(CID)
        ChangeLastIdTo(CID)
        datee = date.today()
        Transaction(CID,datee,amount)
        PaymentsEntry(PID,CID)
        return datee

def GetAllPayments():
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        Database.execute(f"""
                select PatientID,amount,Date from Payments INNER JOIN Transaction
                ON Payments.chargesID = Transaction.ChargesID
        """) 
        done = Database.fetchall()
        Database.execute(f"""
                SELECT ID from Patient LEFT JOIN Payments
                ON Patient.ID=Payments.patientID
                where chargesID is NULL 

        """) 
        remaining = Database.fetchall()
        HosDB.commit()
        return done,remaining

def getPatientTreatementData(ID):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        DATA=['True']
        try:
                Database.execute(f"""
                        select prescription, diagnosis from Patient
                        where ID = '{ID}'
                """)
                DATA.append(Database.fetchall()[0])
        except:
                DATA[0]='False'
                DATA.append((None,None))

        Admited=['True']
        try:
                Database.execute(f"""
                        SELECT roomNo,wardNo FROM AdmitedPatients
                        where patientID = '{ID}'
                """)
                R=Database.fetchall()[0]
                Admited.append(R)
        except:
                Admited=['False']

        return DATA,Admited

def DischargePatient(ID):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        todaydate = str(date.today())
        try:
                Database.execute(f"""
                        UPDATE AdmitedPatients
                        SET Till = '{todaydate}'
                        WHERE patientID = '{ID}'
                """)
        except:
                pass
        HosDB.commit()
        return 
