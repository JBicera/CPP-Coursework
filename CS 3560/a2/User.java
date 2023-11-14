package a2;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
import javax.swing.border.Border;
import javax.swing.border.TitledBorder;
import java.lang.String;

public class User{
	//Private Variables
	private String currUser;
	private JTextArea userID;
    private JButton followUser;
    private JTextArea tweetMessage;
    private JButton tweet;
    private JList<String> newsFeed;
    private JFrame jfrm;
    private DefaultListModel<String> tweetModel;
    private String[] followers = new String[100];
    private String[] messages = new String[100];
    private int totalMessages = 0;
    private int positiveMessages = 0;
    private int numFollow = 0;

	
	User(String currUser,final Admin admin){
		this.currUser = currUser;
		//Initialize JFrame
		jfrm = new JFrame("User");
		jfrm.setSize(300,400);
		jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	
		//2 Rows, 1 Column
		JPanel mainPanel = new JPanel();
		mainPanel.setLayout(new GridLayout(2,1,7,7));
		mainPanel.setBorder(new TitledBorder(currUser));

		//Top and bottom parts of the main panel
		JPanel userTopJPanel = new JPanel();
		userTopJPanel.setLayout(new BorderLayout());
		JPanel userBottomJPanel = new JPanel();
		userBottomJPanel.setLayout(new BorderLayout());
		
		//Organize the top and bottom panels with grid layout
		JPanel userTopSubPanel = new JPanel();
		userTopSubPanel.setLayout(new GridLayout(1,2,5,5));
		JPanel userTopSubPanel2 = new JPanel();
		userTopSubPanel2.setLayout(new GridLayout(1,1,5,5));
		JPanel userBottomSubPanel = new JPanel();
		userBottomSubPanel.setLayout(new GridLayout(1,2,5,5));
		JPanel userBottomSubPanel2 = new JPanel();
		userBottomSubPanel2.setLayout(new GridLayout(1,1,5,5));
		
		//Initialize private variables
		userID = new JTextArea(currUser);
		followUser = new JButton("Follow User");
		tweetMessage = new JTextArea("Tweet Message");
		tweet = new JButton("Post Tweet");
		newsFeed = new JList<>(tweetModel = new DefaultListModel<>());
		
		//Sets black border
		Border simpleBorder = BorderFactory.createLineBorder(Color.BLACK);
		userID.setBorder(simpleBorder);
		tweetMessage.setBorder(simpleBorder);
		newsFeed.setBorder(simpleBorder);
		
		userTopSubPanel.add(userID);
		userTopSubPanel.add(followUser);
		userBottomSubPanel2.add(newsFeed);
		userBottomSubPanel.add(tweetMessage);
		userBottomSubPanel.add(tweet);
		
		userTopJPanel.add(userTopSubPanel, BorderLayout.NORTH);
		userTopJPanel.add(userTopSubPanel2, BorderLayout.CENTER);
		userBottomJPanel.add(userBottomSubPanel,BorderLayout.NORTH);
		userBottomJPanel.add(userBottomSubPanel2, BorderLayout.CENTER);
		
		mainPanel.add(userTopJPanel);
		mainPanel.add(userBottomJPanel);
		
		jfrm.add(mainPanel);
		
		tweet.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				String message = tweetMessage.getText();
				if(message.toLowerCase().contains("good") ||
					message.toLowerCase().contains("great") ||
					message.toLowerCase().contains("excellent"))
					positiveMessages += 1;

				String userTweet = "- " + currUser + ": " + message;
				messages[totalMessages] = userTweet;
				totalMessages += 1;
				
				tweetModel.addElement(userTweet);
				
				newsFeed.repaint();
				
				admin.notifyFollowers(currUser, userTweet, followers);
			}
		});

		followUser.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				followers[numFollow] = userID.getText();
				numFollow += 1;
			}
		});
	}

	public void setVisible() {
		jfrm.setVisible(true);
	}
	public int getTotalMessages() {
        return totalMessages;
    }

    public int getPositiveMessages() {
        return positiveMessages;
    }
	public String getUsername(){
		return currUser;
	}
	
    public double getPositivePercentage() {
        if (totalMessages == 0) {
            return 0.0;
        }
        return ((double) positiveMessages / totalMessages) * 100.0;
    }
	public JList<String> getNewsFeed(){
		return newsFeed;
	}
	public DefaultListModel<String> getTweetModel()
	{
		return tweetModel;
	}
}