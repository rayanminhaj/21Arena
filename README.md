<p align="center">
  <img src="https://github.com/rayanminhaj/21Arena/blob/main/21_preview.png" alt="Mathly Preview" width="800"/>
</p>

# 21Arena

21Arena is a Python-based Blackjack simulator that demonstrates the use of stack and queue data structures in game design.  
It replicates a casino-style Blackjack environment, complete with reshuffling, multiple decks, and statistical tracking.

---

## About the Project

21Arena is a simplified simulation of Blackjack (21) designed to highlight how stack (LIFO) and queue (FIFO) structures operate in practical applications.  
The simulation runs automatically, handling card dealing, score evaluation, and result tracking without human input.

This project demonstrates:
- Object-oriented programming in Python
- Data structure implementation (Stack and Queue)
- Fisher–Yates shuffle algorithm
- Statistical analysis of simulation results

---

## Features

- Multi-player support (1–7 players)
- Multiple deck support (1–8 decks)
- Marker card for automatic reshuffling
- Win, loss, and push percentage statistics
- Supports single-hand and multi-hand simulations

---

## Game Flow

1. Cards are pushed onto a stack and shuffled.
2. The shuffled deck is enqueued into the dealer’s shoe.
3. Players and the dealer are dealt two cards each.
4. Hand totals are calculated using Blackjack rules (Ace = 1 or 11).
5. The system automatically determines the outcome for each hand.
6. When the marker card appears, the deck is reshuffled.

---

## Class Overview

| Class | Description |
|--------|-------------|
| `Card` | Represents a single playing card with suit and rank. |
| `Stack` | Models the deck (LIFO structure). |
| `Queue` | Models the dealer’s shoe (FIFO structure). |
| `BlackjackGame` | Handles simulation, dealing, reshuffling, and statistics. |

---

## Screenshots

| Section | Image |
|----------|--------|
| Single Hand Simulation | ![SingleHand](https://github.com/rfm5898/21Arena/blob/main/21Arena_SingleHand.png) |
| Marker Card Insertion | ![MarkerInsertion](https://github.com/rfm5898/21Arena/blob/main/21Arena_MarkerInsertion.png) |
| Extended Simulation Results | ![FurtherSim](https://github.com/rfm5898/21Arena/blob/main/21Arena_FurtherSim.png) |

---

## How to Run

### Step 1 — Clone the Repository
```bash
git clone https://github.com/rfm5898/21Arena.git
```
---

### Step 2 — Navigate to the Project Folder

```bash
cd 21Arena
```
---

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

If you face errors, try:
```bash
python -m pip install -r requirements.txt
```

---

### Step 4 — Run the Application

```bash
python 21Arena.py
```
---

## Folder Structure

```
21Arena/
│
├── 21Arena.py
├── 21Arena (Report).docx
├── 21Arena_SingleHand.png
├── 21Arena_MarkerInsertion.png
├── 21Arena_FurtherSim.png
├── requirements.txt

```

---

## Technologies Used

- **Python 3.12**
- **Object-Oriented Programming**
- **Stacks and Queues**
- **Fisher–Yates Shuffle Algorithm**
- **Randomization and Probability**

---

## WHAT YOU CAN DO:

You can choose to:
- Play a single hand
- Simulate 100, 500, 1000, or 10000 hands
- Enter a custom number of hands
- The program automatically displays win/loss/push statistics after each session.  

---

## About the Developer

Developed by **Rayan Minhaj**  
Computer Science Major @The Pennsylvania State University  
Connect with ME: [LinkedIn](https://www.linkedin.com/in/rayan-minhaj-%F0%9F%A4%96-a8492134b/) | [GitHub](https://github.com/rfm5898)
