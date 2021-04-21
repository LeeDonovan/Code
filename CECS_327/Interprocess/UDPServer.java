import java.net.*;
import java.nio.charset.StandardCharsets;
import java.io.*;

public class UDPServer 
{
    public static void main(String[] args) 
    {
        DatagramSocket aSocket = null;
        int port;
        String IPAddress;
        String message;
        try{
            IPAddress = args[0];// gets ip address from cmd line
            port = Integer.valueOf(args[1]);//gets port number from cmd line
            System.out.println("Server is active. Now listening on port " + port);//tells user server is up
            InetAddress aHost = InetAddress.getByName(IPAddress); //gets ip address from where you're sending it to
            aSocket = new DatagramSocket(port, aHost);//creates the server
            
            while(true){
                byte[] buffer = new byte[1000];//sets up a buffer for string
                DatagramPacket request = new DatagramPacket(buffer, buffer.length);//gets the request that is sent to the server
                aSocket.receive(request);//receives the request
                System.out.println("Packet received! ");
                byte[] byteArray = request.getData();//grabs the bytes that were sent over
                String str = new String(byteArray, StandardCharsets.UTF_8);// converts bytes to string 
                System.out.println("Message sent from Client: " + str);
                message = str.toUpperCase();//uppercase message
                byteArray = message.getBytes();//converts string to bytes
                DatagramPacket reply = new DatagramPacket(byteArray,request.getLength(), request.getAddress(),request.getPort());//sends bytes over to client side
                aSocket.send(reply);
            }
        }catch (SocketException e){System.out.println("Socket: " + e.getMessage());}
        catch (IOException e) {System.out.println("IO: " + e.getMessage());}
        finally{if (aSocket != null) aSocket.close();}
    }
}