package SessionSimulator;

import java.util.HashMap;
import java.util.Map;
import java.sql.*;

public class SessionSimulator {
    public static final String DB_Driver = "org.postgresql.Driver";
    public static final String DB_URL = "jdbc:h2:/c:/JavaPrj/SQLDemo/db/stockExchange";

    public static void main(String[] args) throws ClassNotFoundException {
        try {
            Class.forName(DB_Driver); //Проверяем наличие JDBC драйвера для работы с БД
            Connection connection = DriverManager.getConnection(DB_URL);//соединениесБД
            System.out.println("Соединение с СУБД выполнено.");
            connection.close();       // отключение от БД
            System.out.println("Отключение от СУБД выполнено.");
        } catch (ClassNotFoundException e) {
            e.printStackTrace(); // обработка ошибки  Class.forName
            System.out.println("JDBC драйвер для СУБД не найден!");
        } catch (SQLException e) {
            e.printStackTrace(); // обработка ошибок  DriverManager.getConnection
            System.out.println("Ошибка SQL !");
        }

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