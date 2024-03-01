class Profile:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


    def validate_password(self, password):
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False

        return True

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 < len(value) < 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property 
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not self.validate_password(value):
            raise ValueError(f"The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value
        return


    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*"*len(self.password)}'
