using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC 
{
    class Day4
    {
        private string InputPath = "../../data/input4.txt";
        private List<int[]> Pairs = new List<int[]>();
        public Day4() {
            this.ParseInput();
            Console.WriteLine("Fully contained: " + this.FullyContained());
            Console.WriteLine("Partially contained: " + this.PartiallyContained());
        }

        private void ParseInput() {
            this.Pairs = System.IO.File.ReadAllLines(InputPath).Select(
                s => new int[] { 
                    int.Parse(s.Split(',')[0].Split('-')[0]),
                    int.Parse(s.Split(',')[0].Split('-')[1]),
                    int.Parse(s.Split(',')[1].Split('-')[0]),
                    int.Parse(s.Split(',')[1].Split('-')[1]),
                }).ToList();
        }

        private int PartiallyContained() {
            int pairNumber = 0;
            foreach (int[] pair in this.Pairs) {
                if (pair[0] <= pair[2] && pair[2] <= pair[1])
                    pairNumber += 1;
                else if (pair[2] <= pair[0] && pair[0] <= pair[3])
                    pairNumber += 1;
            }
            return pairNumber;
        }

        private int FullyContained() {
            int pairNumber = 0;
            foreach(int[] pair in this.Pairs) {
                if (pair[0] <= pair[2] && pair[1] >= pair[3])
                    pairNumber += 1;
                else if (pair[0] >= pair[2] && pair[1] <= pair[3])
                    pairNumber += 1;
            }
            return pairNumber;
        }
    }
}