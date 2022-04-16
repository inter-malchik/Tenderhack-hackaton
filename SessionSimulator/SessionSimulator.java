package SessionSimulator;

import java.util.HashMap;
import java.util.Map;
import java.util.Vector;

public class SessionSimulator {
    public static void main(String[] args) {
        Map<String, Person> tokens = new HashMap<>();

        Customer Ivan = new Customer("Ivan");
        Customer Artyom = new Customer("Artyom");
        Customer Maria = new Customer("Maria");

        Session IS = new Session("IS", Ivan, 1000, 2.5, 3);
        Session VT = new Session("VT", Artyom, 2000, 1, 3);
        Session CT = new Session("CT", Maria, 500, 5, 3);

        Provider Alex = new Provider("Alex");
        Provider Leo = new Provider("Leo");
        Provider Mila = new Provider("Mila");
        Provider Anton = new Provider("Anton");
        Provider Ksenia = new Provider("Ksenia");

        tokens.put(Ivan.password, Ivan);
        tokens.put(Artyom.password, Artyom);
        tokens.put(Maria.password, Maria);
        tokens.put(Alex.password, Alex);
        tokens.put(Leo.password, Leo);
        tokens.put(Mila.password, Mila);
        tokens.put(Anton.password, Anton);
        tokens.put(Ksenia.password, Ksenia);


    }
}
