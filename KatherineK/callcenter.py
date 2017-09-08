
# "Hacker Level"

#Create class CallCenter, with methods add, remove, removebyphone, info, and sort

class CallCenter(object) :
    def __init__(self) :
        self.calls = []
        self.queuesize = 0

    def add(self, call) :
        self.calls.append(call)
        self.queuesize += 1

    def remove(self, call) :
        self.calls.remove(call)
        self.queuesize -= 1

    def removebyphone(self, phone) :
        for calls in self.calls :
            if calls.phone == phone :
                self.remove(calls)
        print "------------------"
        self.info()

    def info(self) :
        for calls in self.calls :
            calls.display()
            print self.queuesize

# Selection sorts by hour, then bubble sorts by min. Yes, I know I could just use .sort() but this is good practice
    def sort(self) :
        a = 0
        temp = 0
        for calls in self.calls :
            for i in range(a, len(self.calls)) :
                if self.calls[a].hour > self.calls[i].hour :
                    temp = self.calls[a]
                    self.calls[a] = self.calls[i]
                    self.calls[i] = temp
            a += 1
        for calls in self.calls :
            for i in range(a, len(self.calls)) :
                if self.calls[a].hour == self.calls[i].hour and self.calls[a].min > self.calls[a].min :
                    self.calls[a], self.calls[i] = self.calls[i], self.calls[a]
        print "------------------"
        self.info()


# create class Call, with method display

class Call(object):
    id = 1
    def __init__(self, name, phone, hour, min, reason, id=id):
        self.id = Call.id
        self.name = name
        self.phone = phone
        self.hour = hour
        self.min = min
        self.reason = reason
        Call.id += 1

    def display(self):
        print "Id: {} / Name: {} / Phone: {} / Time: {}:{} / Reason: {}".format(self.id, self.name, self.phone, self.hour, self.min, self.reason)

# Testing:

# Create new instance of CallCenter
callcenter1 = CallCenter()

# Create 5 instances of Call
call1 = Call('Holly', 214, 1, 30, "question")
call2 = Call('Phylis', 225, 2, 30, "question")
call3 = Call('GlAdos', 298, 3, 30, "complaint")
call4 = Call('Chel', 456, 1, 20, "inaudible")
call5 = Call('Annie', 879, 6, 30, "question")

# Add calls using .add() method
callcenter1.add(call1)
callcenter1.add(call2)
callcenter1.add(call3)
callcenter1.add(call4)
callcenter1.add(call5)

# Print info using .info() method, which calls .display() method in the Call class
callcenter1.info()

# Remove a call from the call log by phone number, print remaining
callcenter1.removebyphone(214)

#Sort the call log by time of call
callcenter1.sort()
