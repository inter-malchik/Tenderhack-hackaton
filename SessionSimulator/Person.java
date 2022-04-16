package SessionSimulator;

public class Person {
    String name;
    Session[] history;

    Person(String name, Session[] history) {
        this.name = name;
        this.history = history;
    }
}
