import unittest


class MyTestCase(unittest.TestCase):
    game_key = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

    shape_score = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    outcome_score = {'lose': 0, 'draw': 3, 'win': 6}

    #rules Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    def player2_result(self, theirMove, myMove):
        theirShape = self.game_key[theirMove]
        myShape = self.game_key[myMove]

        if myShape == theirShape:
            return 'draw'
        if theirShape == 'Rock' and myShape == 'Paper':
            return 'win'
        if theirShape == 'Paper' and myShape == 'Scissors':
            return 'win'
        if theirShape == 'Scissors' and myShape == 'Rock':
            return 'win'
        else:
            return 'lose'

    def score(self, move, result):
        outcome_score = self.outcome_score[result]
        shape = self.game_key[move]
        return (outcome_score + self.shape_score[shape])




    def test_my_score(self):
        filename = "./data/day2.txt"
        my_score = 0
        with open(filename) as f:
            for line in f:
                moves = line.strip().split(' ')
                theirMove = moves[0]
                myMove = moves[1]

                result = self.player2_result(theirMove, myMove)

                my_score += self.score(myMove, result)
        self.assertEqual(10, my_score)


    def test_paper_beats_rock(self):

        moves = ['B', 'X']

        myMove = moves[1]
        theirMove = moves[0]

        result = self.player2_result(theirMove, myMove)

        theirShape = self.game_key[theirMove]
        myShape = self.game_key[myMove]

        self.assertEqual('Paper', theirShape)
        self.assertEqual('Rock', myShape)
        self.assertEqual('lose', result)

    def test_rock_defeated_by_paper(self):

        moves = ['A', 'Y']

        myMove = moves[1]
        theirMove = moves[0]

        result = self.player2_result(theirMove, myMove)

        theirShape = self.game_key[theirMove]
        myShape = self.game_key[myMove]

        self.assertEqual('Rock', theirShape)
        self.assertEqual('Paper', myShape)
        self.assertEqual('win', result)

    def test_A_Y_is_8(self):
        moves = ['A', 'Y']
        theirMove = moves[0]
        myMove = moves[1]
        result = self.player2_result(theirMove, myMove)
        myScore = self.score(myMove, result)
        self.assertEqual(8, myScore)

    def test_both_draw_same(self):

        moves = ['A', 'X']
        theirMove = moves[0]
        myMove = moves[1]

        result = self.player2_result(theirMove, myMove)

        self.assertEqual('draw', result)

if __name__ == '__main__':
    unittest.main()