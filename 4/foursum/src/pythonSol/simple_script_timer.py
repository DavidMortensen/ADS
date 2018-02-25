import time
import glob
import os


#print(type(all_files))
def run_script():
    print('Starting Script!')
    dir_100 = '../../data/ints-100-*.txt'
    dir_200 = '../../data/ints-200-*.txt'

    files_100 = glob.glob(dir_100)
    files_200 = glob.glob(dir_200)
    dir = files_100 + files_200
    times = []
    count = 0
    print('Loading For-Loop')
    for i in range(len(dir)):
        print('starting ', dir[count])
        start_time = time.time()
        os.system('python simple.py < ' + dir[count])
        end_time = time.time()
        run_time = end_time-start_time
        times.append(run_time)
        print('Finished ', dir[count])
        count += 1
    print(times)


run_script()