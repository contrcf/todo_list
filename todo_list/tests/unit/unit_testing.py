from src.todo_list.methods import file_functions
import pandas as pd
import pytest
import shutil


@pytest.fixture(scope="function")
def tmp_dir(tmpdir_factory):
    my_tmpdir = tmpdir_factory.mktemp("pytestdata")
    file_functions.PATH_TO_DATA = str(my_tmpdir)
    yield my_tmpdir
    shutil.rmtree(str(my_tmpdir))


@pytest.fixture(scope="session")
def df_empty():
    return pd.DataFrame(
        columns=["created", "task", "summary", "status", "owner"])


@pytest.fixture(scope="function")
def df_empty_stored(tmp_dir, df_empty):
    df_empty.to_csv(f"{tmp_dir}/todos.csv", index=False)
    return df_empty


def test_check_list_exists(df_empty_stored):
    assert file_functions.check_list_exists("todos") == True


def test_get_list_path():
    assert file_functions.get_list_path("todos") == \
        file_functions.PATH_TO_DATA + "/" + "todos.csv"


def test_get_filename():
    assert file_functions.get_list_filename("data") == "data.csv"


def test_check_list_exists_fail(tmp_dir):
    assert file_functions.check_list_exists("todos") == False


def test_load_list(df_empty_stored, tmp_dir):
    df = file_functions.load_list("todos")
    pd.testing.assert_frame_equal(df_empty_stored, df)


def test_check_number_of_files(df_empty_stored):
    assert len(file_functions.get_existing_lists()) == 1
