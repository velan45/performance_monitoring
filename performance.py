import psutil
import re
import sys

class Performance:
    def __init__(self):
        pass

    def performance_info(self):
        my_dict = { 'type':"text/json", 'encoding': "utf-8", 'content': {}}
        regex = r"^\W\W\W"
        with open('config.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:

                var = re.findall(regex, line)
                param = None
                if not var:
                    if str(line) == 'cpu_times\n':
                        param = psutil.cpu_times(percpu=False)

                    elif str(line) == 'cpu_percent\n':
                        param = psutil.cpu_percent(interval=None, percpu=False)

                    elif str(line) == 'cpu_count\n':
                        param = psutil.cpu_count(logical=True)

                    elif str(line) == 'cpu_stats\n':
                        param = psutil.cpu_stats()

                    elif str(line) == 'cpu_freq\n':
                        param = psutil.cpu_freq(percpu=False)

                    elif str(line) == 'getloadavg\n':
                        param = psutil.getloadavg()

                    elif str(line) == 'virtual_memory\n':
                        param = psutil.virtual_memory()

                    elif str(line) == 'swap_memory\n':
                        param = psutil.swap_memory()
                    #print(repr(line))
                    my_dict['content'][line.strip()]= param
        #print(my_dict)
        return my_dict



if __name__ == '__main__':
    print('in main')
    my_comp_perf = Performance()
    print(my_comp_perf.performance_info())