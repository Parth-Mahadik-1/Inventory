import java.util.Scanner;

public class input_methods {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        // reading integer values
        System.out.println("enter number 1: ");
        int a = sc.nextInt();

        System.out.println("enter number 2: ");
        int b = sc.nextInt();

        int sum = a+b;
        System.out.println("sum is : "+sum);




        // reading float values
        System.out.println("enter float numbers: ");
        System.out.println("1st :");
        float x = sc.nextFloat();
        System.out.println("2nd: ");
        float y = sc.nextFloat();
        float sum1 = x+y;
        System.out.println("sum is "+sum1);


        //reading char values
        System.out.println("enter string values: ");
        System.out.println("enter your name: ");
        String m = sc.nextLine();
        System.out.println("enter your std: ");
        String n = sc.next();
        System.out.println("your name: "+m);
        System.out.println("your std: "+n);


        // code to read student details
        System.out.println("enter student name: ");
        String name = sc.nextLine();
        System.out.println("enter student roll number: ");
        int roll = sc.nextInt();
        System.out.println("enter student marks: ");
        double marks = sc.nextDouble();
        System.out.println("enter student grade: ");
        String grade = sc.next();

        System.out.println("name of student: "+name);
        System.out.println("roll no of student: "+roll);
        System.out.println("marks of student: "+marks);
        System.out.println("grade of student: "+grade);


    }
}
