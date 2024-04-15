package aufgabe2;

/**
 * Hauptprogramm für KalahMuster.
 *
 * @since 29.3.2021
 * @author oliverbittel
 */
public class Kalah {

    private static final String ANSI_BLUE = "\u001B[34m";

    /**
     *
     * @param args wird nicht verwendet.
     */
    public static void main(String[] args) {
        //testExample();
        //testHHGame();
        testMiniMaxAndAlphaBetaWithGivenBoard();
        //testHumanMiniMax();
        //testHumanAlphaBeta();
    }

    /**
     * Beispiel von https://de.wikipedia.org/wiki/Kalaha
     */
    public static void testExample() {
        KalahBoard kalahBd = new KalahBoard(new int[]{5, 3, 2, 1, 2, 0, 0, 4, 3, 0, 1, 2, 2, 0}, 'B');
        kalahBd.print();

        System.out.println("B spielt Mulde 11");
        kalahBd.move(11);
        kalahBd.print();

        System.out.println("B darf nochmals ziehen und spielt Mulde 7");
        kalahBd.move(7);
        kalahBd.print();
    }

    /**
     * Mensch gegen Mensch
     */
    public static void testHHGame() {
        KalahBoard kalahBd = new KalahBoard();
        kalahBd.print();

        while (!kalahBd.isFinished()) {
            int action = kalahBd.readAction();
            kalahBd.move(action);
            kalahBd.print();
        }

        System.out.println("\n" + ANSI_BLUE + "GAME OVER");
    }

    public static void testMiniMaxAndAlphaBetaWithGivenBoard() {
        KalahBoard kalahBd = new KalahBoard(new int[]{2, 0, 4, 3, 2, 0, 0, 1, 0, 1, 3, 2, 1, 0}, 'A');
        // A ist am Zug und kann aufgrund von Bonuszügen 8-aml hintereinander ziehen!
        // A muss deutlich gewinnen!
        kalahBd.print();

        while (!kalahBd.isFinished()) {
            int action;
            if (kalahBd.getCurPlayer() == 'A') {
                // Berechnen Sie für A eine Aktion mit Ihrem Verfahren und geben Sie die Aktion auf der Konsole aus.
                // ...
                System.out.println("-------------------- MINIMAX -------------------");
                //int actionMinimax = kalahBd.getMinimaxChoice(16);
                //System.out.println("Minimax choice: " + actionMinimax);
                System.out.println("-------------------- ALPHA-BETA -------------------");
                int actionAlphaBeta = kalahBd.alphaBetaSearch(20);
                System.out.println("Alpha-Beta choice: " + actionAlphaBeta);
                System.out.println("-------------------- SORTED ALPHA-BETA ---------------------");
                int actionSortedAlphaBeta = kalahBd.sortedAlphaBetaSearch(14);
                System.out.println("Sorted Alpha-Beta choice: " + actionSortedAlphaBeta);
                action = actionSortedAlphaBeta;
            }
            else {
                action = kalahBd.readAction();
            }
            kalahBd.move(action);
            kalahBd.print();
        }

        System.out.println("\n" + ANSI_BLUE + "GAME OVER");
    }

    public static void testHumanMiniMax() {
        KalahBoard kalahBd = new KalahBoard();
        kalahBd.print();

        while (!kalahBd.isFinished()) {
            int action;
            if (kalahBd.getCurPlayer() == 'A') {
                // Berechnen Sie für A eine Aktion mit Ihrem Verfahren und geben Sie die Aktion auf der Konsole aus.
                // ...
                System.out.println("-------------------- MINIMAX -------------------");
                int actionMinimax = kalahBd.getMinimaxChoice(14);
                System.out.println("Minimax choice: " + actionMinimax);
                action = actionMinimax;
            }
            else {
                action = kalahBd.readAction();
            }
            kalahBd.move(action);
            kalahBd.print();
        }

        System.out.println("\n" + ANSI_BLUE + "GAME OVER");
    }

    public static void testHumanAlphaBeta() {
        KalahBoard kalahBd = new KalahBoard();
        kalahBd.print();

        while (!kalahBd.isFinished()) {
            int action;
            if (kalahBd.getCurPlayer() == 'A') {
                // Berechnen Sie für A eine Aktion mit Ihrem Verfahren und geben Sie die Aktion auf der Konsole aus.
                // ...
                System.out.println("-------------------- ALPHA-BETA -------------------");
                int actionAlphaBeta = kalahBd.sortedAlphaBetaSearch(14);
                System.out.println("Alpha-Beta choice: " + actionAlphaBeta);
                action = actionAlphaBeta;
            }
            else {
                action = kalahBd.readAction();
            }
            kalahBd.move(action);
            kalahBd.print();
        }

        System.out.println("\n" + ANSI_BLUE + "GAME OVER");
    }
}
