package SessionSimulator;

public class SessionSimulator {
    private Customer[] customers;
    private Provider[] providers;
    private Session[] sessions;

    public static void main(String[] args) {
        Customer Ivan = new Customer("Ivan");
        System.out.println(Ivan.password);
    }
}
