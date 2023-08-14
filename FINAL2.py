#Names: Reem Rasheed Sarah Fletcher Cooper Armstrong
#Date: August 10th 2023

#Alberta Hospital (AH) management system is a program designed to sort, store and read patient and doctor information at the alberta hosptial

#This class houses all of the functions to read and write individual sections of the doctors information
class Doctor:
    #This sets all the variables used in the class
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
    
    #When called the get function will locate doctors in the doctors.txt file using their id
    def get_doctor_id(self):
        return self.doctor_id
    
    #The set doctor id function will set a new id to a doctor
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id
        
    #This get function will locate doctors in the text file using their name
    def get_name(self):
        return self.name
    
    #The set name function will write a new name to a doctor 
    def set_name(self, new_name):
        self.name = new_name
        
    #This function will locate doctors specializations via the text file as it is a get funcation
    def get_specialization(self):
        return self.specialization
    
    #Being a set function this will write a new specialization for a doctor in the text file when called
    def set_specialization(self, new_specialization):
        self.specialization = new_specialization
        
    def get_working_time(self):
        return self.working_time
    
    def set_working_time(self, new_working_time):
        self.working_time = new_working_time
        
    def get_qualification(self):
        return self.qualification
    
    def set_qualification(self, new_qualification):
        self.qualification = new_qualification
        
    def get_room_number(self):
        return self.room_number
    
    def set_room_number(self, new_room_number):
        self.room_number = new_room_number
    
    #This function outputs the information in the correct format 
    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"
        
#This class houses all of the functions that actually read and write the text files using the functions and variables created above
class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()
    
    #This function calls on the last function in the Doctor class formatting the doctors information to be printed correctly
    def format_dr_info(self, doctor):
        return str(doctor)
        
    #This function allows the user to input new doctor information based on each section
    def enter_dr_info(self):
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Doctor Specialization: ")
        working_time = input("Enter Doctor Working Time: ")
        qualification = input("Enter Doctor Qualification: ")
        room_number = input("Enter Doctor Room Number: ")
        
        new_doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
        
        return new_doctor

    #This function opens and reads the doctors.txt file
    def read_doctors_file(self):
        with open("C:\class\doctors.txt", "r") as file:
            for line in file:
                doctor_id, name, specialization, working_time, qualification, room_number = line.strip().split("_")
                new_doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
                self.doctors.append(new_doctor)
                
    #This function searches the text file for a doctor match via the users input for and ID
    def search_doctor_by_id(self):
        doctor_id = input("Enter Doctor ID: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor...")
    
    #This function searches the text file for a doctor match via the users input for a Doctor Name
    def search_doctor_by_name(self):
        name = input("Enter Doctor Name: ")
        for doctor in self.doctors:
            if doctor.get_name() == name:
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor...")
        
    #This function prints the doctors information in the correct format
    def display_doctor_info(self, doctor):
        print(f"Doctor ID: {doctor.get_doctor_id()}")
        print(f"Name: {doctor.get_name()}")
        print(f"Specialization: {doctor.get_specialization()}")
        print(f"Working Time: {doctor.get_working_time()}")
        print(f"Qualification: {doctor.get_qualification()}")
        print(f"Room Number: {doctor.get_room_number()}")

    #This function allows the user to edit the doctors information per each section
    def edit_doctor_info(self):
        doctor_id = input("Enter Doctor ID to Edit: ")
        doctor_found = False
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                doctor_found = True
                doctor.name = input("Enter New Doctor Name: ")
                doctor.specialization = input("Enter New Doctor Specialization: ")
                doctor.working_time = input("Enter New Doctor Working Time: ")
                doctor.qualification = input("Enter New Doctor Qualification: ")
                doctor.room_number = input("Enter New Doctor Room Number: ")
                self.write_list_of_doctors_to_file()
                print("Doctor edited successfully.")
                break
        if not doctor_found:
            print(f"Cannot find the doctor with ID {doctor_id}.")

    #This function prints the list of doctors via the text file 
    def display_doctors_list(self):
        for doctor in self.doctors:
            print(f"Doctor ID: {doctor.get_doctor_id()}")
            print(f"Name: {doctor.get_name()}")
            print(f"Specialization: {doctor.get_specialization()}")
            print(f"Working Time: {doctor.get_working_time()}")
            print(f"Qualification: {doctor.get_qualification()}")
            print(f"Room Number: {doctor.get_room_number()}")

    #This function writes the users input information into the text file
    def write_list_of_doctors_to_file(self):
        with open("C:\class\doctors.txt", "w") as file:
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor))

    #This function adds the new created doctor onto the doctors.txt file
    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        with open("C:\class\doctors.txt", "a") as file:
            file.write(self.format_dr_info(new_doctor))
        print("Doctor added successfully.")

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

#This class houses all of the functions for the main and individual submenus
class Management:
    def __init__(self, doctors_file, patients_file):
        self.doctors_file = doctors_file
        self.patients_file = patients_file

#This function prints the main menu with 3 options the two sub menus and the quit program
    def display_menu(self):
        while repeat:
            print("\nMAIN MENU\n1. Doctors\n2. Patients\n3. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.doctors_submenu()
            elif choice == "2":
                self.patients_submenu()
            elif choice == "3":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Try again.")

 #This function is called when the user selects 1 on the main menu
 #This function houses all of the options to use to read or write on the doctors file
    def doctors_submenu(self):
        while repeat:
            print("\nDOCTORS SUBMENU\n1. Display Doctors\n2. Search Doctor by ID\n3. Search Doctor by Name\n4. Add Doctor\n5. Edit Doctor\n6. Return to Main Menu")
            choice = input("Enter your choice: ")
            
            doctor_manager = DoctorManager()

            if choice == "1":
                doctor_manager.display_doctors_list()
            elif choice == "2":
                doctor_manager.search_doctor_by_id()
            elif choice == "3":
                doctor_manager.search_doctor_by_name()
            elif choice == "4":
                doctor_manager.add_dr_to_file()
            elif choice == "5":
                doctor_manager.edit_doctor_info()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Try again.")
         
    def patients_submenu(self):
        while repeat:
            print("\nPATIENTS SUBMENU\n1. Display Patients\n2. Search Patient by ID\n3. Edit Patient Info\n4. Add Patient\n5. Go back to MAIN MENU")
            choice = input("Enter your choice: ")

            patient_manager = PatientManager()

            if choice == "1":
                patient_manager.display_patients_list()
            elif choice == "2":
                patient_manager.search_patient_by_id()
            elif choice == "3":
                patient_manager.add_patient_to_file()
            elif choice == "4":
                patient_manager.edit_patient_info_by_id()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")


    
if __name__ == "__main__":
    management_instance = Management("doctors.txt", "patients.txt")
    management_instance.display_menu()




