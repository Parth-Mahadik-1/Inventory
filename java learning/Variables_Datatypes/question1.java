package Variables_Datatypes;
import  java.util.Scanner;
public class question1 {
    public static void main(String[] args){
        // Program To print Sum of Three numbers in Java
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 1st number: ");
        double a = sc.nextDouble();

        System.out.println("Enter 2nd  number: ");
        double b = sc.nextDouble();

        System.out.println("Enter 3rd number: ");
        double c = sc.nextDouble();

        double sum = a+b+c;
        System.out.println("Sum of Three numbers  is "+ sum);


    }
}
