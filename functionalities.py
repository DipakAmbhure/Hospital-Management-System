from modules import *





#To Get Last ID stored in Database
def getLastId(whos):
        HosDB = mysql.connector.connect(
                                host = "localhost",
                                user = "Hospital",
                                passwd = "Hospital@123", 
                                database = "HospitalManagement" )
        Database = HosDB.cursor()
        Database.execute(f"""
                SELECT LastID FROM IDS
                WHERE `whos`='{whos}'
        """)
        r = Database.fetchall()[0][0]
        HosDB.commit()
        return r

#generate Next ID 
def getNextID(curID):
        val=str(int(curID[2:])+1)
        return curID[:2] + '0' * (8 - len(val)) + val

#Store New Last ID to database
def ChangeLastIdTo(ID):
        HosDB = mysql.connector.connect(
                host = "localhost",
                user = "Hospital",
                passwd = "Hospital@123",
                database = "HospitalManagement" )
        Database = HosDB.cursor()
        if(ID[1]=='P'):
                who='patient'
        elif(ID[1]=='D'):
                who='doctor'
        elif(ID[1]=='V'):
                who='visitor'
        elif(ID[1]=='W'):
                who='worker'
        elif(ID[1]=='L'):
                who='address'
        elif(ID[1]=='C'):
                who='charges'
        else:
                return

        Database.execute(f"""
                        UPDATE IDS
                        SET LastID='{ID}'
                        WHERE whos='{who}' """)
        HosDB.commit()
        return








def getAllWards():
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        Database.execute(f"""
                SELECT Name FROM wards
        """)
        result = Database.fetchall()
        HosDB.commit()
        return list(result)

def getWardNo(Name):
        Name=Name.lower()
        print(Name)
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        Database.execute(f"""
                SELECT No FROM wards
                WHERE Name = '{Name}'
        """)
        result = Database.fetchall()[0][0]
        HosDB.commit()
        return result

def getFirstDoctorID(WardNo):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        Database.execute(f"""
                SELECT ID FROM Doctors
                WHERE WardNo='{WardNo}' and grade='HA'
        """)
        result = Database.fetchall()
        HosDB.commit()
        return result[random.randint(0,len(result)-1)][0]


def getCommonDetails(ID):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        Database.execute(f"""
                SELECT Name,LineNo1,city,pincode,state,ContactNo,gender,DOB FROM CommonDetails
                INNER JOIN Addresses ON CommonDetails.AddressID=Addresses.ID
                WHERE CommonDetails.ID = '{ID}' """)
        CommonDetails = Database.fetchall()[0]
        HosDB.commit()
        return CommonDetails

def GetFreeRoom(WardNo):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        Database.execute(f"""
                SELECT RoomNo from Rooms
                WHERE RoomNo not in (
                SELECT roomNo from AdmitedPatients
                WHERE wardNo = '{WardNo}'
                and Till is null
                )
        """)
        result = Database.fetchall()
        HosDB.commit()
        if(len(result)) == 0:
                return -1
        return result[0][0]

def deleteFromHasToTreat(PID,DID):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        Database.execute(f"""
                DELETE FROM hastoTreat
                WHERE patientID='{PID}' and doctorID='{DID}'
        """)
        HosDB.commit()
        return 
