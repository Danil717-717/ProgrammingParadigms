import java.util.Scanner;

public class Task03 {

    public static void fibonacciValue(int num) {
        if (num <= 1) {
            System.out.println("0");
        } else if (num == 2) {
            System.out.println("1");
        } else {
            // return fibonacciValue(num - 1) + fibonacciValue(num - 2);
            int[] arr = new int[num];
            arr[0] = 1;
            arr[1] = 1;
            for (int i = 2; i < arr.length; ++i) {
                arr[i] = arr[i - 1] + arr[i - 2];
            }
            for (int i = 0; i < arr.length; ++i) {
                System.out.println(arr[i]);
              }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        System.out.print("Введите число: ");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        
        fibonacciValue(n);
    }
}
