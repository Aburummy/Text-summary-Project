import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name ="summarizer"

list_files = [
    ".github/workflow/.gitkeep/",
    f"src/{project_name}/_init__.py",
    f"src/{project_name}/components_init__.py",
    f"src/{project_name}/utils/_init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/_init__.py",
    f"src/{project_name}/config/_init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/_init__.py",
    f"src/{project_name}/entity/_init__.py",
    f"src/{project_name}/constants/_init_.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for filepath in list_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    s
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")
            
    else:
        logging.info(f"File {filepath} already exists and is not empty.")
        