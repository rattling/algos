package test.java;

import org.junit.Test;

import static org.junit.Assert.*;

import main.java.QuickFind3;

public class QuickFindTest {

    @Test
    public void testUnionAndConnected() {
        QuickFind3 qf = new QuickFind3(10);

        // Initially, no elements should be connected
        assertFalse(qf.connected(3, 4));

        // Perform a union and test again
        qf.union(3, 4);
        assertTrue(qf.connected(3, 4));

        // Test another connection
        qf.union(5, 6);
        assertTrue(qf.connected(5, 6));

        // Check non-connected elements
        assertFalse(qf.connected(3, 5));
    }
}

