from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def show_state(structure):
    """Print the structure after an operation."""
    print("Current state:", structure)
    print("Empty:", structure.is_empty(), "| Full:", structure.is_full())


def balanced_parentheses(expression):
    """Check (), [] and {} using a stack."""
    stack = LinkedStack()
    matching = {")": "(", "]": "[", "}": "{"}
    opening = set(matching.values())

    for character in expression:
        if character in opening:
            stack.push(character)
        elif character in matching:
            if stack.is_empty() or stack.pop() != matching[character]:
                return False
    return stack.is_empty()


def print_queue_exercise():
    """Demonstrate FIFO printing jobs with an unbounded linked queue."""
    queue = LinkedQueue()
    count = int(input("How many print jobs? "))
    for _ in range(count):
        job_id = input("Job ID: ")
        pages = int(input("Number of pages: "))
        queue.enqueue({"id": job_id, "pages": pages})
        print("Enqueued:", job_id, "| State:", queue)

    print("\nPrint order (FIFO):")
    order = 1
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"Wait order {order}: Job {job['id']} - {job['pages']} page(s)")
        order += 1
        print("Queue after printing:", queue)


def choose_structure():
    """Create the selected stack or queue implementation."""
    print("\nChoose implementation:")
    print("1. Array Stack")
    print("2. Linked Stack")
    print("3. Circular Array Queue")
    print("4. Linked Queue")
    choice = input("Choice: ").strip()

    if choice == "1":
        capacity = int(input("Stack capacity (default 5): ") or "5")
        return ArrayStack(capacity), "stack"
    if choice == "2":
        return LinkedStack(), "stack"
    if choice == "3":
        capacity = int(input("Queue capacity (default 5): ") or "5")
        return ArrayQueue(capacity), "queue"
    if choice == "4":
        return LinkedQueue(), "queue"
    print("Invalid implementation choice.")
    return None, None


def operate_structure(structure, kind):
    """Run an operation menu for one selected structure."""
    while True:
        if kind == "stack":
            print("\nOperations: 1 Push | 2 Pop | 3 Peek | 4 Is empty | 5 Is full | 0 Back")
        else:
            print("\nOperations: 1 Enqueue | 2 Dequeue | 3 Peek front | 4 Is empty | 5 Is full | 0 Back")
        choice = input("Choose operation: ").strip()

        try:
            if choice == "0":
                break
            elif choice == "1":
                value = input("Value to add: ")
                structure.push(value) if kind == "stack" else structure.enqueue(value)
                print("Item added.")
            elif choice == "2":
                value = structure.pop() if kind == "stack" else structure.dequeue()
                print("Removed:", value)
            elif choice == "3":
                value = structure.peek() if kind == "stack" else structure.peek_front()
                print("Front/top item:", value)
            elif choice == "4":
                print("Empty:", structure.is_empty())
            elif choice == "5":
                print("Full:", structure.is_full())
            else:
                print("Invalid operation choice.")
                continue
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)

        show_state(structure)


def main():
    while True:
        print("\n=== STACKS AND QUEUES LAB ===")
        print("1. Use a data structure")
        print("2. Balanced parentheses exercise")
        print("3. Print queue exercise")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Program ended.")
            break
        elif choice == "1":
            structure, kind = choose_structure()
            if structure is not None:
                show_state(structure)
                operate_structure(structure, kind)
        elif choice == "2":
            expression = input("Enter an expression using ()[]{}: ")
            result = balanced_parentheses(expression)
            print("Balanced." if result else "Not balanced.")
        elif choice == "3":
            try:
                print_queue_exercise()
            except ValueError:
                print("Error: enter a valid whole number for page counts and job count.")
        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()
