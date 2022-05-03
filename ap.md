# AP Test Prep 

## Practice Test #3
Score: 47/50

### Q3
Answer: II only
My answer: I only
Explanation: Correct. Algorithm I does not work correctly. In algorithm I, if two people are tied for the earliest birthday, they both sit down when they are eventually paired. Algorithm II works correctly. Because algorithm II allows both people to remain standing when there is a tie, a person with the earliest birthday is not eliminated. Algorithm II continues until all remaining people have the same birthday, which is the earliest birthday. Algorithm III does not work correctly. Algorithm III chooses the person(s) with the earliest day, disregarding the month. For example, algorithm III will incorrectly determine that a person born on February 1 has an earlier birthday than a person born on January 5.

### Q18
Answer: [1, 2, 3]
My answer: [-1, 0, 1]
Explanation: The procedure traverses this list and eventually encounters the positive value 1. At this point, the procedure returns true when it should return false because the list does not contain only positive values.

### Q32 
A computer program uses 4 bits to represent nonnegative integers. Which of the following statements describe a possible result when the program uses this number representation?

I. The operation 4 plus 8 will result in an overflow error.

II. The operation 7 plus 10 will result in an overflow error.

III. The operation 12 plus 3 will result in an overflow error.

Answer: II only
My answer: II and III only
Explanation: The operation 10 plus 7 causes an overflow error, but 12 plus 3 does not produce a result large enough to cause an overflow error.





# Week 1 Reflection:

This week I started reviewing Big Idea 1 and 2, and watched some of the AP Exam daily videos to help refresh my knowledge. I learned about collaboration and the fundamental principles of coding. I was able to understand it well and did the practice questions successfully



## Practice Test #2

Score: 44/50

### Q14: A file storage application allows users to save their files on cloud servers. A group of researchers gathered user data for the first eight years of the application’s existence. Some of the data are summarized in the following graphs. The line graph on the left shows the number of registered users each year. The line graph on the right shows the total amount of data stored by all users each year. The circle graph shows the distribution of file sizes currently stored by all users. Which of the following best describes the average amount of data stored per user for the first eight years of the application’s existence?

Answer: A : Across all eight years, the average amount of data stored per user was about 10 GB.
My answer: C: The average amount of data stored per user appears to increase by about 10 GB each year.
Explanation: Correct. The two line graphs are roughly the same shape. Each value on the right line graph is about 10 times the corresponding value on the left line graph. Therefore, the average amount of data stored per user is about 10 GB.


 





## Practice Test #1 4/20

Score: 49/50


### Q4:  ASCII characters can also be represented by hexadecimal numbers. According to ASCII character encoding, which of the following letters is represented by the hexadecimal (base 16) number 56?

Answer: V, because the hex number 56 converts to 86 in decimal. In the hex number, 6 is multiplied by 16^0, since it's in that place. 5 is multiplied by 16^1, so 5 times 16 is 80. Adding the two numbers together, we get 6 + 80 = 86. V corresponds to 86 in decimal.


### Q21: Which of the following best describes the relationship between the World Wide Web and the Internet?

Answer: C (The World Wide Web is a system of linked pages, programs, and files that is accessed via a network called the Internet.)
My answer: The World Wide Web is a system of linked pages, programs, and files that is accessed using a data stream called the Internet.
Explanation: The internet is not a data stream. It is a network.


### Q23: Which of the following has the greatest potential for compromising a user’s personal privacy?
Options: A)A group of cookies stored by the user’s Web browser
         B) The Internet Protocol (IP) address of the user’s computer
         C)Email address
         D) User's public key

Answer: A 
My answer: B
Explanation: Browser cookies can track information about users on different websites. IP address doesn't have any extra info about user.


### Q29: In order to test the program, the programmer initializes numList to [0, 1, 4, 5]. The program displays 10, and the programmer concludes that the program works as intended.Which of the following is true?
Correct answer: The conclusion is incorrect; using the test case [0, 1, 4, 5] is not sufficient to conclude the program is correct.
My answer: The conclusion is correct; the program works as intended.
Explanation: Because the variable sum is initialized to store the value of the first element of numList, and because the iteration block is a FOR EACH loop, the value of the first element is added to sum twice. Since the first element of the list is 0, adding this number to the sum does not affect the sum. A non-zero first element would give an incorrect result. In general, a single test case is not sufficient to confirm that a program works as intended.
A different test case with no zero in the list doesn't give correct sum.


### Q37: The following code segment is intended to set max equal to the maximum value among the integer variables x, y, and z. The code segment does not work as intended in all cases. Which of the following initial values for x, y, and z can be used to show that the code segment does not work as intended?
Correct answer: x = 3, y = 2, z = 1
My answer: x = 2, y = 3, z = 1
Explanation: The values work for the top half of the code, but for the bottom half, the else statement makes it so that it displays z as the max in addition to x.


### Q50: Digital images are often represented by the red, green, and blue values (an RGB triplet) of each individual pixel in the image. A photographer is manipulating a digital image and overwriting the original image. Which of the following describes a lossless transformation of the digital image?
Correct answer: Creating the negative of an image by creating a new RGB triplet for each pixel in which each value is calculated by subtracting the original value from 255. The negative of an image is reversed from the original; light areas appear dark, and colors are reversed.
My answer: Modifying part of the image by taking the pixels in one part of the picture and copying them to the pixels in another part of the picture.
Explanation: If a negative of the original image is made, each RGB triplet value will be computed by subtracting the original value from 255. The original value can then be restored by subtracting the new value from 255. This process is lossless because the exact original can be restored. The option I chose is still changing the original picture.











