# basic-ai
AI made in Texas instruments TI83 BASIC

This is my code, so please don't steal it and say that it's your own.

Feel free to use it as long as you put credit somewhere (unless your uploading to calc). Thanks!

Anyway I used the TI-84CSE to program this bot. 

It is an RNG based bot, but it works because YOU are human! 

^that means you try to make sense of the conversation

This program uses 3 strings, 3 lists, and many variables to make it work

There is one thing to note: The TI CONNECT CE software breaks the program on first run. Please use alpha11 (or later) unless you know how to program in BASIC 

     The CharMap (looks like "eE...") needs to be retyped by hand, also the DelVar commands need to be redone. This is a compatability issue and cannot be fixed via software :(
     
  STRINGS
  
    [str0] Responses. Broken up by "Θ", so don't respond with it, because the bot breaks.
    [str1] CharMap. Used for L2N (letter to number: encoding for M2M) and M2M (message to message: 1 response per input) 
    [str2] UrInput. Works with L2N so M2M can work
    
  LISTS
  
    [lAII] AI Input. The output for L2N
    [lAIO] AI Output. Response IDs linked with L2N to provide M2M
    [lAIR] AI Responses. The location list for "Θ" to greatly increase speed
