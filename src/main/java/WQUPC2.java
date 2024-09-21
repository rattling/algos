package main.java;

public class WQUPC2 implements UnionFind {
    private final int[] id;
    private final int[] sz;

    public WQUPC2(int N) {
        id = new int[N];
        sz = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
            sz[i] = 1;
        }
    }

    private int root(int i) {
        while (i != id[i]) {
            id[i] = id[id[i]]; //path compression, each node points to its grandparent ie skip a level, halving length
            i = id[i];
        }
        return i;
    }

    public boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    public void union(int p, int q) {
        //NOTE: Only the root node of the newly formed tree (i.e. the root of the tree into which the other tree is being merged is updated);
        //Size means size of tree from a root. A root that is being absorbed and any other node no longer need to be tracked for size;
        int i = root(p);
        int j = root(q);
        if (i == j) {
            return;
        }
        if (sz[i] <= sz[j]) {
            id[i] = j;
            sz[i] = sz[i] + sz[j];
        } else {
            id[j] = i;
            sz[j] = sz[i] + sz[j];
        }
    }

    public static void main(String[] args) {
        WQUPC2 qu = new WQUPC2(10);
        qu.union(4, 3);
        qu.union(3, 8);
        qu.union(6, 5);
        qu.union(9, 4);
        qu.union(2, 1);
        System.out.println(qu.connected(8, 9));
        System.out.println(qu.connected(5, 4));
        qu.union(5, 0);
        qu.union(7, 2);
        qu.union(6, 1);
        qu.union(7, 3);
    }
}




