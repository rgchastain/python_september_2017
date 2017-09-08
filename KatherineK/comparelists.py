a = [1,2,3]
b = [1,2,3]
same = 0

if len(a) != len(b) :
    print "These lists are not the same."
else :
    for i in range (0, len(a)) :
        if a[i] != b[i] :
            print "These lists are not the same."
            break
        elif a[i] == b[i] :
            same += 1
if same == len(a) :
    print "These lists are the same."
