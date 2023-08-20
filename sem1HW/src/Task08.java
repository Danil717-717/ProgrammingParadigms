import java.util.Scanner;

public class Task08 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите число: ");
        int n = scanner.nextInt();
        int sum = 0;
        while (n != 0) {
            sum += (n % 10);
            n /= 10;
        }
        System.out.println(sum + " ");
    }
}
