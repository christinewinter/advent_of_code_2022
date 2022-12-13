import numpy as np
scores = {
    "rock": 1,
    "paper": 2,
    "scissor": 3,
    "lost": 0,
    "draw": 3,
    "win": 6
}
game_outcome = {
 "X": "lost",
 "Y": "draw",
 "Z": "win"
}

shape = {
    "A": "rock",
    "X": "rock",
    "B": "paper",
    "Y": "paper",
    "C": "scissor",
    "Z": "scissor"
}


def select_winner(shape_1, shape_2):
    """
    Rock defeats Scissors,
    Scissors defeats Paper,
    Paper defeats Rock
    """
    if shape_1 == shape_2:
        return "draw"  # nobody won
    if shape_1 == "rock":
        if shape_2 == "scissor":
            return "player_1"
        if shape_2 == "paper":
            return "player_2"
    if shape_1 == "scissor":
        if shape_2 == "paper":
            return "player_1"
        if shape_2 == "rock":
            return "player_2"
    if shape_1 == "paper":
        if shape_2 == "rock":
            return "player_1"
        if shape_2 == "scissor":
            return "player_2"


def round_score_part1(player_1, player_2):
    shape_player_1 = shape[player_1]
    shape_player_2 = shape[player_2]
    winner = select_winner(shape_player_1, shape_player_2)
    if winner == "draw":
        return [scores["draw"] + scores[shape_player_1], scores["draw"] + scores[shape_player_2]]
    elif winner == "player_1":
        return [scores["win"] + scores[shape_player_1], scores["lost"] + scores[shape_player_2]]
    elif winner == "player_2":
        return [scores["lost"] + scores[shape_player_1], scores["win"] + scores[shape_player_2]]


def select_shape(shape_1, game_end):
    """
    Rock defeats Scissors,
    Scissors defeats Paper,
    Paper defeats Rock
    """
    if shape_1 == "rock":
        if game_end == "X":  # loose game
            return "scissor"
        if game_end == "Y":  # draw
            return "rock"
        if game_end == "Z":  #win
            return "paper"
    if shape_1 == "scissor":
        if game_end == "X":  # loose game
            return "paper"
        if game_end == "Y":  # draw
            return "scissor"
        if game_end == "Z":  # win
            return "rock"
    if shape_1 == "paper":
        if game_end == "X":  # loose game
            return "rock"
        if game_end == "Y":  # draw
            return "paper"
        if game_end == "Z":  # win
            return "scissor"


def round_score_part2(player_1, round_end):
    shape_player_1 = shape[player_1]
    shape_player_2 = select_shape(shape_player_1, round_end)
    round_score = scores[game_outcome[round_end]]

    return [scores[shape_player_1] + round_score, scores[shape_player_2] + round_score]


with open("input_day2.txt", 'r') as file:
    game_score_part1 = np.array([0,0])
    for row in file:
        player_1, player_2 = row.rstrip().split(" ")
        round_score = round_score_part1(player_1, player_2)
        game_score_part1 += round_score

print(game_score_part1)


with open("input_day2.txt", 'r') as file:
    game_score_part2 = np.array([0,0])
    for row in file:
        player_1, round_end = row.rstrip().split(" ")
        round_score = round_score_part2(player_1, round_end)
        game_score_part2 += round_score

print(game_score_part2)



