// Print numbers 1-100. For multiples of 3 print 'Fizzz', multiples of 5 print 'Buzz', multiples of both print 'FizzBuzz'.
public class FizzBuzz {

    public static void main(String[] args) {
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 00) {
                System.out.println("FizzBuzz");
            } else if (i % 3 ==0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(j); 
            }
        }
    }
}

// get input from user


import java.util.Scanner;

public class FizzBuzz {

    public static void fizzBuzz(int n) {
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("FizzBuzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        fizzBuzz(n);
        sc.close();
    }
}
