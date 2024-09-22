package main.java;

public class QuickFind3 implements UnionFind {
    private final int N;
    private final int[] id;

    public QuickFind3(int N) {
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
        int pid = id[p];
        int qid = id[q];
        for (int i = 0; i < N; i++) {
            if (id[i] == pid) {
                id[i] = qid;
            }

        }

    }

    public void DoStuff() {
        System.out.println(N);
    }

    public static void main(String[] args) {
        QuickFind3 qf1 = new QuickFind3(10);
        qf1.DoStuff();
        qf1.union(0, 1);
        qf1.union(1, 2);
        System.out.println("0 connected to 1: " + qf1.connected(0, 1));
        System.out.println("0 connected to 6: " + qf1.connected(0, 6));


    }
}
