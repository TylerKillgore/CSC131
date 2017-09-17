#Project One Medical Diagnosis
#Tyler Killgore


"""
Application Name: Medical Diagnosis

Purpose: Program asks patient to enter today's month and day (e.g., 3 14), full name, body temperature, and if patient
is experiencing congestion, aches, and/or a rash. Program then determines diagnosis of either healthy, cold, flu,
measles or uncertain based on patient input.


"""

# function to take patient_info into consideration for diagnosis


def get_patient_diagnosis():
    if patient_temperature < 99:
        if patient_congestion == "n" or "N" and patient_aches == "n" or "N" and patient_rash == "n" or "N":
            print("Diagnosis: Healthy")
        else:
            print("Diagnosis: Uncertain")
    elif 100 < patient_temperature > 99:
        if patient_congestion == "y" or "Y":
            print("Diagnosis: Cold")
        else:
            print("Diagnosis: Uncertain")
    elif patient_temperature > 100 or patient_temperature == 100:
        if patient_aches == "y" or "Y":
            print("Diagnosis: Flu")
        elif patient_rash == "y" or "Y":
            print("Diagnosis: Measles")
    else:
        print("Diagnosis: Uncertain")



# take in patient information as input() and call get_patient_diagnosis function
# and assign diagnosis to patient_diagnosis variable


patient_name = input("Patient Name: ")
patient_date = input("Month Day (e.g., 3 25): ")
patient_temperature = float(input("Temperature: "))
patient_congestion = input("Congestion (y,n): ")
patient_aches = input("Aches (y,n): ")
patient_rash = input("Rash (y,n): ")


# slice numbers from input for date output of month/day/year, checking for whether m or mm

if len(patient_date) < 5:
    date_month = patient_date[0:1]
    date_day = patient_date[2:4]
    return_date = "{}/{}/2017".format(date_month, int(date_day) + 2)
else:
    date_month = patient_date[0:2]
    date_day = patient_date[3:5]
    return_date = "{}/{}/2017".format(date_month, int(date_day) +2)
# response following program run
print()
print()
print("Patient: {}".format(patient_name))
print("Date: {}/{}/2017".format(date_month,date_day))
get_patient_diagnosis()
print("Return Date: {}".format(return_date))
