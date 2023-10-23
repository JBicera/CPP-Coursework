package a1;
import java.util.ArrayList;

public class MultipleChoice implements Question
{
    private char answerChoice = 'A';
    private String question;
    private ArrayList<String> choices = new ArrayList<>();
	private ArrayList<String> answers = new ArrayList<>();
    public void setQuestion(String question){this.question = question;}
    public void setAnswer(String answer){this.answers.add(answer);}
    public void addAnswerChoices(String choice)
    {
        choices.add(answerChoice + ") " + choice);
        answerChoice++;
    }
    public void resetChoices(){answerChoice = 'A';}
    public String getQuestion(){return question;}
    public void printOptions() {
		for(int i = 0; i < choices.size(); i++) {
			System.out.println(choices.get(i));
		}
	}
    public boolean checkAnswer(String studentAnswer){return answers.contains(studentAnswer);}
};