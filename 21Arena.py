"""
BlackJackSim
------------
A simplified Blackjack simulation built in Python using stack and queue data structures.
This program mimics a casino-style multi-deck Blackjack game with multiple players,
automatic reshuffling, and simulation statistics.
"""

import random

# Represents a playing card with a suit and rank.
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # Ace defaults to 11
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"


# Queue implementation (used for the dealer’s shoe)
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Stack implementation (used for the deck)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Core Blackjack Game Logic
class BlackjackGame:
    def __init__(self, num_players, num_decks):
        self.num_players = num_players
        self.num_decks = num_decks
        self.deck = Stack()
        self.shoe = Queue()
        self.marker_card = "MARKER"
        self.player_scores = [0] * num_players
        self.player_losses = [0] * num_players
        self.player_pushes = [0] * num_players
        self.player_hands_played = [0] * num_players
        self.games_played = 0
        self.initialize_deck()

    def initialize_deck(self):
        self.deck = Stack()
        self.shoe = Queue()
        suits = ['♥', '♦', '♣', '♠']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        for _ in range(self.num_decks):
            for suit in suits:
                for rank in ranks:
                    self.deck.push(Card(suit, rank))

        self.shuffle_deck()
        self.insert_marker_card()
        self.fill_shoe_from_deck()

    def shuffle_deck(self):
        cards = []
        while not self.deck.is_empty():
            cards.append(self.deck.pop())

        # Fisher-Yates shuffle
        for i in range(len(cards) - 1, 0, -1):
            j = random.randint(0, i)
            cards[i], cards[j] = cards[j], cards[i]

        for card in cards:
            self.deck.push(card)

    def insert_marker_card(self):
        deck_size = self.deck.size()
        min_pos = int(deck_size * 0.4)
        max_pos = int(deck_size * 0.9)
        marker_pos = random.randint(min_pos, max_pos)

        temp_stack = Stack()
        for _ in range(deck_size - marker_pos):
            temp_stack.push(self.deck.pop())

        self.deck.push(self.marker_card)

        while not temp_stack.is_empty():
            self.deck.push(temp_stack.pop())

    def fill_shoe_from_deck(self):
        while not self.deck.is_empty():
            card = self.deck.pop()
            self.shoe.enqueue(card)

    def deal_card(self):
        return self.shoe.dequeue()

    def get_hand_total(self, hand):
        total, aces = 0, 0

        for card in hand:
            if card == self.marker_card:
                continue
            if isinstance(card, Card):
                if card.rank == 'A':
                    aces += 1
                    total += 11
                else:
                    total += card.get_value()

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total

    def play_hand(self):
        player_hands = [[] for _ in range(self.num_players)]
        dealer_hand = []
        marker_hit = False

        # Deal initial cards
        for i in range(self.num_players):
            for _ in range(2):
                card = self.deal_card()
                if card == self.marker_card:
                    marker_hit = True
                    card = self.deal_card()
                player_hands[i].append(card)

        for _ in range(2):
            card = self.deal_card()
            if card == self.marker_card:
                marker_hit = True
                card = self.deal_card()
            dealer_hand.append(card)

        player_values = [self.get_hand_total(hand) for hand in player_hands]
        dealer_value = self.get_hand_total(dealer_hand)

        # Determine winners
        for i in range(self.num_players):
            self.player_hands_played[i] += 1
            player_value = player_values[i]

            if player_value > 21:
                self.player_losses[i] += 1
                result = "LOSS (Bust)"
            elif dealer_value > 21:
                self.player_scores[i] += 1
                result = "WIN (Dealer Bust)"
            elif player_value == 21:
                if dealer_value == 21:
                    self.player_pushes[i] += 1
                    result = "PUSH (Both have 21)"
                else:
                    self.player_scores[i] += 1
                    result = "WIN (Blackjack)"
            elif player_value > dealer_value:
                self.player_scores[i] += 1
                result = "WIN"
            elif player_value < dealer_value:
                self.player_losses[i] += 1
                result = "LOSS"
            else:
                self.player_pushes[i] += 1
                result = "PUSH"

            player_hand_str = ' '.join(str(card) for card in player_hands[i] if card != self.marker_card)
            dealer_hand_str = ' '.join(str(card) for card in dealer_hand if card != self.marker_card)
            print(
                f"Player {i + 1} had {player_hand_str} = {player_value} | Dealer had {dealer_hand_str} = {dealer_value} → {result}")

        self.games_played += 1
        return marker_hit

    def display_statistics(self):
        print("\n--- GAME STATISTICS ---")
        print(f"Total hands played: {self.games_played}")

        for i in range(self.num_players):
            wins = self.player_scores[i]
            losses = self.player_losses[i]
            pushes = self.player_pushes[i]
            total = self.player_hands_played[i]

            if total > 0:
                win_percentage = (wins / total) * 100
                loss_percentage = (losses / total) * 100
                push_percentage = (pushes / total) * 100
            else:
                win_percentage = loss_percentage = push_percentage = 0.0

            print(f"🎲 Player {i + 1}: ✅ {wins} ({win_percentage:.2f}%) | ❌ {losses} ({loss_percentage:.2f}%) |"
                  f" 🤝 {pushes} ({push_percentage:.2f}%)")

    def run_simulation(self, num_hands):
        print(f"\n--- Running simulation for {num_hands} hands ---\n")

        self.player_scores = [0] * self.num_players
        self.player_losses = [0] * self.num_players
        self.player_pushes = [0] * self.num_players
        self.player_hands_played = [0] * self.num_players
        self.games_played = 0
        self.initialize_deck()

        hands_played = 0
        while hands_played < num_hands:
            if self.shoe.size() < (self.num_players + 1) * 2:
                print("Not enough cards in the shoe. Reshuffling...")
                self.initialize_deck()

            if num_hands > 100 and hands_played % (num_hands // 10) == 0:
                print(f"Progress: {hands_played}/{num_hands} hands")

            marker_hit = self.play_hand()
            hands_played += 1

            if marker_hit:
                print("Marker card appeared — reshuffling deck.")
                self.initialize_deck()

        print(f"\n--- Simulation of {num_hands} hands completed ---")
        self.display_statistics()


def main():
    print("\n===== BLACKJACK SIMULATOR =====\n")

    try:
        num_players = int(input("Enter number of players (1–7): "))
        if num_players < 1 or num_players > 7:
            print("Invalid number of players. Defaulting to 1.")
            num_players = 1

        num_decks = int(input("Enter number of decks (1–8): "))
        if num_decks < 1 or num_decks > 8:
            print("Invalid number of decks. Defaulting to 1.")
            num_decks = 1
    except ValueError:
        print("Invalid input. Using default: 1 player, 1 deck.")
        num_players = num_decks = 1

    game = BlackjackGame(num_players, num_decks)

    while True:
        print("\n----- MENU -----")
        print("1. Play a single hand")
        print("2. Simulate 100 hands")
        print("3. Simulate 500 hands")
        print("4. Simulate 1000 hands")
        print("5. Simulate 10000 hands")
        print("6. Custom number of hands")
        print("7. Exit")

        try:
            choice = int(input("Choose an option (1–7): "))
            if choice == 1:
                marker_hit = game.play_hand()
                game.display_statistics()
                if marker_hit:
                    print("Marker appeared — reshuffling deck.")
                    game.initialize_deck()
            elif choice == 2:
                game.run_simulation(100)
            elif choice == 3:
                game.run_simulation(500)
            elif choice == 4:
                game.run_simulation(1000)
            elif choice == 5:
                game.run_simulation(10000)
            elif choice == 6:
                try:
                    num_hands = int(input("Enter number of hands: "))
                    if num_hands < 1:
                        print("Invalid number. Running 100 hands.")
                        num_hands = 100
                    game.run_simulation(num_hands)
                except ValueError:
                    print("Invalid input. Running 100 hands.")
                    game.run_simulation(100)
            elif choice == 7:
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()