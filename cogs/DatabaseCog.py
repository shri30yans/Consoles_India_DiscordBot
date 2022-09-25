from discord.ext import commands
import json


class DatabaseFunctions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # async def get_user_info(self, user):
    #     async with self.bot.pool.acquire() as connection:
    #         async with connection.transaction():
    #             await self.has_account(user, server_id)
    #             user_account = await connection.fetchrow(
    #                 "SELECT * FROM info WHERE user_id=$1", user.id
    #             )
    #             user_account = dict(user_account)
    #             return user_account

    async def get_user_rep(self, user, server_id):
        async with self.bot.pool.acquire() as connection:
            async with connection.transaction():
                await self.has_account(user, server_id)
                query = f'SELECT "{server_id}" FROM info WHERE user_id={user.id}'
                user_account = await connection.fetchrow(query)
                rep = user_account.get(server_id)
                return rep

    async def has_account(self, user, server_id):
        async def create_account(user):
            query = f"INSERT INTO info (user_id) VALUES ({user.id})"
            await connection.execute(query)

        if user.bot:
            return
        else:
            async with self.bot.pool.acquire() as connection:
                async with connection.transaction():
                    user_account = dict(
                        await connection.fetchrow(
                            "SELECT EXISTS(SELECT 1 FROM info WHERE user_id=$1)",
                            user.id,
                        )
                    )

                    if user_account["exists"] == False:
                        await create_account(user)
                    else:
                        return

    async def add_user_rep(self, user, server_id, amt ):
        if amt == 0:
            return
        elif user.bot:
            return
        else:
            await self.has_account(user, server_id)
            async with self.bot.pool.acquire() as connection:
                async with connection.transaction():
                    query = f'UPDATE info SET "{server_id}" = "{server_id}" + {amt} WHERE user_id={user.id}'
                    await connection.execute(query)

    async def set_user_rep(self, user, server_id, amt):
        if user.bot:
            return
        else:
            await self.has_account(user, server_id)
            async with self.bot.pool.acquire() as connection:
                async with connection.transaction():
                    query = f'UPDATE info SET "{server_id}" = {amt} WHERE user_id={user.id}'
                    await connection.execute(query)

    async def get_leaderboard(self, server_id, offset=None):
        async with self.bot.pool.acquire() as connection:
            async with connection.transaction():
                if offset is not None: #if we know how many entries we want
                    query = f'SELECT user_id, "{server_id}" FROM info ORDER BY "{server_id}" DESC LIMIT 10 OFFSET {offset}'
                    all_rows = await connection.fetch(query)
                    return all_rows
                else:
                    query = f'SELECT user_id, "{server_id}" FROM info ORDER BY "{server_id}" DESC'
                    all_rows = await connection.fetch(query)
                    return all_rows
async def setup(bot):
    await bot.add_cog(DatabaseFunctions(bot))
