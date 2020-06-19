class student:
    school_name = 'School'
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
181
    @staticmethod
    def info():
        return 'This class beloangs to {}'.format(student.school_name)

    @name.setter
    def name(self, other):
        if not (isinstance(other, str) or other.isalpha()):
            raise TypeError(
                'the name {} '.format(other) +
                'shoud contain only alphabets :'
                )
        elif len(other) > 30:
            raise ValueError('Name cannot excseed 30 charcters')
        self.__name = other

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if (new_age < 0) or (new_age > 26):
            raise ValueError(
                'Student age must be ' +
                'lies between 0 and 26'
                )
        else:
            self.__age = new_age

    age = property(get_age, set_age)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, val):
        return setattr(self, key, val)

    def __lt__(self, other):
        if not isinstance(other, student):
            raise TypeError(
                '\"<\" operator not ' +
                'supported for \"{}\"'.format(type(other)) +
                'and \"student\" type.'
                )
        return self['age'] < other['age']




def main():
    s1 = student('namehi', 18)
    s1['name'] = 'abc' 
    #s1['age'] = 24
    s2 = student('namehelo', 20)
    #s2['age'] = s1['age']
    #print(s1 < 36)
    print(s1['age'])
    print(student.info())

if __name__ == '__main__':
    main()