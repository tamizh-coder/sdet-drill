#Approach 1: Built-in (StringBuilder)
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
