import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    private final boolean[][] grid;
    private final int N;
    private final WeightedQuickUnionUF uf;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        this.N = n;
        grid = new boolean[n][n];
        uf = new WeightedQuickUnionUF(n * n + 2);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                //Set up the grid values - default to closed;
                grid[i][j] = false;
                //Connect the top virtual node to first row and bottom virtual node to bottom row
                if (i == 0) {
                    uf.union(j, n);
                } else if (i == n - 1) {
                    int q = i * n + j;
                    uf.union(q, n + 1);
                }

            }
        }

    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        grid[row][col] = true;

        int p = row * N + col;
        //left neighbour;
        if (col > 0 && isOpen(row, col - 1)) {
            {
                uf.union(p, p - 1);
            }
        }
        //right neighbour;
        if (col < N && isOpen(row, col + 1)) {
            uf.union(p, p + 1);
        }
        //above neighbour;
        if (row > 0 && isOpen(row - 1, col)) {
            uf.union(p, p - N);
        }
        //below neighbour;
        if (row < N && isOpen(row + 1, col)) {
            uf.union(p, p + N);
        }

    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        return (grid[row][col]);
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        boolean connected = false;
        boolean open = false;
        int p;
        //Special case of the virtual bottom node
        if (row == N && col == N) {
            p = N + 1;
            open = true;
        } else {
            p = row * N + col;
            open = isOpen(row, col);
        }
        connected = uf.find(p) == uf.find(N);
        return (open && connected);
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (isOpen(i, j)) {
                    count++;
                }
            }
        }
        return count;
    }

    // does the system percolate?
    public boolean percolates() {
        return (isFull(N, N));
    }

    // test client (optional)
    public static void main(String[] args) {
        int n = 10;
        Percolation perc = new Percolation(n);
        StdRandom.setSeed(10);
        for (int i = 0; i < n * n; i++) {
            int r = StdRandom.uniformInt(n);
            int row = r / n;
            int col = r % n;
            perc.open(row, col);
            if (perc.percolates()) {
                System.out.println("System percolates at i=" + i);
            }

        }


    }
}