package prac3;
import java.util.Scanner;

public class constructor {
    private int a;
    private int b;
    private int c;


    public constructor(){
        System.out.println("I am from deafult consturctor...");
    }
    public constructor(int a,int b){
        System.out.println("I am from overload / parameterize constructor");
        int sum = a+b;
        System.out.println("Sum of "+a+" and b "+b+ " is="+sum);
    }
    public constructor(int a,int b,int c){
        this.a=a;
        this.b=b;
        this.c=c;

        System.out.println("I am from overload / parameterize constructor");
        int sum = a+b+c;
        System.out.println("Sum of "+a+" and b "+b+ " is="+sum);
    }
    public constructor(constructor other){
        this.a=other.a;
        this.b=other.b;
        this.c=other.c;


        System.out.println("I am from copy constructor");
        int sum = this.a+this.b+this.c;
        System.out.println("Sum of "+a+" and b "+b+ " and c "+c+ " is="+sum);
    }



    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        constructor c1  = new constructor();
        constructor c2  = new constructor(2,3);
        constructor c3  = new constructor(2,3,4);
        constructor c4  = new constructor(c3);


    }
}
