# Data Structures

## This challenge will help you to:
- Know what a data structure is
- Learn the different types of data structures and the main operations/methods associated with each
- Create each data structure

## Summary
We're going to create several data structures and the methods most commonly used for that data structure using Object Oriented Programming.

### READING DOCUMENTATION IS KEY THROUGHOUT YOUR CAREER (80% reading, 20% coding)

## What is a Data Structure?

“In computer science, a data structure is a data organization, management, and storage format that enables efficient access and modification. __More precisely, a data structure is a collection of data values, the relationships among them within computer memory, and the functions or operations that can be applied to the data.__”

## Types of Data Structures (Please Watch The Video Links)
__Part One__
- [Stacks & Queues](https://youtu.be/wjI1WNcIntg) (Stacks are LIFO "Last in, First out" and have `push` and `pop` methods. Queues are FIFO "First in, First out" and have `enqueue` and `dequeue` methods)
- [Linked Lists](https://youtu.be/njTh_OwMljA) (Linked Lists utilize `Nodes` at each individual 'point' in the Linked list. Each `Node` has a `data` value and `next` value that points to the next `Node`. Linked Lists have an `insert`, `remove`, `display`, and `search` methods)

__Part Two__
- [Binary Tree/Binary Search Tree](https://youtu.be/D5SrAga1pno) (BSTs utilze `Nodes` at each individual point in the BST. Each `Node` has a `key` or `data` value, a `left` value, and a `right` value. The `left` and `right` values point to the `Node` to the left and right of them on the Tree. Binary Search Trees have an `insert`, `delete`, and `search` method)
![BST Example](https://github.com/kiloplatoon/curriculum/blob/master/week-03/lecture-materials/bst.png)
- [Hash Table](https://youtu.be/h2d9b_nEzoA) - [Overview](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)


### Linked List
A Link List is a collection of _Nodes_ (a basic unit of a data structure) that contains data, the `data` or  `value` of the _Node_ and a `next` value that points to the next _Node_ in the Linked List.

```
Head of the Linked List -> Node A
Node A has a value of 23 and a pointer to the next Node -> Node B
Node B has a value of 78 and a pointer to the next Node -> Node C
Node C has a value of 46 and a pointer to the next Node -> null/None (there is no next Node)
```

A Node is a Class Object in and of itself, seperate from a Linked List. A Linked List has many Nodes.

### What do you think a Node Class looks like for a Singly Linked List?
<details><summary>Click here for a Hint</summary>
<p>

__Node Example in Python__
```python
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
```
</p>
</details>


### What do you think a the __init__ method looks like for a Linked List?
<details><summary>Click here for a Hint</summary>
<p>

__Here is the basic Class structure of a Linked List in Python__
```python
class LinkList():
  def __init__(self, head=None):
    self.head = head
    self.length # we're going to store the length of the Linked List here

  def add(self, data):
    # write your code to ADD an element to the Linked List
    pass

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    pass

  def get(self, element):
    # write you code to GET and return an element from the Linked List
    pass

# ---- Node -----
class Node():
  # your __init__ method here

```
</p>
</details>

__ENDED HERE__

## Resources
* [Fundamentals Explaned](https://www.interviewcake.com/article/python/data-structures-coding-interview)
