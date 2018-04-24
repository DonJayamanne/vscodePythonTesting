# example.py
import os
print('Hello,', os.environ.get('WHO'), '!')

import myMod1.insideMyMod1
myMod1.insideMyMod1.this_is_inside_mymod1()