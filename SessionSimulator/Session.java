package SessionSimulator;

import java.util.Vector;

public class Session {
    long startTime;
    long sessionTime; // minutes

    String name;
    public Customer customer;
    public Vector<Provider> providers;
    public Provider winner; // or an id of a winner in participants array

    public double maxValue; // max price the customer can offer
    public double curValue;
    public double percent; // min percent on which the deal can be lessened

    public Session(String name, Customer customer, double maxValue, double percent, long time) {
        startTime = System.currentTimeMillis();
        this.sessionTime = time;
        this.name = name;
        this.curValue = maxValue;
        this.customer = customer;
        this.maxValue = maxValue;
        this.percent = percent;
        customer.add(this);
    }

    public void add(Provider provider, int curValue) {
        if (curValue > this.curValue - percent * maxValue / 100 || provider == winner) {
            return;
        }
        if (providers != null && !providers.contains(provider)) {
            providers.add(provider);
            provider.add(this);
        }
        winner = provider;
        this.curValue = curValue;
        if (((startTime + sessionTime * 1000 * 60) - System.currentTimeMillis()) / 1000 / 60 < 1) {
            System.out.println((sessionTime - System.currentTimeMillis()) / 1000 / 60);
            sessionTime += 1000 * 60; // 1000 ms * 60 = 60s = 1m
        }
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
