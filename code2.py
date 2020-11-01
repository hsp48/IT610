# Hemali Patel

import datetime

d = datetime.datetime.utcnow()
Time = d.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n")


PatientName = input("Enter your name: ")
print("Welcome to your HealthRecord, " + PatientName)
print("Today is " + Time)

#PatientAddress = input("Enter your address: ")
#PatientDOB = input("Enter your Date of Birth (MM/DD/YYYY): ")


PatientWeight = input("Enter your Weight: ")
PatientTemp = input("Enter your Temperature: ")
PatientPulse = input("Enter your Pulse Rate: ")
PatientBloodPressure = input("Enter your Blood Pressure (Systolic/Diastolic): ")
Systolic = PatientBloodPressure.split("/")[0]
Diastolic = PatientBloodPressure.split("/")[1]
SRead = ""
DRead = ""
for i in Systolic:
    if int(Systolic) < 120:
        SRead = "Systolic - Normal"
    if int(Systolic) in range(120, 129):
        SRead = "Systolic - Elevated"
    if int(Systolic) in range(130, 139):
        SRead = "Systolic - High Blood Pressure (Hypertension) Stage 1"
    if int(Systolic) in range(140, 180):
        SRead = "Systolic - High Blood Pressure (Hypertension) Stage 2"
    if int(Systolic) >= 180:
        SRead = "Systolic - Hypertensive Crisis"
        #print("Systolic Reading Too High")
print(SRead)

for ii in Diastolic:
    if int(Diastolic) < 80:
        DRead = "Diastolic - Normal"
    if int(Diastolic) in range(80, 90):
        DRead = "Diastolic - High Blood Pressure (Hypertension) Stage 1"
    if int(Diastolic) in range(91, 120):
        DRead = "Diastolic - High Blood Pressure (Hypertension) Stage 2"
    if int(Diastolic) >= 120:
        #print("Diastolic Reading Too High")
        DRead = "Diastolic - Hypertensive Crisis"
print(DRead)
PatientOxygen = input("Enter your SPO2 Reading: ")
PatientNotes = input("Enter any Notes: ")