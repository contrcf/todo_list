from src.to_do_list.cli_methods import helper_functions
from tests.unit.unit_test import tmp_dir
from tests.unit.unit_test import df_empty
from tests.unit.unit_test import df_empty_stored
import pandas as pd
import pytest
import shutil
from datetime import datetime

@pytest.fixture(scope="function")
def df_full_stored(tmp_dir, df_full):
    df_full.to_csv(f"{tmp_dir}/todos.csv",index=False)
    return df_full


@pytest.fixture(scope="session")
def new_row():
    return {
        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "task": "Correr",
        "summary": "Correr en el parque",
        "status": "todo",
        "owner": "jose",
    }


@pytest.fixture(scope="session")
def df_full(new_row):
    return pd.DataFrame(
        [new_row], columns=["created", "task", "summary", "status", "owner"]
    )


def test_create_list(tmp_dir, df_empty):
    helper_functions.create_list("todos")
    df1 = helper_functions.load_list("todos")
    pd.testing.assert_frame_equal(df1, df_empty)


def test_store_list(tmp_dir, df_empty):
    helper_functions.store_list(df_empty, "todos")
    df2 = helper_functions.load_list("todos")
    pd.testing.assert_frame_equal(df_empty, df2)


def test_add_to_list(new_row, df_full, tmp_dir,df_empty_stored):
    helper_functions.add_to_list("todos", new_row)
    df1 = helper_functions.load_list("todos")
    pd.testing.assert_frame_equal(df1, df_full)


def test_update_list(df_full_stored):
    df_full_stored.loc[0, "owner"] = "Ivan"
    helper_functions.update_task_in_list("todos", 0, "owner", "Ivan")
    df = helper_functions.load_list("todos")
    pd.testing.assert_frame_equal(df, df_full_stored)

def test_create_multiple_list(tmp_dir, df_empty):
    for i in range(5):
        helper_functions.create_list(f"todos_{i}")
    assert len(helper_functions.get_existing_lists()) == 5

def test_update_list_add_column(df_full_stored):
    helper_functions.create_list("new_list")
    helper_functions.create_list("other")
    helper_functions.update_task_in_list("new_list", 0, "new_column", "other")
    df_add_column = helper_functions.load_list("new_list")
    df_other = helper_functions.load_list("other")
    assert df_add_column.shape[1] == df_other.shape[1] + 1