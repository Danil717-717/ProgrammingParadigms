import java.util.Arrays;

public class Task06 {
    public static void bubbleSort(int[] sortArr){
        for (int i = 0; i < sortArr.length - 1; i++) {
            for(int j = 0; j < sortArr.length - i - 1; j++) {
                if(sortArr[j + 1] < sortArr[j]) {
                    int swap = sortArr[j];
                    sortArr[j] = sortArr[j + 1];
                    sortArr[j + 1] = swap;
                }
            }
        }
    }
    
    public static void main(String args[]) {
        int[] sortArr = {12, 6, 4, 1, 15, 10};
        System.out.println(Arrays.toString(sortArr));
        bubbleSort(sortArr);
        System.out.println(Arrays.toString(sortArr));
    }
}
