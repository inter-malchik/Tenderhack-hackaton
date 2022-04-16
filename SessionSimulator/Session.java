package SessionSimulator;

import java.util.Vector;

public class Session {
    public Customer customer;
    public Vector<Provider> providers;
    public Person winner; // or an id of a winner in participants array

    public int maxValue; // max price the customer can offer
    public int curValue;
    public int percent; // min percent on which the deal can be lessen

    public int time;
    public int leftTime;
    public Session(Customer customer, int maxValue, int percent, int time) {
        this.customer = customer;
        this.maxValue = maxValue;
        this.percent = percent;
        this.time = time;
        this.leftTime = time;
    }

    public void add(Provider provider, int curValue) {
        providers.add(provider);
        this.curValue = curValue;
    }
}
