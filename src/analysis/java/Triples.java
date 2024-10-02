package analysis.java;

import edu.princeton.cs.algs4.StdRandom;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

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

        // Save size and timings to a CSV file
        try (PrintWriter writer = new PrintWriter(new FileWriter("C:\\Users\\john\\IdeaProjects\\algos\\data\\output\\size_timings.csv"))) {
            writer.println("Size,Timing"); // CSV header
            for (int s = 0; s < Trials; s++) {
                writer.println(size[s] + "," + timings[s]);
            }
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }

        // Create and display the scatter plot (set true for log scale, false for normal scale)
    }
}


