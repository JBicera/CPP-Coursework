package a1;
import java.util.ArrayList;


public class Student
{
    private String uniqueID;
    private ArrayList<String> answers = new ArrayList<>();
    private static int countID = 0;
    public Student()
    {
        this.uniqueID = "0";
    }
    public Student(String ID)
    {
        this.uniqueID = ID;
    }
    public void setAnswer(String input) {this.answers.add(input);}
    public String getID() {return uniqueID;}
	public void incrementID() {countID++;}
}