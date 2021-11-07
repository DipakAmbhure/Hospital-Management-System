from modules import *

def GeneratePassword():
        return str(random.randint(10,99))+str(random.randint(1,9))+str(random.randint(10,99))

def loginDataEntry(ID):
        password=GeneratePassword()
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        try:
                Database.execute(f"""
                        INSERT INTO logindata
                        values ('{ID}','{password}')
                """)
        except:
                pass
        HosDB.commit()
        return ID,password

def Isvalid(IDE,passen):
        HosDB = mysql.connector.connect(
                                host = "localhost", 
                                user = "Hospital", 
                                passwd = "Hospital@123", 
                                database = "HospitalManagement")
        Database = HosDB.cursor()
        IDE=str(IDE)
        passen=str(passen)
        print(passen)
        try:
                Database.execute(f"""
                        SELECT passkey FROM logindata
                        where ID='{IDE}'
                """)
                passd=Database.fetchall()[0][0]
        except:
                return False
        print(passd)
        HosDB.commit()
        return passen==passd
