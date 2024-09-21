package main.java;

public class QuickFind implements UnionFind {
    private final int[] id;

    public QuickFind(int N) {
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    public boolean connected(int p, int q) {
        return id[p] == id[q];
    }

    public void union(int p, int q) {
        int pid = id[p];
        int qid = id[q];
        if (pid == qid) {
            return;
        }
        for (int i = 0; i < id.length; i++) {
            if (id[i] == pid) {
                id[i] = qid;
            }
        }
    }

    public static void main(String[] args) {
        QuickFind qf = new QuickFind(10);
        qf.union(4, 3);
        qf.union(3, 8);
        qf.union(6, 5);
        qf.union(9, 4);
        qf.union(2, 1);
        System.out.println(qf.connected(8, 9));
        System.out.println(qf.connected(5, 4));
        qf.union(5, 0);
        qf.union(7, 2);
        qf.union(6, 1);
        qf.union(7, 3);
    }
}
