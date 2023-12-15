// 1.PRIME NO. MIN AND MAX
// public class accenture{
// public static void main(String[] args) {
//     int[] arr = { 1, 2, 3, 4, 5, 6, 7 };
//     int min = Integer.MAX_VALUE;
//     int max = Integer.MIN_VALUE;
//     for (int i = 0; i < arr.length; i++) {
//         if (isPrime(arr[i])) {
//             min = Math.min(min, arr[i]);
//             max = Math.max(max, arr[i]);
//         }
//     }
//     System.out.println("Minimum prime number: " + min);
//     System.out.println("Maximum prime number: " + max);
// }

// public static boolean isPrime(int n) {
//     if (n <= 1) {
//         return false;
//     }
//     for (int i = 2; i <= Math.sqrt(n); i++) {
//         if (n % i == 0) {
//             return false;
//         }
//     }
//     return true;
// }
// }
// 2.2D Sorted Array 
// public class ArraySort {
//     static int sortRowWise(int arr[][]) {
//         for (int i = 0; i < arr.length; i++)
//             Arrays.sort(arr[i]);
//         for (int i = 0; i < arr.length; i++) {
//             for (int j = 0; j < arr[i].length; j++)
//                 System.out.print(arr[i][j] + " ");
//             System.out.println();
//         }
//         return 0;
//     }

//     public static void main(String args[]) {
//         int arr[][] = {
//             {9, 2, 6, 4, 5},
//             {8, 3, 7, 0, 2},
//             {5, 3, 8, 1, 2},
//             {3, 5, 7, 1, 0}
//         };
//         sortRowWise(arr);
//     }
// }
// // 3.Unique characters in java
// public class UniqueCharacters {
//     static final int MAX_CHAR = 256;

//     static void printDistinct(String str) {
//         int n = str.length();
//         boolean[] visited = new boolean[MAX_CHAR];
//         Arrays.fill(visited, false);

//         for (int i = 0; i < n; i++) {
//             if (!visited[str.charAt(i)]) {
//                 visited[str.charAt(i)] = true;
//                 System.out.print(str.charAt(i) + " ");
//             }
//         }
//     }

//     public static void main(String[] args) {
//         String inputString = "Hello";
//         System.out.println("Unique characters in the string:");
//         printDistinct(inputString);
//     }
// }
// *4. 3.Unique string in java
// import java.util.HashSet;

// public class UniqueCharacters {
//     static boolean hasUniqueCharacters(String str) {
//         HashSet<Character> set = new HashSet<>();
//         for (char c : str.toCharArray()) {
//             if (!set.add(c)) {
//                 return false;
//             }
//         }
//         return true;
//     }

//     public static void main(String[] args) {
//         String inputString = "Hello";
//         if (hasUniqueCharacters(inputString)) {
//             System.out.println("The string contains all unique characters.");
//         } else {
//             System.out.println("The string does not contain all unique characters.");
//         }
//     }
// }
// 5.Pack of cards
import java.util.Arrays;
import java.util.Collections;

public class SimpleCardGame {

    public static void main(String[] args) {
        // Create and shuffle a deck
        String[] deck = createShuffledDeck();

        // Draw and print the first 5 cards
        System.out.println("Drawing the first 5 cards:");
        for (int i = 0; i < 5; i++) {
            String drawnCard = drawCard(deck);
            System.out.println("Card " + (i + 1) + ": " + drawnCard);
        }

        // Display the remaining cards in the deck
        System.out.println("\nRemaining cards in the deck: " + deck.length);
    }

    // Function to create and shuffle a deck
    private static String[] createShuffledDeck() {
        String[] suits = { "Hearts", "Diamonds", "Clubs", "Spades" };
        String[] ranks = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace" };

        String[] deck = new String[suits.length * ranks.length];
        int index = 0;

        for (String suit : suits) {
            for (String rank : ranks) {
                deck[index++] = rank + " of " + suit;
            }
        }

        shuffleDeck(deck);
        return deck;
    }

    // Function to shuffle a deck
    private static void shuffleDeck(String[] deck) {
        Collections.shuffle(Arrays.asList(deck));
    }

    // Function to draw a card from the deck
    private static String drawCard(String[] deck) {
        if (deck.length == 0) {
            throw new IllegalStateException("Deck is empty");
        }
        return deck[--deck.length];
    }
}
// PRIME FACTORS:
// https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
// SUM OF PRIME NUMBERS:https://www.javatpoint.com/sum-of-prime-numbers-in-java

// 6.Circular Primes
import java.lang.*;

class CircularPrime {
    // Function to check if a number is prime or not
    static boolean isPrime(int n) {
        // Corner cases
        if (n <= 1)
            return false;
        if (n <= 3)
            return true;
        if (n % 2 == 0 || n % 3 == 0)
            return false;
        for (int i = 5; i * i <= n; i = i + 6)
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        return true;
    }

    // Function to check if a number is circular prime or not
    static boolean checkCircular(int num) {
        int n = num;
        int count = 0;
        int temp = num;
        while (isPrime(temp)) {
            int rem = temp % 10;
            int div = temp / 10;
            temp = (int) ((Math.pow(10, (int) Math.log10(num))) * rem) + div;
            if (temp == num)
                break;
            count++;
        }
        return (count == (int) Math.log10(n));
    }

    // Driver Program
    public static void main(String[] args) {
        int N = 1193;
        if (checkCircular(N))
            System.out.println("Yes");
        else
            System.out.println("No");
    }
}
// 7.Consider 2 integers dice ,num given range check the value of dice is even
// or odd if it is even print sum of digits at odd positions if it is odd print
// sum of digits at even positions.
import java.util.Scanner;

public class DiceNumberAnalyzer {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input range of dice numbers
        System.out.print("Enter the lower bound of the dice range: ");
        int lowerBound = scanner.nextInt();

        System.out.print("Enter the upper bound of the dice range: ");
        int upperBound = scanner.nextInt();

        // Generate a random dice number within the specified range
        int diceNumber = generateRandomDiceNumber(lowerBound, upperBound);

        System.out.println("Generated dice number: " + diceNumber);

        // Check if the dice number is even or odd
        if (diceNumber % 2 == 0) {
            // If even, print the sum of digits at odd positions
            int oddSum = sumDigitsAtOddPositions(diceNumber);
            System.out.println("The dice number is even. Sum of digits at odd positions: " + oddSum);
        } else {
            // If odd, print the sum of digits at even positions
            int evenSum = sumDigitsAtEvenPositions(diceNumber);
            System.out.println("The dice number is odd. Sum of digits at even positions: " + evenSum);
        }

        scanner.close();
    }

    // Function to generate a random dice number within the specified range
    private static int generateRandomDiceNumber(int lowerBound, int upperBound) {
        return lowerBound + (int) (Math.random() * (upperBound - lowerBound + 1));
    }

    // Function to calculate the sum of digits at odd positions
    private static int sumDigitsAtOddPositions(int number) {
        int sum = 0;
        int position = 1;

        while (number > 0) {
            int digit = number % 10;

            if (position % 2 == 1) {
                sum += digit;
            }

            number /= 10;
            position++;
        }

        return sum;
    }

    // Function to calculate the sum of digits at even positions
    private static int sumDigitsAtEvenPositions(int number) {
        int sum = 0;
        int position = 1;

        while (number > 0) {
            int digit = number % 10;

            if (position % 2 == 0) {
                sum += digit;
            }

            number /= 10;
            position++;
        }

        return sum;
    }
}

// 7.Vowel Repetition
public class VowelCount {
    static int countVowels(String str) {
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
                    ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        String inputString = "Hello World";
        int vowelCount = countVowels(inputString);
        System.out.println("The number of vowels in the string is: " + vowelCount);
    }
}

// 8.Problem shortening
public class StringShorten {
    static String shorten(String str, int maxLength) {
        if (str.length() <= maxLength) {
            return str;
        } else {
            return str.substring(0, maxLength - 3) + "...";
        }
    }

    public static void main(String[] args) {
        String inputString = "This is a long string that needs to be shortened.";
        String shortenedString = shorten(inputString, 20);
        System.out.println(shortenedString);
    }
}

// 9.Sorting an Array
public class ArraySort {
    static void bubbleSort(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = { 64, 34, 25, 12, 22, 11, 90 };
        bubbleSort(arr);
        System.out.println("Sorted array:");
        for (int i = 0; i < arr.length; ++i) {
            System.out.print(arr[i] + " ");
        }
    }
}
