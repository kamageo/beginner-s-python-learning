class Human:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age, 'лет')

class Student( Human ):
    def __init__(self, name, age, _school, _class):
        super().__init__( name, age )
        self._school = _school
        self._class  = _class

    def print_school(self):
        print( self._school )

    def print_class(self):
        print( self._class )

class Teacher( Human ):
    def __init__(self, name, age, _school, _subject):
        super().__init__( name, age )
        self._school = _school
        self._subject = _subject

    def print_school(self):
        print( self._school )

    def print_subject(self):
        print( self._subject )


class Director( Human ):
    def __init__(self, name, age, _school):
        super().__init__( name, age )
        self._school = _school

    def print_school(self):
        print( self._school )

class DTeacher( Teacher , Director ):
    pass

st = Student( 'Коля', 16, 'Гимназия №52', 'класс 10А' )
st.print_name   ()
st.print_age    ()
st.print_school ()
st.print_class  ()

print()

st = Teacher( 'Алексей', 37, 'Гимназия №52', 'География' )
st.print_name   ()
st.print_age    ()
st.print_school ()
st.print_subject()

print()

st = Director( 'Евгений', 40, 'Гимназия №52' )
st.print_name   ()
st.print_age    ()
st.print_school ()