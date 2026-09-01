"""The agent programs for Challenge 1.

You implement three things in this file: `simple_reflex_agent`,
`describe_environment`, and `find_crossover`. Everything else is provided.
"""

from __future__ import annotations

import random

from environment import (
    ACTIONS,
    DIRTY,
    LEFT,
    RIGHT,
    SUCK,
    A,
    B,
    Percept,
    run,
)


def simple_reflex_agent(percept: Percept) -> str:
    """Choose an action from the current percept alone.

    A simple reflex agent is a lookup table from percept to action. It has no
    memory of anything it has seen before, so the only information you may use
    is the percept you are handed.

    The four rules you are implementing are in the README, under "What you
    implement". Read them there.

    Args:
        percept: A `(location, status)` pair, for example `("A", "Dirty")`.

    Returns:
        One of `Suck`, `Left`, `Right`, or `NoOp`.
    """
    # TODO: unpack the percept and return the action the rule table calls for.
    raise NotImplementedError("simple_reflex_agent is not implemented yet")


def random_agent(percept: Percept) -> str:
    """Provided as a baseline. Ignores the percept completely and guesses."""
    return random.choice(ACTIONS)


def describe_environment() -> dict[str, str]:
    """Classify the vacuum world along the six standard environment properties.

    Answer for the environment implemented in `src/environment.py`, not for
    vacuum cleaners in general. Every answer is decidable from that file.

    The six keys, and the two permitted values for each, are listed in the
    README. Use them exactly.

    You will justify each choice in `docs/summary.md`. A correct dictionary with
    no reasoning behind it earns the programming points and loses the writing
    points, so do not guess.

    Returns:
        A dictionary with the six required keys.
    """
    # TODO: return the dictionary described in the README.
    raise NotImplementedError("describe_environment is not implemented yet")


def find_crossover(
    max_steps: int = 100,
    trials: int = 400,
    move_cost: int = 1,
) -> int:
    """Find the horizon where the random agent starts beating the reflex agent.

    Run both agents from a world that starts dirty in both squares. For a short
    run your reflex agent scores higher. Somewhere past that, the random agent
    pulls ahead and stays ahead. Your job is to locate that boundary.

    For each horizon from 1 up to and including `max_steps`:

    1. Score `simple_reflex_agent` over one run of that many steps. It is
       deterministic, so one run is sufficient.
    2. Score `random_agent` over `trials` runs of that many steps and take the
       mean. It is not deterministic, which is why one run would not tell you
       anything.
    3. Return the first horizon where the random mean is strictly greater than
       the reflex score.

    Pass `move_cost` straight through to `run()`. It is what the
    environment charges for each move, and question 4 of the reflection
    asks you to run this function with a different value for it.

    Use `run()` from `environment`, which returns a finished environment
    whose `.score` you can read. Do not lower `trials` below 200; the mean
    gets too noisy to trust and your answer will move around between runs.

    Whatever number you get, put it in `docs/summary.md` and explain it.

    Args:
        max_steps: The longest horizon to test.
        trials: How many random runs to average at each horizon.
        move_cost: Points the environment charges for each move.

    Returns:
        The smallest horizon at which the random agent's mean score beats the
        reflex agent, or -1 if that never happens within `max_steps`.
    """
    # TODO: loop over horizons, score both agents, return the first crossover.
    raise NotImplementedError("find_crossover is not implemented yet")
