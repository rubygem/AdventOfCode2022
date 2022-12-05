import unittest

class MyTestCase(unittest.TestCase):

    shape_score = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    outcome_score = {'lose': 0, 'draw': 3, 'win': 6}

    #X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    game_key = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'lose', 'Y': 'draw', 'Z': 'win'}


    def score(self, shape, result):
        outcome = self.game_key[result]
        outcome_score = self.outcome_score[outcome]
        return (outcome_score + self.shape_score[shape])

    def getMove(self, theirMove, result):
        theirShape = self.game_key[theirMove]
        if (self.game_key[result] == 'draw'):
            return theirShape
        if (self.game_key[result] == 'win'):
            if theirShape == 'Rock':
                return 'Paper'
            if theirShape == 'Paper':
                return 'Scissors'
            if theirShape == 'Scissors':
                return 'Rock'
        if (self.game_key[result] == 'lose'):
            if theirShape == 'Paper':
                return 'Rock'
            if theirShape == 'Scissors':
                return 'Paper'
            if theirShape == 'Rock':
                return 'Scissors'
        return 0

    def test_case_one(self):
        #In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.

        theirMove = 'A'
        result = 'Y'

        myMove = self.getMove(theirMove, result)

        self.assertEqual('Rock', myMove)
        self.assertEqual(4, self.score(myMove, result))

    def test_case_two(self):
        #In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.

        theirMove = 'B'
        result = 'X'

        myMove = self.getMove(theirMove, result)

        self.assertEqual('Rock', myMove)
        self.assertEqual(1, self.score(myMove, result))

    def test_case_three(self):
        #In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

        theirMove = 'C'
        result = 'Z'

        myMove = self.getMove(theirMove, result)

        self.assertEqual('Rock', myMove)
        self.assertEqual(7, self.score(myMove, result))

    def test_my_score(self):
        #In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.

        filename = "./data/day2.txt"
        my_score = 0
        with open(filename) as f:
            for line in f:
                moves = line.strip().split(' ')
                theirMove = moves[0]
                result = moves[1]

                myMove = self.getMove(theirMove, result)
                my_score +=self.score(myMove, result)

        self.assertEqual(10, my_score)



if __name__ == '__main__':
    unittest.main()