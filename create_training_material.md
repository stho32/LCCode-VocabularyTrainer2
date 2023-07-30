This is the structure of the qa.json file:

```
[{"id": "118b5d31-f43e-4385-bee5-09e3254a2a21", "question": "What is my name?", "expected_response": "Stefan", "position": 0}]
```

The file represents:
- id : a random guid
- question: a question to answer
- expected_response: the response that should be given
- explanation: Contains an explanation about why the question should be answered like the expected response and why it should not be answered in another way. 
- positon: always 0

Please generate the necessary json for this file with made up questions about the following content.
Please note the following rules: 
- Do not use the questions directly but rather reformulate them.
- Ask for the Category of Legitimate Reservation that is broken, when the statements are true.
- You may also ask something like '"Apples are dark blue": Which Category of Legitimate Reservation is challenged here?'.
- Thinking like a teacher you might make up examples of your own, about physics, biology or math, but make sure that the user can always just name a Category of Legitimate Reservation as an answer.
- Make up at least 5 questions per category and 10 questions per category at maximum.

```
# Categories of Legitimate Reservation

## Clarity

Clarity wants to establish a certain ground check before we go into too much detail.
It validates some general rules against the statements and expressed causalites in the logic tree.

- Is the meaning or the context of the words unambiguous?
- Is the meaning or the context of the words clear?
- Does the statement make sense? ("Can you comprehend what is being said?")
- Is the connection between cause and effect convincing "at face value"?
- Are no intermediate steps missing?

## Entity Existence

Entity Existence validates one statement in the logic tree. It is not concerned with causality yet.

- Does the statement validly indicate the existence of entity?
- Is the statement a complete sentence?
- Is the statement sensible? ("Is this a wise or logical thing to say or propose?")
- Does the statement not contain embedded "if-then" statements? (Look for "... because ..." and "... in order to ...")
- Does the statement not convey more than one idea? 
- Is the statement not a compound entity?
- Does the statement exist in my (or someone's) perception?
- Can the statement be documented with evidence?

```