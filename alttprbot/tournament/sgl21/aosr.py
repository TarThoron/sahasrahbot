from alttprbot.alttprgen.randomizer import roll_aosr
from alttprbot.tournament.core import TournamentConfig
from alttprbot_discord.bot import discordbot
from .sglcore import SGLRandomizerTournamentRace

class AOSR(SGLRandomizerTournamentRace):
    async def configuration(self):
        guild = discordbot.get_guild(590331405624410116)
        return TournamentConfig(
            guild=guild,
            racetime_category='sgl',
            racetime_goal="Aria of Sorrow Randomizer",
            event_slug="sgl21aosr",
            audit_channel=discordbot.get_channel(774336581808291863),
            commentary_channel=discordbot.get_channel(631564559018098698),
            coop=False
        )

    # TODO confirm flags with admins
    async def roll(self):
        self.seed_id, self.permalink = roll_aosr(logic='AreaTechTeirs', panther='Rand70Dup', boss='Vanilla', weight="2.5", kicker='false', levelexp='Vanilla')

    @property
    def seed_info(self):
        return self.permalink