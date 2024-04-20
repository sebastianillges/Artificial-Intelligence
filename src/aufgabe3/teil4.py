from constraint import Problem

rechtecke = {"1": (6, 4), "2": (5, 2), "3": (2, 2), "4": (3, 2), "5": (1, 8), "6": (1, 4)}

def no_overlap(x1, y1, w1, h1, x2, y2, w2, h2):
    """ Überprüft, ob sich zwei Rechtecke nicht überschneiden. """
    return x1 + w1 <= x2 or x2 + w2 <= x1 or y1 + h1 <= y2 or y2 + h2 <= y1


def solve():
    problem = Problem()

    positionen = {}
    for rechteck, (width, height) in rechtecke.items():
        pos_list = []

        # Für horizontale Platzierung
        for x in range(7 - width + 1):
            for y in range(8 - height + 1):
                pos_list.append((x, y, width, height))

        # Für vertikale Platzierung (gedreht)
        for x in range(7 - height + 1):
            for y in range(8 - width + 1):
                pos_list.append((x, y, height, width))

        positionen[rechteck] = pos_list
        problem.addVariable(rechteck, pos_list)


    # for i in positionen.keys():
    #     for j in positionen.keys():
    #         if i != j:
    #             problem.addConstraint(lambda r1, r2: no_overlap(r1[0], r1[1], r1[2], r1[3], r2[0], r2[1], r2[2], r2[3]),
    #                                   (positionen[i], positionen[j]))

    # Constraints hinzufügen, dass sich keine Rechtecke überschneiden
    keys = list(positionen.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            problem.addConstraint(
                lambda pos1, pos2: no_overlap(pos1[0], pos1[1], pos1[2], pos1[3], pos2[0], pos2[1], pos2[2], pos2[3]),
                (keys[i], keys[j])
            )

    # Get the solutions.
    solutions = problem.getSolutions()

    return solutions


def main():
    solutions = solve()

    print("Number of solutions:", len(solutions))

    grid = [[0 for _ in range(7)] for _ in range(8)]
    for solution in solutions:
        for rechteck, (x, y, w, h) in solution.items():
            for i in range(x, x + w):
                for j in range(y, y + h):
                    grid[j][i] = rechteck
        print("Solution:")
        for row in grid:
            print(row)





if __name__ == "__main__":
    main()
