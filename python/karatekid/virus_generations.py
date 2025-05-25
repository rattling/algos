from itertools import repeat
import random


class Virus:
    def __init__(self, genome, parent):
        self.genome = genome
        self.parent = parent


def create_initial_pop(bases, gene_length, pop_size):
    s = random.choices(bases, k=pop_size * gene_length)
    pop_genes = [s[i : i + gene_length] for i in range(0, len(s), gene_length)]
    pop = []
    for g in pop_genes:
        pop.append(Virus(g, None))
    return pop


def replicate(g, p_mut):
    new_g = g.copy()
    if random.random() < p_mut:
        n_mut = random.randint(1, gene_length)
        for i in range(0, n_mut):
            new_base = random.choice(bases)
            target = random.randint(0, gene_length - 1)
            new_g[target] = new_base
        return new_g
    else:
        return new_g


def build_phylo_tree(viruses):
    phylo_tree = {}
    for virus in viruses:
        parent = virus.parent
        if parent not in phylo_tree:
            phylo_tree[parent] = []
        phylo_tree[parent].append(virus)
    return phylo_tree


def print_tree(virus, phylo_tree, depth=0):
    m = "M" if virus.parent is not None and virus.parent.genome != virus.genome else ""
    print("  " * depth + f"- {virus.genome} {m}")
    for child in phylo_tree.get(virus, []):
        print_tree(child, phylo_tree, depth + 1)


def run_simulation(pop, sims, p_rep, p_mut):
    for i in range(sims):
        for v in pop:
            if random.random() < p_rep:
                n_replications = random.choice(off)
                for i in range(1, n_replications):
                    pop.append(Virus(replicate(v.genome, p_mut), v))

    return pop


if __name__ == "__main__":
    bases = ["A", "C", "G", "T"]
    gene_length = 2
    pop_size = 5
    sims = 3
    p_rep = 0.8
    p_mut = 0.3
    off = [0, 1, 2, 3]

    pop = create_initial_pop(bases, gene_length, pop_size)
    new_pop = run_simulation(pop, sims, p_rep, p_mut)
    phylo_tree = build_phylo_tree(new_pop)
    roots = [v for v in new_pop if v.parent is None]
    for root in roots:
        print("\n\n")
        print_tree(root, phylo_tree)

    # Finish my aside with recursion by way of Levenshtein
    # When I come back, ask for other stuff re virus and recursive algos
    # Check rate of mutation is as expected, still a bit low?
    # start on the clustering solution to construct the phylogenic tree (when tree not unknown)
    # Robinson-Foulds distance to compare inferred to actual
