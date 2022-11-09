import os
from todo_list.config import settings,ROOT_DIR
from pathlib import Path
import pandas as pd


def get_list_filename(name: str) -> str: 
    """Return the name of argument with the extension .csv

    Args:
      name: File name
      name: str:

    Returns:
      The file name with extension .csv

    >>>get_list_filename('hola_mundo')
    hola_mundo.csv
    """
    return f"{name}.csv"


def get_existing_lists() ->str:
    """

    Args:

    Returns:
      :return: list of filenames

    >>>get_existing_lists()
    file_1,file_2,......file_n
    """
    return os.listdir(Path(ROOT_DIR, settings["DATA_PATH"]))


def check_list_exists(name: str) -> bool:
    """Return a true if the filename exists in directory else false

    Args:
      name: Filename to search
      name: str

    Returns:
      true if filename exists else false

    >>>check_list_exists('my_file')
    False
    """
    return get_list_filename(name) in get_existing_lists()


def get_list_path(name: str) -> str:
    """Return a relative path from filename
    Args:
      name: Filename

    Returns:
      relative path + filename

    >>>get_list_path('my_file')
    my_path/my_file
    """
    path_to_data = Path(ROOT_DIR, settings["DATA_PATH"])
    return f"{path_to_data}/{get_list_filename(name)}"


#Escribe el dataframe en un archivo csv con el nombre indicado
def store_list(df: pd.DataFrame, name: str):

  df.to_csv(get_list_path(name), index=False)


#Lee un archivo csv y regresa un df
def load_list(name: str) -> pd.DataFrame:
    return pd.read_csv(get_list_path(name))


#Crea un archivo con los encabezados
def create_list(name: str):
    df = pd.DataFrame(columns=["created", "task", "summary", "status", "owner"])
    store_list(df, name)


#Lee un archivo, actualiza un registro y guarda el archivo
def update_task_in_list(list_name: str, task_id: int, field: str, change: object):
    df = load_list(list_name)
    df.loc[task_id, field] = change
    store_list(df, list_name)


#Lee un archivo, agrega un registro y guarda el archivo
def add_to_list(list_name: str, new_row: dict):
    df = load_list(list_name)
    df.loc[len(df.index)] = new_row
    store_list(df, list_name)