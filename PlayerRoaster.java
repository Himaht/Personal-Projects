import java.util.Scanner;

public class PlayerRoaster{
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        int[] jerseyNum = new int[5];
        int[] coachRating = new int[5];

        for (int i = 0; i < jerseyNum.length; i++) {
            System.out.println("Enter player " + (i + 1) + "'s jersey number:");
            jerseyNum[i] = scnr.nextInt();
            System.out.println("Enter player " + (i + 1) + "'s rating:");
            coachRating[i] = scnr.nextInt();
            System.out.println();
        }
        System.out.println("ROSTER");
        for (int i = 0; i < 5; i++) {
            System.out.println("Player " + (i + 1) + " -- Jersey number: " + jerseyNum[i] + ", Rating: " + coachRating[i]);
        }
        System.out.println();

        char option = ' ';

        while (option != 'q') {
            System.out.println("MENU");
            System.out.println("u - Update player rating");
            System.out.println("a - Print players above a rating");
            System.out.println("r - Replace player");
            System.out.println("p - Print roster");
            System.out.println("q - Quit");
            System.out.println();
            System.out.print("Choose an option:");
            option = scnr.next().charAt(0);

            switch (option) {
                case 'p':
                    System.out.println("ROSTER");
                    for (int i = 0; i < 5; i++) {
                        System.out.println("Player " + (i + 1) + " -- Jersey number: " + jerseyNum[i] + ", Rating: " + coachRating[i]);
                    }
                    break;
                case 'u':
                    System.out.println("Enter a jersey number:");
                    int updateJersey = scnr.nextInt();
                    for (int i = 0; i < 5; i++) {
                        if (jerseyNum[i] == updateJersey) {
                            System.out.println("Enter a new rating for player:");
                            coachRating[i] = scnr.nextInt();
                            break;
                        }
                    }
                    break;
                case 'a':
                    //System.out.println("\nEnter a rating:");
                    int newRating = scnr.nextInt();
                    System.out.println("ABOVE " + newRating);
                    for (int i = 0; i < coachRating.length; i++) {
                        if (coachRating[i] > newRating) {
                            System.out.println("Player " + (i + 1) + " -- Jersey number: " + jerseyNum[i] + ", Rating: " + coachRating[i]);
                        }
                    }
                    break;
                case 'r':
                    System.out.println("Enter the jersey number of the player to replace:");
                    int replaceJersey = scnr.nextInt();
                    for (int i = 0; i < 5; i++) {
                        if (jerseyNum[i] == replaceJersey) {
                            System.out.println("Enter the new jersey number:");
                            jerseyNum[i] = scnr.nextInt();
                            System.out.println("Enter the new rating for player:");
                            coachRating[i] = scnr.nextInt();
                            break;
                        }
                    }
                    break;
                default:
                    break;
            }
            System.out.println();
        }
    }
}
