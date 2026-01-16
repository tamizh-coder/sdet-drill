// #Approach 1: Built-in (StringBuilder)
public class ReverseString {

    public static String reverseString(String s) {
        if (s == null || s.length() <= 1) {
            return s;
        }
        return new StringBuilder(s).reverse().toString();
    }

    public static void main(String[] args) {
        System.out.println(reverseString(""));
        System.out.println(reverseString("a"));
        System.out.println(reverseString("hello"));
    }
}


/*Approach 2: Manual Loop */
public class ReverseStringManual {

    public static String reverseString(String s) {
        if (s == null || s.length() <= 1) {
            return s;
        }

        char[] chars = s.toCharArray();
        int left = 0, right = chars.length - 1;

        while (left < right) {
            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;
            left++;
            right--;
        }

        return new String(chars);
    }

    public static void main(String[] args) {
        System.out.println(reverseString(""));
        System.out.println(reverseString("a"));
        System.out.println(reverseString("hello"));
    }
}


Time Complexity: O(n)
Space Complexity: O(n)
