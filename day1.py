import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        filename = "./data/day1.txt"


        elfCalories = []

        with open(filename) as f:
            elf = []
            for line in f:
                strippedLine = line.strip()
                if strippedLine:
                    elf.append(int(strippedLine))
                else:
                    elfsTotalCalories = 0
                    for i in elf:
                        elfsTotalCalories += i
                    elfCalories.append(elfsTotalCalories)
                    elf=[]

        self.assertEqual(258, len(elfCalories))
        self.assertEqual(44427, elfCalories[0])
        self.assertEqual(33711 + 6672, elfCalories[1])
        elfCalories.sort(reverse=True)
        self.assertEqual(71124, elfCalories[0])
        top3 = elfCalories[0] + elfCalories[1] + elfCalories[2]
        self.assertEqual(204639, top3)

if __name__ == '__main__':
    unittest.main()