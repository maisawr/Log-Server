using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using static Client.WriteLog;

namespace Client
{
    internal class ConnectServer
    {
        // constants
        const int SUCCESS = 0;
        const int FAILURE = 1;

        // private members
        private static IPAddress ipAddress;
        private static IPEndPoint remoteEP;
        private static Socket sender;

        public static int StartClient(string IP_address, int IP_port)
        {
            try
            {
                // Connect to a Remote server
                ipAddress = IPAddress.Parse(IP_address);
                remoteEP = new IPEndPoint(ipAddress, IP_port);

                // Create a TCP/IP socket.
                sender = new Socket(ipAddress.AddressFamily,
                    SocketType.Stream, ProtocolType.Tcp);

                // Connect to Remote EndPoint
                sender.Connect(remoteEP);

            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
                return FAILURE;
            }

            return SUCCESS;
        }

        public static void CloseClient()
        {
            try
            {
                // Release the socket.
                sender.Shutdown(SocketShutdown.Both);
                sender.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }

        }

        public static void SendLog(string logMessage)
        {
            byte[] bytes = new byte[1024];

            // Connect the socket to the remote endpoint. Catch any errors.
            try
            {
                // Encode the data string into a byte array.
                string text = CreateLog(Level.Info, logMessage);
                byte[] msg = Encoding.ASCII.GetBytes(text);

                // Send the data through the socket.
                int bytesSent = sender.Send(msg);

                // Receive the response from the remote device.
                int bytesRec = sender.Receive(bytes);
                //Console.WriteLine("Echoed test = {0}",
                //    Encoding.ASCII.GetString(bytes, 0, bytesRec));

            }
            catch (ArgumentNullException ane)
            {
                Console.WriteLine("ArgumentNullException : {0}", ane.ToString());
            }
            catch (SocketException se)
            {
                Console.WriteLine("SocketException : {0}", se.ToString());
            }
            catch (Exception e)
            {
                Console.WriteLine("Unexpected exception : {0}", e.ToString());
            }
        }
    }

}
