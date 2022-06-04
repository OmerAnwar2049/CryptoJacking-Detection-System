from util import extract_suspicious




if __name__ == "__main__":

    sus_processes = extract_suspicious()

    print("Suspicous processes:")
    for process in sus_processes:
        print("=============")
        print(process["pid"])
        print(process["name"])
        print(process["cpu_usage"])
        print(process["create_time"])
        print("=============\n")
