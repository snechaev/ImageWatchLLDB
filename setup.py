import os
import shutil

# Path to the current directory
currPath = os.path.dirname(os.path.realpath(__file__))

# Check that all the necessary modules exist
try:
    import cv2
except ImportError:
    raise ImportError('Missing package cv2')
try:
    import PIL
except ImportError:
    raise ImportError('Missing package pillow')

# Write necessary files
with open(os.path.join(os.path.expanduser('~'), '.pythonrc'), 'a') as currFile:
	currFile.write('import sys\n  sys.path = sys.path + ["/Applications/Xcode.app/Contents/SharedFrameworks/LLDB.framework/Resources/Python"]')

with open(os.path.join(os.path.expanduser('~'), '.bash_profile'), 'a') as currFile:
    currFile.write('# LLDB debug\n  export PYTHONSTARTUP="$HOME/.pythonrc"\n')
    
with open(os.path.join(os.path.expanduser('~'), '.lldbinit'), 'w') as currFile:
    currFile.write('command script import %s' % os.path.join(currPath, r'files', 'iw.py'))