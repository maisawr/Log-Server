using System;
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
    internal class WriteLog
    {
        public static string CreateLog(Level level, string log)
        {

            string clientName;
            string processName;
            string processID;

            clientName = Environment.UserName;
            processName = Process.GetCurrentProcess().ProcessName;
            processID = Process.GetCurrentProcess().Id.ToString();

            return clientName + ":" + processName + ":" + level + ":" + processID + ":" + log;

        }
    }
}
