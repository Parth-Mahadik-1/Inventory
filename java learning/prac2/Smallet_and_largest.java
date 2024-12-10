package prac2;
import java.util.Scanner;
public class Smallet_and_largest {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        System.out.println("enter a size of an array: ");
        int s = sc.nextInt();

        int arr[] = new int[s];
        System.out.println("enter elemnet  of an array: ");
        for (int i=0;i<s;i++){
            arr[i]=sc.nextInt();
        }
        System.out.println("given array: ");
        for (int i=0;i<s;i++){
            System.out.print(" "+arr[i]);
        }
        System.out.println();
        int small = arr[0];
        int large = arr[0];

        for (int i=0;i<s;i++){
            if(arr[i]<small){
                small = arr[i];
            }
            if(arr[i]>large){
                large = arr[i];
            }
        }
        System.out.println("Smallest elemnt is : "+small);
        System.out.println("Largest elemnt is : "+large);




    }
}
