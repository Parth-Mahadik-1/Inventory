package Prac4;
import java.util.Scanner;

abstract class base1{
    int num1;
    int num2;
    Scanner sc = new Scanner(System.in);

    //abstract fucntions
    abstract void add();
    abstract void sub();
    abstract void mul();
    abstract void div();


    void input1(){

        System.out.println("Enter 1st number");
        num1 = sc.nextInt();
        System.out.println("Enter 1st number");
        num2 = sc.nextInt();


    }
}
class derive1 extends base1{

        @Override
        void add(){
            System.out.println("Addition");
            System.out.println(num1+" + "+ num2+" = "+(num1+num2));
        }
        @Override
        void sub(){
            System.out.println("Substraction");
            System.out.println(num1+" - "+ num2+" = "+(num1-num2));
        }
        @Override
        void mul(){
            System.out.println("multiplication");
            System.out.println(num1+" * "+ num2+" = "+(num1*num2));
        }
        @Override
        void div(){
            System.out.println("Division");
            if (num2 !=0){
                System.out.println(num1+" / "+ num2+" = "+(num1/num2));
            }else{
                System.out.println("Division by zero is not allowed.");
            }

        }void operation(){
        System.out.println("choose 1-ADD | 2-SUB | 3-MUL | 4-DIV");
        int opt = sc.nextInt();
        switch (opt){
            case 1 -> add();
            case 2 -> sub();
            case 3 -> mul();
            case 4 -> div();

        }
    }

}

public class abstract_implimentation {
    public static void main(String[]args){
        derive1 d = new derive1();
        d.input1();
        d.operation();

    }
}
