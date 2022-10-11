from slist import SList
from course import Course


def calculate_gpa(courseList: SList) -> float:
    if len(courseList) == 0:
        return 0.0
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
    test_course()


def test_course():

    courseList = SList()
    course = Course(1234, "course1234", 1234, 1.23)
    course2 = Course(1234, "course1234", 1234, 1.23)
    assert course == course2
    assert course >= course2
    assert course <= course2

    for i in range(12):
        c = Course(i + 100, "course" + str(i), float(3), float(i) % 4)
        courseList.insert(c)

    for i in range(len(courseList) - 1):
        assert courseList[i] != courseList[i + 1]
        assert courseList[i] < courseList[i + 1]
        assert courseList[i] <= courseList[i + 1]
    assert is_sorted(courseList)
    assert calculate_gpa(courseList) == 1.5
    for c in courseList:
        print(c)


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
    assert is_sorted(lyst)
    assert lyst.find(10) == 10
    assert (lyst.remove(10))
    assert not (lyst.find(10))
    assert not (lyst.remove(10))
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
