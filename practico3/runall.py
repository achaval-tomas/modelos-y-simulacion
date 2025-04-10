#!/bin/python3
import subprocess

with open("resultados.txt", "w") as f:
    for i in range(1, 10):
        output = subprocess.run(
            ["python3", f"ej{i}.py"],
            stdout=subprocess.PIPE,
        ).stdout.decode('utf-8')

        f.write(output + "\n")

