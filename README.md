# RNG BASED AI
**Status: `[BUILD|ONGOING]`**

## This project is no longer just for TI-BASIC, rather all forms possible :D
## For support and other stuff, join my discord server here: [[DISCORD]](https://discord.gg/Z84Nm6n)

# TI-BASIC AI
AI made in Texas instruments TI83 BASIC

This is my code, so please don't steal it and say that it's your own.

Feel free to use it as long as you put credit somewhere (unless your uploading to calc). Thanks!

Anyway I used the TI-84+ CSE to program this bot.

It is an RNG based bot, but it works because YOU are human!

^that means you try to make sense of the conversation

This program uses 3 strings, 3 lists, and many variables to make it work

There is one thing to note: The TI CONNECT CE software breaks the program on first run. Please use alpha13 (or later) unless you know how to program in BASIC

     Big Bug! Fix over at "BigBug.md", got it?

  STRINGS

    [str0] Responses. Broken up by "Θ", so don't respond with it, because the bot breaks.
    [str1] CharMap. Used for L2N (letter to number: encoding for M2M) and M2M (message to message: 1 response per input)
    [str2] UrInput. Works with L2N so M2M can work
    [str3] AntiBreak, now "Θ" and any strings over 25 chars won't break the AI

  LISTS

    [lAII] AI Input. The output for L2N
    [lAIO] AI Output. Response IDs linked with L2N to provide M2M
    [lAIR] AI Responses. The location list for "Θ" to greatly increase speed

If ypu want to learn how to do this, please visit [this site](http://tibasicdev.wikidot.com/home) to learn more :)

FYI, my program isn't on there. I am independent from that site, other than me using it to learn.

# SWIFT AI
A very bad version of the Basic AI, although it uses basically the same stuff.

However, because I can use collections, AntiBreak is not included in this version

To use this version, please download Swift Playgrounds here: [[iOS]](https://itunes.apple.com/us/app/swift-playgrounds/id908519492?mt=8) [[Android]](https://android-apk.net/app/swift-playgrounds/908519492/)(report as an issue if this one is unsafe)

# PYTHON-LINUX AI

A Discord version of the same SwiftAI

This version runs on linux, so there is a few things you need to do every time you start it up (notes are in the file)
