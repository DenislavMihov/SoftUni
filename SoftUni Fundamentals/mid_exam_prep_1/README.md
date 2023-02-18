1.	Bonus Scoring System

Create a program that calculates bonus points for each student enrolled in a course. On the first line, you are going to receive the number of students. On the second line, you will receive the total number of lectures in the course. The course has an additional bonus, which you will receive on the third line. On the following lines, you will be receiving the count of attendances for each student.
The bonus is calculated with the following formula:
{total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
Find the student with the maximum bonus and print them, along with his attendance, in the following format:
"Max Bonus: {max bonus points}."
"The student has attended {student attendances} lectures."
Round the bonus points at the end to the nearest larger number.
Input / Constraints

•	On the first line, you are going to receive the number of the students – an integer in the range [0…50]

•	On the second line, you will receive the number of the lectures – an integer number in the range [0...50].

•	On the third line, you will receive the additional bonus – an integer number in the range [0….100].

•	On the following lines, you will be receiving the attendance of each student.

•	There will never be students with equal bonuses.

Output

•	Print the maximum bonus points and the attendances of the given student, rounded to the nearest larger number, scored by a student in this course in the format described above.

2.	Shopping List

It's the end of the week, and it is time for you to go shopping, so you need to create a shopping list first.

Input

You will receive an initial list with groceries separated by an exclamation mark "!".

After that, you will be receiving 4 types of commands until you receive "Go Shopping!".

•	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.

•	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this command.

•	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one. Otherwise, skip this command.

•	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end of the list. Otherwise, skip this command.

Constraints

•	There won't be any duplicate items in the initial list

Output

•	Print the list with all the groceries, joined by ", " :
"{firstGrocery}, {secondGrocery}, … {nthGrocery}"

3.	Man O War


The pirates encounter a huge Man-O-War at sea. 
Create a program that tracks the battle and either chooses a winner or prints a stalemate. On the first line, you will receive the status of the pirate ship, which is a string representing integer sections separated by ">". On the second line, you will receive the same type of status, but for the warship: 
"{section1}>{section2}>{section3}… {sectionn}"

On the third line, you will receive the maximum health capacity a section of the ship can reach. 

The following lines represent commands until "Retire":

•	"Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section. Check if the index is valid and if not, skip the command. If the section breaks (health <= 0) the warship sinks, print the following and stop the program: "You won! The enemy ship has sunken."

•	"Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that range (indexes are inclusive). Check if both indexes are valid and if not, skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
"You lost! The pirate ship has sunken."

•	"Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. Check if the index is valid and if not, skip the command. The health of the section cannot exceed the maximum health capacity.

•	"Status" - prints the count of all sections of the pirate ship that need repair soon, which are all sections that are lower than 20% of the maximum health capacity. Print the following:
"{count} sections need repair."

In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, in the following format:

"Pirate ship status: {pirateShipSum}

Warship status: {warshipSum}"

4.	Input

•	On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')

•	On the 2nd line, you are going to receive the status of the warship

•	On the 3rd line, you will receive the maximum health a section of a ship can reach.

•	On the following lines, until "Retire", you will be receiving commands.

5.	Output

•	Print the output in the format described above.

6.	Constraints

•	The section numbers will be integers in the range [1….1000]

•	The indexes will be integers [-200….200]

•	The damage will be an integer in the range [1….1000]

•	The health will be an integer in the range [1….1000]

