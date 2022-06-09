import os, json
from main import WritePaths
from pdpyras import APISession

def list_business_services(session:APISession, paths: WritePaths) -> None:
    """Gets all of the services by accessing the https://api.pagerduty.com/services endpoint. 
    Writes the output as json files.

    Args:
        session APISession): PagerDuty session
        paths (WritePaths): object containing all the path locations
    """
    print("Generating the business services ...")
    objects_list = []
    counter = 0

    for item in session.iter_all("business_services"):
        # Append to large json
        objects_list.append(item)
        counter += 1
        # Write the individual json
        id = item["id"]
        with open(f"{paths.business_services_ind}/{id}.json", "w") as f:
            json.dump(item, f, indent=4, ensure_ascii=False)

    # Write the large json
    with open(f"{paths.business_services}/business_services.json", "w") as f:
        json.dump(objects_list, f, indent=4, ensure_ascii=False)

    print(f"Finished business services - total of {counter}!")

def list_escalation_policies(session: APISession, paths: WritePaths) -> None:
    """Gets all of the escalation policies by accessing the https://api.pagerduty.com/escalation_policies endpoint. 
    Writes the output as json files.

    Args:
        session (APISession): PagerDuty session
        paths (WriePaths): object containing all the path locations
    """
    print("Generating the escalation policies ...")
    objects_list = []
    counter = 0

    for item in session.iter_all("escalation_policies"):
        # Append to large json
        objects_list.append(item)
        counter += 1
        # Write the individual json
        id = item["id"]
        with open(f"{paths.escalation_policies_ind}/{id}.json", "w") as f:
            json.dump(item, f, indent=4, ensure_ascii=False)

    # Write the large json
    with open(f"{paths.escalation_policies}/escalation_policies.json", "w") as f:
        json.dump(objects_list, f, indent=4, ensure_ascii=False)

    print(f"Finished escalation policies - total of {counter}!")

def list_priorities(session: APISession, paths: WritePaths) -> None:
    """Gets all of the priorities by accessing the https://api.pagerduty.com/priorities endpoint. 
    Writes the output as json files.

    Args:
        session (APISession): PagerDuty session
        paths (WritePaths): object containing all the path locations
    """
    print("Generating the priorities ...")
    objects_list = []
    counter = 0

    for item in session.iter_all("priorities"):
        # Append to large json
        objects_list.append(item)
        counter += 1
        # Write the individual json
        id = item["id"]
        with open(f"{paths.priorities_ind}/{id}.json", "w") as f:
            json.dump(item, f, indent=4, ensure_ascii=False)

    # Write the large json
    with open(f"{paths.priorities}/priorities.json", "w") as f:
        json.dump(objects_list, f, indent=4, ensure_ascii=False)

    print(f"Finished priorities - total of {counter}!")

def list_rulesets(session: APISession, paths: WritePaths) -> None:
    """Gets all of the rulesets by accessing the https://api.pagerduty.com/rulesets endpoint. 
    Writes the output as json files.

    Args:
        session (APISession): PagerDuty session
        paths (WritePaths): object containing all the path locations
    """
    print("Generating the rulesets ...")
    objects_list = []
    counter = 0

    for item in session.iter_all("rulesets"):
        # Append to large json
        objects_list.append(item)
        counter += 1
        # Write the individual json
        id = item["id"]
        with open(f"{paths.rulesets_ind}/{id}.json", "w") as f:
            json.dump(item, f, indent=4, ensure_ascii=False)

    # Write the large json
    with open(f"{paths.rulesets}/rulesets.json", "w") as f:
        json.dump(objects_list, f, indent=4, ensure_ascii=False)

    print(f"Finished rulesets - total of {counter}!")

def list_event_rules(session: APISession, paths: WritePaths) -> None:
    """Gets all of the event rules by accessing the https://api.pagerduty.com/rulesets/$rule_id/rules endpoint. 
    Writes the output as json files.

    Args:
        session (APISession): PagerDuty session
        paths (WritePaths): object containing all the path locations
    """
    print("Generating the event rules ...")
    objects_list = []
    counter = 0

    for ruleset in session.iter_all("rulesets"):
        ruleset_id = ruleset["id"]
        os.makedirs(f"{paths.event_rules}/{ruleset_id}", exist_ok=True)
        for item in session.iter_all(f"rulesets/{ruleset_id}/rules"):
            # Append to large json
            objects_list.append(item)
            counter += 1
            # Write the individual json
            id = item["id"]
            with open(f"{paths.event_rules}/{ruleset_id}/{id}.json", "w") as f:
                json.dump(item, f, indent=4, ensure_ascii=False)

    # Write the large json
    with open(f"{paths.event_rules}/event_rules.json", "w") as f:
        json.dump(objects_list, f, indent=4, ensure_ascii=False)

    print(f"Finished rulesets event rules - total of {counter}!")

def list_schedules(session: APISession, paths: WritePaths) -> None:
    """Gets all of the schedules by accessing the https://api.pagerduty.com/schedules endpoint. 
    Writes the output as json files.

    Args:
        session (APISession): PagerDuty session
        paths (WritePaths): object containing all the path locations
    """
    print("Generating the schedules ...")
    objects_list = []
    counter = 0

    for item in session.iter_all("schedules"):
        # Append to large json
        objects_list.append(item)
        counter += 1
        # Write the individual json
        id = item["id"]
        with open(f"{paths.schedules_ind}/{id}.json", "w") as f:
            json.dump(item, f, indent=4, ensure_ascii=False)

    # Write the large json
    with open(f"{paths.schedules}/schedules.json", "w") as f:
        json.dump(objects_list, f, indent=4, ensure_ascii=False)

    print(f"Finished schedules - total of {counter}!")

def list_services(session: APISession, paths: WritePaths) -> None:
    """Gets all of the services by accessing the https://api.pagerduty.com/services endpoint. 
    Writes the output as json files.

    Args:
        session (APISession): PagerDuty session
        paths (WritePaths): object containing all the path locations
    """
    print("Generating the services ...")
    objects_list = []
    counter = 0

    for item in session.iter_all("services"):
        # Append to large json
        objects_list.append(item)
        counter += 1
        # Write the individual json
        id = item["id"]
        with open(f"{paths.services_ind}/{id}.json", "w") as f:
            json.dump(item, f, indent=4, ensure_ascii=False)

    # Write the large json
    with open(f"{paths.services}/services.json", "w") as f:
        json.dump(objects_list, f, indent=4, ensure_ascii=False)

    print(f"Finished services - total of {counter}!")

def list_teams(session: APISession, paths: WritePaths) -> None:
    """Gets all of the teams by accessing the https://api.pagerduty.com/teams endpoint. 
    Writes the output as json files.

    Args:
        session (APISession): PagerDuty session
        paths (WritePaths): object containing all the path locations
    """
    print("Generating the teams ...")
    objects_list = []
    counter = 0

    for item in session.iter_all("teams"):
        # Append to large json
        objects_list.append(item)
        counter += 1
        # Write the individual json
        id = item["id"]
        with open(f"{paths.teams_ind}/{id}.json", "w") as f:
            json.dump(item, f, indent=4, ensure_ascii=False)

    # Write the large json
    with open(f"{paths.teams}/teams.json", "w") as f:
        json.dump(objects_list, f, indent=4, ensure_ascii=False)

    print(f"Finished teams - total of {counter}!")

def list_users(session: APISession, paths: WritePaths) -> None:
    """Gets all of the users by accessing the https://api.pagerduty.com/users endpoint. 
    Writes the output as json files.

    Args:
        session (APISession): PagerDuty session
        paths (WritePaths): object containing all the path locations
    """
    print("Generating the users ...")
    objects_list = []
    counter = 0

    for item in session.iter_all("users"):
        # Append to large json
        objects_list.append(item)
        counter += 1
        # Write the individual json
        id = item["id"]
        with open(f"{paths.users_ind}/{id}.json", "w") as f:
            json.dump(item, f, indent=4, ensure_ascii=False)

    # Write the large json
    with open(f"{paths.users}/users.json", "w") as f:
        json.dump(objects_list, f, indent=4, ensure_ascii=False)

    print(f"Finished users - total of {counter}!")


def list_all(session: APISession, paths: WritePaths) -> None:
    """Goes through every function above and generates the json files.

    Args:
        session (APISession): PagerDuty session
        paths (WritePaths): object containing all the path locations
    """
    list_business_services(session, paths)
    list_escalation_policies(session, paths)
    list_event_rules(session, paths)
    list_priorities(session, paths)
    list_rulesets(session, paths)
    list_schedules(session, paths)
    list_services(session, paths)
    list_teams(session, paths)
    list_users(session, paths)