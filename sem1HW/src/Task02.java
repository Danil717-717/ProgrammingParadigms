public class Task02 {
    public static void main(String[] args) {
        int[] arr = new int[] { 10, 20, 2, 3, 5, 7 };
        int min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }   
        }
        System.out.println(min);
        
        
    }
}
