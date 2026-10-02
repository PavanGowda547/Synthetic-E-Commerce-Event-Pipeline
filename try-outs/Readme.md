# Learning & Exploration

This directory is a space for understanding the codebase by actively experimenting with it.

The goal is not just to make the code work, but to understand **how and why it works.**

Instead of reading the entire codebase passively, I am using small experiments and focused examples to understand individual concepts, modules, functions, and design decisions.


## What I Am Trying to Do

For each concept I encounter, I want to:

1. Find a small piece of code or functionality to understand.
2. Create a simple example or experiment around it.
3. Run the code and observe the behaviour.
4. Modify the code and see what changes.
5. Add comments explaining what I understand.
6. Record anything that was confusing or surprising.
7. Document the decisions I made and why.
8. Keep the experiment small enough that I can easily come back to it later.

The purpose is to turn the process of exploring the codebase into a collection of understandable notes and experiments.

## Learning Through Experiments  
When I encounter something I don't fully understand, I create a small Python file to isolate that concept.

For example, while learning Python's random module, I can create a file containing small examples of:

- `random.random()`
- `random.uniform()`
- `random.randint()`
- `random.randrange()`
- `random.choice()`
- `random.choices()`
- `random.sample()`
- `random.shuffle()`

The purpose isn't to create production code.

The purpose is to answer questions such as:

> What does this function do?
> What does it return?
> Does it modify the original object?
> What happens with different inputs?
> Why does it behave this way?

For example, `random.shuffle()` initially produced an unexpected `None` value. Investigating that behaviour helped clarify that shuffle() modifies the list in place rather than returning a new list.

These small discoveries are part of the learning process and should be documented rather than forgotten.

## Keeping the Experiments Easy to Run

The experiments are run inside a consistent Docker-based Python environment.

The Docker image provides the Python environment and installed dependencies, while the source files are mounted into the container.

This allows me to repeatedly change and run Python files without rebuilding the environment for every code change.

The basic workflow is:

```
Understand something
       ↓
Create a small experiment
       ↓
Write / modify Python code
       ↓
Run the experiment
       ↓
Observe the result
       ↓
Investigate unexpected behaviour
       ↓
Add comments to the code
       ↓
Document what was learned
```

Different Python files can be run without changing the Docker configuration:
```
./run.sh random-module.py
```
```
./run.sh another-example.py
```
```
./run.sh experiment.py
```

The Docker environment is treated as the stable foundation, while the Python files are the things being continuously changed and explored.

## Code Comments

Comments are used to capture understanding directly next to the code.
For example:

```
# shuffle() modifies the existing list in place.
# It does not return the shuffled list.
random.shuffle(fruits)

print(fruits)
```

The comments should explain things that are useful for future understanding, especially behaviour that isn't immediately obvious.

The goal is not to comment every line.

The goal is to capture why something works the way it does.

## Learning Notes

Alongside the Python experiments, I will create separate Markdown files to record what I learn.

These notes can contain things such as:
- What I learned
- Questions I had
- Experiments I performed
- Unexpected behaviour
- Important Python concepts
- Important project concepts
- Decisions I made
- Why I made those decisions
- Things I initially misunderstood
- Things I want to investigate later

For example:
```
random-module.py
random-module.md
```

The Python file contains the experiment.

The Markdown file contains the reasoning and learning around that experiment.

## Decisions Matter
An important part of this process is documenting decisions rather than only documenting results.

For example:

> I decided to keep the Python experiments outside the Docker image and mount them at runtime because I expect the code to change frequently while the Python environment should remain stable.


This makes it easier to understand not only what the code does, but also why the development environment and code are structured this way.

## The Bigger Goal
The ultimate goal is to build a deeper understanding of the larger codebase by breaking it into smaller concepts.

Rather than trying to understand everything at once:
```
Large codebase
      ↓
Smaller concepts
      ↓
Focused experiments
      ↓
Observations
      ↓
Understanding
      ↓
Documented knowledge
```

Over time, these experiments and notes should become a personal reference for the codebase and the concepts behind it.

The documentation is therefore not intended to be a polished tutorial.

It is a record of the learning process, experiments, discoveries, and decisions made while understanding the system.
