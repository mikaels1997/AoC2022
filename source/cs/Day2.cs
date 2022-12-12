using System;
using System.Collections.Generic;

namespace AoC
{
    class Day2
    {
        private string InputPath = "../../data/input02.txt";
        // Opponent input: (losing player move, draw player move, winning player move)
        private Dictionary<char, char[]> GameLogic = new Dictionary<char, char[]>() {
            {'A', new char[] {'Z', 'X', 'Y'}},
            {'B', new char[] {'X', 'Y', 'Z'}},
            {'C', new char[] {'Y', 'Z', 'X'}}
        };
        private Dictionary<char, int> Points = new Dictionary<char, int>() {
            {'X', 1},
            {'Y', 2},
            {'Z', 3}
        };
        private List<string> Strategy = new List<string>();
        
        public Day2 ()
        {
            this.ParseInput();
            Console.WriteLine("Normal strategy: " + NormalStrategy());
            Console.WriteLine("Secret strategy: " + SecretStrategy());
        }

        private void ParseInput() {
            string[] lines = System.IO.File.ReadAllLines(InputPath);
            foreach (string line in lines) {
                this.Strategy.Add(line);
            }
        }

        private int NormalStrategy() {
            int totalPoints = 0;
            foreach (var round in this.Strategy) {
                var resultPoints = 0;
                var logic = this.GameLogic;
                if (logic[round[0]][2] == round[2])
                    resultPoints += 6;
                if (logic[round[0]][1] == round[2])
                    resultPoints += 3;
                totalPoints += this.Points[round[2]] + resultPoints;
            }
            return totalPoints;
        }

        private int SecretStrategy() {
            int totalScore = 0;
            foreach(var round in this.Strategy) {
                var logic = this.GameLogic;
                var playerInput = logic[round[0]][0];     // Losing move
                if (round[2] == 'Y') {
                    totalScore += 3;
                    playerInput = logic[round[0]][1]; // Drawing move
                }
                else if (round[2] == 'Z') {
                    totalScore += 6;
                    playerInput = logic[round[0]][2]; // Winning move
                }
                totalScore += this.Points[playerInput];             
            }
            return totalScore;
        }
    }
}
