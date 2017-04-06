import json
import pandas as pd

class Policy():
    def __init__(self, policy_path, user, device, location):
        """
        Constructor of policy.
        Policy is expected to have characteristics of location, devices, and
        user information.

        Parameters
        ----------
        policy_path: string
            path to json file to define policy
        user: string
            name of user making request
        location: str
            context derved from humidity and temp sensors

        Returns
        -------
        """
        self.user = user
        self.device = device
        self.policy = json.load(open(policy_path))
        self.location = location

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

        if self.device in self.policy['devices'] and self.location in self.policy['locations'] and self.user in self.policy['users']:
            return True
        else:
            return False
