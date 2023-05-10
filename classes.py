class Human:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def what_is_your_name(self):
        print(self.name)

    def how_old_are_you(self):
        print(self.age, 'лет')

class Student( Human ):
    def __init__(self, name, age, _school, _class):
        super().__init__( name, age )
        self._school = _school
        self._class  = _class

    def where_are_you_from(self):
        print( self._school )

    def what_grade_are_you(self):
        print( self._class )

class Teacher( Human ):
    def __init__(self, name, age, _school, _subject):
        super().__init__( name, age )
        self._school = _school
        self._subject = _subject

    def where_are_you_from(self):
        print( self._school )

    def what_are_you_teaching(self):
        print( self._subject )


class Director( Human ):
    def __init__(self, name, age, _school):
        super().__init__( name, age )
        self._school = _school

    def where_are_you_from(self):
        print( self._school )

class DTeacher( Teacher , Director ):
    pass

st = Student( 'Коля', 16, 'Гимназия №52', 'класс 10А' )
st.what_is_your_name ()
st.how_old_are_you   ()
st.where_are_you_from()
st.what_grade_are_you()

print()

st = Teacher( 'Алексей', 37, 'Гимназия №52', 'География' )
st.what_is_your_name    ()
st.how_old_are_you      ()
st.where_are_you_from   ()
st.what_are_you_teaching()

print()

st = Director( 'Евгений', 40, 'Гимназия №52' )
st.what_is_your_name ()
st.how_old_are_you   ()
st.where_are_you_from()
