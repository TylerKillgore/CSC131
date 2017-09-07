#Project One Medical Diagnosis
#Tyler Killgore

def get_patient_info():
    patient_name = input("Patient Name: ")
    patient_date = input("Month Day (e.g., 3 25): ")
    patient_temperature = input("Temperature: ")
    patient_congestion = input("Congestion (y,n): ")
    patient_aches = input("Aches (y,n): ")
    patient_rash = input("Rash (y,n): ")
    return(patient_name, patient_date, patient_temperature, patient_congestion, patient_aches, patient_rash)


#take patient_info into consideration for diagnosis

#def get_patient_diagnosis():


get_patient_info()

