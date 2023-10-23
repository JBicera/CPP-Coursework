package a1;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.Scanner;

public class VotingService
{
    public ArrayList<Question> questions = new ArrayList<>();
	public ArrayList<Student> students = new ArrayList<>();
    public HashMap<String, Integer> answerStats = new HashMap<>();
    Scanner scanner = new Scanner(System.in);
    public void addQuestion(Question question){questions.add(question);}
    public void addStudent(Student student){students.add(student);}
    public int getQuestionType()
    {
        System.out.println("1.Multiple Choice");
		System.out.println("2.Single Choice");
		return scanner.nextInt();
    }
    public void calcStatistic()
    {
        for(Map.Entry<String, Integer> entry : answerStats.entrySet())
        {
            String key = entry.getKey();
            int value = entry.getValue();
            System.out.println(key + " : " + value);
        }
    }
}