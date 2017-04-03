import json
import pandas as pd

class Policy():
    def __init__(self, policy_path, user, location, device):
        """
        Constructor of policy.
        Policy is expected to have characteristics of location, devices, and
        user information.

        Parameters
        ----------
        policy_path: string
            path to json file to define policy

        Returns
        -------
        """
        self.document = json.load(open(policy_path))
        self.devices = pd.read_csv('./data/devices.csv')

    def enforce_policy(self):
        """
        Enforcment of policy.
        Based on the rules specified in the policy and the request attributes,
        a decision will be made to grant access to the RabbitMQ communication.

        Parameters
        ----------

        Returns
        -------
        access: boolean
            value indicating whether access is granted
        """
