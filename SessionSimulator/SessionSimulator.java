package SessionSimulator;

import java.time.LocalTime;
import java.util.Vector;

public class SessionSimulator {
    private Vector<Customer> customers;
    private Vector<Provider> providers;
    private Vector<Session> sessions;

    public static void main(String[] args) {
        Customer Ivan = new Customer("Ivan");
        Provider Alex = new Provider("Alex");
        Provider Leo = new Provider("Leo");
        Session tender = new Session("IS", Ivan, 100, 1, 2);
        System.out.println(tender.name + " " + tender.customer + " " + tender.curValue);
        tender.add(Alex, 50);
        tender.add(Leo, 45);
        System.out.println(Ivan.name + " " + Ivan.password);
        System.out.println(tender.name + " " + tender.customer + " " + tender.curValue);
        while ((System.currentTimeMillis() - tender.startTime) / 1000 / 60 < tender.sessionTime) {}
        Ivan.del(tender);
        System.out.println(tender.curValue + " " + tender.winner);
    }
}
