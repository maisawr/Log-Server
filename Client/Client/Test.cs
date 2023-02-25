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
            if (StartClient(IP_address, IP_port) == SUCCESS)
            {
                string logConnected = "Socket connected to " + IP_address + ":" + IP_port;
                Console.WriteLine(logConnected);
                SendLog(logConnected);
            }
            else
            {
                Console.WriteLine("Fail to connect to " + IP_address + ":" + IP_port);
            }
        }


    }
}
