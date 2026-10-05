# student-task-manager
def confirm_delete():
    """
    Ask the user for delete confirmation.
    """
    while True:

        choice = input(
            "Are you sure you want to delete this task? (y/n): "
        ).lower()

        if choice == "y":
            return True

        elif choice == "n":
            return False

        else:
            print("Please enter y or n.")


def delete_task(tasks):
    """
    Delete a selected task from the task list.
    """
    print("\n======================================")
    print("             DELETE TASK")
    print("======================================")

    if len(tasks) == 0:
        print("No tasks available to delete.")
        return

    print("\nAvailable Tasks:")

    for number, task in enumerate(tasks, start=1):

        status = "Completed" if task["completed"] else "Pending"

        print(
            f"{number}. {task['name']} [{status}]"
        )

    try:
        number = int(
            input("\nEnter task number to delete: ")
        )

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        selected_task = tasks[number - 1]

        print(
            "\nSelected Task:",
            selected_task["name"]
        )

        if confirm_delete():

            deleted_task = tasks.pop(number - 1)

            print(
                f"Task '{deleted_task['name']}' "
                "deleted successfully!"
            )

        else:
            print("Delete operation cancelled.")

    except ValueError:
        print("Please enter a valid number.")


def delete_completed_tasks(tasks):
    """
    Delete all completed tasks.
    """
    if len(tasks) == 0:
        print("No tasks available.")
        return

    original_count = len(tasks)

    tasks[:] = [
        task for task in tasks
        if not task["completed"]
    ]

    deleted_count = original_count - len(tasks)

    print(
        f"{deleted_count} completed task(s) deleted."
    )