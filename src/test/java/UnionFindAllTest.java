package test.java;

import main.java.UnionFind;
import main.java.QuickFind;
import main.java.QuickFind2;
import main.java.QuickFind3;
import main.java.QuickUnion;
import main.java.QuickUnion2;
import main.java.QuickUnion3;
import main.java.WQUPC2;
import main.java.WQUPC3;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.Collection;

@RunWith(Parameterized.class)
public class UnionFindAllTest {

    private final UnionFind uf;

    public UnionFindAllTest(UnionFind uf) {
        this.uf = uf;
    }

    @Parameterized.Parameters
    public static Collection<Object[]> provideUnionFindImplementations() {
        return Arrays.asList(new Object[][]{
                {new QuickFind(10)},
                {new QuickFind2(10)},
                {new QuickFind3(10)},
                {new QuickUnion(10)},
                {new QuickUnion2(10)},
                {new QuickUnion3(10)},
                {new WQUPC2(10)},
                {new WQUPC3(10)},

        });
    }

    @Test
    public void testUnionAndConnected() {
        uf.union(3, 4);
        assertTrue(uf.connected(3, 4));

        uf.union(5, 6);
        assertTrue(uf.connected(5, 6));

        assertFalse(uf.connected(3, 5));
    }
}
