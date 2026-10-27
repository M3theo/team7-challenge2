class RobotEconomyContract:
    def __init__(self, admin_address):
        self.admin = admin_address
        self.balances = {
            "alice": 1000,
            "bob": 500,
            "robot_01": 0,
            "robot_02": 0,
            "admin": 10000,
        }
        self.deliveries = []
        self.is_paused = False
        self.events = []  # The devs created this but forgot to use it!

    # --- PAYMENT FUNCTION ---
    def pay_robot(self, caller, robot, amount):
        # TODO: Devs forgot to check if the contract is paused!
        # TODO: Devs forgot to check if amount is positive!
        # TODO: Devs forgot to check if caller has enough balance!
        # TODO: Devs forgot to check if the robot actually exists!

        # VULNERABILITY: Updating state before validating everything
        self.balances[caller] = self.balances[caller] - amount
        self.balances[robot] = self.balances[robot] + amount

        return {"status": "success", "message": f"{amount} tokens sent to {robot}"}

    # --- REFUND FUNCTION ---
    def request_refund(self, caller, delivery_id, amount):
        # TODO: Devs forgot to verify if the delivery actually failed!
        # TODO: Devs forgot to check if the refund amount matches the original payment!

        # VULNERABILITY: Free money exploit
        self.balances[caller] = self.balances[caller] + amount
        return {"status": "success", "message": "Refund processed"}

    # --- ADMIN FUNCTION ---
    def pause_contract(self, caller):
        # TODO: Devs forgot to check if the caller is the admin!
        self.is_paused = True
        return "Contract paused by emergency admin"

    # --- ADMIN FUNCTION ---
    def withdraw_emergency_funds(self, caller, amount):
        # TODO: Devs forgot to check if the caller is the admin!
        self.balances[caller] = self.balances[caller] + amount
        self.balances["admin"] = self.balances["admin"] - amount
        return "Emergency funds withdrawn"
