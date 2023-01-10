from config import Config
from modules.grant_finder import GrantFinder
from modules.grant_writer import GrantWriter
from modules.grant_submitter import GrantSubmitter
from auth.user_management import UserManagement
from analytics.reporting import Reporting
from api.funding_org import FundingOrganization


def main():
    config = Config()
    grant_finder = GrantFinder(config)
    grant_writer = GrantWriter(config)
    grant_submitter = GrantSubmitter(config)
    user_management = UserManagement(config)
    reporting = Reporting(config)
    funding_org = FundingOrganization(config)

    # Interact with the user and guide them through the grant application process
    user_management.login()
    grants = grant_finder.search_grants(user_inputs)
    proposal = grant_writer.generate_proposal(user_inputs, grants)
    grant_submitter.submit_proposal(proposal, grant_id)
    reporting.track_progress(grant_id)
    funding_org.check_status(grant_id)
    user_management.logout()
