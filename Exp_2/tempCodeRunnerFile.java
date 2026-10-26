
class SingletonPattern {
    private static SingletonPattern obj = new SingletonPattern();

    private SingletonPattern() {
        System.out.println("Object Created");
    }

    public static SingletonPattern getInstance() {
        return obj;
    }

    public void display() {
        System.out.println("Singleton Design Pattern");
    }

    public static void main(String[] args) {
        SingletonPattern s1 = SingletonPattern.getInstance();
        SingletonPattern s2 = SingletonPattern.getInstance();

        s1.display();

        if (s1 == s2) {
            System.out.println("Both objects are same");
        }
    }
}
