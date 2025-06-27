class Policy:
    def __init__(self, policy_id=None, policy_name=None, policy_type=None, coverage_amount=0.0, premium_amount=0.0):
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.coverage_amount = coverage_amount
        self.premium_amount = premium_amount

    def __str__(self):
        return f"[Policy] ID: {self.policy_id}, Name: {self.policy_name}, Type: {self.policy_type}, " \
               f"Coverage: {self.coverage_amount}, Premium: {self.premium_amount}"
