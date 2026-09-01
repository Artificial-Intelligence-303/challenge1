# Challenge 1: A Simple Reflex Agent

|                    |                                             |
| :----------------- | :------------------------------------------ |
| `Tuesday 1 Sep`    | Released, in lab                            |
| `Tuesday 8 Sep`    | Due at 2:30pm, the start of lab             |
| `Tuesday 8 Sep`    | Verbal checks, during that same lab session |
| Points             | 3                                           |

You are going to build the smallest thing that still counts as an intelligent
agent, and then find out exactly where it fails.

The world is two squares, `A` and `B`. Each one is either clean or dirty. Your
agent stands in one square at a time, can see only that square, and can suck,
move left, move right, or do nothing. 

## Course learning outcomes

This challenge addresses the following outcomes:

1. **Outcome 1.** Correctly implement an intelligent agent and accurately
   describe its properties. You implement the agent program in `src/agents.py`
   and you classify its environment in `describe_environment`.
2. **Outcome 5.** Evaluate intelligent systems while considering their social,
   political, and ethical implications, and communicate their outcomes in both
   written and oral forms. You evaluate your agent against a baseline, argue
   about what its performance measure rewards, and defend your reasoning both in
   `docs/summary.md` and out loud during the verbal check.

## What you implement

Everything you write goes in `src/agents.py`. Three functions:

**`simple_reflex_agent(percept)`** returns an action for a percept. It is a
lookup table and nothing more. It may not remember anything between calls, and
one of the tests specifically checks that it does not.

| percept      | action  |
| :----------- | :------ |
| `(A, Dirty)` | `Suck`  |
| `(B, Dirty)` | `Suck`  |
| `(A, Clean)` | `Right` |
| `(B, Clean)` | `Left`  |

**`describe_environment()`** returns a dictionary classifying this environment
along the six standard properties. Use these keys, and for each one use exactly
one of the two values listed:

| key                      | one of                                        |
| :----------------------- | :-------------------------------------------- |
| `observability`          | `fully observable`, `partially observable`     |
| `determinism`            | `deterministic`, `stochastic`                  |
| `episodic_or_sequential` | `episodic`, `sequential`                       |
| `dynamism`               | `static`, `dynamic`                            |
| `discreteness`           | `discrete`, `continuous`                       |
| `agent_count`            | `single agent`, `multi agent`                  |

Answer for the environment in `src/environment.py`, not for vacuum cleaners in
general. Every answer is decidable from that file. Read it!

**`find_crossover()`** locates the horizon where the random agent starts
outscoring your reflex agent. For a short run your agent wins. Past some number
of steps it loses, and stays losing. Find that number.

For each horizon from 1 to `max_steps`: score the reflex agent over one run (it
is deterministic, so one run is the whole answer), score the random agent over
`trials` runs and take the mean (it is not deterministic, which is why one run
would tell you nothing), and return the first horizon where the random mean is
strictly higher. Return `-1` if it never happens.

Keep `trials` at 200 or more. Below that the mean is too noisy and your answer
will move around between runs.

**Whatever number you get, write it in your reflection.** You are asked to
explain it, and you cannot explain a number you did not produce.

`src/environment.py` is provided and you should not need to change it.

## Running it

```
uv run python src/main.py     # watch your agent work, and see the comparison
uv run pytest                 # run the tests
uv run gatorgrade             # run the checks the way they will be graded
```

Start with `src/main.py`. It prints a step-by-step trace of one run, then scores
your agent against an agent that ignores its percept entirely and picks at
random, at a short horizon and a long one. **The winner changes between them.**
That reversal is expected and it is not a bug in your code. `find_crossover` has you 
find out where it happens, and question 2 of the reflection is asks you to
explain why.

## Evaluation

This challenge is worth **3 points**.

| Component                 | Value   |
| :------------------------ | :------ |
| Programming               | 1     |
| Written reflection        | 1       |
| Verbal check              | 1     |
| **Total**                 | **3**   |

### Programming, 1 point

Run by `gatorgrade`, awarded as the fraction of the **code** checks that pass.
These are:

- The agent sucks whenever it stands on a dirty square.
- The agent moves right from a clean `A` and left from a clean `B`.
- The agent only ever returns actions the environment accepts.
- The agent holds no state between calls, so it is genuinely a reflex agent.
- Starting dirty everywhere, the agent cleans both squares, in the minimum
  three steps.
- The agent keeps moving once the world is clean, as a simple reflex agent must.
- `find_crossover` finds a crossover, it lands in the expected window, and it
  stays put when the random seed changes.
- All six environment properties are present and correctly classified.
- Type annotations check out under `mypy`.
- No `TODO` markers are left behind, and your code carries at least four
  comments explaining your reasoning.

`gatorgrade` also runs two checks on `docs/summary.md`. Those belong to the
reflection below, not to this point.

Autograder results are preliminary. The final grade is determined by the instructor.

### Written reflection, 1 point

Complete `docs/summary.md`. Four questions and the disclosure, **300 words
minimum across all of them**. You are graded on whether the reasoning is correct
and specific, not on length. A correct `describe_environment` dictionary with no
reasoning behind it earns the programming point and loses this one.

`gatorgrade` checks two things here, and both are floors rather than the grade:
that no `TODO` markers are left, and that the word count is met. Clearing both
does not mean the answers are right.

### Verbal check, 1 point

During lab you answer two or three questions about your own code **without
looking at it**. This is not a presentation and there is nothing to prepare
beyond understanding what you wrote. If you can explain why your agent behaves
the way it does, you will be fine. If not, you will lose points.

## AI use on this challenge

Full policy: **[AI in this course](https://areweagentsyet.com/ai/)**. The short version is that AI tools are allowed here, you
disclose them, and you have to be able to explain what you submit.

> ### The skill this time: explain it back
>
> Every challenge names one habit worth building. This one is the habit
> everything else rests on.
>
> Before you accept any suggestion, say what it does in your own words. Not
> "this returns the action" but "this checks the status field first, so a dirty
> square is cleaned no matter which square it is." If you cannot produce that
> sentence, you do not yet understand the line, and next Tuesday you will be
> asked for exactly that sentence with your screen closed.

Concretely, for this assignment:

- **Write the four rules yourself.** It is four lines and it is the vocabulary
  of the whole course. Reaching for a tool here costs you more than it saves.
- **A tool is genuinely useful** for the parts that are not the point: what a
  type annotation means, why `pytest` cannot find your import, how to take a
  mean in Python.
- **A tool cannot do `find_crossover` for you.** It can write the loop. It
  cannot tell you your number, because your number comes from running your code.
  If you report a number you did not run, you might run into a problem during the verbal check.

## Disclosing your AI use

At the end of `docs/summary.md` there is a disclosure section. Answer three
things, a sentence or two each:

1. **Which tool.** Name it: GitHub Copilot, ChatGPT, Claude, Gemini, whatever
   you actually used. If you used more than one, name each.
2. **What you used it for.** Which part of the assignment, not your exact
   wording.
3. **What you did with what it gave you.** Accepted it as written, edited it,
   checked it against something, or threw it out.

Two examples of the level of detail expected:

> I used GitHub Copilot for the loop in `find_crossover`. It structured the loop
> correctly but averaged the wrong variable, and I caught that when the test
> failed and fixed it myself.

> I asked Claude what a percept is. It answered in general terms and I worked
> out what that meant for this environment on my own. I wrote all the code.

**If you did not use any tool, write that.** That is a complete and perfectly
good answer.

Disclosing costs you nothing. There is no version of this where naming a tool
loses you points.

