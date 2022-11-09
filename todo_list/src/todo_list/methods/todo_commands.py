from todo_list.methods.file_functions import get_existing_lists
from todo_list.methods.file_functions import add_to_list
from todo_list.methods.file_functions import check_list_exists
from todo_list.methods.file_functions import create_list
from todo_list.methods.file_functions import load_list
from todo_list.methods.file_functions import update_task_in_list
from datetime import datetime
import typer


app = typer.Typer(add_completion=False)


@app.command("create")
def create(name: str = typer.Option("Unnamed", "-ln", "--listname")):

    """Create a new todo list"""

    if check_list_exists(name):
        print("There is already a todo list with this name.")
        return

    create_list(name)
    print(f"Todo list {name} successfully created!")


@app.command("show")
def show_list(list_name: str = typer.Option(..., "-ln", "--listname")):
    """Shows Task in one list"""
    if not check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
        return
    df = load_list(list_name)
    print(df.to_markdown())


@app.command("add")
def add_task(
    list_name: str = typer.Option(..., "-ln", "--listname"),
    task_name: str = typer.Option(..., "-tn", "--taskame"),
    summary: str = typer.Option(None, "-d", "--description"),
    owner: str = typer.Option(..., "-o", "--owner"),
):
    """Add a task to a given todo list"""

    if not check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
        return

    new_row = {
        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "task": task_name,
        "summary": summary if summary else None,
        "status": "todo",
        "owner": owner,
    }

    add_to_list(list_name, new_row)
    print("Task successfully added")


@app.command("update")
def update_task(
    list_name: str = typer.Option(..., "-ln", "--listname"),
    task_id: int = typer.Option(..., "-i", "--taskid"),
    field: str = typer.Option(..., "-f", "--field"),
    change: str = typer.Option(..., "-c", "--change"),
):

    """Update a task in a given todo list"""
    if not check_list_exists(list_name):
        print("The list does not exist. Use create list first.")
        return
    update_task_in_list(list_name, task_id, field, change)
    print("Task successfully updated")


@app.command("list")
def list_lists():
    """Lists all existing todo lists"""

    filenames = get_existing_lists()
    for filename in filenames:
        print(filename)

