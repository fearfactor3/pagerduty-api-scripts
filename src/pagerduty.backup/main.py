import os, json, shutil
from pdpyras import APISession
from dotenv import load_dotenv
load_dotenv()
from pd_calls import *

class WritePaths:
    def __init__(self, path: str) -> None:
        self.path = f"{path}/pagerduty-files"
        self.business_services = f"{self.path}/business_services"
        self.escalation_policies = f"{self.path}/escalation_policies"
        self.event_rules = f"{self.path}/event_rules"
        self.priorities = f"{self.path}/priorities"
        self.rulesets = f"{self.path}/rulesets"
        self.schedules = f"{self.path}/schedules"
        self.services = f"{self.path}/services"
        self.teams = f"{self.path}/teams"
        self.users = f"{self.path}/users"

        self.business_services_ind = f"{self.business_services}/individual"
        self.escalation_policies_ind = f"{self.escalation_policies}/individual"
        self.event_rules_ind = f"{self.event_rules}/rulesets"
        self.priorities_ind = f"{self.priorities}/individual"
        self.rulesets_ind = f"{self.rulesets}/individual"
        self.schedules_ind = f"{self.schedules}/individual"
        self.services_ind = f"{self.services}/individual"
        self.teams_ind = f"{self.teams}/individual"
        self.users_ind = f"{self.users}/individual"

    def rm_dirs(self) -> None:
        """Removes the folders. These are everything inside self.path.
        """
        shutil.rmtree(self.path, ignore_errors=True)

    def mk_dirs(self) -> None:
        """Creates the folders if they do not exist yet. These are the object attribute values.
        """
        [os.makedirs(value, exist_ok=True) for attr, value in self.__dict__.items()]


def main():
    # Defining paths
    write_path = os.getcwd()
    paths = WritePaths(write_path)
    
    # Create the API Session
    api_key = os.environ['PD_API_KEY']
    try:
        session = APISession(api_key)
    except :
        raise

    # Deleting previous folder content and creating the new one
    paths.rm_dirs()
    paths.mk_dirs()

    # Call to the pd_functions
    list_all(session, paths)

if __name__ == "__main__":
    main()