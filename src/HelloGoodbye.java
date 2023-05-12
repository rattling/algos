public class HelloGoodbye {
    public static void main(String[] args) {
        if (args.length > 0) {
            // create a string with spaces from the args
            String name = String.join(" and ", args);
            System.out.println("Hello " + name);
            // reverse the order of the args to print a goodbye message
            String[] reversedArgs = new String[args.length];
            for (int i = 0; i < args.length; i++) {
                reversedArgs[i] = args[args.length - i - 1];
            }
            name = String.join(" and ", reversedArgs);
            System.out.println("Goodbye " + name);
            System.out.println("A");
        }
    }
}
