import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PercolationDebug {

    // Print the Union-Find graph structure
    public static void printGraph(WeightedQuickUnionUF uf, int N) {
        System.out.println("Union-Find Graph:");

        // Create a map to store root -> children relationships
        Map<Integer, List<Integer>> rootToChildren = new HashMap<>();

        // Traverse the Union-Find structure to build the root -> children map
        for (int i = 0; i < N * N + 2; i++) {
            int root = uf.find(i);  // Get the root of the current node
            rootToChildren.computeIfAbsent(root, k -> new ArrayList<>()).add(i);
        }

        // Print the graph based on root -> children relationships
        for (Map.Entry<Integer, List<Integer>> entry : rootToChildren.entrySet()) {
            int root = entry.getKey();
            List<Integer> children = entry.getValue();
            System.out.println("Root " + root + ": " + children);
        }
    }

    // Print the percolation grid structure
    public static void printGrid(boolean[][] grid, int N, WeightedQuickUnionUF uf, int top) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (uf.find(i * N + j) == uf.find(top)) {
                    System.out.print(" x ");  // full site
                } else if (grid[i][j]) {
                    System.out.print(" . ");  // open site
                } else {
                    System.out.print(" # ");  // blocked site
                }
            }
            System.out.println();  // move to the next row
        }
        System.out.println();  // extra line for clarity
    }
}


