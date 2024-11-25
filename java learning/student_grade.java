import javax.swing.*;
import java.util.Scanner;


public class student_grade {
    public static  void main (String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter name of Student:  ");
        String name = sc.nextLine();

        System.out.println("Enter Exam no:  ");
        int Ex_no = sc.nextInt();

        System.out.println("Enter Total marks: ");
        int Tot=sc.nextInt();

        System.out.println("enter marks in sub1: ");
        double s1 = sc.nextDouble();

        System.out.println("enter marks in sub2: ");
        double s2 = sc.nextDouble();

        System.out.println("enter marks in sub3: ");
        double s3 = sc.nextDouble();

        System.out.println("enter marks in sub4: ");
        double s4= sc.nextDouble();

        System.out.println("enter marks in sub5: ");
        double s5 = sc.nextDouble();

        double sum = (s1+s2+s3+s4+s5);
        int tot_sum = Tot*5;
        double tot_marks = (sum /tot_sum) * 100;


        if (tot_marks >90){
            System.out.println(name + "got an A grade..");
        } else if ( tot_marks >=80 && tot_marks<90 ) {
            System.out.println(name + "got an B grade..");
        } else if (tot_marks >=60 && tot_marks<80) {
            System.out.println(name + "got an c grade..");
        } else if (tot_marks < 35 ) {
            System.out.println(name + "failed...");
        }


    }
}
