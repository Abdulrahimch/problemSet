#  Three status
# A for 'Absent', P for 'Present', L for 'Late'
# return False(Student does not deserve attendence award) if they get three consecutive 'L', or more than 2 'A'
def student_attendence_rec(s):
    return not (s.count('A') >= 2 or s.count('LLL') > 0)


print(student_attendence_rec('NJASNFKAJSD'))
