from Process import Process
import os


class Process_List:
    
    def __init__(self) -> None:

        self.proc_dict = {}
        self.counter = 0
    
    ## def getter,setter

    def addProc(self,p):
        self.proc_dict[p['pid']] = Process(p)

    def update(self,p,c):
        self.proc_dict[p].usage_update(c)

    def display_history(self):
        for i in self.proc_dict:
            print(self.proc_dict[i].process['pid']," -> ",self.proc_dict[i].history)

    def killAllProcs(self):
        for i in self.proc_dict:
            os.kill(self.proc_dict[i].process['pid'],9)
            # self.proc_dict.pop(self.proc_dict[i].process['pid'])

    def killProc(self,id):
        os.kill(id,9)
        self.proc_dict.pop(id.process['pid'])
        
    def increment_counter(self):
        self.counter+=1