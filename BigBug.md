[!] There is a major bug where the AI will not output something instantly when sending "e"

How to Fix it:
 
Get LowerCase Letters:
     
     You must do the following exactly perfectly, otherwise you may loose all your programs and other data in RAM
     [A] Create a program
          [1] Click "PGRM"
          [2] Click the left arrow
          [3] Press enter
          [4] Enter a name (in this case, it's "TEXTCASE")
          [5] Press Enter
     
     [B] Lowercase Program Data
          [1] Click "2ND" then "0"
          [2] Click the down arrow key 8 times (Until "Asm84CPrgm" or "Asm84CEPrgm" is selected
          [3] Press enter
          [4] Type the following 100% perfectly: FD7E24EE08FD7724C9
          
     [C] Get Lowercase Letters
          [1] Click "2ND" then "MODE"
          [2] Click "2ND" then "0"
          [3] Press the down arrow key 6 times (Until "Asm(" is selected)
          [4] Press enter
          [5] Press "PRGM" and scroll down to "TEXTCASE" (or whatever you named the program you just created)
          [6] Press enter, wait for 3 seconds, and press enter again
          
     [D] Signs
          If you did it correctly, then your calculator should NOT have shut down. 
          Instead it should stay on and by pressing "2ND" and then "ALPHA" twice, you should have a blinking inverted "a" icon :)

Fixing the bug

     [A] Finding the string
          [1] Click "PRGM"
          [2] Click the right arrow button
          [3] Scroll down to "AI" (the AI program name)
          [4] Press enter
          [5] Scroll down to the line that says ':Output(1,25,"=B")'
          [6] Press the down arrow
          
     [B] The "UhOh" part :(
          [1] Proceed to RE-TYPE every character (100% perfectly) until the "→" character is reached

Not doing these steps may greatly affect your experience with BASIC AI
