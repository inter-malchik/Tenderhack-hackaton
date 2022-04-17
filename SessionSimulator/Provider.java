package SessionSimulator;

import java.util.HashMap;
import java.util.Map;

public class Provider extends Person {
    public Map<Session, String> historyStats = new HashMap<>();
    public Provider(String name) {
        super(name);
    }
}