import discord
from discord.ext import commands
import config
import datetime
import StockChecker.ScrapperConfig as ScrapperConfig

colourlist = config.embed_colours


class Tags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.launch_time = datetime.datetime.utcnow()

    @commands.command(
        name="ATC",
        aliases=["ps5 amazon atc",],
        help="Shows all Add to Cart links",
    )
    async def add_cart_links(self, ctx):
        embed = discord.Embed(title="Direct Add to Cart links")
        embed.add_field(
            name="Consoles Only",
            value=f'[PS5 Disc](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag={config.amazon_affiliate_tag}&ASIN.1=B09V59MD1P&Quantity.1=1)\
            \n[PS5 Digital](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag={config.amazon_affiliate_tag}&ASIN.1=B09V58Q6DY&Quantity.1=1)\
            \n[XSX](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag={config.amazon_affiliate_tag}&ASIN.1=B08J7QX1N1&Quantity.1=1)\
            \n[XSS](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag={config.amazon_affiliate_tag}&ASIN.1=B08J89D6BW&Quantity.1=1)\
            ',inline=False
        )
        embed.add_field(
            name="PS5 Bundles",
            value=f'[PS5 Camera Bundle](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag={config.amazon_affiliate_tag}&ASIN.1=B08NTT4RTQ&Quantity.1=1)\
            \n[PS5 DE Camera Bundle](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag=?tag={config.amazon_affiliate_tag}&ASIN.1=B08NTV53TC&Quantity.1=1)\
            \n[PS5 DE Remote Bundle](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag=?tag={config.amazon_affiliate_tag}&ASIN.1=B08NTVH9VG&Quantity.1=1)\
            \n[PS5 DE Pulse Bundle](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag=?tag={config.amazon_affiliate_tag}&ASIN.1=B08NTV1QDX&Quantity.1=1)\
            \n[PS5 DE Charging Station Bundle](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag=?tag={config.amazon_affiliate_tag}&ASIN.1=B08NTVHTPT&Quantity.1=1)\
            ',inline=False
        )
        embed.add_field(
            name="XSX Bundles",
            value=f'[XSX Gears Tactics Bundle](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag={config.amazon_affiliate_tag}&ASIN.1=B08NRLQ294&Quantity.1=1)\
            \n[XSX Blue Controller Bundle](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag=?tag={config.amazon_affiliate_tag}&ASIN.1=B08NRBNSPW&Quantity.1=1)\
            \n[XSX White Controller Bundle](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag=?tag={config.amazon_affiliate_tag}&ASIN.1=B08NRLS39X&Quantity.1=1)\
            \n[XSX Black Controller Bundle](https://www.amazon.in/gp/aws/cart/add.html?AssociateTag=?tag={config.amazon_affiliate_tag}&ASIN.1=B08NQZGSJ2&Quantity.1=1)\
            ',inline=False
        )
        
        embed.set_footer(
            icon_url=ctx.author.display_avatar.url,
            text=f"Requested by {ctx.message.author} • {self.bot.user.name}",
        )
        await ctx.send(embed=embed)

    @commands.command(
        name="Playstation",
        aliases=["ps5 links", "PS5", "PS5 DE"],
        help="Shows all PS5 links",
    )
    async def ps5links(self, ctx):
        embed = discord.Embed(title="PS5 Links")
        embed.add_field(
            name="Amazon Wishlist",
            value=f"[Wishlist]({ScrapperConfig.PS5_wishlist}?tag={config.amazon_affiliate_tag})",
            inline=False,
        )
        embed.add_field(
            name="Amazon",
            value=f"""
                    [Physical](https://www.amazon.in/dp/B09V59MD1P/?tag={config.amazon_affiliate_tag} "Physical edition")
                    [Digital](https://www.amazon.in/dp/B09V58Q6DY/?tag={config.amazon_affiliate_tag} "Digital edition")
                    [Physical HFW Edition](https://www.amazon.in/dp/B0B9GH5TTN/?tag={config.amazon_affiliate_tag} "Physical HFW edition")
                    [Digital HFW Edition](https://www.amazon.in/dp/B0B9GDVHQQ/?tag={config.amazon_affiliate_tag} "Digital HFW edition")
                    [Physical GT7 Edition](https://www.amazon.in/dp/B09YD71MZT/?tag={config.amazon_affiliate_tag} "Physical GT7 edition")
                    """,
        )
        embed.add_field(
            name="ShopatSC",
            value="""
                [Physical](https://shopatsc.com/products/playstation-5-console/ "Physical edition")
                [Digital](https://shopatsc.com/collections/playstation-5/products/playstation5-digital-edition/ "Digital edition")
                [Physical HFW Edition](https://shopatsc.com/collections/playstation-5/products/playstation-5-console-horizon-forbidden-west-voucher-inside-box "Physical HFW edition")
                [Digital HFW Edition](https://shopatsc.com/collections/playstation-5/products/playstation-5-digital-edition-with-horizon-forbidden-west-voucher-inside-box "Digital HFW edition")
                [Physical GT7 Edition](https://shopatsc.com/collections/playstation-5/products/playstation%C2%AE5-console-with-ps5-gran-turismo-7-standard-ed "Physical GT7 edition")

            """,
        )

        embed.add_field(
            name="Flipkart",
            value="""
            [Physical](https://www.flipkart.com/sony-playstation-5-cfi-1008a01r-825-gb-astro-s-playroom/p/itma0201bdea62fa/ "Physical edition")
            [Digital](https://www.flipkart.com/sony-playstation-5-cfi-1008b01r-825-gb-astro-s-playroom/p/itm8bf74f8d0b890?/ "Digital edition")
            [Physical HFW Edition](https://www.flipkart.com/sony-cfi-1108a01r-825-gb-ssd-horizon-forbidden-west-for-ps5-voucher-inside-box/p/itm1e58025bea2d9 "Physical HFW edition")
            [Digital HFW Edition](https://www.flipkart.com/sony-cfi-1108b01r-825-gb-ssd-horizon-forbidden-west-for-ps5-voucher-inside-box/p/itm3783a181f39d4 "Digital HFW edition")
            
            """,
        )
        embed.add_field(
            name="Croma",
            value='[Physical](https://www.croma.com/sony-playstation-5-825gb-ssd-cfi-1008a01r-white-/p/231643/ "Physical edition")\n[Digital](https://www.croma.com/sony-playstation-5-digital-edition-825gb-ssd-cfi-1008b01r-white-/p/231644/ "Digital edition")',
        )
        embed.add_field(
            name="Vijay Sales",
            value='[Physical](https://ps5.vijaysales.com/Sony-PS5-Console.html "Physical edition")\n[Digital](https://ps5.vijaysales.com/Sony-PS5-Console-Digital.html "Digital edition")',
        )
        embed.add_field(
            name="Reliance Digital",
            value='[Physical](https://www.reliancedigital.in/sony-playstation-5-console/p/491936180 "Physical edition")\n[Digital](https://www.reliancedigital.in/sony-playstation-5-console/p/491936181 "Digital edition")',
        )
        embed.add_field(
            name="E2Z (Formerly PPGC)",
            value='[Physical](https://e2zstore.com/product/playstation-5-console-ps5/ "Physical edition")\n[Digital](https://e2zstore.com/product/playstation-5-digital-edition-ps5/ "Digital edition")',
        )
        embed.add_field(
            name="Games the Shop",
            value='[Physical](https://www.gamestheshop.com/PlayStation-5-Console/5111/ "Physical edition")\n[Digital]( https://www.gamestheshop.com/PlayStation-5-Digital-Edition/5112/ "Digital edition")',
        )
        embed.add_field(
            name="Gameloot",
            value='[Physical](https://gameloot.in/shop/sony-playstation-5/ "Physical edition")\n[Digital]( https://gameloot.in/shop/sony-playstation-5-digital-edition// "Digital edition")',
        )
        embed.set_footer(
            icon_url=ctx.author.display_avatar.url,
            text=f"Requested by {ctx.message.author} • {self.bot.user.name}",
        )
        await ctx.send(embed=embed)

    @commands.command(
        name="Xbox", aliases=["XSX", "XSS"], help="Shows all Xbox page links"
    )
    async def xboxlinks(self, ctx):
        embed = discord.Embed(title="Xbox Links")
        embed.add_field(
            name="Amazon Wishlist",
            value=f"[Wishlist]({ScrapperConfig.XBOX_wishlist}?tag={config.amazon_affiliate_tag})",
            inline=False,
        )
        embed.add_field(
            name="Amazon",
            value=f"""
                [Xbox Series X](https://www.amazon.in/Xbox-Series-X/dp/B08J7QX1N1/?tag={config.amazon_affiliate_tag} "Xbox Series X")
                [XSX Halo Edition](https://www.amazon.in/dp/B09LMY7K1L/?tag={config.amazon_affiliate_tag} "XSX Halo Edition")
                [XSX Gear Tactics Bundle](https://www.amazon.in/dp/B08NRLQ294/?tag={config.amazon_affiliate_tag} "XSX Gear Tactics Bundle")
                [XSX White Controller Bundle](https://www.amazon.in/dp/B08NRLS39X/?tag={config.amazon_affiliate_tag} "XSX White controller Bundle")
                [XSX Black Controller Bundle](https://www.amazon.in/dp/B08NQZGSJ2/?tag={config.amazon_affiliate_tag} "XSX Black controller Bundle")
                [XSX Blue Controller Bundle Gears](https://www.amazon.in/dp/B08NRBNSPW/?tag={config.amazon_affiliate_tag} "XSX Blue controller Bundle")
                [Xbox Series S](https://www.amazon.in/Xbox-Series-S/dp/B08J89D6BW/?tag={config.amazon_affiliate_tag} "Xbox Series S")
                
                """,
        )
        embed.add_field(
            name="Flipkart",
            value="""
                [Xbox Series X](https://www.flipkart.com/microsoft-xbox-series-x-1024-gb/p/itm63ff9bd504f27 "Xbox Series X")
                [XSX Halo Edition](https://www.flipkart.com/microsoft-xbox-series-x-1000-gb-halo-infinite-game-digital-code/p/itmc66869fa47647 "XSX Halo Edition")
                [XSX Forza Bundle](https://www.flipkart.com/xbox-series-x-console-1000-gb-forza-horizon-4/p/itm2c0869097870c "XSX Forza Bundle Edition")
                [Xbox Series S](https://www.flipkart.com/microsoft-xbox-series-s-512-gb/p/itm13c51f9047da8 "Xbox Series S")""",
        )
        embed.add_field(
            name="Vijay Sales",
            value='[Xbox Series X](https://www.vijaysales.com/Xbox-Series-X-Gaming-Console-1-TB/16215 "Xbox Series X")\n[Xbox Series S](https://www.vijaysales.com/Xbox-Series-S-Gaming-Console-512-GB/16213 "Xbox Series S")',
        )
        embed.add_field(
            name="Reliance Digital",
            value='[Xbox Series X](https://www.reliancedigital.in/xbox-series-x-console-with-wireless-controller-1-tb/p/491934660 "Xbox Series X")\n[Xbox Series S](https://www.reliancedigital.in/xbox-series-s-console-with-wireless-controller-512-gb/p/491934659 "Xbox Series S")',
        )
        embed.add_field(
            name="E2Z (Formerly PPGC)",
            value='[Xbox Series X](https://e2zstore.com/product/xbox-series-x/ "Xbox Series X")\n[Xbox Series S](https://e2zstore.com/product/xbox-series-s/ "Xbox Series S")',
        )
        embed.set_footer(
            icon_url=ctx.author.display_avatar.url,
            text=f"Requested by {ctx.message.author} • {self.bot.user.name}",
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Tags(bot))
