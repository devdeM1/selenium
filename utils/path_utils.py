import os

def get_file_path(file_name: str) -> str:
    project_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(project_directory, '..', 'uploads', file_name))

def file_exists(file_path: str) -> bool:
    return os.path.isfile(file_path)