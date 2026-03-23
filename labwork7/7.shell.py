import subprocess
import shlex
import os
import sys


def execute_command(command: str):
    command = command.strip()
    if not command:
        return

    # PIPE |
    if "|" in command:
        execute_pipe(command)
        return

    tokens = shlex.split(command)

    stdin = None
    stdout = None

    # INPUT REDIRECTION <
    if "<" in tokens:
        idx = tokens.index("<")
        filename = tokens[idx + 1]
        stdin = open(filename, "r")
        tokens = tokens[:idx]

    # OUTPUT REDIRECTION >
    if ">" in tokens:
        idx = tokens.index(">")
        filename = tokens[idx + 1]
        stdout = open(filename, "w")
        tokens = tokens[:idx]

    try:
        process = subprocess.Popen(
            tokens,
            stdin=stdin,
            stdout=stdout,
            stderr=sys.stderr,
            shell=False
        )
        process.wait()
    except FileNotFoundError:
        print("Command not found")

    if stdin:
        stdin.close()
    if stdout:
        stdout.close()


def execute_pipe(command: str):
    commands = [cmd.strip() for cmd in command.split("|")]

    prev_process = None

    for i, cmd in enumerate(commands):
        tokens = shlex.split(cmd)

        process = subprocess.Popen(
            tokens,
            stdin=prev_process.stdout if prev_process else None,
            stdout=subprocess.PIPE,
            stderr=sys.stderr,
            shell=False
        )

        if prev_process:
            prev_process.stdout.close()

        prev_process = process

    output, _ = prev_process.communicate()
    if output:
        print(output.decode(errors="ignore"), end="")


def shell():
    print("Python Shell (type 'exit' to quit)")
    print("Working directory:", os.getcwd())

    while True:
        try:
            command = input("pysh> ")
            if command in ("exit", "quit"):
                break
            execute_command(command)
        except KeyboardInterrupt:
            print()
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    shell()
