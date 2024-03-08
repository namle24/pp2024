import os
import subprocess
import shlex

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()

def redirect_output(command, output_file):
    args = shlex.split(command)
    with open(output_file, 'w') as f:
        subprocess.call(args, stdout=f, stderr=subprocess.STDOUT)

def redirect_input(command, input_file):
    args = shlex.split(command)

    with open(input_file, 'r') as f:
        subprocess.call(args, stdin=f, stderr=subprocess.STDOUT)

while True:
    command = input("$ ")

    if command.strip() == "exit":
        break

    if '>' in command:
        command, output_file = command.split('>', 1)
        command = command.strip()
        output_file = output_file.strip()
        redirect_output(command, output_file)

    elif '<' in command:
        command, input_file = command.split('<', 1)
        command = command.strip()
        input_file = input_file.strip()
        redirect_input(command, input_file)

    else:
        output = execute_command(command)
        print(output)