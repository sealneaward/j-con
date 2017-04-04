import json
import pandas as pd

class Policy():
    def __init__(self, policy_path, user, location, device, type):
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
        location: string
            location of request being made
        type: string
            request type (client or listener)

        Returns
        -------
        """
        self.user = user
        self.location = location
        self.device = device
        self.policy_document = json.load(open(policy_path))
        self.devices = pd.read_csv('./data/devices.csv')
        self.type = type

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
        if self.type == 'listen':
            policy = self.policy_document['listen']

        elif self.type == 'write':
            policy = self.policy_document['write']

        if self.device in policy['devices'] and self.location in policy['locations'] and self.user in policy['users']:
            return True
        else:
            return False
