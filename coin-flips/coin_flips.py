import random as rd
import pandas as pd

class coin:

    def __init__(self) -> None:
        self.head = 0
        self.tail = 0
    
    def flip(self, counts = 1) -> None:
        """
        mock flips, by default, it tosses coin once.
        """

        for _ in range(counts):
            result = rd.randint(0, 1)
            if result == 0:
                self.head += 1
            else:
                self.tail += 1
    
    def __str__(self) -> str:
        print("The coin is filped with {} times.\nHead: {}, Tail: {}.\n".format(self.head + self.tail, self.head, self.tail))

flip_counts = 20
coin_counts = 2
threshold = 3.84

coins = [coin() for _ in range(coin_counts)]
for piece in coins:
    piece.flip(flip_counts)

for piece in coins:
    piece.__str__()


results = []
probability = []
for piece in coins:
    results.append([piece.head, piece.tail])

results = pd.DataFrame(results, index=['Coin 1', 'Coin 2'], columns=['Head', 'Tail'])
joint_probability = results / (flip_counts * coin_counts)
print(joint_probability)

print('\nThe marginal probability: ')
print('P(Head)={:.3f}'.format(joint_probability['Head'].sum()))
print('P(Tail)={:.3f}'.format(joint_probability['Tail'].sum()))
print('P(Coin 1)={:.3f}'.format(joint_probability.iloc[0, :].sum()))
print('P(Coin 2)={:.3f}'.format(joint_probability.iloc[1, :].sum()))

chi_square_freedom = 0
for i in range(coin_counts):
    expectation_head = (flip_counts * coin_counts) * joint_probability['Head'].sum() * joint_probability.iloc[i, :].sum()
    expectation_tail = (flip_counts * coin_counts) * joint_probability['Head'].sum() * joint_probability.iloc[i, :].sum()
    chi_square_freedom += ((results.iloc[i, 0] - expectation_head) ** 2 / expectation_head + (results.iloc[i, 1] - expectation_tail) ** 2 / expectation_tail)

if chi_square_freedom < threshold:
    print('The chi-square freedom is: {:.3f}, which is smaller than the threshold {}.'.format(chi_square_freedom, threshold))
    print('Independent')
else:
    print('The chi-square freedom is: {:.3f}, which is bigger than the threshold {}.'.format(chi_square_freedom, threshold))
    print('Not independent')