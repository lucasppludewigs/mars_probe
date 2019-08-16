"""Case for Elo7 programming."""
import sys

from utils.logging import logging_setup
log = logging_setup()

"""Read data input."""
with open('input.txt','r') as f:
    input = f.read()
    lines = input.split('\n')

"""Data input ingestion"""
rectangle_size = lines[0].split(' ')
#if len(rectangle_size) > 2 | 
print('\n')
print('Rectangle size: {0}'.format(rectangle_size))
print('\n')
max_x = int(rectangle_size[0])
max_y = int(rectangle_size[1])

"""Multiple robots in Mars."""
lin = 1
positions_list = ['Positions:']
main_command_list = ['Commands:']
#print(positions_list)
#print(len(lines),'\n')
while lin < len(lines):
    """Get probes positions."""
    position = lines[lin].split(' ')
    position[0] = int(position[0])
    position[1] = int(position[1])
    positions_list.extend(position)
    """Get probes commands."""
    main_command_list.append(lines[lin+1])
    lin = lin+2

print('Input file:')
print(positions_list)
print(main_command_list)

"""Executing commands with multiple robots."""
c = 1
while c < len(main_command_list):
    command_list = list(main_command_list[c])
    for command in command_list:
        if command == 'M':
            if positions_list[3*c] == 'N':
                positions_list[(3*c)-1] = positions_list[(3*c)-1] + 1
                if positions_list[(3*c)-1] > max_y:
                    log.info('Your commands exceeds rectangle_size')
                    sys.exit()
            elif positions_list[3*c] == 'S':
                positions_list[(3*c)-1] = positions_list[(3*c)-1] - 1
                if positions_list[(3*c)-1] < 0:
                    log.info('Your commands exceeds rectangle_size')
                    sys.exit()
            elif positions_list[3*c] == 'E':
                positions_list[(3*c)-2] = positions_list[(3*c)-2] + 1
                if positions_list[(3*c)-2] > max_x:
                    log.info('Your commands exceeds rectangle_size')
                    sys.exit()
            elif positions_list[3*c] == 'W':
                positions_list[(3*c)-2] = positions_list[(3*c)-2] - 1
                if positions_list[(3*c)-1] < 0:
                    log.info('Your commands exceeds rectangle_size')
                    sys.exit()
            else:
                log.info('Something weird happened. Verify input.')
        elif command == 'L':
            if positions_list[3*c] == 'N':
                positions_list[3*c] = 'W'
            elif positions_list[3*c] == 'W':
                positions_list[3*c] = 'S'
            elif positions_list[3*c] == 'S':
                positions_list[3*c] = 'E'
            elif positions_list[3*c] == 'E':
                positions_list[3*c] = 'N'
            else:
                log.info('Something weird happened. Verify input.')
        elif command == 'R':
            if positions_list[3*c] == 'N':
                positions_list[3*c] = 'E'
            elif positions_list[3*c] == 'E':
                positions_list[3*c] = 'S'
            elif positions_list[3*c] == 'S':
                positions_list[3*c] = 'W'
            elif positions_list[3*c] == 'W':
                positions_list[3*c] = 'N'
            else:
                log.info('Something weird happened. Verify input.')
        else:
            log.info('Something weird happened. Verify input.')
    c = c+1

print('\nFinished executing commands.')
print(positions_list)

#print(position[6]) # verify input length

for line in lines:
    #print(line)
    a = 2

"""Data Input validation."""
#log.info('Empty line on input')
#log.info('Not a valid input')
#log.info('Your commands exceeds rectangle_size')

