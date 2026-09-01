"""Run the agents and print what happens. Start here once your code runs.

    uv run python src/main.py

Read the second table carefully. Something in it reverses, and explaining why it
reverses is most of the reflection.
"""

from __future__ import annotations

import random

from agents import (
    describe_environment,
    find_crossover,
    random_agent,
    simple_reflex_agent,
)
from environment import DIRTY, A, B, VacuumEnvironment, run

TRACE_STEPS = 12
HORIZONS = (10, 60)
TRIALS = 1000
SEED = 303


def trace_reflex_agent() -> None:
    """Print one step-by-step run so you can watch the agent decide."""
    print(f"One run, starting dirty in both squares, {TRACE_STEPS} steps.")
    print()
    header = (
        f"{'step':>4}  {'percept':<18} {'action':<7} "
        f"{'A':<7} {'B':<7} {'score':>5}"
    )
    print(header)
    print("-" * 56)

    environment = VacuumEnvironment(status={A: DIRTY, B: DIRTY}, location=A)
    for step in range(1, TRACE_STEPS + 1):
        percept = environment.percept()
        action = simple_reflex_agent(percept)
        environment.step(action)
        print(
            f"{step:>4}  {str(percept):<18} {action:<7} "
            f"{environment.status[A]:<7} {environment.status[B]:<7} "
            f"{environment.score:>5}"
        )
    print()
    print("Look at what it is doing from step 3 onward, and what that costs.")
    print()


def compare_against_random() -> None:
    """Score the reflex agent against the agent that is not thinking at all."""
    print("Now score it against an agent that ignores its percept entirely.")
    print(
        "Both start dirty in both squares. "
        f"Random is the mean of {TRIALS} runs."
    )
    print()
    print(f"{'horizon':>9} {'reflex':>9} {'random':>9}   {'winner':<8}")
    print("-" * 42)

    random.seed(SEED)
    for steps in HORIZONS:
        finished = run(
            simple_reflex_agent, status={A: DIRTY, B: DIRTY}, steps=steps
        )
        reflex = finished.score
        total = sum(
            run(random_agent, status={A: DIRTY, B: DIRTY}, steps=steps).score
            for _ in range(TRIALS)
        )
        rnd = total / TRIALS
        winner = "reflex" if reflex > rnd else "random"
        print(f"{steps:>9} {reflex:>9} {rnd:>9.1f}   {winner:<8}")

    print()
    print("The winner changes somewhere between those two horizons.")
    print("Your agent is not broken and the random agent did not get")
    print("smarter. Finding exactly where the change happens is your job,")
    print("in find_crossover.")
    print()


def report_crossover() -> None:
    """Print the boundary your own code located."""
    crossover = find_crossover()
    if crossover == -1:
        print("find_crossover did not find a crossover. Check your loop.")
    else:
        print(
            "Your find_crossover says the random agent takes the lead at "
            f"{crossover} steps."
        )
        print("Write that number in your reflection, and explain it.")
    print()


def show_environment_description() -> None:
    """Print your classification of the environment."""
    print("Your description of this environment:")
    for prop, value in describe_environment().items():
        print(f"  {prop:<24} {value}")
    print()


def main() -> None:
    """Run every part of the demonstration in order."""
    trace_reflex_agent()
    compare_against_random()
    report_crossover()
    show_environment_description()


if __name__ == "__main__":
    main()
