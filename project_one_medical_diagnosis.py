#Project One Medical Diagnosis
#Tyler Killgore


"""
Application Name: Medical Diagnosis

Purpose: Program asks patient to enter today's month and day (e.g., 3 14), full name, body temperature, and if patient
is experiencing congestion, aches, and/or a rash. Program then determines diagnosis of either healthy, cold, flu,
measles or uncertain based on patient input.


"""


def ask_patient_name():
    global patient_name
    patient_name = input("Patient Name: ")

# ask for date input in form of mm dd and ensure valid date


def ask_patient_date():
    global patient_date
    global month
    global day
    global index_of_space

    patient_date = input("Month Day (e.g., 3 25): ")
    index_of_space = patient_date.find(" ")
    month = patient_date[0:index_of_space]
    day = patient_date[index_of_space + 1:5]
    month = int(month)
    day = int(day)

    if len(patient_date) > 5:
        print("Error.")
        exit(1)
    elif 0 <= month > 12:
        print("Error.")
        exit(1)
    elif 0 <= day > 31:
        print("Error.")
        exit(1)
    elif month in [1, 3, 5, 7, 8, 10] and 1 < day > 31:
        print("Error.")
        exit(1)
    elif month in [2] and 1 < day > 28:
        print("Error.")
        exit()
    elif month in [4, 6, 9, 11] and 1 < day > 30:
        print("Error.")
        exit(1)
    else:
        ()


def december_month():
    if int(day) >= 30:
        if int(day) == 30:
            return_date_day = "01";
        elif int(day) == 31:
            return_date_day = "02";
    else:
        return_date_day = int(day) + 2;
    print("Date: {}/{}/2017".format(month, day))
    print("Return Date: 01/{}/{}".format(return_date_day, return_year))
    get_patient_diagnosis()


def february_month():
    if int(day) >= 27:
        return_date_month = int(month) + 1;
    if int(day) == 27:
        return_date_day = "01";
    elif int(day) == 28:
        return_date_day = "02";
    else:
        return_date_day = int(day) + 2
        return_date_month = "02";
    print("Date: {}/{}/2017".format(month, day))
    print("Return Date: {}/{}/{}".format(return_date_month, return_date_day, return_year))
    get_patient_diagnosis()


def thirty_one_day_month():
    if int(day) >= 30:
        return_date_month = int(month) + 1
    if int(day) == 30:
        return_date_day = "01";
    elif int(day) == 31:
        return_date_day = "02";
    else:
        return_date_day = int(day) + 2
        return_date_month = month
    print("Date: {}/{}/2017".format(month, day))
    print("Return Date: {}/{}/2017".format(return_date_month, return_date_day))
    get_patient_diagnosis()

def thirty_day_month():
    if int(day) >= 29:
        return_date_month = int(month) + 1
        if int(date_day) == 29:
            return_date_day = "01"
        elif int(date_day) == 30:
            return_date_day = "02"
        else:
            return_date_day = int(date_day) + 2
            return_date_month = month
    print("Date: {}/{}/2017".format(month, day))
    print("Return Date: {}/{}/{}".format(return_date_month, return_date_day, return_year))
    get_patient_diagnosis()
# take in input from patient


def ask_patient_temp_and_symptoms():

    # global variables

    global patient_temperature
    global patient_congestion
    global patient_aches
    global patient_rash

    patient_temperature = float(input("Temperature: "))
    patient_congestion = input("Congestion (y,n): ")
    if patient_congestion in ["y", "Y", "n", "N"]:
        ()
    else:
        print("Error.")
        exit()
    patient_aches = input("Aches (y,n): ")
    if patient_aches in ["y", "Y", "n", "N"]:
        ()
    else:
        print("Error.")
        exit()
    patient_rash = input("Rash (y,n): ")
    if patient_rash in ["y", "Y", "n", "N"]:
        ()
    else:
        print("Error.")
        exit()

# function to take patient_info into consideration for diagnosis


def get_patient_diagnosis():

    # global variables

    global patient_aches
    global patient_rash
    global patient_congestion
    global patient_temperature

    if ((int(patient_temperature) < 99) and (patient_congestion == "n" or "N") and (patient_aches == "n" or "N") \
            and (patient_rash == "n" or "N")):
        diagnosis = "Healthy";
    elif ((int(patient_temperature) < 100) and (patient_congestion == "y" or "Y") and (patient_aches == "n" or "N") \
            and (patient_rash == "n" or "N")):
        diagnosis = "Cold";
    elif ((int(patient_temperature) >= 100) and (patient_congestion == "n" or "N") and (patient_aches == "y" or "Y")\
          and (patient_rash == "n" or "N")):
                diagnosis = "Flu";
    elif (int(patient_temperature) >= 100) and (patient_congestion == "n" or "N") and (patient_aches == "n" or "N")\
            and (patient_rash == "y" or "Y"):
                diagnosis = "Measles";
    else:
                diagnosis = "Uncertain";

    print("Diagnosis: {}".format(diagnosis))

# take in patient information as input() and call get_patient_diagnosis function
# and assign diagnosis to patient_diagnosis variable


# initial if and else statement mitigate having two chars or just one char for mm


def get_returns():
    global month
    global day
    global return_date_month
    global return_date_day
    global return_year


    if int(month) == 12 and int(day) >= 30:
        return_year = "2018";
    else:
        return_year = "2017";
    # All months with 31 days
    if int(month) in [1, 3, 5, 7, 8, 10]:
        thirty_one_day_month();
    # All months with 30 days
    elif int(month) in [4, 6, 9, 11]:
        thirty_day_month();
# Months with 28 days (only February)
    elif int(month) == 2:
        february_month();
# December
    elif int(month) == 12:
        december_month();



# sequence of events and functions
ask_patient_name()
ask_patient_date()
ask_patient_temp_and_symptoms()
print()
print()
print("Name: {}".format(patient_name))
get_returns()
