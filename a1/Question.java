package a1;

interface Question
{
    void setQuestion(String question);
    void setAnswer(String answer);
    void addAnswerChoices(String choice);
    void resetChoices();
    String getQuestion();
    void printOptions();
    boolean checkAnswer(String studentAnswer);
}