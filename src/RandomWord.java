import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        String champion = "default";
        int i = 1;

        // Read from standard input
        while (!StdIn.isEmpty()) {
            String word = StdIn.readString();
            // Determine if this word should become the champion
            boolean rnd = StdRandom.bernoulli(1.0 / i);
            if (rnd) {
                champion = word;
            }
            i++;
        }

        // Output the champion word
        if (champion != null) {
            StdOut.println(champion);
        }
    }
}
