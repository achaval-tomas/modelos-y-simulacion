#!/bin/python3
import subprocess
import sys

N = int(sys.argv[1])

with open(f"../practico{N}/resultados.txt", "w") as f:
    for i in range(1, 10):
        output = subprocess.run(
            ["python3", f"../practico{N}/ej{i}.py"],
            stdout=subprocess.PIPE,
        ).stdout.decode('utf-8')

        f.write(output + "\n")

