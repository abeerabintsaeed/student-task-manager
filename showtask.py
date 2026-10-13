def get_task_status(task):
    """
    Return the current status of a task.
    """
    if task["completed"]:
        return "Completed"
    else:
        return "Pending"


def display_single_task(task, number):
    """
    Display one task with its number and status.
    """
    status = get_task_status(task)

    print(
        f"{number}. {task['name']} "
        f"[Status: {status}]"
    )


def show_tasks(tasks):
    """
    Display all tasks available in the system.
    """
    print("\n======================================")
    print("           ALL STUDENT TASKS")
    print("======================================")

    if len(tasks) == 0:
        print("No tasks are available.")
        return

    for number, task in enumerate(tasks, start=1):
        display_single_task(task, number)

    print("--------------------------------------")
    print(f"Total Tasks: {len(tasks)}")


def show_pending_tasks(tasks):
    """
    Display only pending tasks.
    """
    print("\n======================================")
    print("             PENDING TASKS")
    print("======================================")

    pending_count = 0

    for number, task in enumerate(tasks, start=1):

        if not task["completed"]:
            display_single_task(task, number)
            pending_count += 1

    if pending_count == 0:
        print("No pending tasks available.")

    print("--------------------------------------")
    print(f"Pending Tasks: {pending_count}")


def show_completed_tasks(tasks):
    """
    Display only completed tasks.
    """
    print("\n======================================")
    print("            COMPLETED TASKS")
    print("======================================")

    completed_count = 0

    for number, task in enumerate(tasks, start=1):

        if task["completed"]:
            display_single_task(task, number)
            completed_count += 1

    if completed_count == 0:
        print("No completed tasks available.")

    print("--------------------------------------")
    print(f"Completed Tasks: {completed_count}")


def show_task_details(tasks):
    """
    Display detailed information about a selected task.
    """
    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    show_tasks(tasks)

    try:
        number = int(input("\nEnter task number to view details: "))

        if 1 <= number <= len(tasks):

            task = tasks[number - 1]

            print("\n========== TASK DETAILS ==========")
            print("Task Number :", number)
            print("Task Name   :", task["name"])
            print("Status      :", get_task_status(task))
            print("==================================")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def search_task(tasks):
    """
    Search for a task using a keyword.
    """
    print("\n========== SEARCH TASK ==========")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    keyword = input("Enter task keyword: ").strip().lower()

    if keyword == "":
        print("Search keyword cannot be empty.")
        return

    found = False

    print("\nSearch Results:")

    for number, task in enumerate(tasks, start=1):

        if keyword in task["name"].lower():

            display_single_task(task, number)
            found = True

    if not found:
        print("No matching task found.")


def display_task_statistics(tasks):
    """
    Display task statistics.
    """
    total_tasks = len(tasks)

    completed_tasks = 0
    pending_tasks = 0

    for task in tasks:

        if task["completed"]:
            completed_tasks += 1
        else:
            pending_tasks += 1

    print("\n======================================")
    print("          TASK STATISTICS")
    print("======================================")

    print("Total Tasks     :", total_tasks)
    print("Completed Tasks :", completed_tasks)
    print("Pending Tasks   :", pending_tasks)

    print("======================================")


# ==========================================
# TEST DATA
# ==========================================

tasks = [
    {"name": "Python Assignment", "completed": False},
    {"name": "DLD Project", "completed": True},
    {"name": "Math Assignment", "completed": False},
    {"name": "Software Engineering Task", "completed": True}
]


# ==========================================
# TEST SHOW TASK FEATURE
# ==========================================

print("\n\n******** STUDENT TASK MANAGEMENT SYSTEM ********")

show_tasks(tasks)

print("\n\n******** PENDING TASKS ********")
show_pending_tasks(tasks)

print("\n\n******** COMPLETED TASKS ********")
show_completed_tasks(tasks)

print("\n\n******** TASK STATISTICS ********")
display_task_statistics(tasks)

print("\n\n******** SEARCH TASK ********")
search_task(tasks)

print("\n\n******** TASK DETAILS ********")
show_task_details(tasks)

