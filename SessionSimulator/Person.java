package SessionSimulator;

import java.util.Vector;

public class Person {
    public String name;
    public Vector<Session> current = new Vector<>();
    public Vector<Session> history = new Vector<>();
    public String password = PasswordGenerator.generateStrongPassword();

    public Person(String name) {
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
        history.add(session);
    }

    @Override
    public String toString() {
        return name;
    }
}
