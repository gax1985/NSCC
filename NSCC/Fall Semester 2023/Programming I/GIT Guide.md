

1. We can navigate to the folder where the assignments reside, and where we want to clone the repository.

2. If we have *git-bash*, right-click in the folder, and click "Git-BASH"
3. Enter the following command : 

		git clone <repo link>

4. You will see that it is creating the folder, and downloading the repository's files. 
5. Open the cloned folder in VSCode, due to the intention of adding our assignment to it. 
6. Every time a change is done, we can click on *Source-Control*.
7. We can type :

		git status    

8. We can see that the file is not tracked, so we can fix it: 

		git add .    --> This adds all the files in the folder to the repository's index


9. Type the following : 

		git status 


There, we can see that it has  recorded the change.

10. We can type the following command to commit the files : 

		git commit -m "message"

11. We can now push it to the repository : 

		git push 



#### The GIT Proccess in VSCode 


1. Open the folder where you would like to clone the repository
2. With the folder opened, launch the terminal
3. Make sure that the correct folder is represented in the terminal 
4. Type the following to check the status :

		  git status

5. If there has been any untracked changes , type the following : 

		git add . 


6. Then, type the following to commit the changes : 

		git commit -m "This is a message"

7. Type the following when you are ready to commit the files : 

		git push

