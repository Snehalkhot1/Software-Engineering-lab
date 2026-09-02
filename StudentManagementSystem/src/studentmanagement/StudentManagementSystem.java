package studentmanagement;

import java.util.ArrayList;
import java.util.Scanner;

public class StudentManagementSystem {

    static Scanner sc = new Scanner(System.in);

    static ArrayList<Student> students = new ArrayList<>();

    // Login credentials
    static String username = "admin";
    static String password = "1234";

    // Student Registration
    public static void registerStudent() {

        System.out.println("\n===== STUDENT REGISTRATION =====");

        System.out.print("Enter Student ID: ");
        int id = sc.nextInt();
        sc.nextLine();

        // Check duplicate ID
        for (Student s : students) {
            if (s.getId() == id) {
                System.out.println("Student ID already exists!");
                return;
            }
        }

        System.out.print("Enter Student Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Age: ");
        int age = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Course: ");
        String course = sc.nextLine();

        System.out.print("Enter Email: ");
        String email = sc.nextLine();

        Student student = new Student(id, name, age, course, email);

        students.add(student);

        System.out.println("Student registered successfully!");
    }

    // Login
    public static boolean login() {

        System.out.println("\n========== LOGIN ==========");

        System.out.print("Enter Username: ");
        String user = sc.nextLine();

        System.out.print("Enter Password: ");
        String pass = sc.nextLine();

        if (user.equals(username) && pass.equals(password)) {

            System.out.println("Login successful!");
            return true;

        } else {

            System.out.println("Invalid username or password!");
            return false;
        }
    }

    // Add Student
    public static void addStudent() {

        System.out.println("\n========== ADD STUDENT ==========");

        System.out.print("Enter Student ID: ");
        int id = sc.nextInt();
        sc.nextLine();

        for (Student s : students) {

            if (s.getId() == id) {
                System.out.println("Student ID already exists!");
                return;
            }
        }

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Age: ");
        int age = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Course: ");
        String course = sc.nextLine();

        System.out.print("Enter Email: ");
        String email = sc.nextLine();

        Student student = new Student(id, name, age, course, email);

        students.add(student);

        System.out.println("Student added successfully!");
    }

    // Update Student
    public static void updateStudent() {

        System.out.println("\n========== UPDATE STUDENT ==========");

        System.out.print("Enter Student ID: ");
        int id = sc.nextInt();
        sc.nextLine();

        for (Student s : students) {

            if (s.getId() == id) {

                System.out.print("Enter New Name: ");
                String name = sc.nextLine();

                System.out.print("Enter New Age: ");
                int age = sc.nextInt();
                sc.nextLine();

                System.out.print("Enter New Course: ");
                String course = sc.nextLine();

                System.out.print("Enter New Email: ");
                String email = sc.nextLine();

                s.setName(name);
                s.setAge(age);
                s.setCourse(course);
                s.setEmail(email);

                System.out.println("Student updated successfully!");

                return;
            }
        }

        System.out.println("Student not found!");
    }

    // Delete Student
    public static void deleteStudent() {

        System.out.println("\n========== DELETE STUDENT ==========");

        System.out.print("Enter Student ID: ");
        int id = sc.nextInt();
        sc.nextLine();

        for (Student s : students) {

            if (s.getId() == id) {

                students.remove(s);

                System.out.println("Student deleted successfully!");

                return;
            }
        }

        System.out.println("Student not found!");
    }

    // Search Student
    public static void searchStudent() {

        System.out.println("\n========== SEARCH STUDENT ==========");

        System.out.print("Enter Student ID: ");
        int id = sc.nextInt();
        sc.nextLine();

        for (Student s : students) {

            if (s.getId() == id) {

                System.out.println("Student found!");
                s.displayStudent();

                return;
            }
        }

        System.out.println("Student not found!");
    }

    // Display all students
    public static void displayStudents() {

        System.out.println("\n========== ALL STUDENTS ==========");

        if (students.isEmpty()) {

            System.out.println("No students available.");

            return;
        }

        for (Student s : students) {

            s.displayStudent();
        }
    }

    // Main Menu
    public static void main(String[] args) {

        System.out.println("======================================");
        System.out.println("     STUDENT MANAGEMENT SYSTEM");
        System.out.println("======================================");

        boolean loggedIn = false;

        while (!loggedIn) {

            loggedIn = login();
        }

        int choice;

        do {

            System.out.println("\n======================================");
            System.out.println("             MAIN MENU");
            System.out.println("======================================");

            System.out.println("1. Student Registration");
            System.out.println("2. Add Student");
            System.out.println("3. Update Student");
            System.out.println("4. Delete Student");
            System.out.println("5. Search Student");
            System.out.println("6. Display All Students");
            System.out.println("7. Logout");
            System.out.println("======================================");

            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {

                case 1:
                    registerStudent();
                    break;

                case 2:
                    addStudent();
                    break;

                case 3:
                    updateStudent();
                    break;

                case 4:
                    deleteStudent();
                    break;

                case 5:
                    searchStudent();
                    break;

                case 6:
                    displayStudents();
                    break;

                case 7:
                    System.out.println("Logged out successfully!");
                    break;

                default:
                    System.out.println("Invalid choice!");
            }

        } while (choice != 7);

        sc.close();
    }
}