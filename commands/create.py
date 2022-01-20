# Command handler for the create command
import sys
print(sys.argv)
if '.py' in sys.argv[1]:
    print('New Python Project')
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
    