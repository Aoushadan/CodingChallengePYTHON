from dao.policy_service_impl import PolicyServiceImpl
from exceptions.policy_not_found_exception import PolicyNotFoundException

# Create the service instance
service = PolicyServiceImpl()

try:
    # Try to get a policy with an ID that doesn't exist in your DB (like 9999)
    service.get_policy(9999)
except PolicyNotFoundException as e:
    print(" Exception caught:", e)
except Exception as e:
    print(" General error:", e)
