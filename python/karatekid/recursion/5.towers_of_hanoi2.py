def hanoi(n, src, anc, tgt):
    if n == 1:
        print(f"Moving {src} to {tgt}")
    else:
        hanoi(n - 1, src, tgt, anc)
        print(f"Moving {src} to {tgt}")
        hanoi(n - 1, anc, src, tgt)


hanoi(3, "a", "b", "c")

"""
algo
Move n-1 to ancilliary
Move largest to target
Move n-1 to target

Trick is to define the recursive algorithm at a hig level without necessarily knowing how to implement subgoals.
The subgoals because they reduce, eventually unwind into a a single move.
"""
