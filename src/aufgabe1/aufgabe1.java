package aufgabe1;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class aufgabe1 {

    public static void main(String[] args) {
        Integer[] array = {7, 2, 4, 5, null, 6, 8, 3, 1};
        // Integer[] array = {1, 4, 2, null, 6, 7, 8, 3, 5};
        List<Integer> list = new LinkedList<>(Arrays.asList(array));
        System.out.println(check_parity(list));
        System.out.println(h1(list));
        System.out.println(h2(list));
    }

    public static int check_parity(List<Integer> list) {
        int counter = 0;
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) == null) {
                continue;
            }
            for (Integer following : list.subList(i + 1, list.size())) {
                if (following == null) {
                    continue;
                }
                if (list.get(i) > following) {
                    System.out.println(list.get(i) + ", " + following);
                    counter++;
                }
            }
        }
        return counter;
    }

    public static int h1(List<Integer> list) {
        int counter = 0;
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) != null && list.get(i) != i) {
                counter++;
            }
        }
        return counter;
    }

    public static int h2(List<Integer> list) {
        int counter = 0;
        for (int i = 0; i < list.size(); i++) {
            Integer val = list.get(i);
            if (val == null) {
                continue;
            }

            int goalX = val % 3;
            int goalY = val / 3;
            int x = i % 3;
            int y = i / 3;

            int manh_dist = Math.abs(goalX - x) + Math.abs(goalY - y);
            counter += manh_dist;
        }
        return counter;
    }

}
