deck = input().split()
count_of_shuffle = int(input())
left_side = deck[0:len(deck)//2]
right_side= deck[len(deck)//2:len(deck)]

for shuffle in range(count_of_shuffle):
    new_deck = []
    left_side = deck[0:len(deck) // 2]
    right_side = deck[len(deck) // 2:len(deck)]

    for i in range(len(left_side)):
        new_deck.append(left_side[i])
        new_deck.append(right_side[i])

    deck = new_deck.copy()

print(deck)




