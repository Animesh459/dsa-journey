def solve():
    n = int(input())
    cards = []
    for _ in range(n):
        cards.append(list(map(int, input().split())))

    # Separate cards into two groups based on the value of b_i
    engine_cards = [card for card in cards if card[1] > 0]
    scorer_cards = [card for card in cards if card[1] == 0]

    # Sort the scorer cards by their point value (a_i) in descending order
    # to be able to pick the most valuable ones later.
    scorer_cards.sort(key=lambda x: x[0], reverse=True)

    # Initialize the total score and the counter for plays.
    # We start with one play.
    total_score = 0
    cards_to_play = 1

    # Play all "engine" cards (b_i > 0). The order doesn't matter
    # for the total number of plays gained.
    for card in engine_cards:
        total_score += card[0]
        cards_to_play += card[1]
        # Each card played uses up one turn
        cards_to_play -= 1

    # After playing all engine cards, we have a certain number of
    # plays remaining. We use these plays on the most valuable
    # "scorer" cards (b_i = 0).
    num_scorers_to_play = min(cards_to_play, len(scorer_cards))

    for i in range(num_scorers_to_play):
        total_score += scorer_cards[i][0]

    print(total_score)


solve()