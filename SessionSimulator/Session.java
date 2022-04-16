package SessionSimulator;

import java.util.Vector;

public class Session {
    long startTime;
    long time; // minutes

    String name;
    public Customer customer;
    public Vector<Provider> providers;
    public Provider winner; // or an id of a winner in participants array

    public double maxValue; // max price the customer can offer
    public double curValue;
    public double percent; // min percent on which the deal can be lessened

    public Session(String name, Customer customer, double maxValue, double percent, long time) {
        startTime = System.currentTimeMillis();
        this.time = time;
        this.name = name;
        this.curValue = maxValue;
        this.customer = customer;
        this.maxValue = maxValue;
        this.percent = percent;
        customer.add(this);
    }

    public void add(Provider provider, int curValue) {
        if (curValue > this.curValue - percent * maxValue / 100) {
            return;
        }
        if (!providers.contains(provider)) {
            providers.add(provider);
            provider.add(this);
        }
        winner = provider;
        this.curValue = curValue;
    }

    public void end() {
        customer.del(this);
        winner.historyStats.put(this, "Win");
        winner.del(this);
        for (Provider provider : this.providers) {
            if (provider != winner) {
                provider.historyStats.put(this, "Lost");
            }
            provider.del(this);
        }
    }

    @Override
    public String toString() {
        return this.name;
    }
}
