# Analysis

A linked-list stack pushes at the head because the head can be updated directly, so push and pop both take O(1) time. Pushing at the tail of a singly linked list would require traversing the list to find the last node. An array queue must be circular so that positions freed by dequeue can be reused instead of leaving unused spaces at the beginning of the array. The modulo operation wraps the rear and front indexes back to the start when they reach the physical end.
