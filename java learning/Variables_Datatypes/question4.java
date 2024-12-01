package Variables_Datatypes;
import  java.util.Scanner;

public class question4 {
    public static void main(String[] args){
        // Program to convert kilometres(KM) to miles

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter Kilometers: ");
        double km = sc.nextDouble();

        double mile = km * 0.621371;
        System.out.println("You travel"+km+" kilometers means "+ mile +" miles");
    }
}
