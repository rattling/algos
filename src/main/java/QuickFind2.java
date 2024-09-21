package main.java;

public class QuickFind2 implements UnionFind {

    private final int[] id;
    private final int N;

    public QuickFind2(int N) {
        this.N = N;
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    public boolean connected(int p, int q) {
        return (id[p] == id[q]);
    }

    public void union(int p, int q) {

        if (id[p] == id[q]) {
            return;
        }

        for (int i = 0; i < N; i++) {
            if (id[i] == id[p]) {
                id[i] = id[q];
            }
        }

    }


    public static void main(String[] args) {
        QuickFind2 qf = new QuickFind2(10);
        qf.union(4, 3);
        System.out.println(qf.connected(8, 9));
    }
}
