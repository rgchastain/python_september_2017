# Hospital Assignment

# Create Hospital with methods admit, discharge
class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []

    def admit(self, patient):
        if len(self.patients) == self.capacity :
            print "There are no beds available at this time."
        else:
            self.patients.append(patient)
            patient.bednumber = patient.id
            print patient.name, " admitted."
        return self

    def discharge(self, patient):
        self.patients.remove(patient)
        print "Patient discharged."
        return self

# Create class Patient
class Patient(object):
    id = 1
    def __init__(self, name, allergies="None"):
        self.id = Patient.id
        self.name = name
        self.allergies = allergies
        self.bednumber = 0
        Patient.id += 1
        print self.name, " created"

# Creating instances of both classes:

mercywest = Hospital("Mercy West", 5)

meredithgrey = Patient("Meredith Grey")
christinayang = Patient ("Christina Yang", "emotional intimacy")
mcdreamy = Patient("Derek Shephard", "bad hair")
mcsteamy = Patient("Mark Sloane")
lexigrey = Patient ("Lexi Grey")
mirandabailey = Patient ("Miranda Bailey", "penicillin")

# Admitting patients

cast = [meredithgrey, christinayang, mcdreamy, mcsteamy, lexigrey, mirandabailey]

for people in cast:
    mercywest.admit(people)

# Discharge a patient to make room for another patient

mercywest.discharge(mcsteamy).admit(mirandabailey)
