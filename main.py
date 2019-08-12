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
    print(lin)
    """Get probes positions."""
    position = lines[lin].split(' ')
    positions_list.extend(position)
    print(positions_list)
    """Get probes commands."""
    print('comm:',lines[lin+1])
    main_command_list.append(lines[lin+1])
    print(main_command_list)
    lin = lin+2



position = lines[1].split(' ')
pos_x = int(position[0])
pos_y = int(position[1])
#print(pos_x,pos_x+1)
"""Becoming the command."""
command_list = list(lines[2])
#print('\n')
#print(lines[2],command_list)

"""Executing commands."""
print('\n')
print('Position: {0}'.format(position))
print('Commands: {0}'.format(command_list))

for command in command_list:
    print(command)
    if command == 'M':
        if position[2] == 'N':
            pos_y = pos_y + 1
            print('New pos: {0},{1},{2}'.format(pos_x,pos_y,position[2]))
            if pos_y > max_y:
                log.info('Your commands exceeds rectangle_size')
                sys.exit()
        elif position[2] == 'S':
            pos_y = pos_y - 1
            print('New pos: {0},{1},{2}'.format(pos_x,pos_y,position[2]))
            if pos_y < 0:
                log.info('Your commands exceeds rectangle_size')
                sys.exit()
        elif position[2] == 'E':
            pos_x = pos_x + 1
            print('New pos: {0},{1},{2}'.format(pos_x,pos_y,position[2]))
            if pos_x > max_x:
                log.info('Your commands exceeds rectangle_size')
                sys.exit()
        elif position[2] == 'W':
            pos_x = pos_x - 1
            print('New pos: {0},{1},{2}'.format(pos_x,pos_y,position[2]))
            if pos_y < 0:
                log.info('Your commands exceeds rectangle_size')
                sys.exit()
        else:
            log.info('Something weird happened. Verify input.')
    elif command == 'L':
        #print('yeah')
        #print(position[2])
        if position[2] == 'N':
            position[2] = 'W'
            #print('======New position: '+ position[2])
        elif position[2] == 'W':
            position[2] = 'S'
        elif position[2] == 'S':
            position[2] = 'E'
        elif position[2] == 'E':
            position[2] = 'N'
        else:
            log.info('Something weird happened. Verify input.')
    elif command == 'R':
        if position[2] == 'N':
            position[2] = 'E'
        elif position[2] == 'E':
            position[2] = 'S'
        elif position[2] == 'S':
            position[2] = 'W'
        elif position[2] == 'W':
            position[2] = 'N'
        else:
            log.info('Something weird happened. Verify input.')
    else:
        log.info('Something weird happened. Verify input.')

#print(position[6]) # verify input length

for line in lines:
    #print(line)
    a = 2

"""Data Input validation."""
#log.info('Empty line on input')
#log.info('Not a valid input')
#log.info('Your commands exceeds rectangle_size')

"""Data Output Construction"""
