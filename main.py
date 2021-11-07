#Main File

from patient import *
from doctor import *
from worker import *
from modules import *
from functionalities import *
from login import *



@app.route('/')
def Initial():
        return render_template('index.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
        ID = request.form['username']
        passwordd = request.form['passwordKey']
        if(Isvalid(ID, passwordd)):
                if(ID[1] == 'D'):
                        Name, WardNo, PatientToTreat, PatientTreated, specialization, salary, doj, WardName, grade = getDoctorData(ID)
                        return render_template('doctor.html', CommonDetails = "", Name = Name, ID = ID, WardNo = WardNo, PatientToTreat = PatientToTreat, 
                                                PatientTreated = PatientTreated, WardName = WardName, Grade = grade, specialization = specialization, doj = doj, salary = salary)
                if(ID[1] == 'W'):
                        Name, Attendance, WardNo, position, doj, salary, WardName = getDataOfWorker(ID)
                        return render_template("worker.html", CommonDetails = "", ID = ID, Name = Name, WardName = WardName, Attendance = Attendance, 
                                                WardNo = WardNo, position = position)
                if(ID[1] == 'A'):
                        return render_template("admin.html")

                if(ID[1] == 'P'):

                        Doctors, Admited, CommonDetails, Payments, Receipt, prescription, dignosis = GetPatientData(ID)
                        return render_template('patient.html', ID = ID, CommonDetails = CommonDetails, Doctors = Doctors, Admited = Admited, Payments = Payments, 
                                                Receipt = Receipt, prescription = prescription, dignosis = dignosis)

                if(ID[1] == 'M'):
                        Payments, Remaining = GetAllPayments()
                        return render_template('charges.html', Payments = Payments, Remaining = Remaining)
         

        else:
                return render_template('index.html', info = 'invalid user')

@app.route("/gobackadmin", methods = ["GET", "POST"])
def gobackadmin():
        return render_template('admin.html')

@app.route("/gobackindex", methods = ["GET", "POST"])
def gobackindex():
        return render_template('index.html')

@app.route("/gobackcharges", methods = ["GET", "POST"])
def gobackcharges():
        Payments, Remaining = GetAllPayments()
        return render_template('charges.html', Payments = Payments, Remaining = Remaining)


@app.route('/addward', methods = ["POST", "GET"])
def addward():
        WardName = request.form['wardName']
        WardNo = request.form['wardNo']
        if(not WardName):
                return render_template('admin.html', info1 = "Enter WardName")
        
        if(not WardNo):
                return render_template('admin.html', info1 = "Enter Ward No")

        wardsEntry(int(WardNo), WardName)
        return render_template('admin.html')


@app.route("/register", methods = ["POST", "GET"])
def register():
        Name = request.form["name"]
        if(not Name): return render_template('index.html', info1 = "Please Enter Name")
        if(Name.strip() == ""): return render_template('index.html', info1 = "Invalid Name")
        contact = request.form['contact']
        if(not contact or contact.strip() == ''): return render_template('index.html', info1 = "invalid contact")
        dob = request.form['dob']
        if(not dob or dob.strip() == ''): return render_template('index.html', info1 = "select date of birth ")
        gender = request.form.getlist('gender')[0]
        if(not gender): return render_template('index.html', info1 = "Please select Gender")
        l1 = request.form['LineNo1']
        if(not l1 or l1.strip() == ''): render_template('index.html', info1 = "Enter Line1 of address")
        city = request.form['city']
        if(not city or city.strip() == ''): render_template('index.html', info1 = 'Enter city')
        pincode = request.form['pincode']
        if(not pincode or pincode.strip == ''): render_template('index.html', info1 = 'Enter pincode')
        state = request.form['state']
        if(not state or state.strip() == ''): render_template('index.html', info1 = "Enter State")
        problem =  request.form.getlist('problem')[0]
        if(not problem): render_template('please select your problem else choose other')
        DoctorID, WardNo, PID = RegisterPatient(Name, [l1, city, pincode, state], contact, gender, dob, problem)
        TellDoctor(PID, DoctorID)
        PID, password = loginDataEntry(PID)
        return render_template("registerSuccessfully.html", info = 'index', infoID = PID, infopas = password)



@app.route('/addroom', methods = ['POST', 'GET'])
def addroom():
        RoomNo = request.form['roomNo']
        if(not RoomNo): return render_template('admin.html', info2 = 'Enter Room No')
        RoomsEntry(int(RoomNo))
        return render_template('admin.html')    


@app.route('/adddoctor', methods = ['POST', 'GET'])
def adddoctor():
        Name = request.form["name"]
        if(not Name): return render_template('admin.html', info3 = "Please Enter Name")
        contact = request.form['contact']
        if(not contact or contact.strip() == ''): return render_template('admin.html', info3 = "invalid contact")
        dob = request.form['dob']
        print(dob)
        if(not dob): return render_template('admin.html', info3 = "select date of birth ")

        gender = request.form.getlist('gender')[0]
        if(not gender): return render_template('admin.html', info3 = "Please select Gender")
                
        l1 = request.form['LineNo']
        print(l1)
        if(not l1 or l1.strip() == ''): render_template('admin.html', info3 = "Enter Line1 of address")
        city = request.form['city']
        if(not city or city.strip() == ''): render_template('admin.html', info3 = 'Enter city')
        pincode = request.form['pincode']
        if(not pincode or pincode.strip == ''): render_template('admin.html', info3 = 'Enter pincode')
        state = request.form['state']
        if(not state or state.strip() == ''): render_template('admin.html', info3 = "Enter State")
        specialization = request.form['specialization']
        if(not specialization): render_template('admin.html', info3 = "Enter Specialization")
        salary = request.form['salary']
        if(not salary): render_template('admin.html', info3 = "Enter Salary")
        wardNo = request.form['WardNo']
        if(not wardNo): render_template('admin.html', info3 = "Enter Ward")
        doj = request.form['doj']
        if(not doj): render_template('admin.html', info3 = 'Enter Date of joining')
        grade = request.form['grade']
        if(not grade): render_template('admin.html', info3 = 'Enter grade')
        DID = EnterDoctor(Name, [l1, city, pincode, state], contact, gender, dob, specialization, wardNo, salary, doj, grade)
        DID, password = loginDataEntry(DID)
        return render_template("registerSuccessfully.html", info = 'admin', infoID = DID, infopas = password)

@app.route('/showalldoctordata', methods = ['POST', 'GET'])
def givealldoctordata():
        ID = request.form['Id']
        print(ID)
        CommonDetails = getCommonDetails(ID)
        print(CommonDetails)
        Name, WardNo, PatientHasToTreat, TreatedPatient, specialization, salary, doj, WardName, Grade = getDoctorData(ID)
        return render_template('doctor.html', CommonDetails = CommonDetails, Name = Name, ID = ID, WardNo = WardNo, WardName = WardName, 
                        Grade = Grade, PatientToTreat = PatientHasToTreat, PatientTreated = TreatedPatient, specialization = specialization, doj = doj, salary = salary)



@app.route('/addworker', methods = ['POST', 'GET'])
def addworker():
        Name = request.form["name"]
        if(not Name): return render_template('admin.html', info4 = "Please Enter Name")
        if(Name.strip() == ""): return render_template('admin.html', info4 = "Invalid Name")
        contact = request.form["contact"]
        if(not contact or contact.strip() == ''): return render_template('admin.html', info4 = "invalid contact")
        dob = request.form["dob"]
        
        if(not dob or dob.strip() == ''): return render_template('admin.html', info4 = "select date of birth ")
        gender = request.form.getlist('gender')[0]
        if(not gender): return render_template('admin.html', info4 = "Please select Gender")
        l1 = request.form['LineNo1']
        if(not l1 or l1.strip() == ''): render_template('admin.html', info4 = "Enter Line1 of address")
        city = request.form['city']
        if(not city or city.strip() == ''): render_template('admin.html', info4 = 'Enter city')
        pincode = request.form['pincode']
        if(not pincode or pincode.strip == ''): render_template('admin.html', info4 = 'Enter pincode')
        state = request.form['state']
        if(not state or state.strip() == ''): render_template('admin.html', info4 = "Enter State")
        positio = request.form['position']
        if(not positio): render_template('admin.html', info4 = "Enter Position")
        salary = request.form['salary']
        if(not salary): render_template('admin.html', info4 = "Enter Salary")
        wardNo = request.form['WardNo']
        if(not wardNo): render_template('admin.html', info4 = "Enter Ward")
        doj = request.form['doj']
        if(not doj): render_template('admin.html', info4 = 'Enter Date of joining')
        WID = EnterWorker(Name, [l1, city, pincode, state], contact, gender, dob, positio, wardNo, salary, doj)
        WID, password = loginDataEntry(WID)
        return render_template("registerSuccessfully.html", info = 'admin', infoID = WID, infopas = password)


@app.route('/submitattendance', methods = ['POST', 'GET'])
def submitAttendance():
        status = request.form.getlist('attendance')[0]
        ID = request.form.getlist('Id')[0]
        print(ID)
        if(status == 'present'):
                markPresent(ID)
        Name, Attendance, WardNo, position, doj, salary, WardName = getDataOfWorker(ID)
        return render_template("worker.html", CommonDetails = "", ID = ID, Name = Name, Attendance = Attendance, WardName = WardName, doj = doj, 
                                        salary = salary, WardNo = WardNo, position = position)

@app.route('/showallworkerdata', methods = ['POST', 'GET'])
def giveallworkerdata():
        ID = request.form['Id']
        print(ID)
        CommonDetails = getCommonDetails(ID)
        print(CommonDetails)
        Name, Attendance, WardNo, position, doj, salary, WardName = getDataOfWorker(ID)
        return render_template("worker.html", CommonDetails = CommonDetails, ID = ID, Name = Name, WardName = WardName, Attendance = Attendance, 
                                WardNo = WardNo, position = position, doj = doj, salary = salary)


@app.route('/treatpatient', methods = ['POST', 'GET'])
def treatpatient():
        PID = request.form['PId']
        DID = request.form['DId']
        DATA, admited = getPatientTreatementData(PID)
        print(admited)
        return render_template('treatment.html', PID = PID, DID = DID, DATA = DATA, admited = admited)

@app.route('/enterdata', methods = ["POST", "GET"])
def EnterpatientData():
        PID = request.form['PId']
        DID = request.form['DId']
        admited = request.form['admited']
        diagnosis = request.form['diagnosis']
        prescription = request.form['prescription']
        admit = request.form.getlist('admit')[0]
        nextdoctor = request.form.getlist('nextdoctor')[0]

        if(not diagnosis): info1 = "Enter Diagnosis"
        elif(not prescription): info1 = "Enter Prescription"
        elif(not nextdoctor): info1 = "Select Next Doctor Status"
        elif(not admit): info1 = "Select Admit Status"
        PatientEntry(PID, prescription, diagnosis)
        flag = 0
        if(nextdoctor == 'yes'):
                nextG = request.form['nextgrade']
                if(not nextG or nextG not in ['HA', 'HB', 'HC']):
                        DATA, admited = getPatientTreatementData(PID)
                        return render_template('treatment.html', info1 = "Plese enter next doctor grade i.e HA, HB, HC ", PID = PID, DID = DID, DATA = DATA, admited = admited)
                NDID = AssignNextDoctor(PID, DID, nextG)
                flag = 1
        if(admited == 'False' and admit == 'yes'):
                print("here")
                AdmitPatient(PID, DID)
        if(admited == 'True' and admit == 'yes'):
                DischargePatient(PID)
                flag = 1
        if(flag):
                print("here2")
                deleteFromHasToTreat(PID, DID)
                TreatedEntry(PID, DID, date.today())

        Name, WardNo, PatientHasToTreat, AlTreatedPatient, specialization, salary, doj, WardName, grade = getDoctorData(DID)
        return render_template('doctor.html', CommonDetails = "", Name = Name, ID = DID, WardNo = WardNo, Grade = grade, WardName = WardName, 
                                PatientToTreat = PatientHasToTreat, PatientTreated = AlTreatedPatient, specialization = specialization, doj = doj, salary = salary)

        
@app.route("/makepayment", methods = ["GET", "POST"])
def makepayment():
        ID = request.form['PID']
        if(DoNotExists(ID)):
                info = "Patient Doesn't Exist"
                return render_template('charges.html', info = info)

        try:           
                amount = int(request.form['amount'])
        except:
                info = "Invalid Amount"
                return render_template('charges.html', info = info)
        
        datee = SaveRecord(ID, amount)
        return render_template('paidsuccessfully.html', DATE = datee, infoID = ID,infoAmount = amount,info = 'charges')


@app.route("/visitor", methods = ["POST","GET"])
def visitors():
        Name     = request.form["name"]
        Contact  = request.form["contact"] 
        Relation = request.form["relation"]
        PID      = request.form["PID"]
        VID = getNextID(getLastId('visitor'))
        ChangeLastIdTo(VID)
        visitorEntry(VID,Name,Contact,Relation,date.today(),datetime.now())
        visitedByEntry(PID,VID)
        return render_template("index.html",infov = "Visitor Can Visit Now")


app.run(debug = True)




