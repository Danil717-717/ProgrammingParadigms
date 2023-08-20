import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet;

public class Task04 {
    public static void main(String[] args) {
        int[] numbers = {1, 1, 2, 1, 3, 4, 5};
        
        Set<Integer> setUniqueNumbers = new LinkedHashSet<Integer>();
        for(int x : numbers) {
            setUniqueNumbers.add(x);
        }

        System.out.println("Первонач массив: " + Arrays.toString(numbers));
        System.out.println("Массив уникальныx значений: " + setUniqueNumbers);

       
    }
}
