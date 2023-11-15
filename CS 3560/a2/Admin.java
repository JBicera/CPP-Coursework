///Name: Joshua Bicera
/// I don't know why but when I compile the code it makes like 10 .class files
/// It is annoying but my code still works
package a2;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.lang.String;
import java.util.ArrayList;
import java.util.List;

import javax.swing.*;
import javax.swing.border.Border;
import javax.swing.border.TitledBorder;
import javax.swing.event.TreeSelectionEvent;
import javax.swing.event.TreeSelectionListener;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import javax.swing.tree.TreePath;

//Subject(Observer) interface
interface Subject {
    void registerObserver(Observer observer);
    void notifyObservers(String tweet);
}
//Visitor Interface
interface UserVisitor
{
	void visit(User user);
}


public class Admin implements Subject, UserVisitor {

	private static Admin instance;  // Singleton instance
	

	//Instance Variables
	private DefaultMutableTreeNode treeRoot;
	private JTextArea userID;
	private JTextArea groupId;
	private String[] users;
	private String[] groups;
	private User[] userObjects;
	private int numUsers;
	private int numGroups;
	private List<Observer> observers;

	//Create buttons
	private JButton addUser;
	private JButton addGroup;
	private JButton openUserView;
	private JButton showUserTotal;
	private JButton showMessagesTotal;
	private JButton showGroupTotal;
	private JButton showPositivePercentage;
	
	//Display data in a hiearchal tree
	private JTree tree;

	//Method to get the single instance of Admin
    public static Admin getInstance() {
        if (instance == null) {
            instance = new Admin();
        }
        return instance;
    }
	//Observer pattern methods
    @Override
	//Adds new users into the list of observers.
	//This method follows to the Observer pattern by allowing users to register themselves
	//as observers. When a new user is created or added to the system, they register as an
	//observer to receive updates about tweets.
    public void registerObserver(Observer observer) {
        observers.add(observer);
    }

	//No need to remove observers as there are no need to remove users

    @Override
	//This method follows the Observer pattern by iterating through the list of registered
	//observers and notifying each of them about the new tweet. Each observer (user) is
	//expected to implement the update method to handle the received tweet.
    public void notifyObservers(String tweet) {
        for (Observer observer : observers) {
            observer.update(tweet);
        }
    }

	//Visitor Pattern method
	@Override
	//When the program needs to visit a user, it opens up their individual GUI.
	//This method adheres to the Visitor pattern, where the Admin (visitor) can visit
	//individual User objects. In this case, when the Admin visits a User, it triggers
	//the opening of the User's individual GUI, allowing the Admin to interact with
	//and view details specific to that User.
	public void visit(User user)
	{
		user.setVisible();
	}


	//Update following in the admin
    public void updateFollowing(String currUser, String followingUser) {
        for (int i = 0; i < userObjects.length; i++) {
			//Find the user being followed
            if (userObjects[i] != null && userObjects[i].getUsername().equals(followingUser)) {
                userObjects[i].addFollower(currUser); //Add the current user to their following
                break;
            }
        }
    }
	//Notify followers about the new tweet
	public void notifyFollowers(String tweet, String[] followers) {
		// Update the news feed of each follower
		for (String follower : followers) {
			for (User user : userObjects) {
                // Iterate through all Users and find the follower
                if (user != null && user.getUsername().equals(follower)) {
                    user.update(tweet); // Notify followers
					break;
                }
            }
		}
	}
	//Singleton Pattern
	//The private constructor ensures that only one instance of the Admin class can be created.
	//This is a key aspect of the Singleton pattern, where a class has only one instance, and
	//provides a global point of access to that instance. This is important for the program
	//as there is only one admin that controls and holds all other users and is the root at which
	//all user interaction takes place
	private Admin()
	{
		//Initialize instance variabels
		users = new String[10];
		groups = new String[10];
		userObjects = new User[10];
		numUsers = 0;
		numGroups = 0;
		 observers = new ArrayList<>();
	}

	//Method to setup and deploy the GUI
	private void setupGUI(){
		//Sets JFrame
		JFrame jfrm = new JFrame("Admin");
		jfrm.setSize(600,350);
		jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		//Create main panel
		Border simpleBorder = BorderFactory.createLineBorder(Color.DARK_GRAY);
		JPanel mainPanel = new JPanel();
		mainPanel.setBorder(new TitledBorder("Mini Twitter"));
		mainPanel.setBackground(Color.LIGHT_GRAY);
		mainPanel.setLayout(new GridLayout(1,2,7,7));

		//Create tree panel
		JPanel treePanel = new JPanel();
		treePanel.setBorder(new TitledBorder("Tree View"));
		treeRoot = new DefaultMutableTreeNode("Root");
		tree = new JTree(treeRoot);
		treePanel.setBorder(simpleBorder);
		treePanel.add(tree);

		//Create config panel
		JPanel configPanel = new JPanel();
		configPanel.setLayout(new BorderLayout());
		JPanel treeConfig = new JPanel();
		treeConfig.setLayout(new GridLayout(2,2,5,5));
		userID = new JTextArea("User ID");
		groupId = new JTextArea("Group ID");
		addUser = new JButton("Add User");
		addGroup = new JButton("Add Group");
		userID.setBorder(simpleBorder);
		groupId.setBorder(simpleBorder);
		treeConfig.add(userID);
		treeConfig.add(addUser);
		treeConfig.add(groupId);
		treeConfig.add(addGroup);
		
		//User view for individual users
		JPanel userView = new JPanel();
		userView.setLayout(new BorderLayout());
		openUserView = new JButton("Open User View");
		userView.add(openUserView, BorderLayout.NORTH);
		
		//Buttons for stats of the mini-twitter
		JPanel showStats = new JPanel();
		showStats.setLayout(new GridLayout(2,2,5,5));
		showUserTotal = new JButton("Show User Total");
		showMessagesTotal = new JButton("Show Messages Total");
		showGroupTotal = new JButton("Show Group Total");
		showPositivePercentage = new JButton("Show Positive Percentage");
		showStats.add(showUserTotal);
		showStats.add(showMessagesTotal);
		showStats.add(showGroupTotal);
		showStats.add(showPositivePercentage);

		configPanel.add(treeConfig, BorderLayout.NORTH);
		configPanel.add(userView);
		configPanel.add(showStats, BorderLayout.SOUTH);
		mainPanel.add(treePanel, BorderLayout.WEST);
		mainPanel.add(configPanel, BorderLayout.EAST);	


		//Open user's view button
		openUserView.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				DefaultMutableTreeNode selectedNode = (DefaultMutableTreeNode)tree.getLastSelectedPathComponent();
				if(selectedNode != null) {
					//Find User Object and then open it
					for(int i = 0; i < numUsers; i++) {
						if(users[i] != null && users[i].equals(selectedNode.toString()))
							visit(userObjects[i]);
					}
				}
				return;
			}
		});

		//Add User Button
		addUser.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				DefaultMutableTreeNode selectedNode = (DefaultMutableTreeNode) tree.getLastSelectedPathComponent();
				if (selectedNode == null) {
	                    selectedNode = treeRoot;
	            }
				//Check if the user alread exists
				for (int i = 0; i < numUsers; i++) {
					if (users[i] != null && users[i].equals(userID.getText())) {
						JOptionPane.showMessageDialog(null, "User ID already exists. Please choose a different ID.");
						return;
					}
				}

				//Add onto the tree
				DefaultMutableTreeNode newNode = new DefaultMutableTreeNode(userID.getText());
				selectedNode.add(newNode);

				//Create a new user
				userObjects[numUsers] = new User(userID.getText(), Admin.getInstance());//Pass same Admin instance to User
				users[numUsers] = userID.getText();
				//Register as observer
				Admin.getInstance().registerObserver(userObjects[numUsers]);
				numUsers += 1;

				//Update tree
				DefaultTreeModel model = (DefaultTreeModel)tree.getModel();
	            model.nodeStructureChanged(selectedNode);
	            TreePath path = new TreePath(newNode.getPath());
                tree.expandPath(path);
                tree.setSelectionPath(null);
			}
		});

		//Add Group Button
		addGroup.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				DefaultMutableTreeNode selectedNode = treeRoot;
				for (int x = 0; x < numGroups; x++) {
		            if (groups[x].equals(groupId.getText())) {
		                return;
		            }
		        }
				//Add Group node
				DefaultMutableTreeNode newNode = new DefaultMutableTreeNode(groupId.getText());
				selectedNode.add(newNode);

				//Update counters
				groups[numGroups] = groupId.getText();
				numGroups += 1;

				//Update Tree
				DefaultTreeModel model = (DefaultTreeModel) tree.getModel();
	            model.nodeStructureChanged(selectedNode);
	            TreePath path = new TreePath(newNode.getPath());
                tree.expandPath(path);
                tree.setSelectionPath(null);
			}
		});
		
		//Show number of users button
		showUserTotal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				JOptionPane.showMessageDialog(null, "Number of users: " + numUsers);
			}
		});
		
		//Show number of groups button
		showGroupTotal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				JOptionPane.showMessageDialog(null, "Number of groups: " + numGroups);
			}
		});
		
		//Show total number of messages button
		showMessagesTotal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				int totalMessages = 0;
				for (int i = 0; i < numUsers; i++) {
					totalMessages += userObjects[i].getTotalMessages(); //Add all tweets form each user
				}
				JOptionPane.showMessageDialog(null, "Total number of Tweet messages: " + totalMessages);
			}
		});
		
		//Show the ratio/percentage of "good" tweets
		showPositivePercentage.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				int positiveMessages = 0;
				int totalMessages = 0;
				for (int i = 0; i < numUsers; i++) {
					positiveMessages += userObjects[i].getPositiveMessages();
					totalMessages += userObjects[i].getTotalMessages();
				}
				double percentage = totalMessages > 0 ? (double) positiveMessages / totalMessages * 100 : 0.0;
				JOptionPane.showMessageDialog(null, "Positive Percentage: " + percentage + "%");
			}
		});

		//Sets up tree display
		//This method follows the Composite Pattern by treating the tree nodes uniformly,
		//where both individual users (leaf nodes) and groups (composite nodes) are considered.
		//The method checks the selected node in the tree, enabling or disabling buttons
		//based on the type of node selected:
		// - If no node is selected, both "Add User" and "Add Group" buttons are disabled.
		// - If the selected node is the root, both "Add User" and "Add Group" buttons are enabled.
		// - If the selected node is a group, only the "Add User" button is enabled.
		tree.addTreeSelectionListener(new TreeSelectionListener() {
            public void valueChanged(TreeSelectionEvent e) {
            	DefaultMutableTreeNode selectedNode = (DefaultMutableTreeNode) tree.getLastSelectedPathComponent();
                if (selectedNode == null) {
                    addUser.setEnabled(false);
                    addGroup.setEnabled(false);
                } else if (selectedNode.toString().equals("Root")) {
                    addUser.setEnabled(true);
                    addGroup.setEnabled(true);
                } else {
                    addUser.setEnabled(false);
                    addGroup.setEnabled(false);
                    for (int x = 0; x < numGroups; x++) {
                        if (groups[x].equals(selectedNode.toString())) {
                            addUser.setEnabled(true);
                            break;
                        }
                    }
                }
            }
        });
		jfrm.add(mainPanel);
		jfrm.setVisible(true);
	}

	public static void main(String[] args) {
		SwingUtilities.invokeLater(() -> {
			Admin admin = Admin.getInstance();
			admin.setupGUI();
		});
	}

}
