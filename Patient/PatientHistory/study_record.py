import logging
from pathlib import Path
import pydicom
from pydicom import dcmread

from PatientHistory.patient_record import PatientRecord

class StudyRecord(PatientRecord):

    logging.basicConfig(level=logging.INFO)

    folder_dicom = Path("/home/alejandro/Documentos/Prueba/Test_python/prueba_python")
    file_dicom = "sample-02-dicom.dcm"
    file_path_dcm = folder_dicom / file_dicom

    def __init__(self, name,age, birth_date, sex, weight, patient_id, type_id,
                 modality, study_date, study_time, study_instance_uid, series_number):
        super().__init__(name, age, birth_date, sex, weight, patient_id, type_id)
        self._modality = modality
        self._study_date = study_date
        self._study_time = study_time
        self._study_instance_uid = study_instance_uid
        self._series_number = series_number

        logging.info(f"StudyRecord successfully created for {self.name}")

    @property
    def modality(self):
        return self._modality

    @modality.setter
    def modality(self, modality):
        self._modality = modality

    @property
    def study_date(self):
        return self._study_date

    @study_date.setter
    def study_date(self, study_date):
        self._study_date = study_date

    @property
    def study_time(self):
        return self._study_time

    @study_time.setter
    def study_time(self, study_time):
        self._study_time = study_time

    @property
    def study_instance_uid(self):
        return self._study_instance_uid

    @study_instance_uid.setter
    def study_instance_uid(self, study_instance_uid):
        self._study_instance_uid = study_instance_uid

    @property
    def series_number(self):
        return self._series_number

    @series_number.setter
    def series_number(self, series_number):
        self._series_number = series_number

    def load_from_dicom(self, file_path_dcm):
        self.dicom = pydicom.dcmread(file_path_dcm)
        self._modality = self.dicom.Modality
        self._study_date = self.dicom.StudyDate
        self._study_time = self.dicom.StudyTime
        self._study_instance_uid = self.dicom.StudyInstanceUID
        self._series_number = self.dicom.SeriesNumber

    def __str__(self):
        patient_info = super().__str__()
        study_info = (f"Modality:{self._modality}, Study Date: {self._study_date}, Study Time: {self._study_time},"
                      f"Study Instance UID: {self._study_instance_uid}, Serie Number: {self._series_number}")
        return f"{patient_info}\n{study_info}"

study_record = StudyRecord("Juan Martinez",23,"1994-11-22","M",90,"123456","SSN",
                           "XA",19931012,141812,1.1244,1)
print(study_record)
