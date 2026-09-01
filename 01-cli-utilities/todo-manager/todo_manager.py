"""
Task & Todo Productivity Manager
Features persistent JSON storage, priority levels, task completion tracking,
and tabular display without recursive stack overflows.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional


class TodoManager:
    """Encapsulates task operations with JSON persistence."""

    STORAGE_FILE = Path("tasks_data.json")

    def __init__(self):
        self.tasks: List[Dict[str, Any]] = []
        self.load()

    def add_task(self, title: str, category: str = "General", priority: str = "Medium") -> Dict[str, Any]:
        """Create and store a new task."""
        new_id = len(self.tasks) + 1
        task = {
            "id": new_id,
            "title": title.strip(),
            "category": category.strip() or "General",
            "priority": priority.upper(),
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(task)
        self.save()
        print(f"[Added] Task #{task['id']}: '{task['title']}' [{task['priority']}]")
        return task

    def complete_task(self, task_id: int) -> bool:
        """Mark an existing task as completed."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save()
                print(f"[Completed] Task #{task_id}: '{task['title']}' marked as done.")
                return True
        print(f"[Error] Task #{task_id} not found.")
        return False

    def delete_task(self, task_id: int) -> bool:
        """Remove a task and re-index remaining tasks."""
        for index, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed = self.tasks.pop(index)
                for idx, item in enumerate(self.tasks, start=1):
                    item["id"] = idx
                self.save()
                print(f"[Deleted] Task #{task_id}: '{removed['title']}' removed.")
                return True
        print(f"[Error] Task #{task_id} not found.")
        return False

    def list_tasks(self, filter_category: Optional[str] = None):
        """Display formatted table of tasks."""
        print("\n" + "=" * 65)
        print("                     TASK & TODO MANAGER                        ")
        print("-" * 65)
        print(f" {'ID':<4} | {'Status':<6} | {'Priority':<8} | {'Category':<12} | {'Title'}")
        print("-" * 65)

        items = [t for t in self.tasks if not filter_category or t["category"].lower() == filter_category.lower()]
        if not items:
            print("  No tasks found. Add a task to get started!")
        else:
            for t in items:
                status = "[DONE]" if t["completed"] else "[PEND]"
                print(f" #{t['id']:<3} | {status:<6} | {t['priority']:<8} | {t['category']:<12} | {t['title']}")
        print("=" * 65 + "\n")

    def save(self):
        """Persist tasks to JSON file."""
        try:
            with open(self.STORAGE_FILE, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, indent=2)
        except Exception as e:
            print(f"[Storage Warning] Could not save tasks: {e}")

    def load(self):
        """Load tasks from JSON file."""
        if self.STORAGE_FILE.exists():
            try:
                with open(self.STORAGE_FILE, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
            except Exception:
                self.tasks = []


def main():
    manager = TodoManager()
    print("==================================================")
    print("           CLI TASK & TODO MANAGER                ")
    print("==================================================")

    while True:
        print("1. View All Tasks")
        print("2. Add New Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            manager.list_tasks()

        elif choice == "2":
            title = input("Enter task description: ").strip()
            if not title:
                print("[Error] Task description cannot be empty.")
                continue
            category = input("Enter category (e.g. Work, Study, Health) [General]: ").strip()
            priority = input("Enter priority (Low, Medium, High) [Medium]: ").strip() or "Medium"
            manager.add_task(title, category, priority)

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as completed: ").strip())
                manager.complete_task(task_id)
            except ValueError:
                print("[Error] Please enter a valid integer ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: ").strip())
                manager.delete_task(task_id)
            except ValueError:
                print("[Error] Please enter a valid integer ID.")

        elif choice == "5":
            print("\nProductivity session ended. Keep up the good work!")
            break

        else:
            print("[Error] Invalid option. Please select 1 to 5.")


if __name__ == "__main__":
    main()
