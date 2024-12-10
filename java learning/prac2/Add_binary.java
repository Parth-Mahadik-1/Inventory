package prac2;
import  java.util.Scanner;
public class Add_binary {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter 1st binary no: ");
        String str1 = sc.nextLine();

        System.out.println("Enter 2nd binary no: ");
        String str2 = sc.nextLine();

        int a = Integer.parseInt(str1,2);
        int b = Integer.parseInt(str2,2);

        int s = a+b;

        String sum = Integer.toBinaryString(s);
        System.out.println("Sum is : "+sum);




    }
}
