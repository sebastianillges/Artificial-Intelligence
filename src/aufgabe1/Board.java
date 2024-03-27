package aufgabe1;

import aufgabe1.IDFS;

import java.lang.reflect.Array;
import java.util.Deque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.LinkedList;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Klasse Board für 8-Puzzle-Problem
 *
 * @author Ihr Name
 */
public class Board {

    /**
     * Problmegröße
     */
    public static final int N = 8;
    protected static final int dim = (int) Math.floor(Math.sqrt(N + 1));
    /**
     * Board als Feld.
     * Gefüllt mit einer Permutation von 0,1,2, ..., 8.
     * 0 bedeutet leeres Feld.
     */
    protected int[] board = new int[N + 1];

    public static final int[] GOAL_ARR = IntStream.range(0, N + 1).toArray();
    //protected static int[] goal = {0, 1, 2, 3, 4, 5, 6, 7, 8};

    /**
     * Generiert ein zufälliges Board.
     */
    public Board() {
        List<Integer> list = new ArrayList<>(Arrays.stream(GOAL_ARR).boxed().toList());
        java.util.Collections.shuffle(list);
        this.board = list.stream().mapToInt(i -> i).toArray();
        while (!parity()) {
            java.util.Collections.shuffle(list);
            this.board = list.stream().mapToInt(i -> i).toArray();
        }
    }

    /**
     * Generiert ein Board und initialisiert es mit board.
     *
     * @param board Feld gefüllt mit einer Permutation von 0,1,2, ..., 8.
     */
    public Board(int[] board) {
        this.board = board;
    }

    @Override
    public String toString() {
        StringBuilder bld = new StringBuilder();
        bld.append("(");
        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                bld.append(board[i * dim + j]).append(",");
            }
            bld.append('\n');
        }
        bld.append(")");
        return bld.toString();
    }


    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Board other = (Board) obj;
        return Arrays.equals(this.board, other.board);
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 67 * hash + Arrays.hashCode(this.board);
        return hash;
    }

    /**
     * Paritätsprüfung.
     *
     * @return Parität.
     */
    public boolean parity() {
        int counter = 0;
        for (int i = 0; i < board.length; i++) {
            if (board[i] == 0) {
                continue;
            }
            for (int f = i + 1; f < board.length; f++) {
                int following = board[f];
                if (following == 0) {
                    continue;
                }
                if (board[i] > following) {
                    counter++;
                }
            }
        }
        return counter % 2 == 0;
    }

    /**
     * Heurstik h1. (siehe Aufgabenstellung)
     *
     * @return Heuristikwert.
     */
    public int h1() {
        int counter = 0;
        for (int i = 0; i < board.length; i++) {
            if (board[i] != 0 && board[i] != i) {
                counter++;
            }
        }
        return counter;
    }

    /**
     * Heurstik h2. (siehe Aufgabenstellung)
     *
     * @return Heuristikwert.
     */
    public int h2() {
        int counter = 0;
        for (int i = 0; i < board.length; i++) {
            int val = board[i];
            if (val == 0) {
                continue;
            }

            int goalX = val % dim;
            int goalY = val / dim;
            int x = i % dim;
            int y = i / dim;

            int manh_dist = Math.abs(goalX - x) + Math.abs(goalY - y);
            counter += manh_dist;
        }
        return counter;
    }

    /**
     * Liefert eine Liste der möglichen Aktion als Liste von Folge-Boards zurück.
     *
     * @return Folge-Boards.
     */
    public List<Board> possibleActions() {
        List<Board> boardList = new LinkedList<>();
        // ...
        int index_null = 0;
        for (int i = 0; i < board.length; i++) {
            if (board[i] == 0) {
                index_null = i;
                break;
            }
        }
        int x_null = index_null % dim;
        int y_null = index_null / dim;

        if (x_null + 1 < dim) {
            Board new_board = new Board(board.clone());
            new_board.board[index_null] = new_board.board[index_null + 1];
            new_board.board[index_null + 1] = 0;
            boardList.add(new_board);
        }
        if (x_null - 1 >= 0) {
            Board new_board = new Board(board.clone());
            new_board.board[index_null] = new_board.board[index_null - 1];
            new_board.board[index_null - 1] = 0;
            boardList.add(new_board);
        }
        if (y_null + 1 < dim) {
            Board new_board = new Board(board.clone());
            new_board.board[index_null] = new_board.board[index_null + dim];
            new_board.board[index_null + dim] = 0;
            boardList.add(new_board);
        }
        if (y_null - 1 >= 0) {
            Board new_board = new Board(board.clone());
            new_board.board[index_null] = new_board.board[index_null - dim];
            new_board.board[index_null - dim] = 0;
            boardList.add(new_board);
        }
        return boardList;
    }


    /**
     * Prüft, ob das Board ein Zielzustand ist.
     *
     * @return true, falls Board Ziestzustand (d.h. 0,1,2,3,4,5,6,7,8)
     */
    public boolean isSolved() {
        return Arrays.equals(board, GOAL_ARR);
    }


    public static void main(String[] args) {
        Board b = new Board(new int[]{7, 2, 4, 5, 0, 6, 8, 3, 1});        // abc aus Aufgabenblatt
        Board goal = new Board(new int[]{0, 1, 2, 3, 4, 5, 6, 7, 8});

        Board rand = new Board();

        System.out.println(rand);
//        System.out.println(b);
//        System.out.println(b.parity());
//        System.out.println(b.h1());
//        System.out.println(b.h2());
//
//        System.out.println(b);
//
//        for (Board child : b.possibleActions())
//            System.out.println(child);
//
//        System.out.println(goal.isSolved());

        Deque<Board> solve_IDFS = IDFS.idfs(b);
        System.out.println(solve_IDFS.size());
        System.out.println(solve_IDFS);
        Deque<Board> solve_A_Star = A_Star.aStar(b);
        System.out.println(solve_A_Star.size());
//        System.out.println(solve_A_Star);

    }
}

