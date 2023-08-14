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