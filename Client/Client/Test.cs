using System;
using System.IO;
using System.Text;
using static Client.ConnectServer;

namespace Client
{
    internal class Test
    {
        // constants
        const int SUCCESS = 0;
        const int FAILURE = 1;

        private static string path = @".\MyTest.txt";

        public static int TryStartClient(string IP_address, int IP_port)
        {
            Console.WriteLine("[[ Test 0 ]] Connect to the Server");

            if (StartClient(IP_address, IP_port) == SUCCESS)
            {
                string logConnected = "Socket connected to " + IP_address + ";" + IP_port;
                SendLog(Level.Info, logConnected);
                Console.WriteLine("RESULT: Success");
            }
            else
            {
                Console.WriteLine("RESULT: Fail");
                Console.WriteLine("-> Fail to connect to " + IP_address + ";" + IP_port);
                return FAILURE;

            }

            Console.WriteLine();
            return SUCCESS;

        }

        public static void Test1()
        {
            Console.WriteLine("[[ Test 1 ]] Create a file");

            if (File.Exists(path))
            {
                Console.WriteLine("WARNING: File exists already. Delete the file.");
                SendLog(Level.Warning, "File exists already.");

                try
                {
                    File.Delete(path);
                    SendLog(Level.Info, "Delete the file.");
                }
                catch (Exception)
                {
                    SendLog(Level.Error, "Fail to delete the file in " + path);
                }
            }

            try
            {
                using (FileStream fs = File.Create(path))
                {
                    AddText(fs, "This is some text");
                    AddText(fs, "This is some more text,");
                    AddText(fs, "\r\nand this is on a new line");
                    AddText(fs, "\r\n\r\nThe following is a subset of characters:\r\n");

                    for (int i = 1; i < 120; i++)
                    {
                        AddText(fs, Convert.ToChar(i).ToString());

                    }
                }

                SendLog(Level.Info, "Success to create a file in " + path);
                Console.WriteLine("RESULT: Success");
            }
            catch (Exception)
            {
                Console.WriteLine("RESULT: Fail");
                Console.WriteLine("-> Fail to create a file in " + path);
                SendLog(Level.Error, "Fail to create a file in " + path);
            }

            Console.WriteLine();

        }

        public static void Test2()
        {
            Console.WriteLine("[[ Test 2 ]] Try to create a duplicate file");

            if (File.Exists(path))
            {
                SendLog(Level.Warning, "File exists already.");
                Console.WriteLine("RESULT: Success");
            }
            else
            {
                SendLog(Level.Error, "File doesn't exist.");
                Console.WriteLine("RESULT: Fail");
                Console.WriteLine("-> File doesn't exist in " + path);
            }

            Console.WriteLine();

        }


        public static void Test3()
        {
            Console.WriteLine("[[ Test 3 ]] Delete the file");

            try
            {
                File.Delete(path);

                SendLog(Level.Info, "Delete the file in " + path);
                Console.WriteLine("RESULT: Success");

            }
            catch (Exception)
            {
                SendLog(Level.Error, "Fail to delete the file in " + path);
                Console.WriteLine("RESULT: Fail");

            }
            Console.WriteLine();

        }

        public static void Test4()
        {
            Console.WriteLine("[[ Test 4 ]] Delete a file that doesn't exist");

            try
            {
                File.Delete(null);

                SendLog(Level.Info, "Delete the file.");
                Console.WriteLine("RESULT: Fail");

            }
            catch (Exception)
            {
                SendLog(Level.Error, "Cannot delete the file with null pointer");
                Console.WriteLine("RESULT: Success");

            }
        }

        private static void AddText(FileStream fs, string value)
        {
            byte[] info = new UTF8Encoding(true).GetBytes(value);
            fs.Write(info, 0, info.Length);
        }

    }
}
