import random
import os
import importlib.util
from highrise import*
from highrise import BaseBot,Item,Position
from highrise.models import SessionMetadata

moderators = ["ABBY_LARRY_0.1","iMooseMoo","sachin24","jojoGogo196","Miwiii"]

casa = ["I Marry You 💍","Of course I do 💍❤️","I don't want to 💍💔","Of course I don't 💍💔","I Love You Of course I marry you 💍"]

curativo = ["🔴You Used the Bandage Your Life Is at: 100%🔴","🔴You Used the Bandage Your Life is at: 50%🔴","🔴You Used the Bandage Your Life is at: 60%🔴","🔴You Used Your Life Bandage is at: 75% Your Life is at: 90%🔴","🔴You Used the Bandage It is at: 91%🔴"]
         
bomba = ["💣🧟‍♂️ You Threw a Bomb on 1x Boss Zombie 🧟‍♀️💣","💣🧟 You Threw a Bomb on 3x Boss Zombie 🧟💣","💣🧟‍♂️ You Threw a Bomb on 2x Boss Zombie 💣🧟‍♀️","💣 🧟‍♂️ You Threw a Bomb on 7x Boss Zombie 💣🧟‍♂️","💣🧟 You Threw a Bomb on 4x Boss Zombie 🧟💣"]

facada = ["🧟🔪 You Stabbed 1x Zombie 🔪🧟","🧟🔪 You Stabbed 6x Zombie 🔪🧟","🧟🔪 You Stabbed 7x Zombie 🔪🧟","🧟‍♂️🔪🧟‍♂️ You Stabbed 8x Zombie 🔪🧟‍♂️","🧟 🔪 You Stabbed 10x Zombie 🔪🧟","🧟🔪 You Stabbed 9x Zombie 🔪🧟","🧟‍♀️🔪🧟‍♂️ You Stabbed 3x Zombie 🧟‍♂️🔪🧟‍♀️"]

atirar = ["🧟You Shot 5x Zombie🧟","🧟You Shot 1x Zombie🧟","🧟You Shot 8x Zombie🧟","🧟You Shot 3x Zombie🧟","🧟‍♂️You Shot 5x Zombie🧟‍♂️ ","🧟‍♀️You Shot 10x Zombie🧟‍♀️","🧟🧟‍♀️You Shot 9x Zombie 🧟🧟‍♀️"]

play = ["🔴Your Life is at 50% use : /bandage","🔴Your Life is at 20% use : /bandage","🔴Your Life is at 40% use : /bandage","🧟The Zombies Are Coming Use : /stab or /shoot","🧟🧟‍♂️ There Are Many Zombies 🧟‍♀️🧟 🛡 Use: /shield 🛡","🧟The Zombie Boss Is Coming Use: /bomb","🧟The Zombies Are Coming Use: /stab or/ shoot","🧟🧟‍♂️ There are Lots of Zombies 🧟‍♀️🧟 🛡 Use: /shield 🛡","🔴Your Life is at 60% use: /bandage","🔴Your Life is at 10% use: /bandage" ,"🧟The Zombies Are Coming Use : /stab or /shoot" ,"🧟The Zombies Are Coming Use : /stab or /shoot","🧟The Zombies Are Coming Use : /stab or /shoot","🧟The Zombies They're Coming Use : /stab or /shoot","🧟The Zombies Are Coming Use : /stab or /shoot","🧟The Zombies Are Coming Use : /stab or /shoot "]

pescar = ["🥈YOU WON THE MEDAL: SILVER FISHERMAN🥈","🥉YOU WON THE MEDAL: BRONZE FISHERMAN🥉","🥉YOU WON THE MEDAL: BRONZE FISHERMAN🥉","🥉YOU WON THE MEDAL: BRONZE FISHERMAN🥉","🥉YOU WON OR THE MEDAL: BRONZE FISHERMAN🥉","🟡Event: /carp 🟡","⚫️You Fished 3x Night Moon⚫️(+150 POINTS)","⚫️You Fished 2x Night Moon⚫️(+100 POINTS)"," ⚫️You Fished 1x Night Moon⚫️(+50 POINTS)","🟡You Fished 1x Golden Shrimp 🟡 (MULTIPLE POINT)","🟡You Fished 1x Golden Flounder🟡 (MULTIPLE POINT)","🪼🌈You Fished 1x Octopus Rainbow🪼🌈 (EXTRA POINTS)","🐢You Caught 3x Turtle 🐢 (LOSS OF POINTS)","🦑You Caught 1x Giant Squid 🦑 (LEGENDARY)","🦀You Caught 6x Crab 🦀 (COMMON)", "🦀You Caught 2x Crab 🦀 (COMMON)","🦀You Caught 8x Crab 🦀 (COMMON)","🪼You Caught 1x Sea Octopus🪼(EPIC)","🦈You Caught 2x Shark🦈 (EPIC)", "🦈You Fished 5x Sharks🦈 (EPIC)","🦈You Fished 8x Sharks🦈 (EPIC)","🦈You Fished 1x Sharks🦈 (EPIC)","🐠You Fished 1x Sea Tuna🐠 (LEGENDARY)", "🐠You Caught 3x Clown Fish🐠 (LEGENDARIOUS)","🐠You Caught 3x Sea Tuna🐠 (LEGENDARIOUS)","🐠You Caught 1x Clown Fish🐠 (LEGENDARIOUS)","🐠You Caught 8x Clown Fish🐠 (LEGENDARY) )","🐠You Caught 10x Clown Fish🐠 (LEGENDARY)","🐟You Caught 1x Salmon🐟 (RARE)","🧜🏼‍♀️You Caught 5x Mermaid🧜🏼‍♀️(EPIC)","🧜🏼‍ ♀️You Caught 2x Mermaid🧜🏼‍♀️(EPIC)","🧜🏼‍♀️You Caught 1x Mermaid🧜🏼‍♀️(EPIC)","🐟You Caught 3x Salmon🐟 (RARE)","🟡You Caught 1 x Tilapia Dourada🟡 (MULTIPLE POINT)","☠️🐋You Caught 3x Dead Whale☠️🐋 (LOSS OF POINTS)","🐋You Caught 11x Sea Whale🐋(COMMON)","🐋🌈You Caught 1x Rainbow Whale🌈 🐋 (EXTRA POINTS)","🥈YOU WON THE MEDAL: SILVER FISHERMAN🥈","🥇YOU WON THE MEDAL: GOLD FISHERMAN🥇","🏅YOU WON THE MEDAL: STAR FISHERMAN🏅","💎Event: /shrimp 💎"]

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("working")
        await self.highrise.walk_to(Position(4.5 , 0.0 , 1.5, "FrontLeft"))
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entrou na sala")   
        await self.highrise.send_whisper(user.id,f"Welcome {user.username} Use: !emote list or 1-97 For Emotes\n\nloop example: !loop 98 or !loop jetpack")

        await self.highrise.send_whisper(user.id,f"Use: /help For More Informations.")

        await self.highrise.send_whisper(user.id,f"Buy Bot Call @iMooseMoo in private.")
           
        await self.highrise.send_emote("hcc-jetpack")
      
        await self.highrise.send_emote("hcc-jetpack",user.id) 
      
    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")  

        if message.lower().startswith("!tipall ") and user.username in moderators:
              parts = message.split(" ")
              if len(parts) != 2:
                  await self.highrise.send_message(user.id, "Invalid command")
                  return
              # Checks if the amount is valid
              try:
                  amount = int(parts[1])
              except:
                  await self.highrise.chat("Invalid amount")
                  return
              # Checks if the bot has the amount
              bot_wallet = await self.highrise.get_wallet()
              bot_amount = bot_wallet.content[0].amount
              if bot_amount < amount:
                  await self.highrise.chat("Not enough funds")
                  return
              # Get all users in the room
              room_users = await self.highrise.get_room_users()
              # Check if the bot has enough funds to tip all users the specified amount
              total_tip_amount = amount * len(room_users.content)
              if bot_amount < total_tip_amount:
                  await self.highrise.chat("Not enough funds to tip everyone")
                  return
              # Tip each user in the room the specified amount
              for room_user, pos in room_users.content:
                  bars_dictionary = {
                      10000: "gold_bar_10k",
                      5000: "gold_bar_5000",
                      1000: "gold_bar_1k",
                      500: "gold_bar_500",
                      100: "gold_bar_100",
                      50: "gold_bar_50",
                      10: "gold_bar_10",
                      5: "gold_bar_5",
                      1: "gold_bar_1"
                  }
                  fees_dictionary = {
                      10000: 1000,
                      5000: 500,
                      1000: 100,
                      500: 50,
                      100: 10,
                      50: 5,
                      10: 1,
                      5: 1,
                      1: 1
                  }
                  # Convert the amount to a string of bars and calculate the fee
                  tip = []
                  remaining_amount = amount
                  for bar in bars_dictionary:
                      if remaining_amount >= bar:
                          bar_amount = remaining_amount // bar
                          remaining_amount = remaining_amount % bar
                          for i in range(bar_amount):
                              tip.append(bars_dictionary[bar])
                              total = bar + fees_dictionary[bar]
                  if total > bot_amount:
                      await self.highrise.chat("Not enough funds")
                      return
                  for bar in tip:
                      await self.highrise.tip_user(room_user.id, bar)

        if message.lower().startswith("!tipme ") and user.username in moderators:
                try:
                    amount_str = message.split(" ")[1]
                    amount = int(amount_str)
                    bars_dictionary = {
                        10000: "gold_bar_10k",
                        5000: "gold_bar_5000",
                        1000: "gold_bar_1k",
                        500: "gold_bar_500",
                        100: "gold_bar_100",
                        50: "gold_bar_50",
                        10: "gold_bar_10",
                        5: "gold_bar_5",
                        1: "gold_bar_1"
                    }
                    fees_dictionary = {
                        10000: 1000,
                        5000: 500,
                        1000: 100,
                        500: 50,
                        100: 10,
                        50: 5,
                        10: 1,
                        5: 1,
                        1: 1
                    }
                    # Get bot's wallet balance
                    bot_wallet = await self.highrise.get_wallet()
                    bot_amount = bot_wallet.content[0].amount
                    # Check if bot has enough funds
                    if bot_amount < amount:
                        await self.highrise.chat("Not enough funds in the bot's wallet.")
                        return
                    # Convert amount to bars and calculate total
                    tip = []
                    total = 0
                    for bar in sorted(bars_dictionary.keys(), reverse=True):
                        if amount >= bar:
                            bar_amount = amount // bar
                            amount %= bar
                            tip.extend([bars_dictionary[bar]] * bar_amount)
                            total += bar_amount * bar + fees_dictionary[bar]
                    if total > bot_amount:
                        await self.highrise.chat("Not enough funds to tip the specified amount.")
                        return
                    # Send tip to the user who issued the command
                    for bar in tip:
                        await self.highrise.tip_user(user.id, bar)
                    await self.highrise.chat(f"You have been tipped {amount_str}.")
                except (IndexError, ValueError):
                    await self.highrise.chat("Invalid tip amount. Please specify a valid number.")
                    
        if message.startswith("/fish"):
            await self.highrise.send_whisper(user.id,"You Are Fishing 🎣...")
          
        if message.lower() == "/fish":
           frase = random.choice(pescar)
           await self.highrise.send_whisper(user.id,frase)
        
        if message.lower() == "/bomb":
           frase = random.choice(bomba)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/stab":
           frase = random.choice(facada)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/curative":
           frase = random.choice(curativo)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/play":
           frase = random.choice(play)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/shoot":
           frase = random.choice(atirar)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/marry me?":
           frase = random.choice(casa)
           await self.highrise.chat(frase)
            

        if message.startswith("/carp"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"🟡You Caught 1x Golden Carp🟡 YOU WON THE MEDAL: (MEGA FISHERMAN) ")
          
        if message.startswith("/shrimp"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"💎You Caught 1x Diamond Shrimp💎YOU WON THE MEDAL: (DIAMANTE MASTER FISHERMAN  )")                                
        if message.startswith("/curative"):
           await self.highrise.react("heart",user.id)

        if message.startswith("/shield"):
           await self.highrise.react("heart",user.id)
           await self.highrise.send_whisper(user.id,f"@{user.username} 🛡 You Used The Shield 🛡")
            
        if        message.startswith("/tele") or              message.startswith("/tp") or              message.startswith("/fly") or     message.startswith("!tele") or      message.startswith("!tp") or     message.startswith("!fly"):
          if user.username in moderators:            await self.teleporter(message)

        if        message.startswith("/") or              message.startswith("-") or              message.startswith(".") or          message.startswith("!"):
            await self.command_handler(user, message)
          
        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Fashion All , Wrong All , Cutey All , Superpose All , Punk All , Tiktok2 All, Tiktok8 All , Tiktok9 All , Tiktok10 All , Gagging All , Blackpink All , Creepy All , Revelation All , Bashful All , Arabesque All , Party All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Pose3 All , Pose7 All , Pose5 All , Pose1 All , Enthused All , Pose8 All , Sing All , Teleport All , Telekinesis All , Casual All , Icecream All , Watch All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Zombie All , Celebrate All , Kiss All , Bow All , Snowangel All , Confused All , Charging All , Wei All , Cursing All , Greedy All , Russian All , Shop All , Model All , Ren All , Tiktok4 All , Snake All , Uwu All")

        if        message.startswith("-floor1") or message.startswith("!floor1") or message.startswith("-floor 1") or message.startswith("Floor 1") or message.startswith("Floor1") or message.startswith("/floor1") or    message.startswith("floor1") or message.startswith("-1") or                                 message.startswith("floor 1") or message.startswith("!floor 1"):
          await self.highrise.teleport(user.id, Position(3.5 , 0.0 , 7.0 ))

        if        message.startswith("-floor3") or message.startswith("!floor3") or message.startswith("-floor 3") or message.startswith("Floor 3") or message.startswith("Floor3") or message.startswith("/floor3") or    message.startswith("floor3") or message.startswith("-3") or                                 message.startswith("floor 3") or message.startswith("!floor 3"):
          await self.highrise.teleport(user.id, Position(15.0 , 15.2 , 9.5))
     
        if        message.startswith("-floor2") or message.startswith("!floor2") or message.startswith("-floor 2") or message.startswith("Floor 2") or message.startswith("Floor2") or message.startswith("/floor2") or    message.startswith("floor2") or message.startswith("-2") or                                 message.startswith("floor 2") or message.startswith("!floor 2"):
          await self.highrise.teleport(user.id, Position(10.5 , 8.0 , 3.5))
            
        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Skating All , Time All , Gottago All  , Scritchy All , Bitnervous All , Jingle All , Curtsy All , Hot All , Hyped All ,Sleigh All , Surprise All, Repose All , Kawaii All , Touch All , Gift All , Pushit All , Tiktok All , Smooch All , Launch All")
          
        if        message.startswith("/lista") or   message.startswith("/emotes") or         message.startswith("/emote list") or message.startswith("!emotes") or message.startswith("!emote list") or message.startswith("!lista"):
          await self.highrise.send_whisper(user.id,"🕺🏻Lista de emotes gratis:\n\n1.wrong\n2.fashion\n3.gravity\n4.icecream\n5.casual\n6.kiss\n7.no\n8.sad\n9.yes\n10.laughing\n11.hello\n12.wave\n13.shy\n14.tired\n15.flirtywave\n16.greedy\n17.model\n18.bow\n19.curtsy")

        if        message.startswith("/lista") or   message.startswith("/emotes") or         message.startswith("/emote list") or message.startswith("!emotes") or message.startswith("!emote list") or message.startswith("!lista"):
          await self.highrise.send_whisper(user.id,"\n20.snowball\n21.hot\n22.snowangel\n23.charging\n24.confused\n25.telekinesis\n26.float\n27.teleport\n28.maniac\n29.eneryball\n30.snake\n31.frog\n32.superpose\n33.cute\n34.pose7\n35.pose8\n36.pose1\n37.pose5\n38.pose3")

        if        message.startswith("/lista") or   message.startswith("/emotes") or         message.startswith("/emote list") or message.startswith("!emotes") or message.startswith("!emote list") or message.startswith("!lista"):
          await self.highrise.send_whisper(user.id,"\n39.cutey\n40.shuffle\n41.singalong\n42.enthused\n43.letsgoshopping\n44.russian\n45.pennywise\n46.dontstartnow\n47.blackpink\n48.celebrate\n49.gagging\n50.flex\n51.cursing\n52.thumbsup\n53.angry\n54.punk\n55.zombie\n56.sit\n57.fight")

        if        message.startswith("/lista") or   message.startswith("/emotes") or         message.startswith("/emote list") or message.startswith("!emotes") or message.startswith("!emote list") or message.startswith("!lista"):
          await self.highrise.send_whisper(user.id,"\n58.macarena\n59.weird\n60.savage\n61.viralgroove\n62.uwu\n63.sayso\n64.stargazer\n65.pose9\n66.boxer\n67.airguitar\n68.penguin\n69.astronaut\n70.saunter\n71.creepy\n72.watch\n73.revelations\n74.bashful\n75.arabesque\n76.party")

        if        message.startswith("/lista") or   message.startswith("/emotes") or         message.startswith("/emote list") or message.startswith("!emotes") or message.startswith("!emote list") or message.startswith("!lista"):
          await self.highrise.send_whisper(user.id,"\n77.skating\n78.scritchy\n79.bitnervous\n80.timejump\n81.gottago\n82.jingle\n83.hyped\n84.sleigh\n85.surprise\n86.repose\n87.kawaii\n88.touch\n89.foryou\n90.pushit\n91.salute\n92.attention\n93.tiktok\n.94.smooch\n95.launch\n96.fairyfloat\n97.fairytwirl\n98.jetpack")
            
        if        message.startswith("/lista") or         message.startswith("/emote list") or message.startswith("!emoteall") or message.startswith("!emote list") or message.startswith("!lista"):
            await self.highrise.send_emote("dance-floss")

        if        message.startswith("/peoples") or      message.startswith("!peoples"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There are {len(room_users)} people in the room  ")
            await self.highrise.send_emote("dance-floss")
                     
        if        message.startswith("Help") or      message.startswith("/help") or      message.startswith("!help") or message.startswith("help"):
            await self.highrise.chat(f"/emote list | /peoples | /emotes  | /marry me? | /play /fish /userinfo @ | !emoteall | !tele @ | !summon @ | !kick @ | !tele z,y,x | !tele @ z,y,x | !fit [1-11]")
            await self.highrise.chat(f"[Emote] All | !emote all [Emote] | !tipall [amount] | !tipme [amount]")        
            await self.highrise.chat(f"{user.username} all activation codes must be used >> ! or/")
            await self.highrise.send_emote("dance-floss")
          
        if        message.startswith("😡") or      message.startswith("🤬") or      message.startswith("😤") or             message.startswith("🤨") or             message.startswith("😒") or message.startswith("🙄"):
            await self.highrise.send_emote("emote-boxer",user.id)
   
        if        message.startswith("🤔") or      message.startswith("🧐") or      message.startswith("🥸") or             message.startswith("🫤") or message.startswith("😕"):
            await self.highrise.send_emote("emote-confused",user.id)

        if        message.startswith("🤣") or      message.startswith("😂") or             message.startswith("ja") or             message.startswith("Ha") or         message.startswith("Ka") or           message.startswith("Ja") or           message.startswith("ha") or          message.startswith("ks") or             message.startswith("kk") or             message.startswith("Kk") or message.startswith("😁") or message.startswith("😀"):
            await self.highrise.send_emote("emote-laughing",user.id)

        if        message.startswith("😗") or      message.startswith("😘") or      message.startswith("😙") or             message.startswith("💋") or             message.startswith("😚"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("😊") or      message.startswith("🥰") or      message.startswith("😳") or message.startswith("🤗"):
            await self.highrise.send_emote("idle-uwu",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("🤢") or      message.startswith("🤮") or      message.startswith("🤧") or             message.startswith("😵‍💫") or message.startswith("🤒"):
            await self.highrise.send_emote("emoji-gagging",user.id)

        if        message.startswith("😱") or      message.startswith("😬") or      message.startswith("😰") or             message.startswith("😫") or message.startswith("😨"):
            await self.highrise.send_emote("idle-nervous",user.id)

        if message.startswith("🤯"):
            await self.highrise.send_emote("emote-headblowup",user.id)

        if        message.startswith("☺️") or      message.startswith("🫣") or       message.startswith("😍") or      message.startswith("🥺") or message.startswith("🥹"):
            await self.highrise.send_emote("emote-shy2",user.id)

        if        message.startswith("😏") or     message.startswith("🙃") or     message.startswith("🤤") or     message.startswith("😋") or     message.startswith("😏") or message.startswith("😈"):
            await self.highrise.send_emote("emote-lust",user.id)           

        if        message.startswith("🥵") or message.startswith("🫠"):
            await self.highrise.send_emote("emote-hot",user.id)
                   
        if        message.startswith("!wrong") or   message.startswith("wrong") or      message.startswith("/wrong") or      message.startswith("Wrong") or message.startswith("1"):
            await self.highrise.send_emote("dance-wrong",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/fashion") or      message.startswith("fashion") or       message.startswith("!fashion") or      message.startswith("Fashion") or message.startswith("2"):
            await self.highrise.send_emote("emote-fashionista",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/gravity") or      message.startswith("gravity") or       message.startswith("!gravity") or      message.startswith("Gravity") or message.startswith("3"):
            await self.highrise.send_emote("emote-gravity",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/icecream") or                                message.startswith("icecream") or message.startswith("!icecream") or      message.startswith("Icecream") or message.startswith("4"):
            await self.highrise.send_emote("dance-icecream",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/casual") or  message.startswith("casual") or     message.startswith("!casual") or      message.startswith("Casual") or message.startswith("5"):
            await self.highrise.send_emote("idle-dance-casual",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/kiss") or      message.startswith("!kiss") or  message.startswith("kiss") or      message.startswith("Kiss") or message.startswith("6"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/no") or      message.startswith("no") or            message.startswith("!no") or      message.startswith("No") or message.startswith("7"):
            await self.highrise.send_emote("emote-no",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")
        if        message.startswith("/sad") or      message.startswith("!sad") or    message.startswith("sad") or     message.startswith("Sad") or message.startswith("8"):
            await self.highrise.send_emote("emote-sad",user.id)
            

        if        message.startswith("/yes") or      message.startswith("!yes") or    message.startswith("yes") or     message.startswith("Yes") or message.startswith("9"):
            await self.highrise.send_emote("emote-yes",user.id)
            

        if        message.startswith("/lau") or   message.startswith("laughing") or   message.startswith("Laughing") or   message.startswith("/laughing") or   message.startswith("!laughing") or      message.startswith("!lau") or    message.startswith("Lau") or     message.startswith("lau") or message.startswith("10"):
            await self.highrise.send_emote("emote-laughing",user.id)
            
        if        message.startswith("/hello") or message.startswith("hello") or      message.startswith("!hello") or      message.startswith("Hello") or message.startswith("11"):
            await self.highrise.send_emote("emote-hello",user.id)
            

        if        message.startswith("/wave") or  message.startswith("wave") or     message.startswith("!wave") or      message.startswith("Wave") or message.startswith("12"):
            await self.highrise.send_emote("emote-wave",user.id)
            
        if        message.startswith("/shy") or   message.startswith("shy") or      message.startswith("!shy") or      message.startswith("Shy") or message.startswith("13"):
            await self.highrise.send_emote("emote-shy",user.id)
            

        if        message.startswith("/tired") or message.startswith("tired") or      message.startswith("!tired") or      message.startswith("Tired") or message.startswith("14"):
            await self.highrise.send_emote("emote-tired",user.id)
            

        if        message.startswith("/flirt") or message.startswith("flirt") or message.startswith("flirtywave") or message.startswith("flirty") or      message.startswith("!flirt") or      message.startswith("Flirt") or          message.startswith("/Flirty") or           message.startswith("!Flirty") or           message.startswith("Flirty") or       message.startswith("!flirtywave") or    message.startswith("/flirtywave") or    message.startswith("Flirtywave") or message.startswith("15"):
            await self.highrise.send_emote("emote-lust",user.id)
            

        if        message.startswith("/greedy") or      message.startswith("!greedy") or      message.startswith("Greedy") or message.startswith("greedy") or message.startswith("16"):
            await self.highrise.send_emote("emote-greedy",user.id)
            
        if        message.startswith("/model") or      message.startswith("!model") or      message.startswith("Model") or  message.startswith("model") or message.startswith("17"):
            await self.highrise.send_emote("emote-model",user.id)
            
        if        message.startswith("/bow") or      message.startswith("!bow") or      message.startswith("Bow") or    message.startswith("bow") or message.startswith("18"):
            await self.highrise.send_emote("emote-bow",user.id)
            

        if        message.startswith("/curtsy") or      message.startswith("!curtsy") or      message.startswith("Curtsy") or message.startswith("curtsy") or message.startswith("19"):
            await self.highrise.send_emote("emote-curtsy",user.id)
            

        if        message.startswith("/snowball") or      message.startswith("!snowball") or      message.startswith("Snowball") or                              message.startswith("snowball") or message.startswith("20"):
            await self.highrise.send_emote("emote-snowball",user.id)
            
        if        message.startswith("/hot") or      message.startswith("!hot") or      message.startswith("Hot") or    message.startswith("hot") or message.startswith("21"):
            await self.highrise.send_emote("emote-hot",user.id)
            

        if        message.startswith("/snowangel") or      message.startswith("!snowangel") or      message.startswith("Snowangel") or                              message.startswith("snowangel") or message.startswith("22"):
            await self.highrise.send_emote("emote-snowangel",user.id)
            

        if        message.startswith("/charging") or      message.startswith("!charging") or      message.startswith("Charging") or                              message.startswith("charging") or message.startswith("23"):
            await self.highrise.send_emote("emote-charging",user.id)
            

        if        message.startswith("/confused") or      message.startswith("!confused") or      message.startswith("Confused") or                              message.startswith("confused") or message.startswith("24"):
            await self.highrise.send_emote("emote-confused",user.id)
            

        if        message.startswith("/telekinesis") or      message.startswith("!telekinesis") or      message.startswith("Telekinesis") or                            message.startswith("telekinesis") or message.startswith("25"):
            await self.highrise.send_emote("emote-telekinesis",user.id)
            

        if        message.startswith("/float") or      message.startswith("!float") or      message.startswith("Float") or  message.startswith("float") or message.startswith("26"):
            await self.highrise.send_emote("emote-float",user.id)
            

        if        message.startswith("/teleport") or      message.startswith("!teleport") or      message.startswith("Teleport") or                              message.startswith("teleport") or      message.startswith("27"):
            await self.highrise.send_emote("emote-teleporting",user.id)
            

        if        message.startswith("/maniac") or      message.startswith("!maniac") or      message.startswith("Maniac") or message.startswith("maniac") or message.startswith("28"):
            await self.highrise.send_emote("emote-maniac",user.id)
            

        if        message.startswith("/energyball") or      message.startswith("!energyball") or      message.startswith("Energyball") or                             message.startswith("eneryball") or message.startswith("29"):
            await self.highrise.send_emote("emote-energyball",user.id)
            

        if        message.startswith("/snake") or      message.startswith("!snake") or      message.startswith("Snake") or  message.startswith("snake") or message.startswith("30"):
            await self.highrise.send_emote("emote-snake",user.id)
            

        if        message.startswith("/frog") or      message.startswith("!frog") or      message.startswith("Frog") or   message.startswith("frog") or message.startswith("31"):
            await self.highrise.send_emote("emote-frog",user.id)
            

        if        message.startswith("/superpose") or      message.startswith("!superpose") or      message.startswith("Superpose") or                              message.startswith("superpose") or message.startswith("32"):
            await self.highrise.send_emote("emote-superpose",user.id)
            

        if        message.startswith("/cute") or      message.startswith("!cute") or      message.startswith("Cute") or   message.startswith("cute") or message.startswith("33"):
            await self.highrise.send_emote("emote-cute",user.id)

        if        message.startswith("/pose7") or      message.startswith("!pose7") or      message.startswith("Pose7") or  message.startswith("pose7") or message.startswith("34"):
            await self.highrise.send_emote("emote-pose7",user.id)
            

        if        message.startswith("/pose8") or      message.startswith("!pose8") or      message.startswith("Pose8") or  message.startswith("pose8") or message.startswith("35"):
            await self.highrise.send_emote("emote-pose8",user.id)
            

        if        message.startswith("/pose1") or      message.startswith("!pose1") or      message.startswith("Pose1") or  message.startswith("pose1") or message.startswith("36"):
            await self.highrise.send_emote("emote-pose1",user.id)
            

        if        message.startswith("/pose5") or      message.startswith("!pose5") or      message.startswith("Pose5") or  message.startswith("pose5") or message.startswith("37"):
            await self.highrise.send_emote("emote-pose5",user.id)
            

        if        message.startswith("/pose3") or      message.startswith("!pose3") or      message.startswith("Pose3") or  message.startswith("pose3") or message.startswith("38"):
            await self.highrise.send_emote("emote-pose3",user.id)
            

        if        message.startswith("/cutey") or      message.startswith("!cutey") or      message.startswith("Cutey") or  message.startswith("cutey") or message.startswith("39"):
            await self.highrise.send_emote("emote-cutey",user.id)
            
        if        message.startswith("/tik10") or      message.startswith("!tik10") or      message.startswith("Tik10") or  message.startswith("tik10") or message.startswith("40"):
            await self.highrise.send_emote("dance-tiktok10",user.id)
            

        if        message.startswith("/sing") or      message.startswith("!sing") or          message.startswith("Sing") or           message.startswith("Singing") or       message.startswith("/singing") or   message.startswith("!singing") or                              message.startswith("singing") or                              message.startswith("!singalong")  or                             message.startswith("/singalong") or message.startswith("Singaloung") or                             message.startswith("singaloung") or message.startswith("41"):
            await self.highrise.send_emote("idle_singing",user.id)
            

        if        message.startswith("/enthused") or      message.startswith("!enthused") or      message.startswith("Enthused") or                              message.startswith("enthused") or message.startswith("42"):
            await self.highrise.send_emote("idle-enthusiastic",user.id)
            

        if        message.startswith("/shop") or      message.startswith("!shop") or      message.startswith("Shop") or   message.startswith("shop") or   message.startswith("!shopping") or message.startswith("/shopping") or message.startswith("Shopping") or message.startswith("shopping") or message.startswith("43"):
            await self.highrise.send_emote("dance-shoppingcart",user.id)
            

        if        message.startswith("/russian") or      message.startswith("!russian") or      message.startswith("Russian") or                              message.startswith("russian") or message.startswith("44"):
            await self.highrise.send_emote("dance-russian",user.id)
            

        if        message.startswith("/pennywise") or      message.startswith("!pennywise") or      message.startswith("Pennywise") or                              message.startswith("pennywise") or message.startswith("45"):
            await self.highrise.send_emote("dance-pennywise",user.id)
            

        if        message.startswith("/tik2") or      message.startswith("!tik2") or      message.startswith("Tik2") or   message.startswith("!dontstartnow") or   message.startswith("/dontstartnow") or   message.startswith("dontstartnow") or   message.startswith("Dontstartnow") or   message.startswith("tik2") or   message.startswith("46"):
            await self.highrise.send_emote("dance-tiktok2",user.id)
            
        if        message.startswith("/blackpink") or      message.startswith("!blackpink") or      message.startswith("Blackpink") or                              message.startswith("blackpink") or message.startswith("47"):
            await self.highrise.send_emote("dance-blackpink",user.id)
 
        if        message.startswith("/celebrate") or      message.startswith("!celebrate") or      message.startswith("Celebrate") or                              message.startswith("celebrate") or message.startswith("48"):
            await self.highrise.send_emote("emoji-celebrate",user.id)
            
        if        message.startswith("/gagging") or      message.startswith("!gagging") or      message.startswith("Gagging") or                              message.startswith("gagging") or message.startswith("49"):
            await self.highrise.send_emote("emoji-gagging",user.id)
            

        if        message.startswith("/flex") or      message.startswith("!flex") or      message.startswith("Flex") or   message.startswith("flex") or message.startswith("50"):
            await self.highrise.send_emote("emoji-flex",user.id)
            
        if        message.startswith("/cursing") or      message.startswith("!cursing") or      message.startswith("Cursing") or                              message.startswith("cursing") or message.startswith("51"):
            await self.highrise.send_emote("emoji-cursing",user.id)
            

        if        message.startswith("/thumbsup") or      message.startswith("!thumbsup") or      message.startswith("Thumbsup") or                              message.startswith("thumbsup") or message.startswith("52"):
            await self.highrise.send_emote("emoji-thumbsup",user.id)
            
        if        message.startswith("/angry") or      message.startswith("!angry") or      message.startswith("Angry") or  message.startswith("angry") or message.startswith("53"):
            await self.highrise.send_emote("emoji-angry",user.id)


        if        message.startswith("/punk") or      message.startswith("!punk") or      message.startswith("Punk") or   message.startswith("punk") or message.startswith("54"):
            await self.highrise.send_emote("emote-punkguitar",user.id)
            
        if        message.startswith("/zombie") or      message.startswith("!zombie") or      message.startswith("Zombie") or message.startswith("zombie") or message.startswith("55"):
            await self.highrise.send_emote("emote-zombierun",user.id)
            

        if        message.startswith("/sit") or      message.startswith("!sit") or      message.startswith("Sit") or    message.startswith("sit") or message.startswith("56"):
            await self.highrise.send_emote("idle-loop-sitfloor",user.id)
            

        if        message.startswith("/fight") or      message.startswith("!fight") or      message.startswith("Fight") or  message.startswith("fight") or  message.startswith("!swordfight") or message.startswith("/swordfight") or message.startswith("Swordfight") or message.startswith("swordfight") or message.startswith("57"):
            await self.highrise.send_emote("emote-swordfight",user.id)

        if        message.startswith("/ren") or      message.startswith("!ren") or      message.startswith("Ren") or    message.startswith("ren") or    message.startswith("!macarena") or     message.startswith("/macarena") or      message.startswith("Macarena") or message.startswith("macarena") or message.startswith("58"):
            await self.highrise.send_emote("dance-macarena",user.id)
            

        if        message.startswith("/wei") or      message.startswith("!wei") or      message.startswith("Wei") or    message.startswith("wei") or message.startswith("!weird") or message.startswith("/weird") or message.startswith("Weird") or message.startswith("weird") or  message.startswith("59"):
            await self.highrise.send_emote("dance-weird",user.id)
            
        if        message.startswith("/tik8") or      message.startswith("!tik8") or      message.startswith("Tik8") or           message.startswith("/savage") or           message.startswith("!savage") or           message.startswith("Savage") or message.startswith("tik8") or message.startswith("savage") or message.startswith("60"):
            await self.highrise.send_emote("dance-tiktok8",user.id)
            
        if        message.startswith("/tik9") or      message.startswith("!tik9") or      message.startswith("Tik9") or           message.startswith("/viral") or           message.startswith("!viral") or           message.startswith("Viral") or  message.startswith("!viralgroove") or message.startswith("/viralgroove") or message.startswith("Viralgroove") or message.startswith("viralgroove") or message.startswith("tik9") or message.startswith("viral") or message.startswith("61"):
            await self.highrise.send_emote("dance-tiktok9",user.id)
            
        if        message.startswith("/uwu") or      message.startswith("!uwu") or      message.startswith("Uwu") or    message.startswith("uwu") or message.startswith("62"):
            await self.highrise.send_emote("idle-uwu",user.id)

        if        message.startswith("/tik4") or      message.startswith("!tik4") or      message.startswith("Tik4") or               message.startswith("/sayso") or               message.startswith("!sayso") or               message.startswith("Sayso") or  message.startswith("sayso") or message.startswith("tik4") or message.startswith("63"):
            await self.highrise.send_emote("idle-dance-tiktok4",user.id)

        if        message.startswith("/star") or      message.startswith("!star") or      message.startswith("Star") or   message.startswith("star") or message.startswith("64"):
            await self.highrise.send_emote("emote-stargazer",user.id)
            
        if        message.startswith("/pose9") or      message.startswith("!pose9") or      message.startswith("Pose9") or  message.startswith("pose9") or message.startswith("65"):
            await self.highrise.send_emote("emote-pose9",user.id)
            
        if        message.startswith("/boxer") or      message.startswith("!boxer") or      message.startswith("Boxer") or  message.startswith("boxer") or message.startswith("66"):
            await self.highrise.send_emote("emote-boxer",user.id)
            
        if        message.startswith("/guitar") or      message.startswith("!guitar") or      message.startswith("Guitar") or message.startswith("guitar") or message.startswith("67"):
            await self.highrise.send_emote("idle-guitar",user.id)

        if        message.startswith("/penguin") or      message.startswith("!penguin") or      message.startswith("Penguin") or   message.startswith("penguin") or message.startswith("68"):
            await self.highrise.send_emote("dance-pinguin",user.id)

        if        message.startswith("/astronaut") or      message.startswith("!astronaut") or      message.startswith("Astronaut") or                                message.startswith("astronaut") or message.startswith("69"):
            await self.highrise.send_emote("emote-astronaut",user.id)

        if        message.startswith("/saunter") or      message.startswith("!saunter") or      message.startswith("Saunter") or               message.startswith("/anime") or               message.startswith("!anime") or               message.startswith("Anime") or    message.startswith("anime") or   message.startswith("saunter") or   message.startswith("70"):
            await self.highrise.send_emote("dance-anime",user.id)

        if        message.startswith("/creepy") or      message.startswith("!creepy") or      message.startswith("Creepy") or   message.startswith("creepy") or message.startswith("71"):
            await self.highrise.send_emote("dance-creepypuppet",user.id)

        if        message.startswith("/watch") or      message.startswith("!watch") or      message.startswith("Watch") or    message.startswith("watch") or message.startswith("72"):
            await self.highrise.send_emote("emote-creepycute",user.id)

        if        message.startswith("/revelations") or      message.startswith("!revelations") or      message.startswith("Revelations") or                                message.startswith("revelations") or message.startswith("73"):
            await self.highrise.send_emote("emote-headblowup",user.id)

        if        message.startswith("/bashful") or      message.startswith("!bashful") or      message.startswith("Bashful") or  message.startswith("bashful") or message.startswith("74"):
            await self.highrise.send_emote("emote-shy2",user.id)

        if        message.startswith("/arabesque") or      message.startswith("!arabesque") or      message.startswith("Arabesque") or                                message.startswith("arabesque") or message.startswith("75"):
            await self.highrise.send_emote("emote-pose10",user.id)

        if        message.startswith("/party") or      message.startswith("!party") or      message.startswith("Party") or    message.startswith("party") or message.startswith("76"):
            await self.highrise.send_emote("emote-celebrate",user.id)

        if        message.startswith("/skating") or      message.startswith("!skating") or      message.startswith("Skating") or  message.startswith("skating") or message.startswith("77"):
            await self.highrise.send_emote("emote-iceskating",user.id)

        if        message.startswith("/scritchy") or      message.startswith("!scritchy") or      message.startswith("Scritchy") or message.startswith("scritchy") or message.startswith("78"):
            await self.highrise.send_emote("idle-wild",user.id)

        if        message.startswith("/bitnervous") or      message.startswith("!bitnervous") or      message.startswith("Bitnervous") or               message.startswith("!nervous") or               message.startswith("/nervous") or               message.startswith("Nervous") or  message.startswith("nervous") or   message.startswith("bitnervous") or message.startswith("79"):
            await self.highrise.send_emote("idle-nervous",user.id)

        if        message.startswith("/timejump") or      message.startswith("!timejump") or      message.startswith("Timejump") or message.startswith("timejump") or message.startswith("time") or   message.startswith("Time") or   message.startswith("!time") or   message.startswith("/time") or message.startswith("80"):
            await self.highrise.send_emote("emote-timejump",user.id)

        if        message.startswith("/gottago") or      message.startswith("!gottago") or      message.startswith("Gottago") or message.startswith("gottago") or  message.startswith("81"):
            await self.highrise.send_emote("idle-toilet",user.id)

        if        message.startswith("/jingle") or      message.startswith("!jingle") or      message.startswith("Jingle") or  message.startswith("jingle") or message.startswith("82"):
            await self.highrise.send_emote("dance-jinglebell",user.id)

        if        message.startswith("/hyped") or      message.startswith("!hyped") or      message.startswith("Hyped") or   message.startswith("hyped") or message.startswith("83"):
            await self.highrise.send_emote("emote-hyped",user.id)

        if        message.startswith("/sleigh") or      message.startswith("!sleigh") or        message.startswith("sleigh") or      message.startswith("Sleigh") or message.startswith("84"):
            await self.highrise.send_emote("emote-sleigh",user.id)

        if        message.startswith("/surprise") or      message.startswith("!surprise") or      message.startswith("surprise") or      message.startswith("Surprise") or message.startswith("85"):
            await self.highrise.send_emote("emote-pose6",user.id)
          
        if        message.startswith("/repose") or      message.startswith("!repose") or        message.startswith("repose") or      message.startswith("Repose") or message.startswith("86"):
            await self.highrise.send_emote("sit-relaxed",user.id)

        if        message.startswith("/kawaii") or      message.startswith("!kawaii") or        message.startswith("kawaii") or       message.startswith("Kawaii") or message.startswith("87"):
            await self.highrise.send_emote("dance-kawai",user.id)

        if        message.startswith("/touch") or      message.startswith("!touch") or         message.startswith("touch") or      message.startswith("Touch") or message.startswith("88"):
            await self.highrise.send_emote("dance-touch",user.id)

        if        message.startswith("/gift") or      message.startswith("!gift") or          message.startswith("gift") or      message.startswith("Gift") or message.startswith("89"):
            await self.highrise.send_emote("emote-gift",user.id)

        if        message.startswith("/pushit") or      message.startswith("!pushit") or        message.startswith("pushit") or      message.startswith("Pushit") or message.startswith("90"):
            await self.highrise.send_emote("dance-employee",user.id)

        if        message.startswith("salute") or      message.startswith("!salute") or        message.startswith("salute") or      message.startswith("Salute") or message.startswith("91"):
            await self.highrise.send_emote("emote-cutesalute",user.id)

        if        message.startswith("/attention") or      message.startswith("!attention") or        message.startswith("attention") or      message.startswith("Attention") or message.startswith("92"):
            await self.highrise.send_emote("emote-salute",user.id)                                                                   

        if        message.startswith("/tiktok") or      message.startswith("!tiktok") or        message.startswith("tiktok") or    message.startswith("Tiktok") or message.startswith("93"):
            await self.highrise.send_emote("dance-tiktok11",user.id)

        if        message.startswith("/smooch") or      message.startswith("!smooch") or        message.startswith("smooch") or    message.startswith("Smooch") or message.startswith("94"):
            await self.highrise.send_emote("emote-kissing-bound",user.id)

        if        message.startswith("/launch") or      message.startswith("!launch") or        message.startswith("launch") or   message.startswith("Launch") or message.startswith("95"):
            await self.highrise.send_emote("emote-launch",user.id)

        if        message.startswith("/fairyfloat") or      message.startswith("!fairyfloat") or        message.startswith("fairyfloat") or    message.startswith("Fairyfloat") or message.startswith("96"):
            await self.highrise.send_emote("idle-floating",user.id)

        if        message.startswith("/fairytwirl") or      message.startswith("!fairytwirl") or        message.startswith("fairytwirl") or    message.startswith("Fairytwirl") or message.startswith("97"):
            await self.highrise.send_emote("emote-looping",user.id)

        if              message.startswith("Fairyfloat All") or                              message.startswith("/emote all fairyfloat") or       message.startswith("!emote all fairyfloat"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-floating", roomUser.id)
                

        if              message.startswith("Fairytwirl All") or                              message.startswith("/emote all fairytwirl") or       message.startswith("!emote all fairytwirl"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-looping", roomUser.id)

        if              message.startswith("Launch All") or                              message.startswith("/emote all launch") or       message.startswith("!emote all launch"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-launch", roomUser.id)
                
        if              message.startswith("Smooch All") or                              message.startswith("/emote all smooch") or       message.startswith("!emote all smooch"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kissing-bound", roomUser.id)
                
        if              message.startswith("Pushit All") or                              message.startswith("/emote all pushit") or       message.startswith("!emote all pushit"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-employee", roomUser.id)
                
        if              message.startswith("Gift All") or                              message.startswith("/emote all gift") or       message.startswith("!emote all gift"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gift", roomUser.id)
                
        if              message.startswith("Attention All") or                              message.startswith("/emote all attention") or       message.startswith("!emote all attention"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-salute", roomUser.id)
                

        if              message.startswith("Salute All") or                              message.startswith("/emote all salute") or       message.startswith("!emote all salute"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutesalute", roomUser.id)
                
        if              message.startswith("Tiktok All") or                              message.startswith("/emote all tiktok") or       message.startswith("!emote all tiktok"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok11", roomUser.id)
                      
        if              message.startswith("Touch All") or                              message.startswith("/emote all touch") or       message.startswith("!emote all touch"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-touch", roomUser.id)
                           
        if              message.startswith("Kawaii All") or                              message.startswith("/emote all kawaii") or       message.startswith("!emote all kawaii"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-kawai", roomUser.id)
                       
        if              message.startswith("Hot All") or                              message.startswith("/emote all hot") or       message.startswith("!emote all hot"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hot", roomUser.id)
                      
        if              message.startswith("Curtsy All") or                              message.startswith("/emote all curtsy") or       message.startswith("!emote all curtsy"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-curtsy", roomUser.id)
                
        if              message.startswith("Surprise All") or                              message.startswith("/emote all surprise") or       message.startswith("!emote all surprise"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose6", roomUser.id)
                
        if              message.startswith("Jingle All") or                              message.startswith("/emote all jingle") or       message.startswith("!emote all jingle"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)
                
        if              message.startswith("Creepy All") or                              message.startswith("/emote all creepy") or       message.startswith("!emote all creepy"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-creepypuppet", roomUser.id)
                
        if              message.startswith("Nervous All") or message.startswith("Bitnervous All") or      message.startswith("!emote all bitnervous") or message.startswith("/emote all bitnervous") or                             message.startswith("/emote all nervous") or       message.startswith("!emote all nervous"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-nervous", roomUser.id)
                
        if              message.startswith("Scritchy All") or                              message.startswith("/emote all scritchy") or       message.startswith("!emote all scritchy"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-wild", roomUser.id)
                          
        if              message.startswith("Fashion All") or                              message.startswith("/emote all fashion") or       message.startswith("!emote all fashion"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)
                             
        if              message.startswith("Wrong All") or                              message.startswith("/emote all wrong") or       message.startswith("!emote all wrong"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-wrong", roomUser.id)
                
        if              message.startswith("Cutey All") or                              message.startswith("/emote all cutey") or       message.startswith("!emote all cutey"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutey", roomUser.id)
                
        if              message.startswith("Hyped All") or                              message.startswith("/emote all hyped") or       message.startswith("!emote all hyped"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)
                            
        if              message.startswith("Superpose All") or                              message.startswith("/emote all superpose") or       message.startswith("!emote all superpose"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-superpose", roomUser.id)
                
        if              message.startswith("Punk All") or                              message.startswith("/emote all punk") or       message.startswith("!emote all punk"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id) 
                              
        if              message.startswith("Dontstartnow All") or message.startswith("Tiktok2 All") or      message.startswith("!emote all dontstartnow") or message.startswith("/emote all dontstartnow") or                             message.startswith("/emote all tiktok2") or       message.startswith("!emote all tiktok2"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok2", roomUser.id)
                            
        if              message.startswith("Savage All") or message.startswith("Tiktok8 All") or      message.startswith("!emote all savage") or message.startswith("/emote all savage") or                             message.startswith("/emote all tiktok8") or       message.startswith("!emote all tiktok8"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok8", roomUser.id)
                             
        if              message.startswith("Tiktok10 All") or                              message.startswith("/emote all tiktok10") or       message.startswith("!emote all tiktok10"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok10", roomUser.id)
                             
        if              message.startswith("Viral All") or     message.startswith("!emotr all tiktok9") or        message.startswith("/emote all tiktok9") or    message.startswith("Tiktok9 All") or message.startswith("Viralgroove All") or      message.startswith("!emote all viral") or message.startswith("/emote all viralgroove") or                             message.startswith("/emote all viral") or       message.startswith("!emote all viralgroove"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok9", roomUser.id)
                            
        if              message.startswith("Blackpink All") or                              message.startswith("/emote all blackpink") or       message.startswith("!emote all blackpink"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-blackpink", roomUser.id)
                         
        if              message.startswith("Gagging All") or                              message.startswith("/emote all gagging") or       message.startswith("!emote all gagging"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-gagging", roomUser.id)
                
        if              message.startswith("Pose3 All") or                              message.startswith("/emote all pose3") or       message.startswith("!emote all pose3"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose3", roomUser.id)
                
        if              message.startswith("Pose7 All") or                              message.startswith("/emote all pose7") or       message.startswith("!emote all pose7"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose7", roomUser.id)

        if              message.startswith("Pose5 All") or                              message.startswith("/emote all pose5") or       message.startswith("!emote all pose5"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose5", roomUser.id)

        if              message.startswith("Pose1 All") or                              message.startswith("/emote all pose1") or       message.startswith("!emote all pose1"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose1", roomUser.id)
                
        if              message.startswith("Pose8 All") or                              message.startswith("/emote all pose8") or       message.startswith("!emote all pose8"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose8", roomUser.id)
     
        if              message.startswith("Enthused All") or                              message.startswith("/emote all enthused") or       message.startswith("!emote all enthused"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-enthusiastic", roomUser.id)
                
        if              message.startswith("Singing All") or message.startswith("Sing All") or      message.startswith("!emote all sing") or message.startswith("/emote all sing") or                             message.startswith("/emote all singing") or       message.startswith("!emote all singing"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)

        if              message.startswith("Teleport All") or                              message.startswith("/emote all teleport") or       message.startswith("!emote all teleport"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-teleporting", roomUser.id)
                
        if              message.startswith("Telekinesis All") or                              message.startswith("/emote all telekinesis") or       message.startswith("!emote all telekinesis"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-telekinesis", roomUser.id)

        if              message.startswith("Casual All") or                              message.startswith("/emote all casual") or       message.startswith("!emote all casual"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-casual", roomUser.id)
                
        if              message.startswith("Icecream All") or                              message.startswith("/emote all icecream") or       message.startswith("!emote all icecream"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-icecream", roomUser.id)
                   
        if              message.startswith("Zombie All") or                              message.startswith("/emote all zombie") or       message.startswith("!emote all zombie"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)

        if              message.startswith("Celebrate All") or                              message.startswith("/emote all celebrate") or       message.startswith("!emote all celebrate"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-celebrate", roomUser.id)

        if              message.startswith("Kiss All") or                              message.startswith("/emote all kiss") or       message.startswith("!emote all kiss"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kiss", roomUser.id)

        if              message.startswith("Snowangel All") or                              message.startswith("/emote all snowangel") or       message.startswith("!emote all snowangel"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snowangel", roomUser.id)

        if              message.startswith("Bow All") or                              message.startswith("/emote all bow") or       message.startswith("!emote all bow"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-bow", roomUser.id)

        if              message.startswith("Ice All") or message.startswith("Skating All") or      message.startswith("!emote all ice") or message.startswith("/emote all skating") or                             message.startswith("/emote all ice") or       message.startswith("!emote all skating"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-iceskating", roomUser.id)

        if              message.startswith("Confused All") or                              message.startswith("/emote all confused") or       message.startswith("!emote all confused"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-confused", roomUser.id)

        if              message.startswith("Charging All") or                              message.startswith("/emote all charging") or       message.startswith("!emote all charging"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-charging", roomUser.id)

        if              message.startswith("Weird All") or message.startswith("Wei All") or      message.startswith("!emote all wei") or message.startswith("/emote all wei") or                             message.startswith("/emote all weird") or       message.startswith("!emote all weird"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)

        if              message.startswith("Greedy All") or                              message.startswith("/emote all greedy") or       message.startswith("!emote all greedy"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-greedy", roomUser.id)
    

        if              message.startswith("Cursing All") or                              message.startswith("/emote all cursing") or       message.startswith("!emote all cursing"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-cursing", roomUser.id)

        if              message.startswith("Russian All") or                              message.startswith("/emote all russian") or       message.startswith("!emote all russian"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-russian", roomUser.id)            

        if              message.startswith("Repose All") or                              message.startswith("/emote all repose") or       message.startswith("!emote all repose"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("sit-relaxed", roomUser.id)
                            
        if              message.startswith("Shop All") or message.startswith("Shopping All") or      message.startswith("!emote all shopping") or message.startswith("/emote all shop") or                             message.startswith("/emote all shopping") or       message.startswith("!emote all shop"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-shoppingcart", roomUser.id)
                

        if              message.startswith("Macarena All") or message.startswith("Ren All") or      message.startswith("!emote all macarena") or message.startswith("/emote all macarena") or                             message.startswith("/emote all ren") or       message.startswith("!emote all   ren "):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-macarena", roomUser.id)
                

        if              message.startswith("Snake All") or                              message.startswith("/emote all snake") or       message.startswith("!emote all snake"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snake", roomUser.id)              

        if              message.startswith("Model All") or                              message.startswith("/emote all model") or       message.startswith("!emote all model"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-model", roomUser.id)
                
        if              message.startswith("Sleigh All") or                              message.startswith("/emote all sleigh") or       message.startswith("!emote all sleigh"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-sleigh", roomUser.id)
                
        if              message.startswith("Sayso All") or message.startswith("Tiktok4 All") or      message.startswith("!emote all sayso") or message.startswith("/emote all sayso") or                             message.startswith("/emote all tiktok4") or       message.startswith("!emote all tiktok4"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)

        if              message.startswith("Uwu All") or                              message.startswith("/emote all uwu") or       message.startswith("!emote all uwu"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-uwu", roomUser.id)
            
        if              message.startswith("Star All") or                              message.startswith("/emote all star") or       message.startswith("!emote all star"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-stargazer", roomUser.id)
                
        if              message.startswith("Pose9 All") or                              message.startswith("/emote all pose9") or       message.startswith("!emote all pose9"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose9", roomUser.id)

        if              message.startswith("Boxer All") or                              message.startswith("/emote all boxer") or       message.startswith("!emote all boxer"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-boxer", roomUser.id)

        if              message.startswith("Airguitar All") or message.startswith("Guitar All") or      message.startswith("!emote all guitar") or message.startswith("/emote all airguitar") or                             message.startswith("/emote all guitar") or       message.startswith("!emote all airguitar"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-guitar", roomUser.id)

        if              message.startswith("Penguin All") or message.startswith("Pinguin All") or      message.startswith("!emote all penguin") or message.startswith("/emote all penguin") or                             message.startswith("/emote all pinguin") or       message.startswith("!emote all pinguin"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)   
            
        if              message.startswith("Astronaut All") or message.startswith("Zero All") or      message.startswith("!emote all zero") or message.startswith("/emote all zero") or                             message.startswith("/emote all astronaut") or       message.startswith("!emote all astronaut"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)
                
        if              message.startswith("Saunter All") or   message.startswith("Anime All") or   message.startswith("!emote all anime") or   message.startswith("/emote all anime") or                              message.startswith("/emote all saunter") or       message.startswith("!emote all saunter"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)         

        if              message.startswith("Flirt All") or     message.startswith("!emote all flirt") or    message.startswith("/emote all flirt") or    message.startswith("!emote all flirty") or     message.startswith("Flirtywave All") or    message.startswith("/emote all flirty") or    message.startswith("/emote all flirt") or                               message.startswith("/emote all flirtywave") or       message.startswith("!emote all flirtywave"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)        

        if              message.startswith("Watch All") or                              message.startswith("/emote all watch") or       message.startswith("!emote all watch"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-creepycute", roomUser.id)
                        
        if              message.startswith("Revelations All") or                              message.startswith("/emote all revelations") or       message.startswith("!emote all revelations"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-headblowup", roomUser.id)
            
        if              message.startswith("Bashful All") or                              message.startswith("/emote all bashful") or       message.startswith("!emote all bashful"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-shy2", roomUser.id)
            
        if              message.startswith("Arabesque All") or                              message.startswith("/emote all arabesque") or       message.startswith("!emote all arabesque"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose10", roomUser.id)
                  
        if              message.startswith("Party All") or                              message.startswith("/emote all party") or       message.startswith("!emote all party"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-celebrate", roomUser.id)
            
        if              message.startswith("Time All") or                              message.startswith("/emote all time") or       message.startswith("!emote all time"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-timejump", roomUser.id)
                

        if              message.startswith("Gottago All") or                              message.startswith("/emote all gottago") or       message.startswith("!emote all gottago"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)
            
        if        message.startswith("/tp") or      message.startswith("!tp") or      message.startswith("/tele") or          message.startswith("Tp") or          message.startswith("Tele") or  message.startswith("!tele"):
          target_username =         message.split("@")[-1].strip()
          await                     self.teleport_to_user(user, target_username)

        if                            message.startswith("Summon") or         message.startswith("Summom") or         message.startswith("!summom") or        message.startswith("/summom") or        message.startswith("/summon") or  message.startswith("!summon"):
          if user.username in moderators:
           target_username = message.split("@")[-1].strip()
           await self.teleport_user_next_to(target_username, user)

        if              message.startswith("Carteira") or  message.startswith("Wallet") or    message.startswith("!wallet") or       message.startswith("carteira"):
          if user.username in moderators:
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.send_whisper(user.id,f"AMOUNT  : {wallet[0].amount} {wallet[0].type}")
            await self.highrise.send_emote("dance-tiktok14")
              
        if message.startswith("!kick"):
          if user.username in moderators:
              pass
          else:
              await self.highrise.chat("Voce não tem permissao para usar esse comando.")
              return
          #separete message into parts
          parts = message.split()
          #check if message is valid "kick @username"
          if len(parts) != 2:
              await self.highrise.chat("formato de banimento errado.")
              return
          #checks if there's a @ in the message
          if "@" not in parts[1]:
              username = parts[1]
          else:
              username = parts[1][1:]
          #check if user is in room
          room_users = (await self.highrise.get_room_users()).content
          for room_user, pos in room_users:
              if room_user.username.lower() == username.lower():
                  user_id = room_user.id
                  break
          if "user_id" not in locals():
              await self.highrise.chat("user not found, please fix the code coordinate ")
              return
          #kick user
          try:
              await self.highrise.moderate_room(user_id, "kick")
          except Exception as e:
              await self.highrise.chat(f"{e}")
              return
          #send message to chat
          await self.highrise.chat(f"{username} He was banned from the room!!")

        if message == "!fit 1" and user.username in moderators:
          shirt = ["shirt-n_room32019jerseywhite"]
          pant = ["pants-n_room22019longcutoffsdenim"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_malenew16', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='nose-n_03_b', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_malenew16', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='face_hair-n_newbasicfacehairupper06', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='face_hair-n_newbasicfacehairlower16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020whitesocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullround', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malediamondsleepy', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[1] added to the bot. ")
          

        if message == "!fit 2" and user.username in moderators:
          shirt = ["shirt-n_room12019cropsweaterwhite"]
          pant = ["pants-n_room12019rippedpantsblue"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=23),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018mediumcurlymarilyn', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2018marilyncurls', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='blush-f_blush01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020whitesocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019hightopsblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_basic2018toothyfullpeaked', account_bound=False, active_palette=24),
                  Item(type='clothing', amount=1, id='eye-n_basic2018pinkshadow2', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[2] added to the bot. ")

        if message == "!fit 3"  and user.username in moderators:
          shirt = ["shirt-f_punklace"]
          pant = ["pants-n_room22019shortcutoffsdenim"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullpeaked', account_bound=False, active_palette=8),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2018straightbluntbangs', account_bound=False, active_palette=28),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018straighthighpony', account_bound=False, active_palette=28),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018dolleyes', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_starteritems2019flatsblack', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='necklace-n_room32019locknecklace', account_bound=False, active_palette=-1),

Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),


          ]) 
          await self.highrise.chat(f"👕FIT[3] added to the bot. ")

        if message == "!fit 4" and user.username in moderators:
          shirt = ["shirt-n_room22019bratoppink"]
          pant = ["pants-n_room22019undiespink"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=77),
                  Item(type='clothing', amount=1, id='nose-n_01_b', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=77),
                  Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='glasses-n_room32019smallshades', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_basic2018pillowfullpeaked', account_bound=False, active_palette=9),
                  Item(type='clothing', amount=1, id='eye-n_basic2018falselashes', account_bound=False, active_palette=10),
                  Item(type='clothing', amount=1, id='eyebrow-n_26', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[4] added to the bot. ")
            
        if message == "!fit 5" and user.username in moderators:
          shirt = ["shirt-n_room12019cropsweaterblack"]
          pant = ["skirt-n_room12019pleatedskirtgrey"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_basic2018newnose15', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-n_room22019sillymouth', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018teardrop', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle32', account_bound=False, active_palette=-1),

          ]) 
          await self.highrise.chat(f"👕FIT[5] added to the bot. ")       

        if message == "!fit 6" and user.username in moderators:
          shirt = ["shirt-n_room32019longlineteesweatshirtgrey"]
          pant = ["pants-n_starteritems2019cuffedjeansblue"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_malenew19', account_bound=False, active_palette=80),
                  Item(type='clothing', amount=1, id='nose-n_basic2018newnose04', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_malenew19', account_bound=False, active_palette=80),
                  Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018whistlemouth', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malealmondsquint', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_04', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[6] added to the bot. ")

        if message == "!fit 7" and user.username in moderators:
          shirt = ["shirt-n_starteritems2019pulloverblack"]
          pant = ["pants-n_starteritems2019mensshortsblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_malenew23', account_bound=False, active_palette=82),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_malenew23', account_bound=False, active_palette=82),
                  Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-vip_f_01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malealmondsquint', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_26', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[7] added to the bot. ")

        if message == "!fit 8" and user.username in moderators:
          shirt = ["shirt-n_registrationavatars2023arianadress"]
          pant = ["pants-n_room22019undiesblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=23),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_basic2019poofbob', account_bound=False, active_palette=82),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_basic2018straightbangslowpart', account_bound=False, active_palette=82),

Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),
                
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023arianaboots', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_registrationavatars2023pinkmouth', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id='eye-n_registrationavatars2023gymgirleyes', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[8] added to the bot. ")

        if message == "!fit 9" and user.username in moderators:
          shirt = ["shirt-n_room12019sweaterwithbuttondowngrey"]
          pant = ["pants-n_room12019formalslackskhaki"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_malenew05', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='eyebrow-n_06', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_malenew04', account_bound=False, active_palette=4),
                
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018chippermouth', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-m_12b', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='nose-n_03_b', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[9] added to the bot. ")

        if message == "!fit 10" and user.username in moderators:
          shirt = ["shirt-n_winxudcrwrdsone2024winxblueshirt"]
          pant = ["skirt-n_winxudcrwrdsone2024pinkskirtstrawberrys"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_basic2018wavypulledback', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_basic2018sidebangspulledback', account_bound=False, active_palette=1),

Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),
                
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakerspink', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_registrationavatars2023pinkmouth', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id='eye-n_basic2018liftedeyes', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[10] added to the bot. ")

        if message == "!fit 11" and user.username in moderators:
          shirt = ["shirt-n_registrationavatars2023gothguyhoodie"]
          pant = ["pants-n_starteritems2019cuffedjeansblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=6),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-m_23', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='nose-n_01_b', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-m_23', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020blacksocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023furrysneakers', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-vip_f_01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malealmondsquint', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_26', account_bound=False, active_palette=-1),

Item(type='clothing', amount=1, id='bag-n_registrationavatars2023furrytail', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hat-n_registrationavatars2023wolfears', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[11] added to the bot. ")
            
    async def teleport(self, user: User, position: Position):
        try:
            await self.highrise.teleport(user.id, position)
        except Exception as e:
            print(f"Caught Teleport Error: {e}")

    async def teleport_to_user(self, user: User, target_username: str) -> None:
        try:
            room_users = await self.highrise.get_room_users()
            for target, position in room_users.content:
                if target.username.lower() == target_username.lower():
                    z = position.z
                    new_z = z - 1
                    await self.teleport(user, Position(position.x, position.y, new_z, position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting to {target_username}: {e}")

    async def teleport_user_next_to(self, target_username: str, requester_user: User) -> None:
        try:
            # Get the position of the requester_user
            room_users = await self.highrise.get_room_users()
            requester_position = None
            for user, position in room_users.content:
                if user.id == requester_user.id:
                    requester_position = position
                    break

            # Find the target user and their position
            for user, position in room_users.content:
                if user.username.lower() == target_username.lower():
                    z = requester_position.z
                    new_z = z + 1  # Example: Move +1 on the z-axis (upwards)
                    await self.teleport(user, Position(requester_position.x, requester_position.y, new_z, requester_position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting {target_username} next to {requester_user.username}: {e}")
          
    async def teleporter(self, message: str)-> None:
        """
            Teleports the user to the specified user or coordinate
            Usage: /teleport <username> <x,y,z>
                                                                """
        #separates the message into parts
        #part 1 is the command "/teleport"
        #part 2 is the name of the user to teleport to (if it exists)
        #part 3 is the coordinates to teleport to (if it exists)
        try:
            command, username, coordinate = message.split(" ")
        except:
            
            return
        
        #checks if the user is in the room
        room_users = (await self.highrise.get_room_users()).content
        for user in room_users:
            if user[0].username.lower() == username.lower():
                user_id = user[0].id
                break
        #if the user_id isn't defined, the user isn't in the room
        if "user_id" not in locals():
            
            return
            
        #checks if the coordinate is in the correct format (x,y,z)
        try:
            x, y, z = coordinate.split(",")
        except:
          
            return
        
        #teleports the user to the specified coordinate
        await self.highrise.teleport(user_id = user_id, dest = Position(float(x), float(y), float(z)))

    async def command_handler(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "functions"
        # Check if the function exists in the module
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3]  # Remove the '.py' extension
                module_path = os.path.join(functions_folder, file_name)
                
                # Load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Check if the function exists in the module
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)
        
        # If no matching function is found
        return              

           
    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered: {message}")

        if        message.startswith("/tele") or              message.startswith("/tp") or              message.startswith("/fly") or     message.startswith("!tele") or      message.startswith("!tp") or     message.startswith("!fly"):
          if user.username in moderators:
            await self.teleporter(message)

        if        message.startswith("/") or              message.startswith("-") or              message.startswith(".") or          message.startswith("!"):
            await self.command_handler(user, message)

        if                            message.startswith("Summon") or         message.startswith("Summom") or         message.startswith("!summom") or        message.startswith("/summom") or        message.startswith("/summon") or  message.startswith("!summon"):
          if user.username in moderators:
           target_username = message.split("@")[-1].strip()
           await self.teleport_user_next_to(target_username, user)
            
        if              message.startswith("Carteira") or  message.startswith("Wallet") or    message.startswith("!wallet") or       message.startswith("carteira"):
          if user.username in moderators:
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.send_whisper(user.id,f"AMOUNT : {wallet[0].amount} {wallet[0].type}")
            await self.highrise.send_emote("emote-blowkisses")
            
    async def on_user_move(self, user: User, pos: Position) -> None:
        print (f"{user.username} moved to {pos}")

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        print(f"{user.username} emoted: {emote_id}")

    async def on_user_leave(self, user: User) -> None:
        print(f"{user.username} leave the room ")
        await self.highrise.chat(f"Goodbye {user.username}! ")
        await self.highrise.send_emote("hcc-jetpack")
