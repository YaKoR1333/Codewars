def best_match(goals1, goals2):
    score_team2 = 0
    index_best_match = 0
    goal_difference = 99999999999
    for index, (goal_team1, goal_team2) in enumerate(zip(goals1, goals2)):
        match_difference = goal_team1 - goal_team2
        if match_difference == goal_difference and goal_team2 > score_team2:
            index_best_match = index
            score_team2 = goal_team2
        elif match_difference < goal_difference:
            score_team2 = goal_team2
            goal_difference = match_difference
            index_best_match = index
    return index_best_match
