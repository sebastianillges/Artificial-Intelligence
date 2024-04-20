from constraint import Problem, AllDifferentConstraint

def solve():
    problem = Problem()
    for i in range(1, 5):
        problem.addVariable("raum%d" % i, [i])
        problem.addVariable("fach%d" % i, ["D", "M", "P", "E"])
        problem.addVariable("lehrer%d" % i, ["Ma", "Mu", "Hu", "Sc"])

    problem.addConstraint(
        AllDifferentConstraint(), ["raum%d" % i for i in range(1, 5)]
    )
    problem.addConstraint(
        AllDifferentConstraint(), ["fach%d" % i for i in range(1, 5)]
    )
    problem.addConstraint(
        AllDifferentConstraint(), ["lehrer%d" % i for i in range(1, 5)]
    )

    for i in range(1, 5):
        # Hint 1
        problem.addConstraint(
            lambda lehrer, raum: raum != 4 or lehrer != "Ma",
            ("lehrer%d" % i, "raum%d" % i),
        )

        # Hint 2
        problem.addConstraint(
            lambda fach, lehrer: lehrer != "Mu" or fach == "D",
            ("fach%d" % i, "lehrer%d" % i),
        )

        # Hint 3:
        # Herr Schmid und Herr Müller prüfen nicht in benachbarten Räumen:
        # lehrer1 == "Sc" and lehrer2 == "Mu" => abs(raum1 - raum2) > 1
        # 
        # not(lehrer1 == "Sc" and lehrer2 == "Mu") or abs(raum1 - raum2) > 1
        for j in range (1, 5):
            if i != j:
                problem.addConstraint(
                    lambda lehrer1, lehrer2, raum1, raum2: not(lehrer1 == "Sc" and lehrer2 == "Mu") or (abs(raum1 - raum2) > 1),
                    ("lehrer%d" % i, "lehrer%d" % j, "raum%d" % i, "raum%d" % j),
                )

        # Hint 4:
        # Frau Huber prüft Mathematik
        problem.addConstraint(
            lambda fach, lehrer: lehrer != "Hu" or fach == "M",
            ("fach%d" % i, "lehrer%d" % i),
        )

        # Hint 5:
        # Physik wird immer in Raum 4 geprüft
        problem.addConstraint(
            lambda fach, raum: fach != "P" or raum == 4,
            ("fach%d" % i, "raum%d" % i),
        )

        # Hint 6:
        # Deutsch und Englisch werden nicht in Raum 1 geprüft
        problem.addConstraint(
            lambda fach, raum: not(fach == "D" or fach == "E") or raum != 1,
                ("fach%d" % i, "raum%d" % i),
            )

    # Get the solutions.
    solutions = problem.getSolutions()

    return solutions


def main():
    solutions = solve()
    # Print the solutions
    for solution in solutions:
        for i in range(1, 5):
            print("Raum %d: %d" % (i, solution["raum%d" % i]))
            print("Fach %d: %s" % (i, solution["fach%d" % i]))
            print("Lehrer %d: %s" % (i, solution["lehrer%d" % i]))
            print("")
        print("====================================")

if __name__ == "__main__":
    main()
