from pathlib import Path

import pydicom

#dicom_file = pydicom.dcmread('/home/alejandro/Documentos/Prueba/Test_python/prueba_python/sample-02-dicom.dcm')
folder_dicom = Path("/home/alejandro/Documentos/Prueba/Test_python/prueba_python")
file_dicom = "sample-02-dicom.dcm"
file_path_dcm = folder_dicom / file_dicom
ds = pydicom.filereader.dcmread(file_path_dcm)

modality = ds.Modality
study_date = ds.StudyDate
study_time = ds.StudyTime
study_instance_uid = ds.StudyInstanceUID
series_number = ds.SeriesNumber


#Asignar un nuevo nombre a un tag
#print(ds[0x10,0x10])
#ds[0x10,0x10].value = 'NewName'
#print(ds[0x100010])

#Los Valores se cambian con el Tag
#print(ds[0x10,0x20])
ds[0x10,0x20].value = "557352A"
print(ds[0x10,0x20])

#print(f"Modality: {modality}")
#print(f"Study Date: {study_date}")
#print(f"Study Time: {study_time}")
#print(f"Study Instance UID: {study_instance_uid}")
#print(f"Series Number: {series_number}")
print(ds)
