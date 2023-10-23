package a1;
import java.util.ArrayList;

public class SingleChoice implements Question
{
    private String question;
    private ArrayList<String> choices = new ArrayList<>();
	private int answerChoice = 1;
	private String answer;
    public static int curr;
    public void setQuestion(String question){this.question = question;}
    public void setAnswer(String answer){this.answer = answer;}
    public void addAnswerChoices(String choice)
    {
        choices.add((char)answerChoice + ") " + choice);
        answerChoice++;
    }
    public void resetChoices(){answerChoice = 1;}
    public String getQuestion(){return question;}
    public void printOptions() {
		for(int i = 0; i < choices.size(); i++) {
			System.out.println(choices.get(i));
		}
	}
    public boolean checkAnswer(String studentAnswer){return this.answer == studentAnswer;}
};