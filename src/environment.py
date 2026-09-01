"""The two-square vacuum world.

Adapted from Russell and Norvig, *Artificial Intelligence: A Modern
Approach*, chapter 2.

You do not need to change anything in this file. Read it anyway. Part of this
challenge asks you to describe this environment's properties, and every answer
is visible somewhere in this file.
"""

from __future__ import annotations

from typing import Callable

# The two squares the agent moves between.
A = "A"
B = "B"
LOCATIONS = (A, B)

# What a square can be.
CLEAN = "Clean"
DIRTY = "Dirty"

# Everything the agent is allowed to do.
SUCK = "Suck"
LEFT = "Left"
RIGHT = "Right"
NOOP = "NoOp"
ACTIONS = (SUCK, LEFT, RIGHT, NOOP)

# The two actions that count as movement. The performance measure
# charges for these.
MOVES = (LEFT, RIGHT)

# A percept is what the agent sees on one time step: which square it is
# standing in, and whether that square is dirty.
Percept = tuple[str, str]

# An agent program maps a percept to an action. That is the whole interface.
AgentProgram = Callable[[Percept], str]


class VacuumEnvironment:
    """Two squares, A and B. Each one is either Clean or Dirty.

    The performance measure awards one point for every clean square on
    every time step, and charges `move_cost` for every move. Sucking and
    doing nothing are always free.

    `move_cost` is a knob, not a law of nature. Somebody chose it. Turning
    it down changes which agent counts as rational without changing a
    single line of any agent.
    """

    def __init__(
        self,
        status: dict[str, str] | None = None,
        location: str = A,
        move_cost: int = 1,
    ) -> None:
        """Create a world.

        Args:
            status: Starting cleanliness of each square. Defaults to
                both squares dirty.
            location: The square the agent starts in.
            move_cost: Points charged for each move. Defaults to 1.
        """
        if status is None:
            status = {A: DIRTY, B: DIRTY}
        self.status: dict[str, str] = dict(status)
        self.location: str = location
        self.move_cost: int = move_cost
        self.score: int = 0

    def percept(self) -> Percept:
        """Return what the agent can see right now.

        Notice what is missing: the agent is told about its own square only. It
        cannot see the other square from here.
        """
        return (self.location, self.status[self.location])

    def clean_squares(self) -> int:
        """Return how many of the two squares are currently clean."""
        return sum(
            1 for location in LOCATIONS if self.status[location] == CLEAN
        )

    def step(self, action: str) -> None:
        """Carry out one action, then score the resulting time step."""
        if action == SUCK:
            self.status[self.location] = CLEAN
        elif action == LEFT:
            self.location = A
        elif action == RIGHT:
            self.location = B
        elif action == NOOP:
            pass
        else:
            raise ValueError(f"Not a legal action: {action!r}")

        self.score += self.clean_squares()
        if action in MOVES:
            self.score -= self.move_cost


def run(
    agent: AgentProgram,
    status: dict[str, str] | None = None,
    location: str = A,
    steps: int = 20,
    move_cost: int = 1,
) -> VacuumEnvironment:
    """Run `agent` in a fresh environment for `steps` time steps.

    Returns the finished environment so you can inspect both its final
    score and the state it ended up in.

    Args:
        agent: The agent program to run.
        status: Starting cleanliness of each square.
        location: The square the agent starts in.
        steps: How many time steps to run.
        move_cost: Points charged for each move.

    Returns:
        The finished environment.
    """
    environment = VacuumEnvironment(
        status=status, location=location, move_cost=move_cost
    )
    for _ in range(steps):
        environment.step(agent(environment.percept()))
    return environment
