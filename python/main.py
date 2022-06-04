from util import extract_suspicious




if __name__ == "__main__":

    sus_procs = {}
    sus_processes = extract_suspicious()
    # print(sus_processes)
    print("Suspicous processes:")
    for process in sus_processes:
        if process["pid"] not in sus_procs:
            print("=============")
            print(process["pid"])
            print(process["name"])
            print(process["cpu_usage"])
            print(process["create_time"])
            print("=============\n")
            sus_procs[process["pid"]] = process["cpu_usage"]

    print(sus_procs)