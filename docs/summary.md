# Challenge 1 Reflection

Answer all four questions. **300 words minimum across the whole document.** You
are graded on whether the reasoning is correct and specific to this environment. Replace every `TODO` before you submit.

---

> **1. Justify your six environment classifications.**
>
> Go through each of the six properties you returned from `describe_environment`
> and say what in `src/environment.py` makes your answer the right one. Point at
> specific behavior, not general intuitions about vacuum cleaners.
>
> Note on observability: think of the difference between what you can
> see reading the code and what the agent can see at run time.

TODO

---

> **2. Explain your crossover number.**
>
> **State the number your `find_crossover` returned.** Then explain it. Your
> reflex agent beats the random agent over short runs and loses over long ones,
> and neither agent changed. Explain what did.
>
> Your answer should refer to the performance measure in
> `VacuumEnvironment.step` and to what your agent does after step 3 of the trace.
>
> Then answer the harder half: your agent starts oscillating at step 3, so why
> is the crossover somewhere in the thirties rather than at step 3?

TODO

---

> **3. Name the missing piece.**
>
> There is one fact your agent would need to remember in order to stop losing
> points on long runs. What is it, and what would it do differently once it knew
> it?
>
> Then say why a simple reflex agent cannot have that fact, in terms of the
> function signature you implemented.

TODO

---

> **4. Change the performance measure and report what happens.**
>
> The environment charges one point for every move. That number is
> `move_cost`, and somebody chose it.
>
> **Run `find_crossover(move_cost=0)` and state what it returns.** Then
> explain the result: what does that number mean, and why does making
> movement free produce it?
>
> Then answer the question the experiment sets up. You did not change a
> single line of your agent. So is "rational" a property of the agent, of
> the environment, or of something else? Give one case outside this
> assignment where choosing that number badly would matter.

TODO

---

> **AI tool disclosure**
>
> State what AI tools you used on this challenge, if any, and what they did.
> "None" is a complete answer if it is true. Be specific: "I used X to explain
> what a percept was" and "I used X to write the rule table" are very different
> disclosures, and only one of them is a problem.

TODO
