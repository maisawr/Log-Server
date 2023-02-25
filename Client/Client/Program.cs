using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using static Client.ConnectServer;

namespace Client
{
    internal class Program
    {
        private static string IP_address;
        private static int IP_port;

        static int Main(string[] args)
        {
            // check parameters
            if (getParameter(args) != 0)
            {
                return -1;
            }

            // start connecting
            StartClient(IP_address, IP_port);

            SendLog("test");

            return 0;
        }

        public static int getParameter(string[] args)
        {
            try
            {
                IP_address = args[0];
                IP_port = Int32.Parse(args[1]);

            }
            catch (Exception)
            {
                Console.WriteLine("Usage: IP_address IP_port");
                return -1;
            }

            return 0;

        }

    }
}
