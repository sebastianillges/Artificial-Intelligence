package aufgabe1;

import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;

/**
 *
 * @author Ihr Name
 */
public class A_Star {
    // cost ordnet jedem Board die Aktuellen Pfadkosten (g-Wert) zu.
    // pred ordnet jedem Board den Elternknoten zu. (siehe Skript S. 2-25).
    // In cost und pred sind genau alle Knoten der closedList und openList enthalten!
    // Nachdem der Zielknoten erreicht wurde, lässt sich aus cost und pred der Ergebnispfad ermitteln.
    private static HashMap<Board,Integer> cost = new HashMap<>();
    private static HashMap<Board,Board> pred = new HashMap<>();

    // openList als Prioritätsliste.
    // Die Prioritätswerte sind die geschätzen Kosten f = g + h (s. Skript S. 2-66)
    private static IndexMinPQ<Board, Integer> openList = new IndexMinPQ<>();

    public static Deque<Board> aStar(Board startBoard) {
        if (startBoard.isSolved())
            return new LinkedList<>();

        cost.put(startBoard, 0);
        openList.add(startBoard, startBoard.h2());

        int counter = 0;

        while (!openList.isEmpty()) {
            Board node = openList.removeMin();
            if (node.isSolved()) {
                System.out.println("A* Zustände: " + counter);
                return dequeFromPred(node);
            }
            for (Board action : node.possibleActions()) {
                counter++;
                int actionCost = cost.get(node) + 1;
                if(!cost.containsKey(action)) {
                    pred.put(action, node);
                    cost.put(action, actionCost);
                    openList.add(action, actionCost + action.h2());
                } else if (actionCost < cost.get(action)) {
                    pred.put(action, node);
                    cost.put(action, actionCost);
                    openList.change(action, actionCost + action.h2());
                }
            }
        }

        System.out.println("A* Zustände: " + counter);
        return null; // Keine Lösung
    }

    private static Deque<Board> dequeFromPred(Board finish) {
        Board predecessor = finish;
        Deque<Board> path = new LinkedList<>();
        while (pred.containsKey(predecessor)) {
            path.addFirst(predecessor);
            predecessor = pred.get(predecessor);
        }
        return path;
    }
}

