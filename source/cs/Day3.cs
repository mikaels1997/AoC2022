using System;
using System.Collections.Generic;
using System.Linq;

namespace AoC
{
    class Day3
    {
        private string InputPath = "../../data/input3.txt";
        private List<string> Rucksacks = new List<string>();
        private const string Letters = "abcdefghijklmnopqrstuvwxyz" + 
           "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        public Day3() {
            this.ParseInput();
            Console.WriteLine("Priority for common items: " + this.CommonItemsAnalysis());
            Console.WriteLine("Priority for elf groups: " + this.ElfGroupAnalysis());
        }

        private void ParseInput() {
            this.Rucksacks = System.IO.File.ReadAllLines(InputPath).ToList();
        }

        private int CommonItemsAnalysis() { // Part 1
            int totalPriority = 0;
            foreach (var comp in this.Rucksacks) {
                var cLen = comp.Length / 2;
                var comp1 = comp.Substring(0, cLen);
                var comp2 = comp.Substring(cLen);
                var strList = new List<string>(){ comp1, comp2 };
                totalPriority += this.PrioritySum(strList);
            }
            return totalPriority;
        }

        private int ElfGroupAnalysis() {    // Part 2
            int totalPriority = 0;
            int groupNumber = this.Rucksacks.Count / 3;
            for (int i=0; i < groupNumber; i++) {
                var group = this.Rucksacks.GetRange(3*i, 3);
                totalPriority += PrioritySum(group);
            }
            return totalPriority;
        }

        private int PrioritySum(List<string> strs) {
            var common = strs.Aggregate(    // Finds common chars from n strings
                new List<char>(strs[0]),
                (test, next) =>
                    test.Intersect(next).ToList()
            );
            return common.Select(c => Letters.IndexOf(c) + 1).Sum();  // Sum priorities
        }
    }
}
