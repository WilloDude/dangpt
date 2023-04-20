import java.util.Scanner;
import com.openai.api.*;

public class ChatGPTClone {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        OpenAI api = new OpenAI("your-api-key-here");
        String prompt = "";

        while (true) {
            System.out.print("You: ");
            String user_input = scanner.nextLine();
            prompt += "You: " + user_input + "\nAI: ";
            String response = api.complete(prompt, "davinci", 1).get(0).getText();
            prompt += response + "\n";
            System.out.println("AI: " + response);
        }
    }
}
