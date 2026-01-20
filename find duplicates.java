//Approach: Using HashSet
import java.util.*;

public class DuplicateFinder {
    public static List<Integer> findDuplicates(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        Set<Integer> duplicates = new HashSet<>();

        for (int num : nums) {
            // .add() false return panna, adhu munnadiye set-la irukku nu artham
            if (!seen.add(num)) {
                duplicates.add(num);
            }
        }
        return new ArrayList<>(duplicates);
    }

    public static void main(String[] args) {
        int[] input = {1, 2, 3, 2, 4, 5, 1};
        System.out.println(findDuplicates(input)); // Output: [1, 2]
    }
}


// SDET Special: Java Streams (Modern Way)
import java.util.*;
import java.util.stream.Collectors; 

public class Main {
    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1, 2, 3, 2, 4, 5, 1);
        
        Set<Integer> items = new HashSet<>();
        List<Integer> duplicates = list.stream()
                .filter(n -> !items.add(n)) // add panna mudiyadhappo filter aagum
                .distinct()                // oru duplicate-ah oru vaati thaan kaatanum
                .collect(Collectors.toList());

        System.out.println(duplicates); // Output: [2, 1]
    }
}
