package Prac4;
import  java.util.Scanner;

class base{
    int num1;
    int num2;
    Scanner sc = new Scanner(System.in);
    void input(){
        System.out.println("from base class");

        System.out.println("Enter 1st number: ");
        num1 = sc.nextInt();
        System.out.println("Enter 2nd number: ");
        num2 = sc.nextInt();
    }
}

class derive extends base{
    int opt;
    void operation(){
        System.out.println("choose 1-ADD | 2-SUB | 3-MUL | 4-DIV ");
        opt = sc.nextInt();
        if (opt == 1){
            System.out.println("Addition");
            System.out.println(num1 + " + "+num2+" = "+(num1+num2));
        } else if (opt == 2) {
            System.out.println("Substraction");
            System.out.println(num1 + " - "+num2+" = "+ (num1-num2));

        }else if (opt == 3) {
            System.out.println("Multiplication");
            System.out.println(num1 + " * "+num2+" = "+ (num1*num2));

        }else {
                System.out.println("Division");
                System.out.println(num1 + " / "+num2+" = "+ (num1/num2));
        }
    }
}

public class single_inheritance {
    public static void main(String[]args){
        derive a = new derive();
        a.input();
        a.operation();
    }
}
