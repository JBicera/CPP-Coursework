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

//Observer interface
interface Observer {
    void update(String tweet);
}
//Visitor Interface
interface VisitorComponent{
	void accept(UserVisitor visitor);
}
//Represents the individual user of the mini-twitter
public class User implements Observer, VisitorComponent {
	//JFrame
	private JFrame jfrm;
	//Text area to 
	private JTextArea userID;
	private JTextArea tweetMessage;
    private JButton followUser;
	private JButton tweet;
	private JLabel lastUpdateTimeLabel;

	//Lists the twitter feed
    private JList<String> newsFeed;
    private DefaultListModel<String> tweetModel; 
		
	//Lists who you are following
	private DefaultListModel<String> followingModel; 
	private JList<String> followingList;

	//Private Variables
	private String currUser; //Name of the user
	private long creationTime; //Time of creation of user
	private long lastUpdateTime; //Last time user tweeted
    private String[] followers = new String[10];//Who the user is following
    private String[] messages = new String[10];//All tweets
    private int totalMessages = 0; //Number of tweets
    private int positiveMessages = 0; //Number of positive tweets
    private int numFollowers = 0; //Number of people who follow you

	//Initializes with the user's twitter name and the same admin
	User(String currUser,final Admin admin){
		this.currUser = currUser;
		creationTime = System.currentTimeMillis();
		lastUpdateTime = 0;
		//Initialize JFrame
		jfrm = new JFrame("User");
		jfrm.setSize(300,400);
		jfrm.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
	
		//Sets main panel
		JPanel mainPanel = new JPanel();
		mainPanel.setLayout(new GridLayout(2,1,7,7));
		mainPanel.setBackground(Color.LIGHT_GRAY);
		mainPanel.setBorder(new TitledBorder(currUser + " (Account created: " + creationTime + ")"));

		//Top and bottom parts of the main panel
		JPanel userTopJPanel = new JPanel();
		userTopJPanel.setLayout(new BorderLayout());
		JPanel userBottomJPanel = new JPanel();
		userBottomJPanel.setLayout(new BorderLayout());
		lastUpdateTimeLabel = new JLabel("Last Update Time: " + lastUpdateTime);
		
		
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
		tweetModel = new DefaultListModel<String>();
		followingModel = new DefaultListModel<String>();
		userID = new JTextArea("Enter Username");
		followUser = new JButton("Follow User");
		tweetMessage = new JTextArea("Enter Tweet");
		tweet = new JButton("Post Tweet");
		newsFeed = new JList<>(tweetModel = new DefaultListModel<>());
		followingList = new JList<>(followingModel);

		//Sets Dark Grey border
		Border simpleBorder = BorderFactory.createLineBorder(Color.DARK_GRAY);
		userID.setBorder(simpleBorder);
		tweetMessage.setBorder(simpleBorder);
		newsFeed.setBorder(simpleBorder);
		
		//Add in buttons
		userTopSubPanel.add(userID);
		userTopSubPanel.add(followUser);
		userTopSubPanel2.add(followingList);
		userBottomSubPanel2.add(newsFeed);
		userBottomSubPanel.setLayout(new BoxLayout(userBottomSubPanel, BoxLayout.Y_AXIS));
		userBottomSubPanel.add(lastUpdateTimeLabel, BorderLayout.NORTH);
		userBottomSubPanel.add(tweetMessage, BorderLayout.WEST);
		userBottomSubPanel.add(tweet, BorderLayout.EAST);
			
		//Adjust subpanels
		userTopJPanel.add(userTopSubPanel, BorderLayout.NORTH);
		userTopJPanel.add(userTopSubPanel2, BorderLayout.CENTER);
		userBottomJPanel.add(userBottomSubPanel,BorderLayout.NORTH);
		userBottomJPanel.add(userBottomSubPanel2, BorderLayout.CENTER);
			
		//Adjust subpanels
		userTopJPanel.add(userTopSubPanel, BorderLayout.NORTH);
		userTopJPanel.add(userTopSubPanel2, BorderLayout.CENTER);
		userBottomJPanel.add(userBottomSubPanel,BorderLayout.NORTH);
		userBottomJPanel.add(userBottomSubPanel2, BorderLayout.CENTER);
		
		//Add in subpanels to main panel
		mainPanel.add(userTopJPanel);
		mainPanel.add(userBottomJPanel);

		//Add main panel into the J Frame
		jfrm.add(mainPanel);
		
		//Tweet button
		tweet.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				String message = tweetMessage.getText();
				//Check if tweet is positive
				if(message.toLowerCase().contains("good") ||
					message.toLowerCase().contains("great") ||
					message.toLowerCase().contains("excellent"))
					positiveMessages += 1;

				//Add tweet into feed
				String userTweet = "- " + currUser + ": " + message;
				messages[totalMessages] = userTweet;
				totalMessages += 1;
				tweetModel.addElement(userTweet);
				newsFeed.repaint();
				//Notify followers of tweet and add it into their feed
				admin.notifyFollowers(userTweet, followers);
				// Update lastUpdateTimeLabel with the current time
				lastUpdateTime = System.currentTimeMillis();
				lastUpdateTimeLabel.setText("Last Update Time: " + lastUpdateTime);
			}
		});

		//Button to follow a user given their twitter name
		followUser.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				String followingUser = userID.getText();
				//Add to the list of following
				followingModel.addElement("- " + followingUser);
        		followingList.repaint();
				//Notify the admin to add the current user into their followers
				admin.updateFollowing(currUser, followingUser); //Update the user you followed that they now have another follower
			}
		});
	}
	//Observer Functions
	@Override
    public void update(String tweet) {
        // Handle the tweet update
        getTweetModel().addElement(tweet);
        getNewsFeed().repaint();
    }
	@Override
	public void accept(UserVisitor visitor) {
		visitor.visit(this);
	}

	//Helper Functions
	public void addFollower(String follower) {
        followers[numFollowers] = follower;
		numFollowers+=1;
    }
	public double getPositivePercentage() {
        if (totalMessages == 0) {
            return 0.0;
        }
        return ((double) positiveMessages / totalMessages) * 100.0;
    }
	//Getter functions
	public void setVisible() {jfrm.setVisible(true);}
	public int getTotalMessages() {return totalMessages;}
    public int getPositiveMessages() {return positiveMessages;}
	public String getUsername(){return currUser;}
	public JList<String> getNewsFeed(){return newsFeed;}
	public long getLatestUpdated(){return lastUpdateTime;}
	public DefaultListModel<String> getTweetModel(){return tweetModel;}
}