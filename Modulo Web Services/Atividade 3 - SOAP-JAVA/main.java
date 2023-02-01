package app;

import javax.xml.ws.Endpoit;

public class BancoServerPublisher {
    public static void main(String[] args)
    {
        Endpoit.publish("http://127.0.0.1:8080/app"),
        new BancoServer();
    }
}