import time
import glob
import os


#print(type(all_files))
def run_script():
    print('Starting Script!')
    dir_100 = '../../data/ints-100-*.txt'
    dir_200 = '../../data/ints-200-*.txt'
    dir_400 = '../../data/ints-400-*.txt'
    dir_800 = '../../data/ints-800-*.txt'

    files_100, files_200, files_400, files_800 = glob.glob(dir_100), glob.glob(dir_200), glob.glob(dir_400), glob.glob(dir_800)
    
    dir = files_100 + files_200 + files_400 + files_800
    times = []
    count = 0
    print('Loading For-Loop')
    for i in dir:
        print('starting ', i)
        start_time = time.time()
        os.system('python simplefast.py < ' + i)
        end_time = time.time()
        run_time = end_time-start_time
        times.append(run_time)
        print('Finished ', i, 'in time: ', run_time)
        count += 1
    print(times)


run_script()