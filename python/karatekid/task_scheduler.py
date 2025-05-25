from datetime import date

from singly_linked_list import LinkedList


class Task:
    def __init__(self, desc, urgent=False, due_date=None):
        self.desc = desc
        self.urgent = urgent
        self.due_date = due_date

    def __repr__(self):
        return f"Task({self.desc})"


class TaskScheduler:
    def __init__(self):
        self.tasks = LinkedList()

    def add_task(self, desc, urgent=False, due_date=None):
        task = Task(desc=desc, urgent=urgent, due_date=due_date)
        self.tasks.add_right(task)

    def __repr__(self):
        rep = ""
        for task in self.tasks:
            rep += "-->" + str(task.data)
        return rep


if __name__ == "__main__":

    ts = TaskScheduler()
    ts.add_task(desc="Empty Bins", urgent=True, due_date=date(2025, 2, 27))
    ts.add_task(desc="Fix Shed")
    ts.add_task(desc="Paint Bathroom")
    # ts.remove_task(desc="Fix Shed")
    # ts.execute_task(desc="Empty Bins")
    print(ts)
