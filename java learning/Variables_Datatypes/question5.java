package Variables_Datatypes;
import java.util.Scanner;

public class question5 {
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);

        System.out.println("Enter a number: ");
        double a = sc.nextDouble();

        if (a % 1 ==0){
            System.out.println(a+ " is a integer");
        }else System.out.println(a +"is not a integer");

    }
}
