#include <iostream>
#include <vector>
#include <chrono>
#include <cmath>

using namespace std;

void computerMove();
const int SIZE = 8; //Board size
int b[SIZE][SIZE]; //Board is 8x8 
const int winValue = 5000; //Computer wins
const int loseValue = -5000; //Computer loses (human wins)
pair<int, pair<int, int>> alphaBetaPruning(int depth, int alpha, int beta, bool maximizingPlayer);
int evaluate();
int check4winner();
void checkGameOver();
void getPlayerMove();
void setup();
void printboard();

int main()
{
    cout <<"CS 4200 Project 3: 4-in-a-line" << endl;
    cout <<"------------------------------" << endl;
    setup();
    printboard();
    // Ask who will move first
    char choice;
    cout << "Who will move first? (H for human, C for computer): ";
    cin >> choice;
    if (toupper(choice) == 'H')
    {
        cout << "Human moves first!" << endl;
        printboard();
        while (true)
        {
            getPlayerMove();
            checkGameOver();
            computerMove();
            checkGameOver();
        }
    }
    else if (toupper(choice) == 'C')
    {
        cout << "Computer moves first!" << endl;
        printboard();
        while (true)
        {
            computerMove();
            checkGameOver();
            getPlayerMove();
            checkGameOver();
        }
    }
    else
    {
        cout << "Invalid choice! Please enter 'H' or 'C'." << endl;
    }

    return 0;
}
///Prints current board
void printboard()
{
    cout << "  1 2 3 4 5 6 7 8" << endl;
    char rowLabel = 'A';
    for(int i = 0; i < SIZE; i++)
    {
        cout << rowLabel << " ";
        for (int j = 0; j < SIZE; j++)
        {
            if (b[i][j] == 0) ///Represents dash "-"
                cout << "- ";
            else if (b[i][j] == 1)///Represents computer move "X"
                cout << "X ";
            else if (b[i][j] == 2)///Represents player move "O"
                cout << "O ";
        }
        cout << endl;
        rowLabel++;
    }
}
//Initializes board to be all dashes or 0s
void setup()
{
    for (int i = 0; i < SIZE; i++)
        for (int j = 0; j < SIZE; j++)
            b[i][j] = 0;
}
//Prompts player for their move and adds it into the board
void getPlayerMove()
{
    string move;
    cout << "Choose your next move: ";
    cin >> move;
    char rowChar = toupper(move[0]);
    int row = rowChar - 'A';
    int col = move[1] - '1';
    if (row >= 0 && row < SIZE && col >= 0 && col < SIZE && b[row][col] == 0 && move.size() == 2)
        b[row][col] = 2;   // Add the move to the moves vector
    else
    {
        cout << "Invalid move! Try again." << endl;
        getPlayerMove();  // Ask for input again if the move is invalid.
    }
}

//Evaluates current state of the board and returns an integer value of the current
//board's desirability for the MAX player (Computer)
//Higher value = favorable for computer
//Lower/negative value = favorable for human
int evaluate()
{
    int value = 0;
    //Evaluate rows for computer (MAX player) and player (MIN player)
    for (int i = 0; i < SIZE; i++)
    {
        //Iterate through the next 4 values as they are the only ones that matter currently
        for (int j = 0; j <= SIZE - 3; j++)
        {
            int countComputer = 0;
            int countPlayer = 0;
            int emptySpaces = 0; 

            for (int k = 0; k < SIZE; k++)
            {
                if (b[i][j + k] == 1) //Computer's move represented by 1
                    countComputer++;
                else if (b[i][j + k] == 2) //Player's move represented by 2
                    countPlayer++;
                else
                    emptySpaces++;
            }

            //Calculate points for different configurations
            if (countComputer == 2 && emptySpaces == 1)
                value += 10; //Two consecutive spaces with empty space after - Potential winning move

            if (countComputer == 3 && emptySpaces == 1)
                value += 50; //Three consecutive spaces with empty space after - Strong potential winning move

            if (countComputer == 4)
                value += 5000; //Computer wins - Maximize the value for immediate win

            if (countPlayer == 2 && emptySpaces == 1)
                value += 10; //Block two consecutive spaces - Prevent opponent's potential winning move

            if (countPlayer == 3 && emptySpaces == 1)
                value += 100; //Block three consecutive spaces - Prevent opponent's strong potential winning move

            if (countPlayer == 4)
                value += 5000; //Opponent has four consecutive pieces - Heavy penalty to avoid losing
        }
    }

    //Evaluate columns for computer (MAX player) and player (MIN player)
    for (int i = 0; i < SIZE; i++)
    {
        //Iterate through the next 4 values as they are the only ones that matter currently 
        for (int j = 0; j <= SIZE - 3; j++)
        {
            int countComputer = 0;
            int countPlayer = 0;
            int emptySpaces = 0; 

            for (int k = 0; k < SIZE; k++)
            {
                if (b[j + k][i] == 1) //Computer's move represented by 1
                    countComputer++;
                else if (b[j + k][i] == 2) //Player's move represented by 2
                    countPlayer++;
                else
                    emptySpaces++;
            }
            //Calculate points for different configurations
            if (countComputer == 2 && emptySpaces == 1)
                value += 10; //Two consecutive spaces with empty space after - Potential winning move

            if (countComputer == 3 && emptySpaces == 1)
                value += 50; //Three consecutive spaces with empty space after - Strong potential winning move

            if (countComputer == 4)
                value += 5000; //Computer wins - Maximize the value for immediate win

            if (countPlayer == 2 && emptySpaces == 1)
                value += 10; //Block two consecutive spaces - Prevent opponent's potential winning move

            if (countPlayer == 3 && emptySpaces == 1)
                value += 100; //Block three consecutive spaces - Prevent opponent's strong potential winning move

            if (countPlayer == 4)
                value += 5000; //Opponent has four consecutive pieces - Heavy penalty to avoid losing
        }
    }

    return value;
}

//Alpha-Beta Pruning Function
pair<int, pair<int, int>> alphaBetaPruning(int depth, int alpha, int beta, bool maximizingPlayer)
{
    //Get the current time before starting the evaluation
    auto startTime = std::chrono::high_resolution_clock::now();

    //Check if the maximum depth is reached or if the game is over
    int result = check4winner();
    if (depth == 0 || result != 0)
        return make_pair(evaluate(), make_pair(-1, -1));

    int bestRow = -1;
    int bestCol = -1;
    int bestValue;

    //Maximizing player (computer)
    if (maximizingPlayer)
    {
        bestValue = loseValue; //Set to lowest possible value to find the maximum

        //Loop through all possible moves in the board
        for (int i = 0; i < SIZE; i++)
        {
            for (int j = 0; j < SIZE; j++)
            {
                if (b[i][j] == 0)
                {
                    //Simulate the move
                    b[i][j] = 1;
                    //Recur for the next depth with a smaller alpha and beta
                    int value = alphaBetaPruning(depth - 1, alpha, beta, false).first;
                    // Undo the move
                    b[i][j] = 0;

                    if (value > bestValue)
                    {
                        bestValue = value;
                        bestRow = i;
                        bestCol = j;
                    }
                    //Alpha-beta pruning
                    alpha = max(alpha, bestValue);
                    if (alpha >= beta)
                        break;
                }
            }

            //Check if the elapsed time exceeds 5 seconds
            auto endTime = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::seconds>(endTime - startTime).count();
            if (duration >= 5)
            {
                // Return the best move found so far if time is already up
                return make_pair(bestValue, make_pair(bestRow, bestCol));
            }
        }
    }
    //Minimizing player (human)
    else
    {
        bestValue = winValue; //Set to highest possible value to find the minimum

        //Loop through all possible moves
        for (int i = 0; i < SIZE; i++)
        {
            for (int j = 0; j < SIZE; j++)
            {
                if (b[i][j] == 0)
                {
                    //Simulate the move
                    b[i][j] = 2;
                    //Recur for the next depth with a smaller alpha and beta
                    int value = alphaBetaPruning(depth - 1, alpha, beta, true).first;
                    // Undo the move
                    b[i][j] = 0;

                    if (value < bestValue)
                    {
                        bestValue = value;
                        bestRow = i;
                        bestCol = j;
                    }

                    // Alpha-beta pruning
                    beta = min(beta, bestValue);
                    if (alpha >= beta)
                        break;
                }
            }
            //Check if the elapsed time exceeds 5 seconds
            auto endTime = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::seconds>(endTime - startTime).count();
            if (duration >= 5)
            {
                //Return the best move found so far if time is already up
                return make_pair(bestValue, make_pair(bestRow, bestCol));
            }
        }
    }
    //Return the best move found
    return make_pair(bestValue, make_pair(bestRow, bestCol));
}

//Function for computer to make its move 
void computerMove()
{
    //Get 5 moves in as trial value
    int maxDepth = 5;
    int alpha = loseValue; 
    int beta = winValue;

    //Call alphaBetaPruning function to get the best score and best move possible within
    //time frame of 5 seconds
    pair<int, pair<int, int>> result = alphaBetaPruning(maxDepth, alpha, beta, true);

    int bestRow = result.second.first;
    int bestCol = result.second.second;

    char rowChar = 'A' + bestRow;//Converts move into char form 
    //Print the computer's final move
    cout << "Computer Move: " << rowChar << "" << bestCol + 1 << endl;
    b[bestRow][bestCol] = 1; //Make the best move found
}
///Checks all rows and columns if there is a winning 4 combination of consecutive X's or 0's
int check4winner()
{
    int n = 8; //Size of the board
    //Check rows for a winner
    for (int i = 0; i < n; i++)
        for (int j = 0; j <= n - 4; j++)
        {
            if ((b[i][j] == 1) && (b[i][j + 1] == 1) && (b[i][j + 2] == 1) && (b[i][j + 3] == 1))
                return winValue; //Computer wins
            if ((b[i][j] == 2) && (b[i][j + 1] == 2) && (b[i][j + 2] == 2) && (b[i][j + 3] == 2))
                return loseValue; //Player wins
        }

    //Check columns for a winner
    for (int i = 0; i < n; i++)
        for (int j = 0; j <= n - 4; j++)
        {
            if ((b[j][i] == 1) && (b[j + 1][i] == 1) && (b[j + 2][i] == 1) && (b[j + 3][i] == 1))
                return winValue; //Computer wins
            if ((b[j][i] == 2) && (b[j + 1][i] == 2) && (b[j + 2][i] == 2) && (b[j + 3][i] == 2))
                return loseValue; //Player wins
        }

    //Check for a draw
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (b[i][j] == 0)
                return 0; //Game is not over, there are still empty cells

    return 1; //Draw, the board is full
}

///Calls check4winner() to see type of game ending, if not over then break and exit
void checkGameOver()
{
    printboard();
    int result = check4winner();
    switch (result)
    {
        case loseValue:
            cout << "You win! \nGame Over!" << endl;
            exit(0);
            break;
        case winValue:
            cout << "Computer wins! \nGame Over!" << endl;
            exit(0);
            break;
        case 1:
            cout << "Draw, board is full. \nGame Over!" << endl;
            exit(0);
            break;
        default:
            break;
    }
}
