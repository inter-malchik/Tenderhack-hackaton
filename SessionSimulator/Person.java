package SessionSimulator;

import java.util.Vector;

public class Person {
    String name;
    Vector<Session> current;
    Vector<Session> history;
    String password = PasswordGenerator.generateStrongPassword();

    Person(String name) {
        this.name = name;
    }

    public void add(Session session) {
        current.add(session);
    }

    public void del(Session session) {
        if (!current.contains(session)) {
            return;
        }
        current.remove(session);
    }
}
