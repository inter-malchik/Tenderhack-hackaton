package SessionSimulator;

import java.util.HashMap;
import java.util.Map;

public class Test {
    public static void main(String[] args) {
        Map<String, Person> tokens = new HashMap<>();
        Customer Ivan = new Customer("Ivan");
        tokens.put("Ivan", Ivan);
        System.out.println(Ivan.name + " " + Ivan.password);

        Provider Alex = new Provider("Alex");
        Provider Leo = new Provider("Leo");
        tokens.put("Alex", Alex);
        tokens.put("Leo", Leo);

        Session tender = new Session("IS", Ivan, 100, 1, 1);

        System.out.println(tender.name + " " + tender.customer + " " + tender.curValue);
        tender.add(Alex);
        System.out.println(tender.name + " " + tender.customer + " " + tender.curValue);
        tender.add(Leo);
        System.out.println(tender.name + " " + tender.customer + " " + tender.curValue);

        while ((System.currentTimeMillis() - tender.startTime) / 1000 / 60 < tender.sessionTime) {}

        tender.end();
        System.out.println(tender.curValue + " " + tender.winner);

        System.out.println(Alex.historyStats.get(tender));
        System.out.println(Leo.historyStats.get(tender));
    }
}
