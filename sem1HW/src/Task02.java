public class Task02 {
    public static void main(String[] args) {
        int[] arr = new int[] { 10, 20, 1, 3, 5, 7 };
        int min = 0;
        for (int i = 0; i < arr.length; i++) {
            min=arr[0];
            if (arr[i] < min)
                min = arr[i];
                
        }
        System.out.println(min);
    }
}
