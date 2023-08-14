#for this section we have the class patient
#here we will be defining the methods we will be using for our code
#this will be reading the txt file that has been provided and also be setting new information in the txt file
#any function with the name get will read the txt file while you are entering the information of the patient. if the information for the patient is on the txt it will output the information.
#any function with the name set will be doing the opposite it will be crating a new patient or changing the information of the patient on the txt file
class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

#getting the patients id
    def get_pid(self):
        return self.pid

#getting the patients name
    def get_name(self):
        return self.name

#getting the patients disease 
    def get_disease(self):
        return self.disease

#getting the patients gender
    def get_gender(self):
        return self.gender

#getting the patients age    
    def get_age(self):
        return self.age

#setting the patients new id  
    def set_pid(self, new_pid):
        self.pid = new_pid

#setting the patients new name
    def set_name(self, new_name):
        self.name = new_name

#setting the patients new disease   
    def set_disease(self, new_disease):
        self.disease = new_disease

#setting the patients new gender 
    def set_gender(self, new_gender):
        self.gender = new_gender

#setting the patients new age
    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"

#this is the main section of code for the patient section
#here is class patient manager 
#anything that is being used in the code involving patients is in this section of code
class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()
    
    def format_patient_info_for_file(self, patient):
        return str(patient)

#this is the main menu that is prompted when you select patient 
#here it will ask the users the patients information and ask what they should be entering for the patient information
#here this will call from the patient class to read and confirm the infromation being entered 
#it will also call on the class for the functions that are being used in this section. ex. pid or name 
    def enter_patient_info(self):
        pid = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")
        patient = Patient(pid, name, disease, gender, age)
        return patient

#this is where the code reads the patients file which is set by "r" for this it will read the lines of the txt to again confirm the patients information and output the information as well
    def read_patients_file(self):
        with open("C:\class\patients.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                patient_info = line.strip().split("_")
                pid, name, disease, gender, age = patient_info
                patient = Patient(pid, name, disease, gender, age)
                self.patients.append(patient)

#this is going to be searching for the patients ID
    def search_patient_by_id(self):
        patient_id = input("Enter patient ID to search: ")
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                self.display_patient_info(patient)
                return
        print("Can't find the patient...")

#this is displaying the info of the patient
    def display_patient_info(self, patient):
        print(f"Patient ID: {patient.get_pid()}")
        print(f"Patient Name: {patient.get_name()}")
        print(f"Patient Disease: {patient.get_disease()}")
        print(f"Patient Gender: {patient.get_gender()}")
        print(f"Patient Age: {patient.get_age()}")

#here is where all the editing to the patients information takes place
    def edit_patient_info_by_id(self):
        patient_id = input("Enter patient ID to edit: ")
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                name = input("Enter new name: ")
                disease = input("Enter new disease: ")
                gender = input("Enter new gender: ")
                age = input("Enter new age: ")
                patient.set_name(name)
                patient.set_disease(disease)
                patient.set_gender(gender)
                patient.set_age(age)
                self.write_list_of_patients_to_file()
                print("Patient info has been updated.")
                return
        print("Can't find the patient...")

#here is the section that will display the patients list  
    def display_patients_list(self):
        for patient in self.patients:
            self.display_patient_info(patient)
            print()

#here is where the code will write new patients or new inforamtion is done. 
#the reason is writing instead of reading is done by "w"
    def write_list_of_patients_to_file(self):
        with open("C:\class\patients.txt", "w") as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient) + "\n")
        print("Patients list written to file successfully!")

#this is where you will be adding a patient to the file and there information     
    def add_patient_to_file(self):
        patient = self.enter_patient_info()
        self.patients.append(patient)
        with open("C:\class\patients.txt", "a") as file:
            file.write(self.format_patient_info_for_file(patient) + "\n")
        print("New patient added successfully!")

repeat = True