from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
 
    influencer_mapper = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    campaign_mapper = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.influencer_mapper:
            return f"{influencer_type} is not an allowed influencer type."

        try:
            influencer = next(filter(lambda i: i.username == username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:
            influencer = self.influencer_mapper[influencer_type](username, followers, engagement_rate)
            self.influencers.append(influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.campaign_mapper:
            return f"{campaign_type} is not a valid campaign type."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
            return f"Campaign ID {campaign_id} has already been created."
        except StopIteration:
            campaign = self.campaign_mapper[campaign_type](campaign_id, brand, required_engagement)
            self.campaigns.append(campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet" \
                   f" the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)
        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        reached_followers = {}
        if not self.campaigns:
            return None
        for c in self.campaigns:
            if not c.approved_influencers:
                continue
            for i in c.approved_influencers:
                if c not in i.campaigns_participated:
                    continue
                if c not in reached_followers:
                    reached_followers[c] = i.reached_followers(c.__class__.__name__)
                else:
                    reached_followers[c] += i.reached_followers(c.__class__.__name__)

        return reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = next(filter(lambda i: i.username == username, self.influencers))
        if len(influencer.campaigns_participated) == 0:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key = lambda c: (len(c.approved_influencers), -c.budget))
        result = self.calculate_total_reached_followers()
        message = "$$ Campaign Statistics $$\n"
        for c in sorted_campaigns:
            message += f"  * Brand: {c.brand}, Total influencers: {len(c.approved_influencers)}," \
                       f" Total budget: ${c.budget:.2f}, Total reached followers: {result[c]}\n"

        return message.strip('\n')