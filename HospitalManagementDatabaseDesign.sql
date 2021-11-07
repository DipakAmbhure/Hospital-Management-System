
DROP DATABASE HospitalManagement;

CREATE DATABASE HospitalManagement;

USE HospitalManagement;



CREATE TABLE `Addresses`(
	`ID` varchar(10) PRIMARY KEY,
	`LineNo1` varchar(50),
	`city` varchar(50),
	`pincode` int,
	`state` varchar(50)
);

CREATE TABLE `CommonDetails` (
  `ID` varchar(10) PRIMARY KEY,
  `Name` varchar(50),
  `AddressID` varchar(10),
  `ContactNo` varchar(15),
  `gender` varchar(7) check (`gender` in ('male','female','trans')),
  `DOB` date
);

CREATE TABLE `Doctors` (
  `ID` varchar(10) PRIMARY KEY,
  `grade` varchar(5) check (`grade` in ('HA','HB','HC','HD')),
  `wardNo` int,
  `specialization` varchar(15) check (`specialization` in ('MBBS','BDS','BHMS','MD','Ayurveda')),
  `salary` int,
  `WorkingSince` date
);

CREATE TABLE `Patient` (
  `ID` varchar(10) PRIMARY KEY,
  `prescription` varchar(255),
  `diagnosis` varchar(255)
);

CREATE TABLE `wards` (
  `No` int PRIMARY KEY,
  `Name` varchar(50) check (`Name` in ('EYES','EARS','BONES','MUSCLES','TESTS','CHILDRENS','WOMENS'))
);

CREATE TABLE `Rooms` (
  `RoomNo` int PRIMARY KEY 
);

CREATE TABLE `workers` (
  `ID` varchar(10) PRIMARY KEY,
  `wardNo` int,
  `position` varchar(255) check (`position` in ('PION','NURSE','WARDBOY','COMPOUNDER','RECEPTIONLIST','SECURITY')),
  `salary` int,
  `WorkingSince` date
);

CREATE TABLE `visitedBy` (
  `patientID` varchar(10),
  `visitorID` varchar(10),
  PRIMARY KEY (`patientID`, `visitorID`)
);

CREATE TABLE `visitor` (
  `visitorID` varchar(10) PRIMARY KEY,
  `Name` varchar(50),
  `ContactNo` varchar(15),
  `relation` varchar(20),
  `VisitedDate` Date,
  `VisitedTime` datetime
);

CREATE TABLE `Receipt` (
  `ID` varchar(10) PRIMARY KEY,
  `Date` date,
  `time` datetime,
  `DoctorID` varchar(10),
  `Problem` varchar(50)
);

CREATE TABLE `Payments` (
  `patientID` varchar(10),
  `chargesID` varchar(10),
  PRIMARY KEY (`patientID`, `chargesID`)
);

CREATE TABLE `AdmitedPatients` (
  `patientID` varchar(10),
  `wardNo` int,
  `roomNo` int,
  `From` datetime,
  `Till` datetime,
  PRIMARY KEY (`patientID`)
);

CREATE TABLE `Treated` (
  `patientID` varchar(10),
  `doctorID` varchar(10),
  `ondate` date,
  PRIMARY KEY (`patientID`, `doctorID`)
);

CREATE TABLE `hastoTreat` (
	`patientID` varchar(10),
	`doctorID` varchar(10),
	PRIMARY KEY (`patientID`, `doctorID`)
);

CREATE TABLE `Transaction` (
  `chargesID` varchar(10) PRIMARY KEY,
  `Date` date,
  `Amount` int
);

CREATE TABLE `WorkerAttendance` (
  `ID` varchar(10),
  `Day` date,
  PRIMARY KEY (`ID`, `Day`)
);

CREATE TABLE `DoctorT0Doctor` (
  `DoctorID` varchar(10),
  `patientID` varchar(10),
  `NextDoctorID` varchar(10),
  PRIMARY KEY (`DoctorID`, `patientID`, `NextDoctorID`)
);

CREATE TABLE `IDS` (
	`whos` varchar(10) PRIMARY KEY CHECK(`whos` in ('doctor','patient','worker','visitor','address')),
	`LastID` varchar(10)

);


ALTER TABLE `CommonDetails` ADD FOREIGN KEY (`AddressID`) REFERENCES `Addresses` (`ID`) ON DELETE SET NULL;


ALTER TABLE `Doctors` ADD FOREIGN KEY (`ID`) REFERENCES `CommonDetails` (`ID`) ON DELETE CASCADE;

ALTER TABLE `Doctors` ADD FOREIGN KEY (`wardNo`) REFERENCES `wards` (`No`) ON DELETE CASCADE;


ALTER TABLE `Patient` ADD FOREIGN KEY (`ID`) REFERENCES `CommonDetails` (`ID`) ON DELETE CASCADE;




ALTER TABLE  `AdmitedPatients` ADD FOREIGN KEY (`patientID`) REFERENCES `Patient` (`ID`) ON DELETE CASCADE;

ALTER TABLE `visitedBy` ADD FOREIGN KEY (`patientID`) REFERENCES  `AdmitedPatients` (`patientID`) ON DELETE CASCADE; 

ALTER TABLE `AdmitedPatients` ADD FOREIGN KEY (`wardNo`) REFERENCES `wards` (`No`) ON DELETE CASCADE;

ALTER TABLE `AdmitedPatients` ADD FOREIGN KEY (`roomNo`) REFERENCES `Rooms` (`RoomNo`) ON DELETE CASCADE;



ALTER TABLE `Payments` ADD FOREIGN KEY (`chargesID`) REFERENCES `Transaction` (`chargesID`) ON DELETE CASCADE;

ALTER TABLE  `Payments` ADD FOREIGN KEY (`patientID`) REFERENCES `Patient`  (`ID`)  ON DELETE CASCADE;


ALTER TABLE `workers` ADD FOREIGN KEY (`ID`) REFERENCES `CommonDetails` (`ID`) ON DELETE CASCADE;

ALTER TABLE `workers` ADD FOREIGN KEY (`wardNo`) REFERENCES `wards` (`No`) ON DELETE CASCADE;

ALTER TABLE `WorkerAttendance` ADD FOREIGN KEY (`ID`) REFERENCES `workers` (`ID`) ON DELETE CASCADE; 


ALTER TABLE `visitedBy` ADD FOREIGN KEY (`visitorID`) REFERENCES `visitor` (`visitorID`) ON DELETE CASCADE; 


ALTER TABLE `Receipt` ADD FOREIGN KEY (`ID`) REFERENCES `CommonDetails` (`ID`) ON DELETE CASCADE;

ALTER TABLE `Receipt` ADD FOREIGN KEY (`DoctorID`) REFERENCES `Doctors` (`ID`) ON DELETE CASCADE; 








ALTER TABLE `Treated` ADD FOREIGN KEY (`patientID`) REFERENCES `Patient`  (`ID`) ON DELETE CASCADE;

ALTER TABLE `Treated` ADD FOREIGN KEY (`doctorID`) REFERENCES `Doctors` (`ID`) ON DELETE CASCADE;



ALTER TABLE `DoctorT0Doctor` ADD FOREIGN KEY (`DoctorID`) REFERENCES `Doctors` (`ID`) ON DELETE CASCADE;

ALTER TABLE `DoctorT0Doctor` ADD FOREIGN KEY (`patientID`) REFERENCES `Patient` (`ID`) ON DELETE CASCADE;

ALTER TABLE `DoctorT0Doctor` ADD FOREIGN KEY (`NextDoctorID`) REFERENCES `Doctors` (`ID`) ON DELETE CASCADE;




ALTER TABLE `hastoTreat` ADD FOREIGN KEY (`patientID`) REFERENCES `Receipt` ( `ID` ) ON DELETE CASCADE;

ALTER TABLE `hastoTreat` ADD FOREIGN KEY (`doctorID`) REFERENCES `Doctors` ( `ID` ) ON DELETE CASCADE;


create table logindata (
  	ID varchar(10),
 	passkey varchar(5),
	primary key ( ID, passkey )
);

INSERT INTO logindata VALUES ( 'HA00987200', '1234' );

INSERT INTO logindata VALUES ( 'HM00000000', '1234');

INSERT INTO IDS VALUES ('address','HL00000000');

INSERT INTO IDS VALUES ('patient','HP00000000');

INSERT INTO IDS VALUES ('doctor','HD00000000');

INSERT INTO IDS VALUES ('worker','HW00000000');

INSERT INTO IDS VALUES ('visitor','HV00000000');



