package main.java;

public class WQUPC3 implements UnionFind {

    private final int[] id;
    private final int[] sz;
    private final int N;

    public WQUPC3(int N) {
        this.N = N;
        id = new int[N];
        sz = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
            sz[i] = 1;
        }
    }

    public int root(int i) {
        while (i != id[i]) {
            id[i] = id[id[i]]; // path compression
            i = id[i];
        }
        return i;
    }

    public boolean connected(int p, int q) {
        return (root(p) == root(q));
    }

    public void union(int p, int q) {

        if (id[p] == id[q]) {
            return;
        }

        if (sz[p] < sz[q]) {
            id[p] = root(q);
            sz[q] = sz[p] + sz[q];
        } else {
            id[q] = root(p);
            sz[p] = sz[p] + sz[q];
        }

        id[p] = root(q);

    }


    public static void main(String[] args) {
        WQUPC3 qu = new WQUPC3(10);
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
