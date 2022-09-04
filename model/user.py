class User:
    __surname: str
    __name: str
    __patronymic: str
    __date_of_birth: str

    def __init__(self, surname, name, patronymic, date_of_birth):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__date_of_birth = date_of_birth
