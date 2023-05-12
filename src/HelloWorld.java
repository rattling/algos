public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        Integer x = 10;
        Integer y = 20;
        Integer z = x + y;
        System.out.println(z);
        System.out.println("Goodbye world!");
        //I want to multiply x and y n times
        int n = 5;
        for (int i = 0; i < n; i++) {
            z = z + x;
        }
        System.out.println(z);


    }
}
