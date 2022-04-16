package SessionSimulator;

import java.time.LocalTime;
import java.util.Vector;

public class SessionSimulator {
    private Vector<Customer> customers;
    private Vector<Provider> providers;
    private Vector<Session> sessions;

    public static void main(String[] args) {
        Customer Ivan = new Customer("Ivan");
        Session tender = new Session("IS", Ivan, 100, 1, 3);
        System.out.println(Ivan.name + " " + Ivan.password);
        System.out.println(tender.name + " " + tender.customer + " " + tender.curValue);
        while ((System.currentTimeMillis() - tender.startTime) / 1000 / 60 < 3) {}
        Ivan.del(tender);
        System.out.println("deleted");
    }
}
