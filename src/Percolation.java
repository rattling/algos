import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;


public class Percolation {

    private final boolean[][] grid;
    private final int n;
    private final int top;
    private final int bottom;
    private final WeightedQuickUnionUF uf;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        if (n < 1) {
            throw new IllegalArgumentException("Grid length < 1 provided");
        }
        this.n = n;
        // Add virtual top and bottom nodes;
        this.top = n * n;
        this.bottom = top + 1;
        grid = new boolean[n][n];
        uf = new WeightedQuickUnionUF(n * n + 2);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Set up the grid values - default to closed;
                grid[i][j] = false;
                // Connect the top virtual node to first row and bottom virtual node to bottom row
                if (i == 0) {
                    uf.union(j, top);
                } else if (i == n - 1) {
                    int q = i * n + j;
                    uf.union(q, bottom);
                }

            }
        }

    }

    // Helper method to validate row and column indices (1-based)
    private void validateIndices(int row, int col) {
        if (row < 1 || row > n || col < 1 || col > n) {
            throw new IllegalArgumentException("Row or column index out of bounds");
        }
    }

    // Helper method to convert 2D index (row, col) to 1D index for Union-Find
    private int to1D(int row, int col) {
        return (row - 1) * n + (col - 1);  // Convert 1-based to 0-based and map to 1D
    }

    public void open(int row, int col) {
        validateIndices(row, col);  // Validate the indices first
        int p = to1D(row, col);  // Convert to 1D index

        if (!grid[row - 1][col - 1]) {  // Use 0-based indexing for the grid
            grid[row - 1][col - 1] = true;

            // Union with neighbors if they are open
            if (col > 1 && isOpen(row, col - 1)) {  // Left
                uf.union(p, to1D(row, col - 1));
            }
            if (col < n && isOpen(row, col + 1)) {  // Right
                uf.union(p, to1D(row, col + 1));
            }
            if (row > 1 && isOpen(row - 1, col)) {  // Above
                uf.union(p, to1D(row - 1, col));
            }
            if (row < n && isOpen(row + 1, col)) {  // Below
                uf.union(p, to1D(row + 1, col));
            }
        }
    }


    public boolean isOpen(int row, int col) {
        validateIndices(row, col);  // Validate the indices first
        return grid[row - 1][col - 1];  // Return the status using 0-based indexing
    }


    public boolean isFull(int row, int col) {
        validateIndices(row, col);  // Validate the indices first
        return isOpen(row, col) && uf.find(to1D(row, col)) == uf.find(top);  // Check if connected to virtual top node
    }


    // returns the number of open sites
    public int numberOfOpenSites() {
        int count = 0;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (isOpen(i, j)) {
                    count++;
                }
            }
        }
        return count;
    }

    // does the system percolate?
    public boolean percolates() {
        return uf.find(top) == uf.find(bottom);  // Check if virtual top node is connected to virtual bottom node
    }

    // test client (optional)
    public static void main(String[] args) {
        int n = 3;
        boolean debug = true;
        Percolation perc = new Percolation(n);
//        StdRandom.setSeed(99);

        // Debug prints (can comment out for submission)
//        if (debug) {
//            PercolationDebug.printGrid(perc.grid, n, perc.uf, perc.top);
//            PercolationDebug.printGraph(perc.uf, n);
//        }

        for (int i = 0; i < 100; i++) {
            while (true) {
                int r = StdRandom.uniformInt(n * n);  // Generate random site
                int row = r / n + 1;  // Convert r to 1 based row
                int col = r % n + 1;  // Convert r to 1 based col

                if (!perc.isOpen(row, col)) {  // Check if the site is not open
                    perc.open(row, col);  // Open the new site
                    break;  // Exit the loop once a new site is opened
                }
                // If the site is already open, the loop will repeat
            }


            // Debug prints (can comment out for submission)
//            if (debug) {
//                PercolationDebug.printGrid(perc.grid, n, perc.uf, perc.top);
//                PercolationDebug.printGraph(perc.uf, n);
//            }

            if (perc.percolates()) {
//                System.out.println("System percolates at i=" + i);
                return;
            }
        }
//        System.out.println("Finishing up");
    }
}