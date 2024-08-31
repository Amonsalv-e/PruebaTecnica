import logging
class PatientRecord:

    def storePatient(self, name,age, birth_date, sex, weight, patient_id, type_id):
        self._name = name
        self._age = age
        self._birth_date = birth_date
        self._sex = sex
        self._weight = weight
        self._patient_id = patient_id
        self._type_id = type_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self,sex):
        self._sex = sex

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        self._patient_id = patient_id

    @property
    def type_id(self):
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        self._type_id = type_id

    def __str__(self):
        return(f"Name: {self.name}, Age: {self.age}, Birth Date: {self.birth_date},"
               f"Sex: {self.sex}, Weight:{self.weight}, ID Patient: {self.patient_id},"
               f"Type Id : {self.type_id}")

    def update_diagnosis(self,new_diagnosis):
        if isinstance(new_diagnosis, PatientRecord):
            self.name = new_diagnosis.name
            self.birth_date = new_diagnosis.birth_date
            self.age = new_diagnosis.age
            self.sex = new_diagnosis.sex
            self.weight = new_diagnosis.weight
            self.patient_id = new_diagnosis.patient_id
            self.type_id = new_diagnosis.type_id
            logging.info(f"Nuevo diagnostico{self.name}")
        else:
            logging.error(f"new_diagnosis debe ser una instancia de PatientRecord")
