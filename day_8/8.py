tree_map = []
with open('input', 'r') as file:
    for line in file.readlines():
        tree_map.append(list(map(lambda x: int(x), list(line.strip()))))

def is_visible_tree(tree_map, i, j):

    # dir: 0 - left, 1 - top, 2 - right, 3 - bot
    def visible_from_edge_aux(tree_map, i, j, start_tree, dir):
        if dir == 0:
            if j == 1:
                return start_tree > tree_map[i][0]
            else:
                if start_tree > tree_map[i][j-1]:
                    return visible_from_edge_aux(tree_map, i, j-1, start_tree, 0)
                else:
                    return False

        elif dir == 1:
            if i == 1:
                return start_tree > tree_map[0][j]
            else:
                if start_tree > tree_map[i-1][j]:
                    return visible_from_edge_aux(tree_map, i-1, j, start_tree, 1)
                else:
                    return False

        elif dir == 2:
            if j == len(tree_map[0])-2:
                return start_tree > tree_map[i][len(tree_map[0])-1]
            else:
                if start_tree > tree_map[i][j+1]:
                    return visible_from_edge_aux(tree_map, i, j+1, start_tree, 2)
                else:
                    return False
        
        elif dir == 3:
            if i == len(tree_map)-2:
                return start_tree > tree_map[len(tree_map)-1][j]
            else:
                if start_tree > tree_map[i+1][j]:
                    return visible_from_edge_aux(tree_map, i+1, j, start_tree, 3)
                else:
                    return False
        
    for dir in range(4):
        if visible_from_edge_aux(tree_map, i, j, tree_map[i][j], dir):
            return True

    return False

def scenic_score(tree_map, i, j):

    # dir: 0 - left, 1 - top, 2 - right, 3 - bot
    def scenic_score_aux(tree_map, i, j, start_tree, dir, score):
        if dir == 0:
            if j == 1:
                return score + 1
            else:
                if start_tree > tree_map[i][j-1]:
                    return scenic_score_aux(tree_map, i, j-1, start_tree, 0, score+1)
                else:
                    return score+1

        elif dir == 1:
            if i == 1:
                return score + 1
            else:
                if start_tree > tree_map[i-1][j]:
                    return scenic_score_aux(tree_map, i-1, j, start_tree, 1, score+1)
                else:
                    return score+1

        elif dir == 2:
            if j == len(tree_map[0])-2:
                return score + 1
            else:
                if start_tree > tree_map[i][j+1]:
                    return scenic_score_aux(tree_map, i, j+1, start_tree, 2, score+1)
                else:
                    return score+1
        
        elif dir == 3:
            if i == len(tree_map)-2:
                return score + 1
            else:
                if start_tree > tree_map[i+1][j]:
                    return scenic_score_aux(tree_map, i+1, j, start_tree, 3, score+1)
                else:
                    return score+1
    current_scenic_score = 1

    for dir in range(4):
        current_scenic_score *= scenic_score_aux(tree_map, i, j, tree_map[i][j], dir, 0)

    return current_scenic_score

highest_scenic_score = 0
for i in range(1, len(tree_map)-1):
    for j in range(1, len(tree_map[0])-1):
        if is_visible_tree(tree_map, i, j):
            highest_scenic_score = max(highest_scenic_score, scenic_score(tree_map, i, j))

print(highest_scenic_score)

#print(highest_scenic_score)
''' part 1
visible_trees = (2*len(tree_map)) + (2*len(tree_map[0])) - 4
for i in range(1, len(tree_map)-1):
    for j in range(1, len(tree_map[0])-1):
        visible_trees += 1 if is_visible_tree(tree_map, i, j) else 0
'''