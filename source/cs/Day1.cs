using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC
{
    class Day1
    {
        private string InputPath = "../../data/input1.txt";
        private List<int> Calories = new List<int>() { 0 };
        public Day1 ()
        {
            this.ParseInput();
            Console.WriteLine("Most calories:" + this.FindTopSum(1));  // Part 1
            Console.WriteLine("Sum of top 3 calories" + this.FindTopSum(3));  // Part 2
        }

        private void ParseInput() {
            string[] lines = System.IO.File.ReadAllLines(InputPath);
            foreach (string line in lines) {
                if (line.Length == 0) {
                    this.Calories.Add(0);
                    continue;
                }
                this.Calories[this.Calories.Count - 1] += int.Parse(line);
            }
            this.Calories = this.Calories.OrderByDescending(c => c).ToList();
        }

        private int FindTopSum(int topNum) {
            return this.Calories.Take(topNum).Sum();
        }
    }
}
