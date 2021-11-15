import random as rd
import pandas as pd

class coin:

    def __init__(self) -> None:
        self.head = 0
        self.tail = 0
    
    def flip(self, counts = 1) -> None:
        """
        mock flips, by default, it toss coin once.
        """

        for _ in range(counts):
            result = rd.randint(0, 1)
            if result == 0:
                self.head += 1
            else:
                self.tail += 1
    
    def __str__(self) -> str:
        print("The coin is filped with {} times.\nHead: {}, Tail: {}.\n".format(self.head + self.tail, self.head, self.tail))

counts = 20

coins = [coin() for _ in range(2)]
for piece in coins:
    piece.flip(counts)

for piece in coins:
    piece.__str__()


results = []
probability = []
for piece in coins:
    results.append([piece.head, piece.tail])

results = pd.DataFrame(results, index=['Coin 1', 'Coin 2'], columns=['Head', 'Tail'])
joint_probability = results / 40
print(joint_probability)

print('P(Head)={:.3f}'.format(joint_probability['Head'].sum()))
print('P(Tail)={:.3f}'.format(joint_probability['Tail'].sum()))