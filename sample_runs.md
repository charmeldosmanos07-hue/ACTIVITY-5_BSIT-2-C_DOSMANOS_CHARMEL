# Sample Runs

These are representative outputs from the program. The exact menu prompts may appear on the same line when entered interactively.

## 1. Array Stack Underflow

```text
Choose implementation: 1
Stack capacity (default 5): 2
Choose operation: 2
Error: Stack underflow: cannot pop from an empty stack.
Current state: ArrayStack(bottom -> top): [] (capacity=2)
Empty: True | Full: False
```

## 2. Array Stack Overflow

```text
Choose implementation: 1
Stack capacity (default 5): 2
Choose operation: 1
Value to add: A
Item added.
Choose operation: 1
Value to add: B
Item added.
Choose operation: 1
Value to add: C
Error: Stack overflow: cannot push onto a full stack.
Current state: ArrayStack(bottom -> top): ['A', 'B'] (capacity=2)
Empty: False | Full: True
```

## 3. Circular Array Queue Wrap-Around

```text
Choose implementation: 3
Queue capacity (default 5): 3
Enqueue A
Enqueue B
Enqueue C
Dequeue -> A
Dequeue -> B
Enqueue D
Enqueue E
Current logical queue (front -> rear): ['C', 'D', 'E']
```

The queue reuses array positions freed by the two dequeue operations. Its rear index wraps back to the beginning of the array.

## 4. Balanced Parentheses

```text
Enter an expression using ()[]{}: {[()]}
Balanced.

Enter an expression using ()[]{}: ([)]
Not balanced.
```

## 5. Print Queue (FIFO)

```text
How many print jobs? 2
Job ID: P01
Number of pages: 3
Job ID: P02
Number of pages: 5

Print order (FIFO):
Wait order 1: Job P01 - 3 page(s)
Wait order 2: Job P02 - 5 page(s)
```
