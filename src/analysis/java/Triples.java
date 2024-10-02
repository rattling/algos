package analysis.java;

import edu.princeton.cs.algs4.StdRandom;

import javax.swing.*;

public class Triples {
    public Triples(int[] input) {
        int count = 0;
        for (int i = 0; i < input.length; i++) {
            for (int j = i + 1; j < input.length; j++) {
                for (int k = j + 1; k < input.length; k++) {
                    if (input[i] + input[j] + input[k] == 0) {
                        count++;
                    }

                }
            }
        }
//        System.out.println((count));
    }

    public static void main(String[] args) {
        int Trials = 10;
        int n = 10;
        int[] size = new int[Trials];
        long[] timings = new long[Trials];
        long start, duration;
        for (int s = 0; s < Trials; s++) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = StdRandom.uniform(-10 * n, 10 * n);
            start = System.currentTimeMillis();
            Triples t = new Triples((a));
            timings[s] = System.currentTimeMillis() - start;
            size[s] = n;
            n *= 2;
        }
        for (int s = 0; s < Trials; s++) {
            System.out.println("N: " + size[s] + " Time: " + timings[s]);
        }
        // Create and display the scatter plot (set true for log scale, false for normal scale)
        SwingUtilities.invokeLater(() -> {
            ScatterPlot plot = new ScatterPlot("Size vs Timing", size, timings, true);  // Use true for log-scale
            plot.pack();
            plot.setLocationRelativeTo(null);
            plot.setVisible(true);
        });
    }
}


