Projest 2 Readme eeg 
Version 1 9/11/24
A single copy of this template should be filled out and submitted with each project submission, regardless of the number of students on the team. It should have the name readme_”teamname”
Also change the title of this template to “Project x Readme Team xxx”
1	Team Name:	 eeg
2	Team members names and netids
Eve goodrow
egoodrow
3	Overall project attempted, with sub-projects:
NTM Trace
4	Overall success of the project:
The project was very successful! I was able to showcase an NTM solver and how it operates on multiple inputs. I also added extra printing to really understand the tree being build using breadth first search. This helped me in my analysis of what was happening in the code behind the scenes. 
5	Approximately total time (in hours) to complete:

10
6	Link to github repository: https://github.com/egoodrow6/Project1-TOC 

7	List of included files (if you have many files of a certain type, such as test files of different sizes, list just the folder): (Add more rows as necessary). Add more rows as necessary.

File/folder Name	File Contents and Use
Code Files
ntm_tracer.py	All the code that I worked on. Used to parse input files, create breadth first search tree simulation, produces and output of either accept, reject, or timeout, prints this to the terminal.
Test Files
aplus.csv	Test case use “aaa” (accept)
-	All test files are explained more below
abc_star.csv
	-	Test case I used – “bbba” reject and “aaabbc” accept

exactlyA.csv	-	Test case used – bbba accept and bbbaa reject

palindrom.csv	-	Test case used – aaaaaa with max_depth 100

equal_10s.csv	-	Test case used – $0101010101

Output Files
None – output prints to terminal	
Plots (as needed)
 	Screenshot of abc_star
 	Screenshot of exactly1A
 	Screenshot of aplus

 	Screenshot of palindrome

8	Programming languages used, and associated libraries:
Python
Libraries: csv, sys, argparse
9	Key data structures (for each sub-project):
-	Configurations – [left_tape, current_state, right_tape, parent_config]
-	BFS tree
-	Visited set
-	Lists
10	General operation of code (for each subproject)

This program is designed to simulate a nondeterministic Turing Machine using breadth first search tree traversal of all possible configurations. The results I saw were as follows
-	The code explored all possible computation branches up to max_depth input by the user
-	If a branch reaches the accept_state, it prints a success message and backtracks through the tree to display the trace path from the start state to the accept state
-	If all branches at a given level reject, meaning no valid move exists, the machine stops and prints a rejection message
-	If max_depth is reached without finding an accept state, the code stops and prints a timeout message


11	What test cases you used/added, why you used them, what did they tell you about the correctness of your code.
I used the testcases 

Nondeterminism test – aplus.csv
-	Test case use “aaa” (accept)
-	Why this test: this was the baseline test to verify the core nondeterminism feature: splitting into multiple branches. The machine must simultaneously loop and guess the end on the same input character
-	This test confirmed that my BFS implementation correctly generates multiple child configurations from a single parent. It also verified that the execution trace correctly identifies the single successful path out of many failed branches, proving the backtracking logic works


Patter recognition test – abc_star.csv
-	Test case I used – “bbba” reject and “aaabbc” accept
-	Why this test: test machine’s ability to handle complex regular expressions and enforce character ordering
-	This test verified the rejection logic

The State Memory test – exactlyA.csv
-	Test case used – bbba accept and bbbaa reject
-	Why this test: to test if the simulator could track state history correctly. Remember if it’s seen an a by changing states
-	This test told me that state transitions update correctly along the path by rejecting bbbaa

The complexity and depth test – palindrom.csv
-	Test case used – aaaaaa with max_depth 100
-	Why this test: requires zig zag movement creates a VERY deep execution tree. Stress test the BFS loop and the max_depth parameter
-	Initially, this test failed (timed out) at 20 steps, which revealed that my BFS was working but simply needed more depth for complex algorithms. I increased the depth to 100 which allowed it to finish

12	How you managed the code development

First, I started going step by step through the TODO section steps. Thankfully, they were very clearly layed out (up until step 6). The first 5 steps explain what we are supposed to do in great detail and allowed me to get a feel for what I was going to have to do/which variables I needed to keep track of for the future. When it came time for step 6, I started on a large scale and slowly iterated my approach until it worked! This was when I had to pull out a paper and pen a few times to actually draw out what was happening on the tape to understand where I was going wrong. I used the testcases and MANY print statements to debug my logic. I had a few issues with how I was reading/accessing the input files, but once that was resolved, the logic was sound and my program worked!


13	Detailed discussion of results:

The output clearly shows the progression of the machine through levels of the BFS tree, including the left tape, current state, head symbol, and remaining right tape, making it easy to debug and understand the NTM’s operation. The results were in line with what I predicted, a string input that followed the definition of the NTM described in the input was accepted in a certain number of steps, while the others either timed out or were rejected.


14	How team was organized 
Just me 
15	What you might do differently if you did the project again
If I did the project again I would have wanted to think through the logic very soundly before coding. I think the many documents devoted to understanding how the NTM works were really helpful, but I would’ve liked to first write out on paper what I wanted my output to be for a given input, rather than starting to implement code right away. That would have saved me from some debugging in the end
16	Any additional material:

<img width="468" height="641" alt="image" src="https://github.com/user-attachments/assets/20238465-8a6c-4206-a983-3c512b69d120" />
