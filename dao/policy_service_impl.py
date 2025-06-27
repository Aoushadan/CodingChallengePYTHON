from util.db_conn_util import DBConnUtil
from dao.ipolicy_service import IPolicyService
from entities.policy import Policy
from exceptions.policy_not_found_exception import PolicyNotFoundException


class PolicyServiceImpl(IPolicyService):

    def create_policy(self, policy):
        conn = DBConnUtil.get_connection()
        if conn is None:
            raise Exception(" Failed to connect to the database")

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Policies (policyName, policyType, coverageAmount, premiumAmount) VALUES (?, ?, ?, ?)",
            (policy.policy_name, policy.policy_type, policy.coverage_amount, policy.premium_amount)
        )
        conn.commit()
        conn.close()
        print(" Policy created successfully.")
        return True

    def get_policy(self, policy_id):
        conn = DBConnUtil.get_connection()
        if conn is None:
            raise Exception(" Failed to connect to the database")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Policies WHERE policyId = ?", (policy_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Policy(*row)
        else:
            raise PolicyNotFoundException(f" Policy ID {policy_id} not found")

    def get_all_policies(self):
        conn = DBConnUtil.get_connection()
        if conn is None:
            raise Exception(" Failed to connect to the database")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Policies")
        rows = cursor.fetchall()
        conn.close()

        return [Policy(*row) for row in rows]

    def update_policy(self, policy):
        conn = DBConnUtil.get_connection()
        if conn is None:
            raise Exception(" Failed to connect to the database")

        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Policies SET policyName=?, policyType=?, coverageAmount=?, premiumAmount=? WHERE policyId=?",
            (policy.policy_name, policy.policy_type, policy.coverage_amount, policy.premium_amount, policy.policy_id)
        )
        conn.commit()
        conn.close()
        print(f"Policy ID {policy.policy_id} updated successfully.")
        return True

    def delete_policy(self, policy_id):
        conn = DBConnUtil.get_connection()
        if conn is None:
            raise Exception(" Failed to connect to the database")

        cursor = conn.cursor()
        cursor.execute("DELETE FROM Policies WHERE policyId=?", (policy_id,))
        conn.commit()
        conn.close()
        print(f"Policy ID {policy_id} deleted successfully.")
        return True
