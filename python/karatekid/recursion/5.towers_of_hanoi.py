moves = 0


def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk from {source} to {target}")
        return 1
    else:
        count1 = hanoi(n - 1, source, target, auxiliary)
        print(f"Move disk from {source} to {target}")
        count2 = hanoi(n - 1, auxiliary, source, target)
        return count1 + 1 + count2


print(hanoi(3, "A", "B", "C"))

"""

Inital State
1
2
3   X   X

Desired State
        1
        2
x   x   3

What must we do?
We must get the top n-1 disks onto auxiliary so we can move biggest disk to target, then get those to target

ALGORITHM
1. GET top n-1 form source to auxiliary
2. MOVE biggest disk from source to target
3. GET top n-1 from auxiliary to target

WE DON'T KNOW HOW TO DO "GETS" IN ADVANCE SO MUST BREAK DOWN THOS TASKS FURTHER TO FIND OUT

LET'S START
I. ULTIMATE GOAL - MOVE 1,2,3 FROM A TO C
SOURCE=A
AUXILIARY=B
TARGET=C
N=3

hanoi(n, 'A', 'B', 'C') # A TO C

HOW?

1. GET 1,2 from A to B SUBTASK 1.1
2. MOVE 3 to C
3. GET 1,2 from B TO C SUBTASK 1.2

II. GOAL - SOLVE SUBTASK 1.1 -  MOVE 1,2 FROM A TO B
SOURCE=A
AUXILIARY=C
TARGET=B


TRANSITION #1 
SOURCE<-SOURCE
AUXILIARY-<TARGET
TARGET<-AUXILIARY 

hanoi(n-1, 'A', 'C', 'B') # A TO B

HOW?
1. MOVE 1 FROM A TO C
2. MOVE 2 FROM A TO B
3. MOVE 1 FROM C TO B

III. GOAL - SOLVE SUBTASK 1.3 -  MOVE 1,2 FROM B TO C
SOURCE=B
AUXILIARY=A
TARGET=C

TRANSITION #2 
SOURCE<-TARGET<-AUXILIARY
AUXILIARY<-SOURCE<-SOURCE
TARGET<-AUXILIARY<=TARGET

hanoi(n-1, 'B', 'A', 'C')  # B TO C


HOW?
1. MOVE 1 FROM A TO C
2. MOVE 2 FROM A TO B
3. MOVE 1 FROM C TO B

"""
