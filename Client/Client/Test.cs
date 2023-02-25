using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using static Client.ConnectServer;

namespace Client
{
    internal class Test
    {
        // constants
        const int SUCCESS = 0;
        const int FAILURE = 1;

        public static void TryStartClient(string IP_address, int IP_port)
        {
            Console.WriteLine("------------------------------------------");
            Console.WriteLine("Test 0: Connect to the Server");
            Console.WriteLine("------------------------------------------");

            if (StartClient(IP_address, IP_port) == SUCCESS)
            {
                string logConnected = "Socket connected to " + IP_address + ":" + IP_port;
                SendLog(logConnected);
                Console.WriteLine("Result: Success");
            }
            else
            {
                Console.WriteLine("Result: Fail");
                Console.WriteLine("-> Fail to connect to " + IP_address + ":" + IP_port);
            }

            Console.WriteLine("------------------------------------------");
        }

        public static void Test1()
        {
            Console.WriteLine("------------------------------------------");
            Console.WriteLine("Test 1: ");
            Console.WriteLine("------------------------------------------");


            Console.WriteLine("------------------------------------------");

        }

        public static void Test2()
        {
            Console.WriteLine("------------------------------------------");
            Console.WriteLine("Test 2: Open a file that doesn't exist");
            Console.WriteLine("------------------------------------------");


            Console.WriteLine("------------------------------------------");
        }

        public static void Test3()
        {
            Console.WriteLine("------------------------------------------");
            Console.WriteLine("Test 3: ");
            Console.WriteLine("------------------------------------------");


            Console.WriteLine("------------------------------------------");
        }

    }
}
