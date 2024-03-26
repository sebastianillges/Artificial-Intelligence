package aufgabe1;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class parity {

    public static void main(String[] args) {
        // Integer[] array = {7, 2, 4, 5, 6, 8, 3, 1};
        Integer[] array = {1, 4, 2, 6, 7, 8, 3, 5};
        List<Integer> list = new LinkedList<>(Arrays.asList(array));
        System.out.println(check_parity(list));
    }

    public static int check_parity(List<Integer> list) {
        int counter=0;
        for (int i=0; i<list.size(); i++) {
            for (Integer following : list.subList(i+1, list.size())) {
                if (list.get(i) > following) {
                    System.out.println(list.get(i) + ", " + following);
                    counter++;
                }
            }
        }
        return counter;
    }

}
