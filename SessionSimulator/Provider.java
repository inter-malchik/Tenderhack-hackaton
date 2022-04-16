package SessionSimulator;

import java.util.HashMap;
import java.util.Map;

public class Provider extends Person {
    Map<Session, String> historyStats = new HashMap<>();
    Provider(String name) {
        super(name);
    }
}
