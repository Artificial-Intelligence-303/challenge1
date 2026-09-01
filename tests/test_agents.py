"""Tests for Challenge 1. These are the checks gatorgrade runs.

Nothing here is hidden from you. Read the tests to see exactly what is expected.
"""

from __future__ import annotations

import random

from agents import describe_environment, find_crossover, simple_reflex_agent
from environment import (
    A,
    ACTIONS,
    B,
    CLEAN,
    DIRTY,
    LEFT,
    RIGHT,
    SUCK,
    VacuumEnvironment,
    run,
)

ALL_PERCEPTS = [(A, DIRTY), (B, DIRTY), (A, CLEAN), (B, CLEAN)]

EXPECTED_DESCRIPTION = {
    "observability": "partially observable",
    "determinism": "deterministic",
    "episodic_or_sequential": "sequential",
    "dynamism": "static",
    "discreteness": "discrete",
    "agent_count": "single agent",
}


def test_sucks_when_standing_on_dirt() -> None:
    """A dirty square is cleaned regardless of which square it is."""
    assert simple_reflex_agent((A, DIRTY)) == SUCK
    assert simple_reflex_agent((B, DIRTY)) == SUCK


def test_moves_right_from_a_when_a_is_clean() -> None:
    """With nothing to do in A, the only useful move is toward B."""
    assert simple_reflex_agent((A, CLEAN)) == RIGHT


def test_moves_left_from_b_when_b_is_clean() -> None:
    """With nothing to do in B, the only useful move is toward A."""
    assert simple_reflex_agent((B, CLEAN)) == LEFT


def test_only_returns_legal_actions() -> None:
    """Every percept maps to an action the environment actually accepts."""
    for percept in ALL_PERCEPTS:
        assert simple_reflex_agent(percept) in ACTIONS


def test_ignores_everything_except_the_percept() -> None:
    """The same percept always produces the same action.

    This is what makes the agent a *simple reflex* agent. If your implementation
    remembers anything between calls, this test fails.
    """
    for percept in ALL_PERCEPTS:
        first = simple_reflex_agent(percept)
        for _ in range(5):
            assert simple_reflex_agent(percept) == first


def test_cleans_both_squares() -> None:
    """Starting dirty everywhere, the agent gets the whole world clean."""
    environment = run(simple_reflex_agent, status={A: DIRTY, B: DIRTY}, steps=4)
    assert environment.status[A] == CLEAN
    assert environment.status[B] == CLEAN


def test_cleans_both_squares_in_three_steps() -> None:
    """Suck, move, suck. There is no faster route from all dirty to all clean."""
    environment = run(simple_reflex_agent, status={A: DIRTY, B: DIRTY}, steps=3)
    assert environment.clean_squares() == 2


def test_keeps_moving_after_the_world_is_clean() -> None:
    """The agent never settles down, even with nothing left to do.

    This is not a bug in your code. It is the defining limitation of a simple
    reflex agent in a partially observable environment, and the reflection asks
    you to explain it.
    """
    environment = VacuumEnvironment(status={A: CLEAN, B: CLEAN}, location=A)
    before = environment.location
    environment.step(simple_reflex_agent(environment.percept()))
    assert environment.location != before


def test_description_has_the_six_required_keys() -> None:
    """All six environment properties are classified."""
    description = describe_environment()
    assert isinstance(description, dict)
    assert set(description) == set(EXPECTED_DESCRIPTION)


def test_description_is_correct() -> None:
    """Each property is classified correctly for this environment."""
    assert describe_environment() == EXPECTED_DESCRIPTION


def test_crossover_is_found_at_all() -> None:
    """The random agent does overtake the reflex agent within 100 steps."""
    random.seed(303)
    assert find_crossover() != -1


def test_crossover_lands_where_it_should() -> None:
    """The boundary sits in the mid thirties.

    The exact value moves a little from run to run because the random agent is
    random. It does not move much. If your answer is far outside this window,
    something in the loop is wrong, most likely comparing a single random run
    instead of the mean of many.
    """
    random.seed(303)
    crossover = find_crossover()
    assert 28 <= crossover <= 42


def test_crossover_is_stable_across_seeds() -> None:
    """Averaging enough trials means the answer barely moves."""
    results = []
    for seed in (1, 42, 2026):
        random.seed(seed)
        results.append(find_crossover())
    assert max(results) - min(results) <= 8
