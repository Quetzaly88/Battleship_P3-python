# Battleship-P3
 
Project 3
Code Institute

    This project has the workspace template from Code Institute. It's a simple battleship game using exclusively Python code. This game includes: two board, one for the computer and one for a user. Ten oportunities to guess wand hit where the computer's ships are and a track of hits and misses. At the end a message "Game Over" will be printed and the hits, misses and Ships that were in the board will be shown. 

![mockup](./assets/images/mockup.webp)


DESIGN

There is no special design for this project because it's been exxlusiveky focused on Python the language and its functionality. The background color is only taken from the Code Institute template for this project. 


WIREFRAMES / FLOWCHART

    In this project I've usedcreated the flowchart using draw.io. The flowchart shows in resume the steps taken to acconplish the battle game and be functional. 

![flowchart](./assets/images/flowchart.webp)



FEATURES

* The two game boards:

    In the beginning we have the two game boards. One for the user and the another for the computer.  
    The columns are marked with letters and the rows with numbers 0-4. Here I used just five rows and five columns to make the game easier. 

    The user board has "S" that means where the ships are. 

![user board](./assets/images/tom_board.webp)

    The computer board has the ships hidden and the user has to guess where the ships are. 

![computer board](./assets/images/computer_board.webp)

    While the game is running, there will be a message saying "Take your chance and guess where is a battleship. 
    The user has to introduce the write information otherwise an error message is shown. 
    In the case that the player introduces other numbers that are not between 0-4 or letters that are not 'ABCDE'
    the error message will say "Try again, insert numbers between 0-4 and letters between 'ABCDE'!"

![error message](./assets/images/error%20message-insert-again.webp)

    The user has 10 turns until the ships are founded. If all the turns are finished the "Game Over" message will show. 


FUTURE IMPLEMENTATIONS: 

    ACCESIBILITY

    The page is easy to read and understand. The user will be able to restart the game using the button "run program".

    No other colors or fonts were used. 



TECHNOLOGIES USED


* Languages Used:

    I'm learning Python and this project is exclusively in that language.
    Gitpod it's been used for writing code and heroku for deployment. 
   

* Testing

    - The two boards for user and computer are seen in the screen.  
    - The site is avaiable and readable in on all devices. 
    - No errors of indentation were found in "CI Python Linter"
    - In "One Compiler" code tester appears a message "Error: Command failed: timeout 7 python3 main. 
      py". It's an error that doesn't appear as a big issue. The bugs section in README will cover more of this. 
    


![CI lintern TEST](./assets/images/CI%20lintern.webp)


![One compiler tester](./assets/images/tester.webp)


    - The lighthouse open source from Chrome ensures that this website is not only fast and efficient but also accessible, SEO-friendly, and adhering to best practices.
    - The error shown in "One Compiler", "Error: Command failed: timeout 7 python3 main.py" indicates that the script main.py was terminated because it did not complete within the specified timeout of 7 seconds. This error typically occurs when the script takes too long to execute. For this issue I have not any other option that just let it be. I need more advanced code to extend a time period for the input. 


![LIGHTHOUSE TEST](./assets/images/lighthouseebattleship.webp)



* Bugs

    The biggest mistake I did was to not use the correct indentation. Then I realized that my project was not running but the tutors helped me. 
    I still wish to have less functions to avoid repetition but I just need to learn more python to use Refactoring. After this project I will learn more about it. 

    Some other problems that I found are:
    - In the begining the user could use 25 turns because I didn't have a limit of guesses. That 
      produced a game that became exhausting. The problem if fixed with a limit of gueses of 10. 

* Owner stories 

    For me Python is easier to read and write. It's a more understandable language and much more fun to work with. I'm looking foward on taking a specialization on this language. 
    I'm proud of my work but I understand that the game could have more improvements. The messages  were hard to find, I found myself looking for a message so what I did is to add extra spacing in all the text.  
    The target audience will be every person older than 10 years old. I tested it with my child and she was able to play the game. 

* Deployment

    The site was deployed in Heroku. 

    - In Heroku, after opening an account and fixing the credits "Create a new 
      app"
    - When we have the code ready for deployment we can create a new app. 
    - Create a unique name for the app because Heroke doesn't accept 
      repetitions. 
    - After creating the app we need to fix the app settings before deployment.
    - This project doesn't need Config Vars because there are not secret    files.  
    - Then we need to choose Buildpacks. Here I choose Python and Node.js. 
    - After this settings are done we go to Deployment. Here, I used github and the name of my project P3 called Battleship -p3. Push connect. 
    - I set up automatic deployments and I push the "Deploy branch" that is manual because I wanted to see the logs and the packages installed. 
    - The app was succesfully deployed and now I can see the app on the web. 
    - To restart the game we need to push "Run program" and It will reset the game. 



* Code Used

    I wrote most of the code but I checked the previous exercises with loopd in the theory. 
    I was looking for ideas and inspiration and I found "dmoisset/battleship-dojo" on github, I dodn't copy the code directly but I adapted some of its code in my project. The idea of having boxes was great but I did my own instead. 
    The one compiter and CI lintern helped me adjust and fix the code. The Error messages are very helpful. 
    I've been working on the 100 days of coding in Udemy. I purchase this course from Dr. Angela Yu. 

CREDITS

- CI lintern. 
    (https://pep8ci.herokuapp.com/)
    
- I've been working on the 100 days of coding in Udemy. I purchase this course from Dr. Angela Yu. 
    (https://www.udemy.com/share/103IHM3@LSb44Ppc1io0Phvhc0EZ9mIfy1O6bTGmTtNQx3xWUywQ5Pkh3jLvZf9qvBGQu2ku/)

- Freecode camp. I've been practicing a little bit of python in their website. 
   (https://www.freecodecamp.org/learn/scientific-computing-with-python/)

- Slack. Here I found a lot of questions and answers about python and the challenges. 

- Pomodoro focus helped me have breaks and time to focus so my body doesn't get so stressed. 
    (https://pomofocus.io/)

- I learned more about indentation. 
    (https://realpython.com/python-pep8/)

- Most of my questions were answered in W3 schools. 
    (https://www.w3schools.com/python/)


MEDIA CONTENT

- Mock up: https://ui.dev/amiresponsive
- Webp converter app. https://anywebp.com/
- Wireframe/flowchart. https://app.diagrams.net/
- Validator. https://onecompiler.com/python/42ndghjhv


ACNOWLEDGEMENTS

    I want to thank the Udemy course and Anna Grieves for the good explanation on Python code. The walk through project was well explained as it was the deployment process. The tutors were there to help me when I needed. 
    I'm proud of myself for being able to learn more and apply everything I learned from the previous projects. I'm faster in my typing and I can find ansers to my questions easier than before. 


   