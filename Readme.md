#Death By X

This script is a timer for the Crossfit workout called "Death By X"
(e.g. Death By Burpees).

The goal is to do 1 rep in the first minute, 2 reps in the second
minute, 3 reps in the third minute and so on.

Rather than doing all the required reps in quick succession at the
start of each minute this script plays a beep for each rep and spreads
the required reps evenly over the minute. For example in the third
round the required 3 reps are spaced 20secs apart, in the fourth round
the required 4 reps are spaced 15 secs apart and so on.

The prinout shows your score should you stop right now.  e.g. The
following output means you have COMPLETED 10 rounds and 3 reps (you
are now in the 11th round).
```
Rounds 10: Reps 03 | Time 10:11.0
```

## Use

1. Download the beep sound from
[here](https://www.soundjay.com/button/sounds/beep-09.mp3) and save it
in the root directory of this project. (You can download any sound you
like, just be sure that the sound plays at or very close to the
beginning of the audio clip and update the call to the file in the script)

2. Give the script execute permission
```
chmod +x timer.py
```

3. Run the script
```
./timer.py
```

4. Get ready to be tired

