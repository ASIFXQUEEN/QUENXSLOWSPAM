from pyrogram import idle
from SpamX.functions.clients import TheSpamX

async def main():
    await TheSpamX.startup()
    TheSpamX.logs.info("𝗤𝗨𝗘𝗘𝗡 ❣ 𝗔𝗦𝗜𝗙")
    await idle()
    await TheSpamX.SpamX.stop()
    await TheSpamX.stopAllClients()

if __name__ == "__main__":
    TheSpamX.run(main())
