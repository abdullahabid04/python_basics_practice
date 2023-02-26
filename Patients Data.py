import sys


patients = []

BMI = 0.0
Weight = 0.0
Height = 0.0
Temperature = 0.0
Heartbeat = 0.0
Age = 0.0

try:
    file = open("files/Patient_Data_1.txt", 'r')
except FileNotFoundError as error:
    print(error)
    sys.exit(0)

for line in file:
    patient = [item.strip() for item in line.split(" ")]
    patients.append(patient)

print("============================================================================")
print("Underweight Patients : \n")

for i in range(10):
    Weight = float(patients[i][1])
    Height = float(patients[i][2])
    BMI = Weight / (Height * Height)
    if BMI <= 18.5:
        print('\t', i + 1, '\t', BMI)

print("============================================================================")
print("Normal Patients : \n")

for i in range(10):
    Weight = float(patients[i][1])
    Height = float(patients[i][2])
    BMI = Weight / (Height * Height)
    if 18.5 <= BMI <= 25:
        print('\t', i + 1, '\t', BMI)

print("============================================================================")
print("Overweight Patients : \n")

for i in range(10):
    Weight = float(patients[i][1])
    Height = float(patients[i][2])
    BMI = Weight / (Height * Height)
    if BMI > 25:
        print('\t', i + 1, '\t', BMI)
print("============================================================================")
print("Overweight Patients with Normal Temperature & Normal Heartbeat : \n")

for i in range(10):
    Weight = float(patients[i][1])
    Height = float(patients[i][2])
    Heartbeat = float(patients[i][3])
    Temperature = float(patients[i][4])
    BMI = Weight / (Height * Height)
    if (BMI > 24.9) and ((98.6 <= Temperature <= 100) or (70 <= Heartbeat <= 95)):
        print('\t', i + 1, '\t', "BMI : " + str(BMI) + " Temperature : " + str(Temperature) + " Heartbeat : " + str(Heartbeat))

print("============================================================================")
print("Patients older than 40 years with Normal BMI & Abnormal Temperature : \n")

for i in range(10):
    Weight = float(patients[i][1])
    Height = float(patients[i][2])
    Heartbeat = float(patients[i][3])
    Temperature = float(patients[i][4])
    Age = float(patients[i][0])
    BMI = Weight / (Height * Height)
    if (18.8 < BMI < 25) and (Temperature < 98.6 or Temperature > 100) and (Age > 40):
        print('\t', i + 1, '\t', "BMI : " + str(BMI) + " Temperature : " + str(Temperature) + " Heartbeat : " + str(Heartbeat))

print("============================================================================")
print("Underweight Patients of age group (10-40) : \n")

for i in range(10):
    Weight = float(patients[i][1])
    Height = float(patients[i][2])
    Heartbeat = float(patients[i][3])
    Temperature = float(patients[i][4])
    Age = float(patients[i][0])
    BMI = Weight / (Height * Height)
    if (BMI < 18.5) and (10 < Age < 40):
        print('\t', i + 1, '\t', "BMI : " + str(BMI) + " Age : " + str(Age))

print("============================================================================")
