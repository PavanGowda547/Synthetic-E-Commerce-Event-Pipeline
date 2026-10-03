## Subprocess module 

This module lets you start and interact with other programs/process in python.
Some common things you can do with subprocess:
- Run shell commands or external programs
- Pass arguments to programs
- Capture stdout and stderr
- Send input to a process
- Check the exit/return code
- Set environment variables, working directories, timeouts, etc.

For example, the modern pattern for running a command and failing if it returns an error is:
```
subprocess.run(["ls", "-la"], check=True)
```

In this project when we run and collect the sythetic data, we need arguments so that when running we are able to provide the necessary load to the generator, so then we need to execute a script file which takes in the arguments the user provid arguments it will ctach it and runn the script which creates the necessary data to further generate events which are necessary, like a predefined set of things required to generate the events

Go through the `subrpocess-main-module.py` to understand how it works 

The subprocess is mainly a bridge between the python pipline and external programs/commands
You could use it for :
- Running data-generation scripts
- Running shell commands
- Running other Python programs
- Running external data-generation tools
- Passing parameters to generators
- Capturing generated program output
- Capturing errors
- Checking whether a process succeeded
- Getting exit codes
- Running long-running processes
- Streaming output while a process runs
- Sending input to another program
- Running multiple generators
- Running generators in parallel
- Managing process dependencies
- Running validation programs
- Running data-quality tools
- Running database CLI tools
- Running cloud/storage CLI tools
- Running Spark jobs
- Running shell scripts
- Running Java/Scala applications
- Running Docker commands
- Running Git commands
- Setting environment variables for a process
- Running a process in a specific directory
- Setting timeouts
- Terminating/killing processes
- Building retry mechanisms
- Building simple pipeline orchestration

#### Mental flow the program
```
                    Operating System
                          │
             ┌────────────┴────────────┐
             │                         │
             ↓                         ↓
       cli.py process          generate_catalog.py
       Process #100             Process #101
             │                         │
             │                         │
             └── subprocess ──────────┘

```

In this project, `subprocess` is used instead of simply calling a function because `generate_catalog.py` is designed as a **separate executable Python script** with its own command-line arguments and execution environment. A direct function call would run the generator inside the same Python process as `cli.py`, while `subprocess.run()` starts a **separate process**, passes arguments such as `--num-products`, `--num-users`, and `--seed`, waits for the script to finish, and can detect whether it succeeded or failed through its exit code. This separation can be useful when you want the catalog generator to remain an independent program that can also be run directly from the terminal or potentially replaced with another external tool later. In simple terms: **a function call says "run this piece of code inside my current program," whereas `subprocess` says "start this other program and let it do its job."**
