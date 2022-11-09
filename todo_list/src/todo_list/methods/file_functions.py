import os
from todo_list.config import settings
from todo_list.config import ROOT_DIR
from pathlib import Path
import pandas as pd

PATH = ROOT_DIR
PATH_TO_DATA = f"{PATH}/{settings['DATA_PATH']}/"


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


def get_existing_lists() -> str:
    """Shows existin list
    Args:

    Returns:
      :return: list of filenames

    >>>get_existing_lists()
    file_1,file_2,......file_n
    """
    #return os.listdir(Path(ROOT_DIR, settings["DATA_PATH"]))
    return os.listdir(PATH_TO_DATA)


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
    #return f"{path_to_data}/{get_list_filename(name)}"
    return f"{PATH_TO_DATA}/{get_list_filename(name)}"


def store_list(df: pd.DataFrame, name: str):
    """Write a dataframe from namefile
      Args:
        name: df
    """
    df.to_csv(get_list_path(name), index=False)


def load_list(name: str) -> pd.DataFrame:
    """Return a Dataframe
      Args:
        name: File name

      Returns:
        A object DataFrame read from filename

      >>>load_list('my_file')
      pd.DataFrame
    """
    return pd.read_csv(get_list_path(name))


def create_list(name: str):
    """Create a empty list
      Args:
        name: File name
    """
    df = pd.DataFrame(
          columns=["created", "task", "summary", "status", "owner"])
    store_list(df, name)


def update_task_in_list(list_name: str,
                        task_id: int,
                        field: str,
                        change: (int or str)):
    """Update a row from list
      Args:
        name: File name
        task_id: Number of row that use for update
        field: Column name for update
        change: New value for column
    """
    df = load_list(list_name)
    df.loc[task_id, field] = change
    store_list(df, list_name)


def add_to_list(list_name: str, new_row: dict):
    """Add a new row a the list
      Args:
        list_name: File name
        new_row: json with attributes equals to columns from the list
    """
    df = load_list(list_name)
    df.loc[len(df.index)] = new_row
    store_list(df, list_name)
