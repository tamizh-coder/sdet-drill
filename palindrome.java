# java code for string

import java.util.Scanner;

public class StringPalindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String text = sc.nextLine();

        String reverse = new StringBuilder(text).reverse().toString();

        if (text.equals(reverse))
            System.out.println("Palindrome");
        else
            System.out.println("Not a Palindrome");
    }
}