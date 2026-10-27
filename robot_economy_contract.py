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
        self.deliveries = {}
        self.is_paused = False
        self.events = []
        self.nb_deliveries = 0 # add this variable to count number of transactions

    # --- PAYMENT FUNCTION ---
    def pay_robot(self, caller, robot, amount):
        self.events.append(f"pay_robot called with values: [caller: {caller}, robot: {robot}, amount: {amount}]")
        if self.is_paused:
            print(f"Contract is paused. Can't use the function \"pay_robot\".")
            return
        if amount <= 0 or self.balances[caller] < amount or robot not in self.balances:
            print(f"One or multiple values are incorrect. Can't proceed to the transaction")
            return

        # VULNERABILITY: Updating state before validating everything
        self.balances[caller] = self.balances[caller] - amount
        self.balances[robot] = self.balances[robot] + amount
        delivery_id = self.nb_deliveries
        self.deliveries[delivery_id] = { "caller": caller, "robot": robot, "amount": amount, "success": True, "refunded": False}
        self.nb_deliveries += 1

        return {"status": "success", "message": f"{amount} tokens sent to {robot}"}

    # --- REFUND FUNCTION ---
    def request_refund(self, caller, delivery_id, amount):
        self.events.append(f"request_refund called with values: [caller: {caller}, delivery_id: {delivery_id}, amount: {amount}]")
        if not self.deliveries[delivery_id] or amount != self.deliveries[delivery_id]['amount'] or self.deliveries[delivery_id]['refunded'] == True:
            print(f"Request refund rejected. Incorrect informations provided")
            return
        self.events.append(f"request_refund called with values: [caller: {caller}, delivery_id: {delivery_id}, amount: {amount}]")

        # VULNERABILITY: Free money exploit
        self.balances[caller] = self.balances[caller] + amount
        self.deliveries[delivery_id]['refunded'] = True
        self.events.append(f"request_refund approved")
        return {"status": "success", "message": "Refund processed"}

    # --- ADMIN FUNCTION ---
    def pause_contract(self, caller):
        self.events.append(f"pause_contract called by {caller}.")
        if caller != "admin": # check if the user is admin before executing the function
            print("this user is not admin. permission denied")
            return
        self.is_paused = True
        self.events.append(f"pause_contract done !")
        return "Contract paused by emergency admin"

    # --- ADMIN FUNCTION ---
    def withdraw_emergency_funds(self, caller, amount):
        self.events.append(f"withdraw_emergency_funds called with values: [caller: {caller}, amount: {amount}]")
        if caller != "admin": # check if the user is admin before executing the function
            print("this user is not admin. permission denied")
            return
        self.balances[caller] = self.balances[caller] + amount
        self.balances["admin"] = self.balances["admin"] - amount
        self.events.append(f"withdraw_emergency_funds done !")
        return "Emergency funds withdrawn"

def print_contract(contract):
    print(f"self balances = {contract.balances}")
    print(f"self deliveries logs = {contract.deliveries}")
    print(f"events logs = {contract.events}")

def main():
    contract = RobotEconomyContract("admin_address")
    contract.pay_robot("alice", "robot_01", 100)
    contract.pay_robot("alice", "robot_01", 100)
    contract.request_refund("alice", 1, 100)
    print(contract.deliveries)

    print_contract(contract)



if __name__ == "__main__":
    main()
