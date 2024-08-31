from pathlib import Path
import os
#import csv
import pandas as pd
import logging

import pydicom
import pydicom as dicom
import matplotlib.pyplot as plt
from pydicom import dcmread

logging.basicConfig(level=logging.INFO)

_logger = logging.getLogger(__name__)

def iterate():
    folder_path = Path("/home/alejandro/Documentos/Prueba/Test_python/prueba_python")
    #P
    files = [file for file in folder_path.iterdir() if file.is_file()]

    count_files = len(files)

    print(f"Total: {count_files}")
    print(os.listdir(folder_path))

iterate()

def iterateCsv():
    folder_csv = Path("/home/alejandro/Documentos/Prueba/Test_python/prueba_python")
    file_csv ="sample-01-csv.csv"
    file_path = folder_csv / file_csv
    #Existe
    if not os.path.exists(folder_csv):
        logging.error(f"El directorio {folder_csv} no existe")
        return False

    if not os.path.exists(file_path):
        logging.error(f"El archivo {file_csv} no existe")
        return False

    _, file_path_ext = os.path.splitext(file_path)

    #El archivo no es un CSV
    if file_path_ext.lower() != '.csv':
        logging.error(f"El archivo {file_path} no es un archivo CSV")
        return False
    if file_path.is_file():
        print(f"El archivo'{file_csv}' Existe")
        #Lee el archivo
        fp = pd.read_csv(file_path)
        columns = fp.columns
        numeric_col = fp.select_dtypes(include=['number'])
        #Verificar con un archivo CSV vacio
        if numeric_col.empty:
            logging.info("El archivo CSV no contiene numeros.")
            return False
        #Nombre y Numero de Columnas
        for idx, column in enumerate(columns, start=1):
            print(f"{idx}. {column}")
        num_rows_index = len(fp)
        #Numero de Filas
        print(f"El numero de filas es :{num_rows_index}")
        #Calcula y luego imprime media y desviacion estandar
        average_age = fp['Age'].mean()
        average_weight = fp['Weight'].mean()
        average_height = fp['Height'].mean()
        average_cholesterol = fp['Cholesterol'].mean()
        average_heartR = fp['HeartRate'].mean()
        stand_deviation_age = fp['Age'].std()
        #stand_deviation_age_r = round(stand_deviation_age, 2)
        stand_deviation_weight = fp['Weight'].std()
        stand_deviation_height = fp['Height'].std()
        stand_deviation_choles = fp['Cholesterol'].std()
        stand_deviation_heart = fp['HeartRate'].std()
        print(f"La media 'age' es : {round(average_age, 2)} "
              f"y su desviacion estandar es :{round(stand_deviation_age,2)}")
        print(f"La media de la columna 'Weight' es : {round(average_weight,2)}"
              f"y su desviacion estandar es :{round(stand_deviation_weight,2)}")
        print(f"La media de la columna 'Height' es : {round(average_height,2)}"
              f"y su desviacion estandar es :{round(stand_deviation_height,2)}")
        print(f"La media de la columna 'Cholesterol' es : {round(average_cholesterol,2)}"
              f"y su desviacion estandar es :{round(stand_deviation_choles,2)}")
        print(f"La media de la columna 'Heart' es : {round(average_heartR,2)}"
              f"y su desviacion estandar es :{round(stand_deviation_heart,2)}")
        #print(fp)
iterateCsv()

def iterateDicom():

    folder_dicom = Path("/home/alejandro/Documentos/Prueba/Test_python/prueba_python")
    file_dicom = "sample-01-dicom.dcm"
    file_path_dcm = folder_dicom/file_dicom

    x = dcmread(file_path_dcm) ### 'FileDataSet
    #print(x)

    if not os.path.exists(file_path_dcm):
        logging.error(f"El archivo {file_path_dcm} No existe")
        return False
    if file_path_dcm.is_file():
        dataset = pydicom.dcmread(file_path_dcm)
        #print(dataset)
        print("Patient Name :", dataset.PatientName)
        print("Study Date : ", dataset.StudyDate)
        print("Modality :", dataset.Modality)
        tag = (0x0008,0x0016)
        element = dataset.get(tag)
        if element:
            print(f"el Elemento es {element.tag} "
                  f"Nombre: {element.name} "
                  f"VR: {element.VR}")
        else:
            logging.error(f"El tag {tag} no está presente en el archivo DICOM")
iterateDicom()