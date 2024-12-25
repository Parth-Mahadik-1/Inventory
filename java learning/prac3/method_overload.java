package prac3;

public class method_overload {

    public void add(int a,int b){
        System.out.println("i am from 1st define function: ");
        int sum = a+b;
        System.out.println("sum is ="+sum);
    }
    public void add(int a,int b,int c){
        System.out.println("i am from 2st define function: ");
        int sum = a+b+c;
        System.out.println("sum is ="+sum);
    }


    public static void main(String[]args){
        method_overload c1 = new method_overload();
        c1.add(2,4);
        c1.add(2,4,6);

    }
}
