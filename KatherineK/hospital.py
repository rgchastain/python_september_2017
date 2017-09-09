# Hospital Assignment

# Create Hospital with methods admit, discharge
import random

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.meds = 10

    def admit(self, patient):
        if len(self.patients) == self.capacity :
            print "There are no beds available at this time."
        else:
            self.patients.append(patient)
            patient.inpatient()
            print "Patient admitted."
        return self

    def discharge(self, patient):
        self.patients.remove(patient)
        print "Patient discharged."
        return self

    def dispense(self, pills):
        self.meds -= pills
        return self

class Doctor(object):
    def __init__(self, name):
        self.name = name
        print "Hello, Dr. {}." .format(self.name)

    def admit(self, patient, reply):
        if reply == "Y" or reply == "y" or reply == "Yes" :
            mercywest.admit(patient)
            return self
        else:
            initiatenewpatient()

    def discharge(self, patient):
        mercywest.discharge(patient)
        return self

    def choosetreatment(self, patient):
        self.treat(patient, raw_input("Would you like to prescribe medication (M), or perform surgery (S)?"))

    def treat(self, patient, plan):
        if plan == "M" or plan == "m":
            self.medicate(patient, int(raw_input("How many pills (1-10) would you like to prescribe?")))
        if plan == "S" or plan == "s" :
            self.surgery(patient)

    def medicate(self, patient, pills):
        mercywest.dispense(pills)
        if patient.allergies == 1 :
            allergicreaction = random.random()*100
            if allergicreaction <= 40 :
                patient.sicken(30)
                print "Your patient had an allergic reaction to the medication you prescribed."
                return self
        patient.heal(20)
        patient.display()
        return self

    def surgery(self, patient):
        outcome = random.random()*100
        if outcome <= 10 :
            print "Your patient coded on the table and died."
            return self
        if patient.health >= 50 :
            patient.heal(30)
            patient.display()
            return self
        patient.heal(10)
        patient.display()
        self.choosetreatment(patient)
        return self

# Create class Patient, add methods .heal() and .sicken()
class Patient(object):
    id = 1
    def __init__(self, firstname, lastname, age):
        self.id = Patient.id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        allergies = random.random()
        if allergies < 0.5 :
            self.allergies = 1
        else :
            self.allergies = 0
        self.bednumber = 0
        self.health = int((random.random())*100)
        self.status = "New Patient"
        Patient.id += 1
        print "New Patient status report:"
        self.display()

    def inpatient(self):
        self.bednumber = int(random.random()+100)
        self.status = "Admitted"
        return self

    def recover(self):
        self.status = "Discharged"
        self.bednumber = 0
        self.display
        print "You patient has fully recovered! Good job Dr. {}!" .format(doctor.name)

    def heal(self, val):
        if self.health > 100 :
            self.recover
        self.health += val
        doctor.choosetreatment(self)
        return self

    def sicken(self, val):
        if self.health < 20 :
            print "Your patient has died."
            return self
        self.health -= val
        doctor.choosetreatment(patient)
        return self

    def display(self):
        print "*"*25
        print "Stats:"
        print "{}, {} // Age: {}" .format(self.lastname, self.firstname, self.age)
        print "{} // Bednumber: {}" .format(self.status, self.bednumber)
        print "Allergies: {} // Current Health: {}/100" .format(self.allergies, self.health)
        print "*"*25




#GamePlay:



# Create an instance of Hospital

mercywest = Hospital("Mercy West", 5)

# Create and instance of doctor

doctor = Doctor(raw_input("You are a doctor at Mercy West Hospital. What is your name? "))

# Create a new patient:

def initiatenewpatient():

    patient = Patient(raw_input("You have a new patient. What is his/her first name? "), raw_input("What is his/her last name? "), raw_input("What is his/her age? "))

    if patient.health > 75 :
        print "Your patient needs treatment."
    else :
        print "Your patient needs treatment urgently."
    doctor.admit(patient, raw_input("Would you like to admit him/her to your hospital? Y/N --"))

    print "Your patient needs a treatment plan. You can choose between medication and surgery. Medication may cause an allergic reaction, but can improve patient health. Surgery can, in rare cases, be fatal, but if your patient's health is over 50, it may be curative."

    doctor.choosetreatment(patient)

# Begin Game

initiatenewpatient()

# Select treatment plan:
