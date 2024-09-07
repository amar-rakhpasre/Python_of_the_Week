import os # improt a library into your code

print(os.system('df -h')) #for linux or mac disk space

print(os.system('uptime')) #uptime and load average

print(os.system('free -h')) #Unused memory.

print(os.system('total')) #Total installed memory.

print(os.system('used -h')) #Memory currently in use (excluding buffers and cache).

print(os.system('shared -h')) # Memory used by tmpfs and shared between processes.

print(os.system('buff/cache')) # The sum of buffer and cache memory, which are used by the operating system to speed up processes

print(os.system('available -h')) #An estimation of how much memory is available for starting new applications, without swapping.
