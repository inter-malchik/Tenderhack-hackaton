package SessionSimulator;

public class Session {
    Person customer;
    Person[] participants;
    Person winner; // or an id of a winner in participants array

    int maxValue; // max price the customer can offer
    int curValue;
    int percent; // min percent on which the deal can be lessen

    int time;
    int leftTime;
    Session(Person customer, Person[] participants, int maxValue, int curValue, int percent, int time) {
        this.customer = customer;
        this.participants = participants;
        this.maxValue = maxValue;
        this.curValue = curValue;
        this.percent = percent;
        this.time = time;
        this.leftTime = time;
    }
}
