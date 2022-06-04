def extract_suspicious(processes):
    suspicious_processes = []
    for process in processes:
        if process['cpu_usage'] > 50:
            suspicious_processes.append(process)
    return suspicious_processes