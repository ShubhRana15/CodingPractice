# Tool to create a to do list for user using CLI 

import argparse
import os


def create_parser():
    parser = argparse.ArgumentParser(description="CLI Todo List App")
    parser.add_argument("-a", "--add", metavar="", help="Add/append a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all available tasks")
    parser.add_argument("-r", "--remove", metavar="", help="Remove a task using index")
    return parser


def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")


def list_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    else:
        print("List is Empty")


def remove_task(index):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)
        print("Task removed from the list successfully.")
    else:
        print("List is empty")


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
