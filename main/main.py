from entities.policy import Policy
from dao.policy_service_impl import PolicyServiceImpl
from exceptions.policy_not_found_exception import PolicyNotFoundException

def main():
    service = PolicyServiceImpl()

    while True:
        print("\nInsurance Management System - Menu")
        print("1. Add Policy")
        print("2. View Policy by ID")
        print("3. View All Policies")
        print("4. Update Policy")
        print("5. Delete Policy")
        print("6. Exit")
        choice = input("Enter choice: ")



        try:
            if choice == '1':
                name = input("Enter policy name: ")
                ptype = input("Enter policy type: ")
                coverage = float(input("Enter coverage amount: "))
                premium = float(input("Enter premium amount: "))
                policy = Policy(policy_name=name, policy_type=ptype, coverage_amount=coverage, premium_amount=premium)
                service.create_policy(policy)

            elif choice == '2':
                pid = int(input("Enter policy ID: "))
                policy = service.get_policy(pid)
                print(policy)

            elif choice == '3':
                policies = service.get_all_policies()
                for p in policies:
                    print(p)

            elif choice == '4':
                pid = int(input("Enter policy ID to update: "))
                name = input("Enter new name: ")
                ptype = input("Enter new type: ")
                coverage = float(input("Enter new coverage: "))
                premium = float(input("Enter new premium: "))
                policy = Policy(policy_id=pid, policy_name=name, policy_type=ptype,
                                coverage_amount=coverage, premium_amount=premium)
                service.update_policy(policy)

            elif choice == '5':
                pid = int(input("Enter policy ID to delete: "))
                service.delete_policy(pid)
                print("Policy deleted.")

            elif choice == '6':
                print("Exiting.")
                break

            else:
                print("Invalid choice.")

        except PolicyNotFoundException as e:
            print(e)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
