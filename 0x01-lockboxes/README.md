# 0x01. Lockboxes

This folder contains source code for the solution of the Lockboxes project.
In this project, we have n number of locked boxes in front of us. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

We write a method that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
	- We assume all keys will be positive integers
	- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- We return `True` if all boxes can be opened, else return `False`
