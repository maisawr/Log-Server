using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using static Client.ConnectServer;
using static Client.Test;
using System.ComponentModel.Design;

namespace Client
{
    internal class Program
    {
        // constants
        const int SUCCESS = 0;
        const int FAILURE = 1;

        // private members
        private static string IP_address;
        private static int IP_port;

        static int Main(string[] args)
        {
            // check parameters
            if (getParameter(args) == FAILURE)
            {
                return FAILURE;
            }

            // start connecting
            // EXPECTED RESULT: Info
            TryStartClient(IP_address, IP_port);

            // TEST 1: Create a file
            // EXPECTED RESULT: INFO
            Test1();

            // TEST 2: Delete a file
            // EXPECTED RESULT: INFO
            Test2();

            // TEST 3: Open a file that doesn't exist
            // EXPECTED RESULT: ERROR
            Test3();

            // release the connection
            CloseClient();

            return SUCCESS;
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
                return FAILURE;
            }

            return SUCCESS;

        }

    }
}
