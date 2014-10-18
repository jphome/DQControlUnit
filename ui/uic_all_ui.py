import os
for root, dirs, files in os.walk('.'):
    for file_name in files:
        if file_name.endswith('.ui'):
            print file_name
            os.system('pyuic4 -o Ui_%s.py -x %s' % (file_name.rsplit('.', 1)[0], file_name))
        elif file_name.endswith('.qrc'):
            print file_name
            os.system('pyrcc4 -o %s_rc.py %s' % (file_name.rsplit('.', 1)[0], file_name))
