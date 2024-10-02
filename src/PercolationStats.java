import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private static final double Z = 1.96;
    private final int trials;
    private final double[] results;


    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        // Check if n or trials are <= 0 and throw an exception
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("n and trials must be greater than 0");
        }

        this.trials = trials;
        this.results = new double[trials];

        //  StdRandom.setSeed(99);
        for (int t = 0; t < trials; t++) {
            // PercolationDebug.printGrid(perc.grid, n, perc.uf, perc.top);
            // PercolationDebug.printGraph(perc.uf, n);

            Percolation perc = new Percolation(n);

            for (int i = 0; i < n * n; i++) {
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
                // PercolationDebug.printGrid(perc.grid, n, perc.uf, perc.top);
                // PercolationDebug.printGraph(perc.uf, n);
                if (perc.percolates()) {
                    // TODO - what about if the system doesnt percolate. Well it would remain null so deal with later I guess;
                    results[t] = (double) perc.numberOfOpenSites() / (n * n);
//                    System.out.println("System percolates at i=" + i);
                    break;
                }
            }
        }
//        System.out.println("Finishing up");
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(results);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(results);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean() - Z * stddev() / Math.sqrt(trials);
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean() + Z * stddev() / Math.sqrt(trials);
    }

    // test client (see below)
    public static void main(String[] args) {
        if (args.length == 2) {
            PercolationStats ps = new PercolationStats(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
            System.out.println("mean = " + ps.mean());
            System.out.println("stddev = " + ps.stddev());
            System.out.println("95% confidence interval = [" + ps.confidenceLo() + "," + ps.confidenceHi() + "]");
        }
    }
}
