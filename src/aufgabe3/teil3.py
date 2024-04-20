from constraint import Problem
import geopandas as geo
import matplotlib.pyplot as plt


def solve(colors):
    problem = Problem()

    bundeslaender = {"Baden-Württemberg": ["Rheinland-Pfalz", "Hessen", "Bayern"],
                     "Bayern": ["Baden-Württemberg", "Hessen", "Thüringen", "Sachsen"],
                     "Berlin": ["Brandenburg"],
                     "Brandenburg": ["Berlin", "Mecklenburg-Vorpommern", "Sachsen-Anhalt"],
                     "Bremen": ["Niedersachsen"],
                     "Hamburg": ["Niedersachsen", "Schleswig-Holstein"],
                     "Hessen": ["Nordrhein-Westfalen", "Rheinland-Pfalz", "Baden-Württemberg", "Bayern"],
                     "Mecklenburg-Vorpommern": ["Schleswig-Holstein", "Niedersachsen", "Brandenburg"],
                     "Niedersachsen": ["Schleswig-Holstein", "Mecklenburg-Vorpommern", "Brandenburg", "Sachsen-Anhalt",
                                       "Thüringen", "Hessen", "Nordrhein-Westfalen", "Bremen"],
                     "Nordrhein-Westfalen": ["Niedersachsen", "Hessen", "Rheinland-Pfalz"],
                     "Rheinland-Pfalz": ["Nordrhein-Westfalen", "Hessen", "Baden-Württemberg", "Saarland"],
                     "Saarland": ["Rheinland-Pfalz"],
                     "Sachsen": ["Brandenburg", "Thüringen", "Bayern", "Sachsen-Anhalt"],
                     "Sachsen-Anhalt": ["Brandenburg", "Niedersachsen", "Thüringen", "Sachsen"],
                     "Schleswig-Holstein": ["Mecklenburg-Vorpommern", "Niedersachsen", "Hamburg"],
                     "Thüringen": ["Sachsen", "Sachsen-Anhalt", "Niedersachsen", "Hessen", "Bayern"]
                     }

    problem.addVariables(bundeslaender.keys(), colors)

    for bundesland in bundeslaender:
        for nachbar in bundeslaender[bundesland]:
            # print(f"{bundesland}: {nachbar}")
            problem.addConstraint(
                lambda state, neighbour: state != neighbour, (bundesland, nachbar))

    # Get the solutions.
    solutions = problem.getSolutions()

    # Plot solution
    print(f"Number of solutions: {len(solutions)}")
    if solutions:
        print(solutions[0])  # Print the first solution as an example
        map = geo.read_file("data/DEU_adm3.shp")  # Load the correct administrative level shapefile

        # Ensure names match and assign colors
        map['color'] = map['NAME_1'].map(solutions[0])  # Adjust 'NAME_1' according to your shapefile

        # Plot
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))
        map.plot(color=map['color'], ax=ax, legend=True)
        plt.show()

    return solutions


def main():
    solve(["#000000", "#444444", "#888888"])
    solve(["#000000", "#444444", "#888888", "#bbbbbb"])


if __name__ == "__main__":
    main()
