package a2;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Map;

import javax.swing.*;
import javax.swing.border.Border;
import javax.swing.border.TitledBorder;
import javax.swing.event.TreeSelectionEvent;
import javax.swing.event.TreeSelectionListener;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import javax.swing.tree.TreePath;

public class Admin {

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

	//Map to store followers for each user
    private Map<String, DefaultListModel<String>> followersMap;

	//Method to get the Singleton instance
    public static Admin getInstance() {
        if (instance == null) {
            instance = new Admin();
            // Additional setup if needed
        }
        return instance;
    }
	//Notify followers about the new tweet
    public void notifyFollowers(User user, String tweet) {
        String username = user.getUsername();
        // Update the news feed of each follower
        if (followersMap.containsKey(username)) {
            DefaultListModel<String> followerListModel = followersMap.get(username);
            for (int i = 0; i < followerListModel.getSize(); i++) {
                String followerName = followerListModel.getElementAt(i);
                for (int j = 0; j < numUsers; j++) {
                    if (userObjects[j].getUsername().equals(followerName)) {
                        userObjects[j].getTweetModel().addElement(tweet);
                        userObjects[j].getNewsFeed().repaint();
                        break;
                    }
                }
            }
        }
    }
	//Private constructor to enforce Singleton pattern
	private Admin()
	{
		//Initialize instance variabels
		users = new String[100];
		groups = new String[100];
		userObjects = new User[100];
		numUsers = 0;
		numGroups = 0;
		followersMap = new HashMap<>();
	}
	private void setupGUI(){
		//Sets JFrame
		JFrame jfrm = new JFrame("Admin");
		jfrm.setSize(800,400);
		jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Border simpleBorder = BorderFactory.createLineBorder(Color.BLACK);
		//Create main panel
		JPanel mainPanel = new JPanel();
		mainPanel.setBorder(new TitledBorder("Admin"));
		mainPanel.setLayout(new GridLayout(1,2,7,7)	);
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
		userID = new JTextArea("User Id");
		groupId = new JTextArea("Group Id");
		addUser = new JButton("Add User");
		addGroup = new JButton("Add Group");
		userID.setBorder(simpleBorder);
		groupId.setBorder(simpleBorder);
		treeConfig.add(userID);
		treeConfig.add(addUser);
		treeConfig.add(groupId);
		treeConfig.add(addGroup);
		
		JPanel userView = new JPanel();
		userView.setLayout(new BorderLayout());
		openUserView = new JButton("Open User View");
		userView.add(openUserView, BorderLayout.NORTH);
		
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
		
		addUser.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				DefaultMutableTreeNode selectedNode = (DefaultMutableTreeNode) tree.getLastSelectedPathComponent();
				if (selectedNode == null) {
	                    selectedNode = treeRoot;
	            }
				
				// Check for duplicate users
				for (int i = 0; i < numUsers; i++) {
					if (users[i] != null && users[i].equals(userID.getText())) {
						JOptionPane.showMessageDialog(null, "User ID already exists. Please choose a different ID.");
						return;
					}
				}
				
				DefaultMutableTreeNode newNode = new DefaultMutableTreeNode(userID.getText());
				selectedNode.add(newNode);
				
				
				userObjects[numUsers] = new User(userID.getText(), Admin.this);//Pass same Admin instance to User
				users[numUsers] = userID.getText();
				numUsers += 1;

				DefaultTreeModel model = (DefaultTreeModel)tree.getModel();
	            model.nodeStructureChanged(selectedNode);
	            
	            TreePath path = new TreePath(newNode.getPath());
                tree.expandPath(path);
                
                tree.setSelectionPath(null);
			}
		});
		
		addGroup.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				DefaultMutableTreeNode selectedNode = treeRoot;
				
				for (int x = 0; x < numGroups; x++) {
		            if (groups[x].equals(groupId.getText())) {
		                return;
		            }
		        }
				
				DefaultMutableTreeNode newNode = new DefaultMutableTreeNode(groupId.getText());
				selectedNode.add(newNode);
				
				groups[numGroups] = groupId.getText();
				numGroups += 1;
				
				DefaultTreeModel model = (DefaultTreeModel) tree.getModel();
	            model.nodeStructureChanged(selectedNode);
	            
	            TreePath path = new TreePath(newNode.getPath());
                tree.expandPath(path);
                
                tree.setSelectionPath(null);
			}
		});
		
		showUserTotal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				System.out.print("Number of users: " + numUsers + "\n");
			}
		});
		
		showGroupTotal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				System.out.print("Number of groups: " + numGroups + "\n");
			}
		});
			
		openUserView.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				DefaultMutableTreeNode selected = (DefaultMutableTreeNode)tree.getLastSelectedPathComponent();
				if (selected != null) {
					for(int i = 0; i < numUsers; i++) {
						if(users[i] != null && users[i].equals(selected.toString()))
							userObjects[i].setVisible();
					}
				}
				return;
			}
		});
		showMessagesTotal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ae) {
				int totalMessages = 0;
				for (int i = 0; i < numUsers; i++) {
					totalMessages += userObjects[i].getTotalMessages();
				}
				JOptionPane.showMessageDialog(null, "Total number of Tweet messages: " + totalMessages);
			}
		});
		
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
