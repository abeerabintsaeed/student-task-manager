def validate_task_name(task_name):
    """
    Validate the task name before adding it.
    """
    if task_name is None:
        return False

    if task_name.strip() == "":
        return False

    return True


def create_task_object(task_name):
    """
    Create a task dictionary.
    """
    task = {
        "name": task_name.strip(),
        "completed": False
    }

    return task


def add_task(tasks):
    """
    Add a new task to the task list.
    """
    print("\n========== ADD NEW TASK ==========")

    task_name = input("Enter task name: ")

    if not validate_task_name(task_name):
        print("Error: Task name cannot be empty.")
        return

    new_task = create_task_object(task_name)

    tasks.append(new_task)

    print("Task added successfully!")
    print("Task:", new_task["name"])


def add_multiple_tasks(tasks):
    """
    Allow the user to add multiple tasks.
    """
    print("\n========== ADD MULTIPLE TASKS ==========")

    while True:
        task_name = input("Enter task name (or type 'done' to finish): ")

        if task_name.lower() == "done":
            break

        if not validate_task_name(task_name):
            print("Task name cannot be empty.")
            continue

        new_task = create_task_object(task_name)
        tasks.append(new_task)

        print("Task added successfully!")