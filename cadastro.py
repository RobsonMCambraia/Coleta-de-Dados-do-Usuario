class User:
    def __init__(self, name, birth_day, gender, career, remuneration, marital_status):
        self.name = name
        self.birth_day = birth_day
        self.gender = gender
        self.career = career
        self.remuneration = remuneration
        self.marital_status = marital_status
        
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_birth_day(self):
        return self._birth_day
    def set_birth_day(self, birth_day):
        self._birth_day = birth_day

    def get_gender(self):
        return self._gender
    def set_gender(self, gender):
        self._gender = gender

    def get_career(self):
        return self._career
    def set_career(self, career):
        self._career = career

    def get_remuneration(self):
        return self._remuneration
    def set_remuneration(self, remuneration):
        self._remuneration = remuneration

    def get_marital_status(self):
        return self._marital_status
    def set_marital_status(self, marital_status):
        self._marital_status = marital_status

        
    def getUsers (self):
        return {
            "name": user.name,
            "birth_day": user.birth_day,
            "gender": user.gender,
            "career": user.career,
            "remuneration": user.remuneration,
            "marital_status": user.marital_status
        }
