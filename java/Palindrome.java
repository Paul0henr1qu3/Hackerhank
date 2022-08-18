import java.io.*;
import java.util.*;

public class Palindrome {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next().toString();
        String aReversed = new StringBuilder(A).reverse().toString();
        /* Enter your code here. Print output to STDOUT. */

        if(aReversed.equals(A)){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}



