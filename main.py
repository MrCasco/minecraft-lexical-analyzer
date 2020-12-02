commands = {
    'ability':'command',
    'attribute':'command',
    "attribute":'command',
    "advancement":'command',
    "ban":'command',
    "ban-ip":'command',
    "banlist":'command',
    "bossbar":'command',
    "clear":'command',
    "clone":'command',
    "data":'command',
    "datapack":'command',
    "debug":'command',
    "defaultgamemode":'command',
    "deop":'command',
    "difficulty":'command',
    "effect":'command',
    "enchant":'command',
    "execute":'command',
    "experience":'command',
    "fill":'command',
    "forceload":'command',
    "function":'command',
    "gamemode":'command',
    "gamerule":'command',
    "give":'command',
    "help":'command',
    "kick":'command',
    "kill":'command',
    "list":'command',
    "locate":'command',
    "locatebiome":'command',
    "loot":'command',
    "me":'command',
    "msg":'command',
    "op":'command',
    "pardon":'command',
    "particle":'command',
    "playsound":'command',
    "publish":'command',
    "recipe":'command',
    "reload":'command',
    "save-all":'command',
    "save-on":'command',
    "save-off":'command',
    "say":'command',
    "schedule":'command',
    "scoreboard":'command',
    "seed":'command',
    "setblock":'command',
    "setidletimeout":'command',
    "setworldspawn":'command',
    "spawnpoint":'command',
    "spectate":'command',
    "spreadplayers":'command',
    "stop":'command',
    "stopsound":'command',
    "summon":'command',
    "tag":'command',
    "teammsg":'command',
    "teleport":'command',
    "tell":'command',
    "tellraw":'command',
    "time":'command',
    "title":'command',
    "tp":'command',
    "trigger":'command',
    "w":'command',
    "weather":'command',
    "whitelist":'command',
    "worldborder":'command',
    "xp":'command'
}
operators = '+-*/='
separator = ';,:."()[]<>~'
literal = '0123456789'

def lexical_analyzer(cmd):
    if not cmd[0] == '/':
        return 'This is a comment'
    else:
        cmd = cmd[1:].split()
        res = ''
        for token in cmd:
            try:
                res += commands[token] + ' '
            except:
                if token in operators:
                    res += 'operator '
                elif token in separator:
                    res += 'separator '
                elif token[0] in literal:
                    try:
                        float(token)
                        res += 'literal '
                    except:
                        res += 'identifier '
                else:
                    res += 'identifier '
        return res

running = 'y'
while running == 'y':
    txt = input('Ingrese el comando a analizar: ')
    print("Su comando se descompone como: "+lexical_analyzer(txt))
    running = input('¿Desea volver a probar un comando? (y/n)  ')
    print('\n')
    while running != 'y' and running != 'n':
        print('\nInput no deseado. Prueba otra vez (Sólo se admite "y" o "n")\n')
        running = input('¿Desea volver a probar un comando? (y/n)  ')

# print(lexical_analyzer('/tp casco 0 0 0'))
# print(lexical_analyzer('/summon 100 200 0 minecraft:enderman'))
# print(lexical_analyzer('/effect player1 minecraft:speed 60 2'))
# print(lexical_analyzer('/teleport playerTwo 0 0 100'))
# print(lexical_analyzer('/fill 0 0 0 100 100 100 minecraft:water'))
