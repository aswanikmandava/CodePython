from task import Task
from typing import List, Optional

class TaskList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        self.tasks.append(new_task)

    # get task id to edit descriptiona and state
    def get_task(self, t_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.t_id == t_id:
                return task

    def change_task_description(self, t_id: int, new_description: str) -> None:
        # get task using id
        cur_task = self.get_task(t_id)
        if cur_task:
            cur_task.change_description(new_description)

    def change_task_state(self, t_id: int, new_state: str) -> None:
        cur_task = self.get_task(t_id)
        if cur_task:
            cur_task.change_state(new_state)

    # remove given task
    def delete_task(self, t_id: int):
        self.tasks = [task for task in self.tasks if task.t_id != t_id]