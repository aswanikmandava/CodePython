from task import Task
from tasklist import TaskList

def print_tasks(task_list):
    print(f"---------Task List---------")
    for task in task_list.tasks:
        print(task)


def main():
    print("#"*40)
    print("My TODO application")
    print("#"*40)

    # add a few tasks
    t_list = TaskList()
    t_list.add_task(Task(10, "Go for walk"))
    t_list.add_task(Task(20, "Pay utility bill"))
    t_list.add_task(Task(30, "Play tennis"))
    print_tasks(t_list)
    
    print("Editing the task with id: 20")
    t_list.change_task_description(20, "Pay PSEG bill")
    print_tasks(t_list)

    print("Deleting the task - 30")
    t_list.delete_task(30)
    print_tasks(t_list)

    print("Edited Task 20 state")
    t_list.change_task_state(20, "Done")
    print_tasks(t_list)

if __name__ == "__main__":
    main()