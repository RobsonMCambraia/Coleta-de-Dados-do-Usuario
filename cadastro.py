class User:
    def __init__(self):
        self.name = []
        self.birth_day = []
        self.gender = []
        self.career = []
        self.remuneration = []
        self.marital_status = []
        
    def get_name(self):
        return self.name
    def set_name(self, name):
        while True:
            name = input('Digite seu nome completo:\t').upper().lstrip(' ')
            if len(name) > 3:
                self.name.append(name)
                break
            else:
                print('Insira um nome com mais de 3 caracteres!')
        
        print(self.name)
        
    def get_birth_day(self):
        return self.birth_day
    def set_birth_day(self, birth_day):
        self.birth_day = birth_day

    def get_gender(self):
        return self.gender
    def set_gender(self, gender):
        self.gender = gender

    def get_career(self):
        return self.career
    def set_career(self, career):
        self.career = career

    def get_remuneration(self):
        return self.remuneration
    def set_remuneration(self, remuneration):
        self.remuneration = remuneration

    def get_marital_status(self):
        return self.marital_status
    def set_marital_status(self, marital_status):
        self.marital_status = marital_status

        
    def getUsers (self):
        return {
            "name": self.name,
            "birth_day": self.birth_day,
            "gender": self.gender,
            "career": self.career,
            "remuneration": self.remuneration,
            "marital_status": self.marital_status
        }
