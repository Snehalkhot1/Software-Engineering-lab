package calculator;
public class BoundaryValueAnalysis {

    // Addition
    static int add(int a, int b) {
        return a + b;
    }

    // Division
    static int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        return a / b;
    }

    public static void main(String[] args) {

        System.out.println("=== Boundary Value Analysis ===");

        // Test Case 1: Minimum
        System.out.println("\nTest Case: Minimum");
        System.out.println("Input: 0, 0");
        System.out.println("Expected Result: 0");
        System.out.println("Actual Result: " + add(0, 0));

        // Test Case 2: Maximum
        System.out.println("\nTest Case: Maximum");
        System.out.println("Input: Integer.MAX_VALUE, 0");
        System.out.println("Expected Result: Valid Output");
        System.out.println("Actual Result: " +
                add(Integer.MAX_VALUE, 0));

        // Test Case 3: Negative
        System.out.println("\nTest Case: Negative");
        System.out.println("Input: 5, -25");
        System.out.println("Expected Result: -15");
        System.out.println("Actual Result: " +
                add(-10, -5));

        // Test Case 4: Divide by Zero
        System.out.println("\nTest Case: Divide by Zero");
        System.out.println("Input: 10, 0");
        System.out.println("Expected Result: Exception");

        try {
            System.out.println("Actual Result: " + divide(10, 0));
        } catch (ArithmeticException e) {
            System.out.println("Actual Result: Exception");
            System.out.println("Message: " + e.getMessage());
        }
    }
}