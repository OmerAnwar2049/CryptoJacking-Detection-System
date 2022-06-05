from util import *

if __name__ == "__main__":

    sus_processes = extract_suspicious()

    print("Suspicous processes:")
    rule_builders = {}
    for process in sus_processes:
        print("=============")
        print(process["pid"])
        print(process["name"])
        print(process["cpu_usage"])
        print(process["create_time"])
        print("=============\n")
        rule_builders[process["pid"]] = RuleBuilder(loadRules(),process["name"],process["pid"])

    
    while rule_builders:
        for pid in rule_builders:
            rule_builders[pid].check_rules()

