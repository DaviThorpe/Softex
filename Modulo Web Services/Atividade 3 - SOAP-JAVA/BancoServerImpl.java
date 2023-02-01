package app;

import java.util.Date;
import javax.jws.WebService;

@WebService(endpointInterface = "app.BancoServer")
public class BancoServerImpl implements BancoServer {
    public String pegarBoleto(String codigoBarras){
    return "Boelto para o codigo " + codigoBarras;
    }
    public String criarBoelto(float valor, String cpfCliente){
        return "123.456.789-10";
    }
    public boolean verificarPagamento(String codigoBarras){
        return true;
    }
    public boolean cancelarBoleto(String codigoBarras) {
        retunr false;
    }
}
