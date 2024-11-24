import java.util.Scanner;

public class Star_patterns {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Pyramid pattern
        System.out.println("Enter number of rows for Pyramid: ");
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int k = 1; k <= 2 * i - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // Inverted Pyramid pattern
        System.out.println("Enter number of rows for Inverted Pyramid: ");
        int n1 = sc.nextInt();
        for (int i = n1; i >= 1; i--) {
            for (int j = 1; j <= n1 - i; j++) {
                System.out.print(" ");
            }
            for (int k = 1; k <= 2 * i - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // Right-Angled Triangle
        System.out.println("Enter number of rows for Right-Angled Triangle: ");
        int n2 = sc.nextInt();
        for (int i = 1; i <= n2; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // Inverted Right-Angled Triangle
        System.out.println("Enter number of rows for Inverted Right-Angled Triangle: ");
        int n3 = sc.nextInt();
        for (int i = n3; i >= 1; i--) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        sc.close();
    }
}
