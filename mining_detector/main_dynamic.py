from time import sleep
from Process_List import Process_List
from util import extract_suspicious
from static_detector import *
from util import extract_suspicious


def dynamic_analysis_intitiate():

    procList = Process_List()
    while (1):
        sus_processes = extract_suspicious()
        # print(sus_processes)
        # print("Suspicous processes:")
        for process in sus_processes:
            if process["pid"] not in procList.proc_dict:
                print("\n======New suspicious process=======")
                print(process["pid"])
                print(process["name"])
                print(process["cpu_usage"])
                print(process["create_time"])
                print("=============\n")

                procList.addProc(process)
                print(process)    
            else:
                procList.update(process["pid"],process["cpu_usage"])

        procList.display_history()    
        sleep(3)

        procList.increment_counter()

        if procList.counter%3 == 0:
            if len(procList.proc_dict)>0:
                procList.killAllProcs()



def static_analysis_initiate():
    s_monitor = Static_Detector()
    s_monitor.statrtMonitor()


if __name__ == "__main__":

    dynamic_analysis_intitiate()