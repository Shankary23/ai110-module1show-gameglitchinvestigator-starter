# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- Answers:
  - Q1:
    - The game looked pretty normal and functional at the start. Then when I started to start guessing I noticed bugs. And by the end of the game I realized that most of it wasn't as functional as it seemed.
  - Q2: 
    - It let us input negative numbers and 0, I expected it to throw an error
      - When I guessed a negative number it said to go lower, I thought the hint would be accurate and helpful
      - We could guess the same number twice, I assumed it would say pick a new number
      - The new game button didnt work, I thought it would refresh the game state
      - The tracker for attempts is off by one, I didnt notice at first but it should be one less than it is
      - The hint doesnt seem to help, I thought the hints would point towards numbers within the bounds.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- Answers:
  - I used claude for this 

  - An example of a correct suggestion was when Claude suggested modifying the guess bounds to actually constraint the users guess in between the numbers 1 and 100. I verified the result by running the game again and seeing the error message. 
  - Claude's suggestion:  ``` if value < 1 or value > 100:
        return False, None, "Guess must be between 1 and 100."
    return True, value, None ```

  - One example of a misleading suggestion is when the AI tried to fix, it just fixed one aspect and didnt realise it created or didnt find a bug that the fix caused. I was trying to fix the hints and it just fixed the fact the hints were being given in reverse order, not the fact that they were based on if the number was even or odd.
    -This was the fix it suggested:
    ```
            if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    ```
  - I then ran the game again and saw that nothing for the hints really changed, I then pointed out how the hints were based on the number divisibility rather than being reflefctive of the number.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  - I decided my bug was actually fixed when I was able to test the edge cases for the bug. For example the guessing range bug, 
  I was able to stress test it again and see that it actually worked. Whenever I guessed invalid inputs an error message would pop up, 
  this showed me that the issue for this part was fixed. But I did see other bugs when I was testing this part.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I ran both, but the manual test was checking the number range outlined above. Then I had claude write a few test cases to ensure that the hints were working correctly and accurately outputted a message based on the users guess.

- Did AI help you design or understand any tests? How?
  - I used AI to design the tests, they seemed pretty simple but utilizing AI allowed me to write more tests helping covering a wider variety. I feel like tests help but also just testing in the live site was just as beneficial but using tests helped me check if a change actually fixed before going through sometimes the long process of guessing.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - The secret session number used to keep changing because the app was reloaded so that number would never stay constant.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - I would explain Streamlit reruns like reloading a Google doc anytime you made a meaningful change.

- What change did you make that finally gave the game a stable secret number?
  - We did not have to make a change to fix the stability, the issue was before was the fact that we would make changes and then streamlit would trigger a reload and then the session state would be wiped and a new one would need to be generated but now thats not the case.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    - One habbit Im going to take away from this project and reuse later is asking AI to write tests for me.
    Normally I use to manually write tests and try to think of edge cases but asking AI to come up with tests lets you 
    creater a wider array and its more likely to catch some logic that shouldnt be happening.

- What is one thing you would do differently next time you work with AI on a coding task?
  - I think I use AI as like a last resort when Im stuck on a bug. Academically I think thats the approach we were taught, but 
  for coding projects or debugging it is just more efficient to just ask AI to explain the parts you dont understand right away rather
  than looking at the code for 20-30 minutes and not understanding it.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project both showed me how useful AI can be when it has context but also how it having context doesnt mean it wont make mistakes or errors. It showed me to use it as a tool but never to blindly accept it solutions and changes.
