import re
import time
from datetime import datetime
from iqso import StartTime, iqthon
from iqso.Config import Config
from iqso.plugins import mention
help1 = ("**🝳 ⦙ كيفيه التنصيب :**")
help2 = ("**🝳 ⦙ قـائمـه الاوامـر :**\n**🝳 ⦙ قنـاه السـورس :** @D8_8Q\n**🝳 ⦙ شـرح اوامـر السـورس : @DevKiMo**\n**🝳 ⦙ شـرح فـارات السـورس : @DevKiMo** \n - اوامر الاونلاين تشتغل فقط في المجموعات ")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**‎⿻┊My 𖠄 {mention} ٫ **\n‌‎**⿻┊BoT 𖠄 {TG_BOT} ٫**\n**‌‎⿻┊TimE 𖠄 {TM} ٫**\n**‌‎⿻┊‌‎VeRsIoN 𖠄 (8.2) ,** \n**⿻┊‌‎Jethon Kimo 𖠄** @D8_8Q"
