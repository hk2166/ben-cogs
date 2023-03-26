import io
import discord
from redbot.core import commands
from PIL import Image, ImageFilter, ImageDraw

class ImageManipulation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def blur(self, ctx, radius: int = 5, user: typing.Union[int, discord.User] = None):
    """Applies a Gaussian blur to an attached image, a mentioned user's avatar, or a user's avatar using their ID."""
    if ctx.message.attachments or user:
        # Apply blur based on the first available source (attachment or user ID/mention)
        if ctx.message.attachments:
            img = await ctx.message.attachments[0].read()
            img = Image.open(io.BytesIO(img)).convert('RGB')
        else:
            if isinstance(user, int):
                user = await self.bot.fetch_user(user)
            avatar_url = user.avatar_url_as(format='png', size=1024)
            img = await avatar_url.read()
            img = Image.open(io.BytesIO(img)).convert('RGB')
        
        # Apply blur and send the result
        img_blur = img.filter(ImageFilter.GaussianBlur(radius=radius))
        with io.BytesIO() as img_buffer:
            img_blur.save(img_buffer, format='PNG')
            img_buffer.seek(0)
            await ctx.send(file=discord.File(img_buffer, filename='blurred.png'))
    else:
        await ctx.send("Please attach an image, mention a user, or provide a user ID to apply the blur.") 




@commands.command()
async def circle(self, ctx):
    """Draws a circle on an attached image."""
    if not ctx.message.attachments and not ctx.message.mentions:
        await ctx.send("Please attach an image to draw the circle.")
        return

    # Check if an image attachment was provided, otherwise try to grab the user's avatar
    if ctx.message.attachments:
        img_url = ctx.message.attachments[0].url
    else:
        user_id = ctx.message.mentions[0].id
        img_url = str(ctx.bot.get_user(user_id).avatar_url_as(format='png'))

    # Download the image and draw a circle
    img = await get_image(img_url)
    img = img.convert('RGBA')
    img_circle = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img_circle)
    draw.ellipse((0, 0, img.size[0], img.size[1]), fill=(255, 255, 255, 128))
    img_circle.putalpha(128)

    # Composite the circle onto the original image and send it
    img.paste(img_circle, mask=img_circle)
    with io.BytesIO() as img_buffer:
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        await ctx.send(file=discord.File(img_buffer, filename='circled.png'))


@commands.command()
async def grayscale(self, ctx):
    """Converts an attached image to grayscale."""
    if not ctx.message.attachments and not ctx.message.mentions:
        await ctx.send("Please attach an image to convert to grayscale.")
        return

    # Check if an image attachment was provided, otherwise try to grab the user's avatar
    if ctx.message.attachments:
        img_url = ctx.message.attachments[0].url
    else:
        user_id = ctx.message.mentions[0].id
        img_url = str(ctx.bot.get_user(user_id).avatar_url_as(format='png'))

    # Download the image and convert to grayscale
    img = await get_image(img_url)
    img = img.convert('L')

    # Save and send the grayscale image
    with io.BytesIO() as img_buffer:
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        await ctx.send(file=discord.File(img_buffer, filename='grayscale.png'))


@commands.command()
async def rotate(self, ctx):
    """Flips an attached image horizontally."""
    if not ctx.message.attachments and not ctx.message.mentions:
        await ctx.send("Please attach an image to flip.")
        return

    # Check if an image attachment was provided, otherwise try to grab the user's avatar
    if ctx.message.attachments:
        img_url = ctx.message.attachments[0].url
    else:
        user_id = ctx.message.mentions[0].id
        img_url = str(ctx.bot.get_user(user_id).avatar_url_as(format='png'))

    # Download the image and flip horizontally
    img = await get_image(img_url)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)

    # Save and send the flipped image
    with io.BytesIO() as img_buffer:
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        await ctx.send(file=discord.File(img_buffer, filename='flipped.png'))


