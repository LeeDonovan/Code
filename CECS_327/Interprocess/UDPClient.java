import java.net.;
import java.io.;
import java.util.*;

public class UDPClient
{
    public static void main(String[] args) 
    {
        Scanner console = new Scanner(System.in);
        String IPAddress;
        int Port;
        String message;
        String response;
        boolean val = true;
        //User input, entering IP address, port number, and message to be sent to 
        System.out.println("Please enter the IP Address: ");
        IPAddress = console.nextLine();
        System.out.println("Please enter the Port Number: ");
        response = console.nextLine();
        Port = Integer.valueOf(response);

        DatagramSocket ds = null;
        while(val)
        {
            System.out.println("Please enter a message: ");
            message = console.nextLine();
            if(message.equals("QUIT"))
                val = false;

        try 
        {
            ds = new DatagramSocket(); //creates a new datagram socket
            byte[] buffer = message.getBytes(); // gets the data from the buffer 
            InetAddress aHost = InetAddress.getByName(IPAddress); 
            DatagramPacket request = new DatagramPacket(buffer, buffer.length, aHost, Port); 
            ds.send(request); // sends the packet (message)
            byte[] buffer1= new byte[1000]; // creates a new buffer with new, fresh space
            DatagramPacket reply = new DatagramPacket(buffer1, buffer1.length);
            //ds.setSoTimeout(3000);
            ds.receive(reply);
            System.out.println("Reply: " + new String(reply.getData()));
        }catch(SocketException e)
        {
            System.out.println("Socket: " + e.getMessage());
            continue;
        }
        catch(IOException e) 
        {
            System.out.println("IO: " + e.getMessage());
            continue;
        }
        finally{if (ds != null) ds.close();}
        }
    }
}
