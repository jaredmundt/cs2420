''' Course Class for Project 3 of cs2420 '''


class Course:
    ''' Course object '''

    def __init__(self, number=0, name="", credit_hour=0.0, grade=0.0):
        if not isinstance(number, int) or number < 0:
            raise ValueError("number must be a positive int")
        self._number: int = number
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        self._name: str = name
        if not isinstance(credit_hour,(int, float)) or credit_hour < 0:
            raise ValueError("credit_hour must be a positive float")
        self._credit_hour: float = credit_hour
        if not isinstance(grade, (int, float)) or grade > 4.0 or grade < 0.0:
            raise ValueError("grade must be a float between 0.0 and 4.0")
        self._grade: float = grade

    def number(self) -> int:
        '''get number'''
        return self._number

    def name(self) -> str:
        '''get name'''
        return self._name

    def credit_hr(self) -> float:
        '''get credit_hour'''
        return self._credit_hour

    def grade(self) -> float:
        '''get grade'''
        return self._grade

    def __str__(self) -> str:
        '''"cs<course_number> <course_name>
        Grade: <grade> Credit Hours: <hours>"'''
        res = f"cs{self._number} {self._name}\
 Grade: {self._grade} Credit Hours: {self._credit_hour}"
        return res

    def __eq__(self, other):
        '''comparisons based on Course._number'''
        if isinstance(other,int):
            return self._number == other
        return self._number == other._number

    def __lt__(self, other):
        '''comparisons based on Course._number'''
        if isinstance(other,int):
            return self._number < other
        return self._number < other._number

    def __le__(self, other):
        '''comparisons based on Course._number'''
        if isinstance(other,int):
            return self._number <= other
        return self._number <= other._number
