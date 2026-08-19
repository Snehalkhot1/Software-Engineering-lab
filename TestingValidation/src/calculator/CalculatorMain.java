package calculator;

public class CalculatorMain {

    public static void main(String[] args) {

        Calculator c = new Calculator();

        System.out.println("-------------------------------------------------------------");
        System.out.println("             BLACK BOX TESTING - CALCULATOR");
        System.out.println("-------------------------------------------------------------");

        System.out.printf("%-10s %-12s %-12s %-12s %-10s%n",
                "Test Case", "Input", "Expected", "Actual", "Result");

        System.out.println("-------------------------------------------------------------");

        // TC01 - Addition
        int expected1 = 15;
        int actual1 = c.add(10, 5);

        System.out.printf("%-10s %-12s %-12d %-12d %-10s%n",
                "TC01", "10 + 5", expected1, actual1,
                expected1 == actual1 ? "Pass" : "Fail");


        // TC02 - Subtraction
        int expected2 = 5;
        int actual2 = c.subtract(10, 5);

        System.out.printf("%-10s %-12s %-12d %-12d %-10s%n",
                "TC02", "10 - 5", expected2, actual2,
                expected2 == actual2 ? "Pass" : "Fail");


        // TC03 - Multiplication
        int expected3 = 50;
        int actual3 = c.multiply(10, 5);

        System.out.printf("%-10s %-12s %-12d %-12d %-10s%n",
                "TC03", "10 * 5", expected3, actual3,
                expected3 == actual3 ? "Pass" : "Fail");


        // TC04 - Division
        int expected4 = 2;
        int actual4 = c.divide(10, 5);

        System.out.printf("%-10s %-12s %-12d %-12d %-10s%n",
                "TC04", "10 / 5", expected4, actual4,
                expected4 == actual4 ? "Pass" : "Fail");


        // TC05 - Division by Zero
        String expected5 = "Exception";
        String actual5;

        try {
            c.divide(10, 0);
            actual5 = "No Exception";
        } catch (ArithmeticException e) {
            actual5 = "Exception";
        }

        System.out.printf("%-10s %-12s %-12s %-12s %-10s%n",
                "TC05", "10 / 0", expected5, actual5,
                expected5.equals(actual5) ? "Pass" : "Fail");

        System.out.println("-------------------------------------------------------------");
    }
}