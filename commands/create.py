# Command handler for the create command
import sys
print(sys.argv)
if '.py' in sys.argv[1]:
    if 'p' in sys.argv:
        print('Creating a private repository')
    print('New Python Project')
    print('Github Repository')
elif '.js' in sys.argv[1]:
    print('Javascript Project')
elif '.java' in sys.argv[1]:
    print('Java Project')
elif '.html' in sys.argv[1]:
    print('Web Project')
elif '.css' in sys.argv[1]:
    print('Web Project')
else:
    print('Unknown Project')
    