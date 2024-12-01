package Variables_Datatypes;
import  java.util.Scanner;

public class Question2 {
    public static void main(String[] args){
        // Program to print CGPA
        Scanner sc = new Scanner(System.in);
        double gp1;
        double gp2;
        double gp3;


        System.out.println("enter sub1 marks: ");
        double sub1 = sc.nextDouble();

        System.out.println("enter sub2 marks: ");
        double sub2 = sc.nextDouble();

        System.out.println("enter sub3 marks: ");
        double sub3 = sc.nextDouble();

        gp1 = cal_gp(sub1);
        gp2 = cal_gp(sub2);
        gp3 = cal_gp(sub3);


        double CGPA = (gp1+gp2+gp3)/3;
        double percentage= CGPA*9.5;

        System.out.println("CGPS of three subject is: "+ CGPA);

        System.out.println("precentage of three subject is: "+ percentage);

    }
    public static double cal_gp(double marks){
        if(marks >= 90) return 10;
        else if (marks>=80 && marks < 90) return 9;
        else if (marks>=70 && marks < 80) return 8;
        else if (marks>=60 && marks < 70) return 7;
        else if (marks>=50 && marks < 60) return 6;
        else if (marks>=40 && marks < 50) return 5;
        else return 0;


    }
}
