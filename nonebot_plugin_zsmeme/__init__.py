from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import PluginMetadata
from .utils import the_meme_url


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
    the_url = str(the_meme_url())
    await pgr_meme.send(MessageSegment.image(the_url))
