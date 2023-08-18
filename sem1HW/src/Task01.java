import java.util.Scanner;

public class Task01 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in) ;
        System.out.println("Введите первую цифру") ;
        int start =console.nextInt();
        System.out.println("Введите вторую цифру") ;
        int end =console.nextInt();
        
        int sum = 0;
        System.out.println("Четные числа между первой цифрой: "+start+" и второй цифрой: "+end+" -  ");
        for (int i = start; i <= end; i++){
                if(i % 2 == 0){
                    sum += i;
                System.out.println(i);
                }
        }
        System.out.println("Сумма четных чисел от " + start + " до " + end + "  равна: " +sum);
    }
}
