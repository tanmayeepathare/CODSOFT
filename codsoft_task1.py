print("MY TO DO LIST PROGRAM")

my_tasks = []

while True:
    print("\n1.Add Task")
    print("2.Show Tasks")
    print("3.Remove Task")
    print("4.Exit")

    option = input("Choose option: ")

    if option == "1":
        new_task = input("Enter new task: ")
        my_tasks.append(new_task)
        print("Task saved!")

    elif option == "2":
        if len(my_tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your Tasks:")
            count = 1
            for t in my_tasks:
                print(count, "-", t)
                count += 1

    elif option == "3":
        if len(my_tasks) == 0:
            print("Nothing to remove.")
        else:
            num = int(input("Enter task number to remove: "))
            if num > 0 and num <= len(my_tasks):
                removed_task = my_tasks.pop(num-1)
                print("Removed:", removed_task)
            else:
                print("Wrong number.")

    elif option == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")
