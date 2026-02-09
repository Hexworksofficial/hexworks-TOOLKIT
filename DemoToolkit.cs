// Hexworks Toolkit Demo (C#)

using System;

namespace HexworksToolkit
{
    class Toolkit
    {
        static void Main()
        {
            Console.WriteLine("Hexworks Toolkit Launcher");
            Console.WriteLine("Version: 1.0 Beta");

            FakeAI ai = new FakeAI();
            ai.Reply("Tell me about the toolkit");

            Console.ReadLine();
        }
    }

    class FakeAI
    {
        public void Reply(string msg)
        {
            Console.WriteLine("AI is typing...");
            System.Threading.Thread.Sleep(1000);

            Console.WriteLine("User: " + msg);
            Console.WriteLine("AI: Hexworks Toolkit is an all-in-one multimedia editor.");
            Console.WriteLine("AI: Enjoy the beta version!");
        }
    }
}
