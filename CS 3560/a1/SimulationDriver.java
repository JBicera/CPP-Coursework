package a1;
import java.util.Random;
import java.util.Scanner;


public class SimulationDriver
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        VotingService iVote = new VotingService();
        getStudents(iVote, 10);

        Question question1 = new SingleChoice();
        Question question2 = new MultipleChoice();

        iVote.addQuestion(question1);
        iVote.addQuestion(question2);

        question1.setQuestion("Panda Express is the only good food at CPP. (True or False)");
        question1.addAnswerChoices("True");
        question1.addAnswerChoices("False");
        question1.setAnswer("1");

        question2.setQuestion("What is 2+2?");
        question2.setQuestion("What is 2+2?");
        question2.addAnswerChoices("532"); 
        question2.addAnswerChoices("46"); 
        question2.addAnswerChoices("4"); 
        question2.addAnswerChoices("7");   
        question2.setAnswer("C");  

        for(int i = 0; i < iVote.questions.size(); i++)
        {
            System.out.println(iVote.questions.get(i).getQuestion());
            iVote.questions.get(i).printOptions();
            for(int j = 0; j < iVote.students.size(); j++)
            {
                System.out.println("Answer for student[" + iVote.students.get(j).getID()+"]");
                String userInput = scanner.nextLine();
                String[] answers = userInput.split(",");
                for(String answer : answers)
                {
                    iVote.students.get(i).setAnswer(answer);
                    if (iVote.answerStats.containsKey(answer)) {
		            	int oldValue = iVote.answerStats.get(answer);
		            	iVote.answerStats.put(answer, ++oldValue);
		            }
		            
		            else {
		            	iVote.answerStats.put(answer,1);
		            }
                }
            }
            iVote.calcStatistic();
            iVote.questions.get(i).resetChoices(); 
            iVote.answerStats.clear();
        }
    }  
    public static void getStudents(VotingService iVote,int max)
    {
        Random random = new Random();
		int randomInt = random.nextInt(max) + 1;
        for(int i = 0; i < randomInt; i++)
            iVote.addStudent(new Student(Integer.toString(i)));
    }
}