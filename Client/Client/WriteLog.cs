using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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

            clientName = Environment.GetEnvironmentVariable("CLIENTNAME");
            processName = Process.GetCurrentProcess().ProcessName;
            processID = Process.GetCurrentProcess().Id.ToString();

            return clientName + ":" + processName + ":" + level + ":" + processID + ":" + log;

        }
    }
}
