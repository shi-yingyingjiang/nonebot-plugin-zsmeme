from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from httpx import AsyncClient
from nonebot.plugin import PluginMetadata
from .config import the_meme_url
from io import BytesIO


__plugin_meta__ = PluginMetadata(
    name='战双表情',
    description='发送bwiki的战双表情',
    usage='使用命令：战双表情/zsmeme',
    type="application",
    homepage="https://github.com/shi-yingyingjiang/nonebot-plugin-zsmeme",
    supported_adapters = {"nonebot.adapters.onebot.v11"},
)


pgr_meme = on_command("战双表情", aliases={'zsmeme','pgrmeme'})


@pgr_meme.handle()
async def get_img():
    async with AsyncClient() as client:
        image = await client.get(the_meme_url())
        picbytes = BytesIO(image.content).getvalue()
    try:
        await pgr_meme.send(MessageSegment.image(picbytes))
    except:
        await pgr_meme.send(f'发送失败')
