using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

enum Level
{
    Debug,
    Info,
    Warning,
    Error,
    Fatal
}

namespace Client
{
    internal class Program
    {
        static int Main(string[] args)
        {
            string IP_address;
            int IP_port;

            try
            {
                IP_address = args[0];
                IP_port = Int32.Parse(args[1]);

                StartClient(IP_address, IP_port);
            }
            catch (Exception)
            {
                Console.WriteLine("Usage: IP_address IP_port");

                return -1;
            }
            
            return 0;
        }

        public static void StartClient(string IP_address, int IP_port)
        {
            byte[] bytes = new byte[1024];

            try
            {
                // Connect to a Remote server
                IPAddress ipAddress = IPAddress.Parse(IP_address);
                IPEndPoint remoteEP = new IPEndPoint(ipAddress, IP_port);

                // Create a TCP/IP socket.
                Socket sender = new Socket(ipAddress.AddressFamily,
                    SocketType.Stream, ProtocolType.Tcp);

                // Connect the socket to the remote endpoint. Catch any errors.
                try
                {
                    // Connect to Remote EndPoint
                    sender.Connect(remoteEP);
                    string logConnected = "Socket connected to " + sender.RemoteEndPoint.ToString();

                    Console.WriteLine(logConnected);

                    // Encode the data string into a byte array.
                    string text = CreateLog(Level.Info, logConnected);
                    byte[] msg = Encoding.ASCII.GetBytes(text);

                    // Send the data through the socket.
                    int bytesSent = sender.Send(msg);

                    // Receive the response from the remote device.
                    int bytesRec = sender.Receive(bytes);
                    Console.WriteLine("Echoed test = {0}",
                        Encoding.ASCII.GetString(bytes, 0, bytesRec));

                    // Release the socket.
                    sender.Shutdown(SocketShutdown.Both);
                    sender.Close();

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
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        public static string CreateLog(Level level, string log)
        {

            string clientName;
            string processName;
            string processID;

            clientName = Environment.GetEnvironmentVariable("CLIENTNAME");
            processName = Process.GetCurrentProcess().ProcessName;
            processID = Process.GetCurrentProcess().Id.ToString();

            return clientName + ":" + processName + ":" + level + ":" + processID + ":" + log;

        }
    }
}
