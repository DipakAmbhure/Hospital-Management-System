#To handle workers
from database import *
from functionalities import *

def EnterWorker(Name,Address,ContactNo,gender,DOB,position,wardNo,salary,doj):
        AID=getNextID(getLastId('address'))
        AddressesEntry(AID,Address[0],Address[1],Address[2],Address[3])
        ChangeLastIdTo(AID)
        WID=getNextID(getLastId('worker'))
        CommonDetailEntry(WID,Name,AID,ContactNo,gender,DOB)
        ChangeLastIdTo(WID)
        workersEntry(WID,wardNo,position,salary,doj)
        return WID




def getDataOfWorker(ID):
        HosDB = mysql.connector.connect(host = "localhost", user="Hospital", passwd="Hospital@123", database = "HospitalManagement")
        Database = HosDB.cursor()
        
        Database.execute(f"""
                SELECT Name FROM CommonDetails
                WHERE CommonDetails.ID='{ID}'
        """)
        Name = Database.fetchall()[0][0]

        Database.execute(f"""
                SELECT Day from WorkerAttendance
                WHERE ID='{ID}'
        """)
        Attendance=Database.fetchall()

        Database.execute(f"""
                SELECT wardNo, position,WorkingSince,salary FROM workers
                WHERE ID = '{ID}'
        """)
        data = Database.fetchall()
        WardNo = data[0][0]
        position = data[0][1]
        doj = data[0][2]
        salary = data[0][3]
        HosDB.commit()

        Database.execute(f"""
                SELECT Name FROM wards
                WHERE No = {WardNo}
        """)
        WardName = Database.fetchall()[0][0]
        HosDB.commit()
        return Name,Attendance,WardNo,position,doj,salary,WardName


def markPresent(ID):
        HosDB = mysql.connector.connect(host = "localhost", user="Hospital", passwd="Hospital@123", database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO WorkerAttendance
                        VALUES ('{ID}','{date.today()}')
                """)
        except:
                pass
        HosDB.commit()
        return