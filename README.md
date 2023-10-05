# themis-cli
[Inspired by @Stylo2k](https://github.com/Stylo2k/Perist-ri)  

CLI tool for you to upload your code to themis, and get feedback.

## File hierarchy
* When you start a course, create a folder `x` with the same name as the ending of the url when you go to that course in themis. 
```
https://themis.housing.rug.nl/course/2023-2024/progfun/
                                               ^^^^^^^
                                               course 
```

* When you start solving a lab/assignment, take a look at the URL and look for the assignment name`y`.  
E.g.  
```
https://themis.housing.rug.nl/course/2023-2024/progfun/tutorial4/
                                                      ^^^^^^^^^^ 
                                                      assignment 
```
* Head into your `x` folder and type `themis-cli -a y`, with `y` being your assignment name. The program will subsequently generate the file structure and download all available inputs and outputs from themis.

## Submitting
* When you're ready with assignment `y`, go ahead and run `themis-cli -l y.c`(inside the folder of the assignment). This will run the available test cases through your code locally, showing you the difference(if any) between your output and the provided one.

* If you *think* you're ready for the real deal, run `themis-cli -s y.c`. This will submit your code and show you what the outcome is.

## Roadmap

* [ ] Create file structure
* [ ] Get (the available) inputs and outputs
* [ ] Submit succesfully
* [ ] Get & render test case outcome

![Flowchart](https://i.imgur.com/naum7ZX.png)