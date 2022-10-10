from slist import SList
from course import Course


def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.grade() * course.credit_hr()
        credits += course.credit_hr()
    return sumGrades / credits


def is_sorted(lyst):
    for i in range(0, len(lyst) - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True


def main():
    test_slist()
    # test_course()


# def test_course():
    
#     for i in range(10):
#         course = Course(i, "" + str(i), )
#     courseList = 

def test_slist():
    lyst = SList()
    lyst.insert(12)
    lyst.insert(24)
    lyst.insert(10)
    lyst.insert(1)
    lyst.insert(32)
    lyst.insert(4)
    lyst.insert(1)   
    print("lyst: ", lyst)
    print("sorted: ", is_sorted(lyst))
    print(lyst.find(10))
    print(lyst.remove(10))
    print(lyst.find(10))
    print(lyst.remove(10))
    print("lyst: ", lyst)
    lyst.remove_all(1)
    print("lyst: ", lyst)
    print("len of lyst: ", len(lyst))
    print("val at 3: ", lyst[3])
    for val in lyst:
        print(val)
    print("sorted: ", is_sorted(lyst))

  
if __name__ == "__main__":
    main()
