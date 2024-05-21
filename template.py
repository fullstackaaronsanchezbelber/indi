#Siempre que ejecute esta template correra todo el entorno por mi

#Importar librerias
import os
from pathlib import Path
import logging

#Importar loggs para que va pasando en la ejecución
##mensahes de info con su respectiva fecha
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

#nombre del projecto
project_name='indi'

list_of_files = [
    # Archivo para mantener el directorio de GitHub Actions
    '.github/workflows/.gitkeep',

    # Archivo de inicialización del paquete principal
    f'src{project_name}/__init__.py',

    # Archivo de inicialización para el directorio de componentes
    f'src{project_name}/components/__init__.py',

    # Archivo de inicialización para el directorio de utilidades
    f'src{project_name}/utils/__init__.py',

    # Archivo con funciones comunes de utilidades
    f'src{project_name}/utils/common.py',

    # Archivo de inicialización para el directorio de configuración
    f'src{project_name}/config/__init__.py',

    # Archivo de configuración
    f'src{project_name}/config/configuration.py',

    # Archivo de inicialización para el directorio del pipeline
    f'src{project_name}/pipeline/__init__.py',

    # Archivo de inicialización para el directorio de entidades
    f'src{project_name}/entity/__init__.py',

    # Archivo de entidad de configuración
    f'src{project_name}/entity/config_entity.py',

    # Archivo de inicialización para el directorio de constantes
    f'src{project_name}/constants/__init__.py',

    # Archivo de configuración del proyecto en YAML
    'config/config.yaml',

    # Archivo de parámetros en YAML
    'params.yaml',

    # Archivo de esquema en YAML
    'schema.yaml',

    # Archivo principal de la aplicación
    'main.py',

    # Archivo de la aplicación web
    'app.py',

    # Archivo de configuración de Docker
    'Dockerfile',

    # Archivo de dependencias del proyecto
    'requirements.txt',

    # Archivo de configuración de instalación del paquete
    'setup.py',

    # Archivo de investigación y pruebas en Jupyter Notebook
    'research/trails.ipynb',

    # Archivo de plantilla HTML
    'templeates/index.html',

    # Archivo de test ML

    'test.py'
]

for filepath in list_of_files:
    filepath=Path(filepath)
    print(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file: {filename}')
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file: {filepath}')

    else:
        logging.info(f'{filename} is already exists')