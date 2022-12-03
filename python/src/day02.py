#!/usr/bin/env python

player1 = {"A": "Rock", "B": "Paper", "C": "Scissors"}
player2 = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

results = {"X": "loss", "Y": "draw", "Z": "win"}

play_scores = {"Rock": 1, "Paper": 2, "Scissors": 3}
round_scores = {"loss": 0, "draw": 3, "win": 6}

winners = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
to_win = {v: k for k, v in winners.items()}


def part1(data):
    score = 0
    for line in data.splitlines():
        p1, p2 = line.split()

        score += play_scores[player2[p2]]
        if winners[player2[p2]] == player1[p1]:
            score += 6
        elif player1[p1] == player2[p2]:
            score += 3
    return score


def part2(data):
    score = 0
    for line in data.splitlines():
        p1, result = line.split()

        if "win" == results[result]:
            score += 6
            score += play_scores[to_win[player1[p1]]]
        elif "draw" == results[result]:
            score += 3
            score += play_scores[player1[p1]]
        elif "loss" == results[result]:
            score += play_scores[winners[player1[p1]]]
    return score
