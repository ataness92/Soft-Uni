from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []


    def add_task(self, new_task: Task):
        for task in self.tasks:
            if new_task.name == task.name:
                return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"


    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"


    def clean_section(self):
        tasks = self.tasks.copy()
        removed = 0
        for task in tasks:
            if task.completed:
                self.tasks.remove(task)
                removed += 1
        return f"Cleared {removed} tasks."


    def view_section(self):
        return f"Section {self.name}:\n{chr(10).join([task.details() for task in self.tasks])}"

