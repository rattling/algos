package main.java;

public class QuickUnion2 implements UnionFind {

    private final int[] id;

    public QuickUnion2(int N) {
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    private int root(int i) {
        while (i != id[i]) {
            i = id[i];
        }
        return i;
    }

    public boolean connected(int p, int q) {
        return (root(p) == root(q));
    }

    public void union(int p, int q) {

        id[p] = root(q);
    }


    public static void main(String[] args) {
        QuickUnion2 qu = new QuickUnion2(10);
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
