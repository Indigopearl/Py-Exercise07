# Exercise 7

This might sound familiar if you did exerise 5...
Write a fantasy game character creator version 2!

- Create a public repository on your GitHub profile or clone an existing one
- Clone it and add these instructions as README.md
- Create a new file called `phantasy.py`
- Ask the user how many characters to create
- Ask the user for character names, one for each character
- A character will randomly be a Barbarian, Cleric or Druid
- Each character has stats: Health, Strength, Magic and Initiative
- Each stat is random, between 3 and 15
- Barbarians will have triple Strength and Health
- Clerics will have triple Magic and Initiative
- Druids will have double Health, Magic and Initiative
- Generate the team of however many characters the user wanted
- **Use at least one function**

Example of program output below.

        $ py creator.py
        Welcome to the character generator!
        How many characters are we creating: 2
        Let's name the brave adventurers:
        Character 1: Veera Shadowstep
        Character 2: Rauli Firebreath

        ***YOUR CHARACTERS ARE COMPLETE***
        "Veera Shadowstep" is a Druid!
            Strength: 5
            Magic: 30
            Health: 18
            Initiative: 18

        "Rauli Firebreath" is a Barbarian!
            Strength: 27
            Magic: 6
            Health: 30
            Initiative: 5

        Happy adventuring!

- Finally, add commit, push your work and add a link to the thread of this message.
- Inspiration
    - https://kilnrpg.com/assets/images/home/en/character-sheets-modules.webp
    - https://rgbstudios.org/projects/dnd-dice/character-roller?r=NDEyMTIxMjU0NTY1MjQ1MzIzNDUxNjI2MDMyLTEtMS0xVmVlcmEgU2hhb3dzdGVw
- Good luck, have fun!

- **OPTIONAL BONUS CHALLENGE**
- Make it so that there is a 10% chance that a single stat is printed as binary, 10% chance that a single stat is printed as hex and 80% chance a single stat is printed as decimal.
