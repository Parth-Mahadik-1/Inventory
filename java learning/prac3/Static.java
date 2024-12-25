package prac3;

public class Static {

    static int a = 0;
    int b = 0;

    static {}
    public Static(){
        a++;
        b++;
        System.out.println("Static variable: "+a);
        System.out.println("Normal variable: "+b);
    }
    public static void hello(String a){
        System.out.println("hello "+a+" i am from static");
    }

    public void hi(String a){
        System.out.println("hello "+a+" i am from non static");
    }

    public static void main(String[]args){
        hello("Parth");
        Static s = new Static();
        s.hi("chinmay");
        Static s1 = new Static();


    }
}
