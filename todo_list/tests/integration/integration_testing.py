from todo_list.src.todo_list.methods import file_functions

from tests.unit.unit_testing import tmp_dir
from tests.unit.unit_testing import df_empty
from tests.unit.unit_testing import df_empty_stored

from datetime import datetime
import pandas as pd
import pytest
import shutil


@pytest.fixture(scope="function")
def df_full_stored(tmp_dir, df_full):
    """

    Parameters
    ----------
    tmp_dir :
        
    df_full :
        

    Returns
    -------

    """
    df_full.to_csv(f"{tmp_dir}/todos.csv",index=False)
    return df_full


@pytest.fixture(scope="session")
def new_row():
    """ """
    return {
        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "task": "Establecer ABP",
        "summary": "Control de Activos",
        "status": "completo",
        "owner": "CCF",
    }


@pytest.fixture(scope="session")
def df_full(new_row):
    """

    Parameters
    ----------
    new_row :
        

    Returns
    -------

    """
    return pd.DataFrame(
        [new_row], columns=["created", "task", "summary", "status", "owner"]
    )


def create_list(tmp_dir, df_empty):
    """

    Parameters
    ----------
    tmp_dir :
        
    df_empty :
        

    Returns
    -------

    """
    file_functions.create_list("todos")
    df1 = file_functions.load_list("todos")
    pd.testing.assert_frame_equal(df1, df_empty)


def test_store_list(tmp_dir, df_empty):
    """

    Parameters
    ----------
    tmp_dir :
        
    df_empty :
        

    Returns
    -------

    """
    file_functions.store_list(df_empty, "todos")
    df2 = file_functions.load_list("todos")
    pd.testing.assert_frame_equal(df_empty, df2)


def add_to_list(new_row, df_full, tmp_dir,df_empty_stored):
    """

    Parameters
    ----------
    new_row :
        
    df_full :
        
    tmp_dir :
        
    df_empty_stored :
        

    Returns
    -------

    """
    file_functions.add_to_list("todos", new_row)
    df1 = file_functions.load_list("todos")
    pd.testing.assert_frame_equal(df1, df_full)


def update_list(df_full_stored):
    """

    Parameters
    ----------
    df_full_stored :
        

    Returns
    -------

    """
    df_full_stored.loc[0, "owner"] = "Ivan"
    file_functions.update_task_in_list("todos", 0, "owner", "Ivan")
    df = file_functions.load_list("todos")
    pd.testing.assert_frame_equal(df, df_full_stored)

def create_multiple_list(tmp_dir, df_empty):
    """

    Parameters
    ----------
    tmp_dir :
        
    df_empty :
        

    Returns
    -------

    """
    for i in range(5):
        file_functions.create_list(f"todos_{i}")
    assert len(file_functions.get_existing_lists()) == 5

def update_list_add_column(df_full_stored):
    """

    Parameters
    ----------
    df_full_stored :
        

    Returns
    -------

    """
 
    file_functions.create_list("new_list")
    file_functions.update_task_in_list("new_list", 0, "new_column", "other")

    df_add_column = file_functions.load_list("new_list")
    df_other = file_functions.load_list("other")
    
    assert df_add_column.shape[1] == df_other.shape[1] + 1