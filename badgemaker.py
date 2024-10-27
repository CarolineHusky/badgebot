import pygame
import urllib
import json
import os

import traceback
import time
import unicodedata

pygame.init()

DOWNLOAD_FOLDER="."
TELEGRAM_TOKEN=#Fill your telegram token here
fonts = pygame.sysfont.get_fonts()
emojis = [font for font in fonts if "emoji" in font]
FONT="Wizzard.ttf"
EMOJI_FONT="NotoEmoji-VariableFont_wght.ttf"
MIN_FONT_SIZE=34
MAX_FONT_SIZE=80
FONT_COLOR=(255,255,255)

EMOJI={169,174,8252,8265,8419,8482,8505,8596,8597,8598,8599,8600,8601,8617,8618,8986,8987,9000,9167,9193,9194,9195,9196,9197,9198,9199,9200,9201,9202,9203,9208,9209,9210,9410,9642,9643,9654,9664,9723,9725,9726,9728,9729,9730,9731,9732,9742,9745,9748,9749,9752,9757,9760,9762,9763,9766,9770,9774,9775,9784,9785,9786,9792,9794,9800,9801,9802,9803,9804,9805,9806,9807,9808,9809,9810,9811,9823,9824,9827,9829,9830,9832,9851,9854,9855,9874,9875,9876,9877,9878,9879,9881,9883,9884,9888,9889,9895,9898,9899,9904,9905,9917,9918,9924,9925,9928,9934,9935,9937,9939,9940,9961,9962,9968,9969,9970,9971,9972,9973,9975,9976,9977,9978,9981,9986,9989,9992,9993,9994,9995,9996,9997,9999,10002,10004,10006,10013,10017,10024,10035,10036,10052,10055,10060,10062,10067,10068,10069,10071,10083,10084,10133,10134,10135,10145,10160,10175,10548,10549,11013,11014,11015,11035,11036,11088,11093,12336,12349,12951,12953,126980,127183,127344,127345,127358,127359,127374,127377,127378,127379,127380,127381,127382,127383,127384,127385,127386,127462,127463,127464,127465,127466,127467,127468,127469,127470,127471,127472,127473,127474,127475,127476,127477,127478,127479,127480,127481,127482,127483,127484,127485,127486,127487,127489,127490,127514,127535,127538,127539,127540,127541,127542,127543,127544,127545,127546,127568,127569,127744,127745,127746,127747,127748,127749,127750,127751,127752,127753,127754,127755,127756,127757,127758,127759,127760,127761,127762,127763,127764,127765,127766,127767,127768,127769,127770,127771,127772,127773,127774,127775,127776,127777,127780,127781,127782,127783,127784,127785,127786,127787,127788,127789,127790,127791,127792,127793,127794,127795,127796,127797,127798,127799,127800,127801,127802,127803,127804,127805,127806,127807,127808,127809,127810,127811,127812,127813,127814,127815,127816,127817,127818,127819,127820,127821,127822,127823,127824,127825,127826,127827,127828,127829,127830,127831,127832,127833,127834,127835,127836,127837,127838,127839,127840,127841,127842,127843,127844,127845,127846,127847,127848,127849,127850,127851,127852,127853,127854,127855,127856,127857,127858,127859,127860,127861,127862,127863,127864,127865,127866,127867,127868,127869,127870,127871,127872,127873,127874,127875,127876,127877,127878,127879,127880,127881,127882,127883,127884,127885,127886,127887,127888,127889,127890,127891,127894,127895,127897,127898,127899,127902,127903,127904,127905,127906,127907,127908,127909,127910,127911,127912,127913,127914,127915,127916,127917,127918,127919,127920,127921,127922,127923,127924,127925,127926,127927,127928,127929,127930,127931,127932,127933,127934,127935,127936,127937,127938,127939,127940,127941,127942,127943,127944,127945,127946,127947,127948,127949,127950,127951,127952,127953,127954,127955,127956,127957,127958,127959,127960,127961,127962,127963,127964,127965,127966,127967,127968,127969,127970,127971,127972,127973,127974,127975,127976,127977,127978,127979,127980,127981,127982,127983,127984,127987,127988,127989,127991,127992,127993,127994,127995,127996,127997,127998,127999,128000,128001,128002,128003,128004,128005,128006,128007,128008,128009,128010,128011,128012,128013,128014,128015,128016,128017,128018,128019,128020,128021,128022,128023,128024,128025,128026,128027,128028,128029,128030,128031,128032,128033,128034,128035,128036,128037,128038,128039,128040,128041,128042,128043,128044,128045,128046,128047,128048,128049,128050,128051,128052,128053,128054,128055,128056,128057,128058,128059,128060,128061,128062,128063,128064,128065,128066,128067,128068,128069,128070,128071,128072,128073,128074,128075,128076,128077,128078,128079,128080,128081,128082,128083,128084,128085,128086,128087,128088,128089,128090,128091,128092,128093,128094,128095,128096,128097,128098,128099,128100,128101,128102,128103,128104,128105,128110,128111,128112,128113,128114,128115,128116,128117,128118,128119,128121,128122,128123,128124,128125,128126,128127,128128,128129,128130,128131,128132,128133,128134,128135,128136,128137,128138,128139,128140,128141,128142,128143,128144,128145,128146,128147,128148,128149,128150,128151,128152,128153,128154,128155,128156,128157,128158,128159,128160,128161,128162,128163,128164,128165,128166,128167,128168,128169,128170,128171,128172,128173,128174,128175,128176,128177,128178,128179,128180,128181,128182,128183,128184,128185,128186,128187,128188,128189,128190,128191,128192,128193,128194,128195,128196,128197,128198,128199,128200,128201,128202,128203,128204,128205,128206,128207,128208,128209,128210,128211,128212,128213,128214,128215,128216,128217,128218,128219,128220,128221,128222,128223,128224,128225,128226,128227,128228,128229,128230,128231,128232,128233,128234,128235,128236,128237,128238,128239,128240,128241,128242,128243,128244,128245,128246,128247,128248,128249,128250,128251,128252,128253,128255,128256,128257,128258,128259,128260,128261,128262,128263,128264,128265,128266,128267,128268,128269,128270,128271,128272,128273,128274,128275,128276,128277,128278,128279,128280,128281,128282,128283,128284,128285,128286,128287,128288,128289,128290,128291,128292,128293,128294,128295,128296,128297,128298,128299,128300,128301,128302,128303,128304,128305,128306,128307,128308,128309,128310,128311,128312,128313,128314,128315,128316,128317,128329,128330,128331,128332,128333,128334,128336,128337,128338,128339,128340,128341,128342,128343,128344,128345,128346,128347,128348,128349,128350,128351,128352,128353,128354,128355,128356,128357,128358,128359,128367,128368,128371,128372,128373,128374,128375,128376,128377,128391,128394,128395,128396,128397,128400,128405,128406,128420,128421,128424,128433,128434,128444,128450,128451,128452,128465,128466,128467,128476,128477,128478,128481,128483,128488,128495,128499,128506,128507,128508,128509,128510,128511,128512,128513,128514,128515,128516,128517,128518,128519,128520,128521,128522,128523,128524,128525,128526,128527,128528,128529,128530,128531,128532,128533,128534,128535,128536,128537,128538,128539,128540,128541,128542,128543,128544,128545,128546,128547,128548,128549,128550,128551,128552,128553,128554,128555,128556,128557,128558,128559,128560,128561,128562,128563,128564,128565,128566,128567,128568,128569,128570,128571,128572,128573,128574,128575,128576,128577,128578,128579,128580,128581,128582,128583,128584,128585,128586,128587,128588,128589,128590,128591,128640,128641,128642,128643,128644,128645,128646,128647,128648,128649,128650,128651,128652,128653,128654,128655,128656,128657,128658,128659,128660,128661,128662,128663,128664,128665,128666,128667,128668,128669,128670,128671,128672,128673,128674,128675,128676,128677,128678,128679,128680,128681,128682,128683,128684,128685,128686,128687,128688,128689,128690,128691,128692,128693,128694,128695,128696,128697,128698,128699,128700,128701,128702,128703,128704,128705,128706,128707,128708,128709,128715,128716,128717,128718,128719,128720,128721,128722,128725,128726,128727,128732,128733,128734,128735,128736,128737,128738,128739,128740,128741,128745,128747,128748,128752,128755,128756,128757,128758,128759,128760,128761,128762,128763,128764,128992,128993,128994,128995,128996,128997,128998,128999,129000,129001,129002,129003,129008,129292,129293,129294,129295,129296,129297,129298,129299,129300,129301,129302,129303,129304,129305,129306,129307,129308,129309,129310,129311,129312,129313,129314,129315,129316,129317,129318,129319,129320,129321,129322,129323,129324,129325,129326,129327,129329,129330,129331,129333,129335,129336,129337,129338,129340,129341,129342,129343,129344,129345,129346,129347,129348,129349,129351,129352,129353,129354,129355,129356,129357,129358,129359,129360,129361,129362,129363,129364,129365,129366,129367,129368,129369,129370,129371,129372,129373,129374,129375,129376,129377,129378,129379,129380,129381,129382,129383,129384,129385,129386,129387,129388,129389,129390,129391,129392,129393,129394,129395,129396,129397,129398,129399,129400,129401,129402,129403,129404,129405,129406,129407,129408,129409,129410,129411,129412,129413,129414,129415,129416,129417,129418,129419,129420,129421,129422,129423,129424,129425,129426,129427,129428,129429,129430,129431,129432,129433,129434,129435,129436,129437,129438,129439,129440,129441,129442,129443,129444,129445,129446,129447,129448,129449,129450,129451,129452,129453,129454,129455,129456,129457,129458,129459,129460,129461,129462,129463,129464,129465,129466,129467,129468,129469,129470,129471,129472,129473,129474,129475,129476,129477,129478,129479,129480,129481,129482,129483,129484,129485,129486,129487,129488,129489,129490,129491,129492,129493,129494,129495,129496,129497,129498,129499,129500,129501,129502,129503,129504,129505,129506,129507,129508,129509,129510,129511,129512,129513,129514,129515,129516,129517,129518,129519,129520,129521,129522,129523,129524,129525,129526,129527,129528,129529,129530,129531,129532,129533,129534,129535,129648,129649,129650,129651,129652,129653,129654,129655,129656,129657,129658,129659,129660,129664,129665,129666,129667,129668,129669,129670,129671,129672,129673,129679,129680,129681,129682,129683,129684,129685,129686,129687,129688,129689,129690,129691,129692,129693,129694,129695,129696,129697,129698,129699,129700,129701,129702,129703,129704,129705,129706,129707,129708,129709,129710,129711,129712,129713,129714,129715,129716,129717,129718,129719,129720,129721,129722,129723,129724,129725,129726,129727,129728,129729,129730,129732,129733,129734,129742,129743,129744,129745,129746,129747,129748,129749,129750,129751,129752,129753,129754,129755,129756,129759,129760,129761,129762,129763,129764,129765,129766,129767,129768,129769,129776,129777,129778,129779,129780,129781,129782,129783,129784}

def darken(color, amount=1):
    return color[0]>>amount, color[1]>>amount, color[2]>>amount

def glyphInFont( glyph, font ):
    """ Given a glyph and a font, use a pixel-finding heuristic to determine
        if the glyph renders to something other than an "empty border" non-existant
        font symbol.  Returns True if it renders to something. """

    result = False
    WHITE  = ( 255, 255, 255 )   # can be any colour pair with constrast
    BLACK  = (   0,   0,   0 )

    try:
        text_image = font.render( glyph, True, WHITE, BLACK )
        text_rect  = text_image.get_rect()
        x_centre = text_rect.width // 2
        y_centre = text_rect.height // 2

        # On Linux at least, non-renderable glyphs have a border.
        # work out a 50% search box, centred inside the gluph
        box_top    = y_centre - ( text_rect.height // 4 )
        box_bottom = y_centre + ( text_rect.height // 4 )
        box_left   = x_centre - ( text_rect.width // 4 )
        box_right  = x_centre + ( text_rect.width // 4 )

        # Trace a Horizontal line through the middle of the bitmap
        # looking for non-black pixels
        for x in range( box_left, box_right ):
            if ( text_image.get_at( ( x, y_centre ) ) != BLACK ):
                result = True
                break

        # If not found already, trace a line vertically
        if ( result == False ):
            for y in range( box_top, box_bottom ):
                if ( text_image.get_at( ( x_centre, y ) ) != BLACK ):
                    result = True
                    break

        # If still not found, check every pixel in the centre-box
        if ( result == False ):
            for y in range( box_top, box_bottom ):
                for x in range( box_left, box_right ):
                    if ( text_image.get_at( ( x, y ) ) != BLACK ):
                        result = True
                        break

    except UnicodeError as uce:
        # Glyph-ID not supported
        pass  # False goes through
    except pygame.error:
        pass
    return result


def render_text(text, size, bg_color):
    t=""
    d=[]
    regular=pygame.font.Font(FONT, size)
    fallback=pygame.font.Font(None, size)
    emoji=pygame.font.Font(EMOJI_FONT, size)
    emoji1=pygame.font.Font(EMOJI_FONT, 120)
    x=0
    y=0
    t=""
    for char in text:
        if ord(char) in range(0x1F1E6, 0x1F200):
            pass #regional flag indicators
        elif ord(char) in EMOJI:
            if t!="":
                d.append(regular.render(t, True, FONT_COLOR, bg_color))
                x+=d[-1].get_width()
                y=max(y, d[-1].get_height())
                t=""
            d.append(emoji.render(char, True, FONT_COLOR, bg_color))
            x+=d[-1].get_width()
            y=max(y, d[-1].get_height())
        elif glyphInFont(char, regular):
            t+=char
        elif glyphInFont(char, fallback):
            if t!="":
                d.append(regular.render(t, True, FONT_COLOR, bg_color))
                x+=d[-1].get_width()
                y=max(y, d[-1].get_height())
                t=""
            d.append(fallback.render(char, True, FONT_COLOR, bg_color))
            x+=d[-1].get_width()
        else:
            c=unicodedata.normalize("NFKD", char)
            t+=c[0]
    if t!="":
        d.append(regular.render(t, True, FONT_COLOR, bg_color))
        x+=d[-1].get_width()
        y=max(y, d[-1].get_height())
    s=pygame.Surface((x,y))
    s.fill(bg_color)
    x=0
    for ele in d:
        s.blit(ele, (x, (y-ele.get_height())*2/3))
        x+=ele.get_width()
    return s

def draw_text(text, max_width, bg_color, bias=1, max_height=None):
    for size in reversed(range(int(MIN_FONT_SIZE*bias), int(MAX_FONT_SIZE*bias))):
        font = pygame.font.Font(FONT, size)
        surface = render_text(text, size, bg_color)
        width, height = surface.get_size()
        if width>max_width:
            continue
        if max_height is not None and height>max_height:
            continue
        new_surface = pygame.Surface((max_width, surface.get_height()))
        new_surface.fill(bg_color)
        new_surface.blit(surface, ((max_width-surface.get_width())/2, 0))
        return new_surface
    print(text, size, (width, max_width), (height, max_height))
    return None

def draw_full_text(text, max_width, bg_color, bias=1, max_height=None, margin=0):
    def draw_full_text_internal(text, max_width, bg_color, bias=1, max_height=None):
        split_amount=1
        split_text = text.split(" ")
        while split_amount<=len(split_text):
            groups=int(len(split_text)/split_amount)
            drawns=[]
            height=0
            if max_height is not None:
                mxh=max_height/groups
            else:
                mxh=None
            for i in range(0, len(split_text), groups):
                chunk = " ".join(split_text[i:i+groups])
                drawn = draw_text(chunk, max_width, bg_color, bias, mxh)
                if drawn is None:
                    split_amount+=1
                    break
                drawns.append(drawn)
                height+=drawn.get_height()
            else:
                surface=pygame.Surface((max_width, height))
                y=0
                for drawn in drawns:
                    surface.blit(drawn, (0, y))
                    y+=drawn.get_height()
                return surface
        return None
    if max_height is not None:
        max_height_i = max_height-margin
    else:
        max_height_i = None
    surface = draw_full_text_internal(text, max_width-margin, bg_color, bias, max_height_i)
    if surface is None:
        return None
    if max_height is None:
        max_height = surface.get_height()+margin
    out = pygame.Surface((max_width, max_height))
    out.fill(bg_color)
    out.blit(surface, (margin>>1, margin>>1))
    return out

def telegram_bot_send_document(chat, filename):
    if chat is None:
        return
    import requests
    url="https://api.telegram.org/bot"+TELEGRAM_TOKEN
    if filename.lower().endswith(".mp4") or filename.lower().endswith(".webm"):
        url+="/sendVideo"
        #thumbnail_url_alt=os.path.join(os.path.expanduser(config["Folders"]["ThumbnailsAlt"]),get_thumbnail_location(filename))
        #thumbnail_url=os.path.join(os.path.expanduser(config["Folders"]["Thumbnails"]),get_thumbnail_location(filename))
        #if os.path.exists(thumbnail_url_alt):
        #    response=requests.post(url, data={'chat_id': chat}, files={'video': open(filename,"rb"), 'thumbnail':open(thumbnail_url_alt,'rb')})
        #elif os.path.exists(thumbnail_url):
        #    response=requests.post(url, data={'chat_id': chat}, files={'video': open(filename,"rb"), 'thumbnail':open(thumbnail_url,'rb')})
        #else:
        response=requests.post(url, data={'chat_id': chat}, files={'video': open(filename,"rb")})
        return response
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".png"):
        url+="/sendPhoto"
        response=requests.post(url, data={'chat_id': chat}, files={'photo': open(filename,"rb")})
        return response
    if filename.lower().endswith(".ogg"):
        url+="/sendVoice"
        response=requests.post(url, data={'chat_id': chat}, files={'voice': open(filename,"rb")})
        return response
    url+="/sendDocument"
    response=requests.post(url, data={'chat_id': chat}, files={'document': open(filename,"rb")})
    return response


def telegram_bot_execute(command, data=None, method=None):
    try:
        headers={}
        if data is not None:
            data=json.dumps(data).encode("utf-8")
            headers["Content-Length"]=len(data)
            headers["Content-Type"]="application/json"
        url="https://api.telegram.org/bot"+TELEGRAM_TOKEN+"/" + command
        request=urllib.request.Request(url,data,headers,method=method)
        return json.load(urllib.request.urlopen(request))
    except urllib.error.HTTPError as e:
        body = json.loads(e.read().decode())  # Read the body of the error response
        if "too big" in body['description']:
            raise ValueError("File too big")
        print("ERROR:")
        print(body)
        print(command, data)
        raise


def telegram_bot_download_file(file_id, destination=None, chat=None, message=None):
    file_info=telegram_bot_execute("getFile", {"file_id": file_id})
    file_path=file_info['result']['file_path']
    if destination is None:
        destination=file_info['result']['file_path'].split('/')[-1]
    if not destination.endswith("."+file_info['result']['file_path'].split(".")[-1]):
        destination+="."+file_info['result']['file_path'].split(".")[-1]
    destination=os.path.join(DOWNLOAD_FOLDER,destination)
    os.makedirs("/".join(destination.split("/")[:-1]), exist_ok=True)
    if os.path.exists(destination):
        return destination

    try:
        url="https://api.telegram.org/file/bot"+TELEGRAM_TOKEN+"/"+file_path
        urllib.request.urlretrieve(url, destination)
        #if destination.lower().split(".")[-1] in ("jpg","jpeg","png","bmp"):
        #    image = Image.open(destination)
        #    image.thumbnail((256,256))
        #    image.save(os.path.join(os.path.expanduser(DOWNLOAD_FOLDER),get_thumbnail_location(destination)))
        return destination
    except urllib.error.HTTPError as e:
        body = json.loads(e.read().decode())  # Read the body of the error response
        print("ERROR:")
        print(body)
        raise

lastupdate=0

def telegram_bot_get_updates():
    global lastupdate
    updates=telegram_bot_execute("getUpdates", {"offset": int(lastupdate)+1, "allowed_updates": ["message", "callback_query"]})["result"]
    for update in updates:
        if update['update_id']>int(lastupdate):
            lastupdate = update['update_id']
        if "message" in update:
            yield update["message"]
        elif "callback_query" in update:
            callback_query=update["callback_query"]
            #telegram_bot_process_callback(update["callback_query"]["data"], str(update["callback_query"]["from"]["id"]))
            telegram_bot_execute("answerCallbackQuery",{"callback_query_id": callback_query["id"]})


def telegram_bot_process_updates():
    global hook_sticker_state
    has_updates=False
    important_command=False
    chat = None
    text = None
    download_file = None

    for update in telegram_bot_get_updates():
        for ele in update:
            if ele=="chat":
                chat=update["chat"]
            elif ele=="text":
                text=update[ele]
            elif isinstance(update[ele],dict) and "file_id" in update[ele]:
                telegram_bot_execute("sendChatAction",{"chat_id":update["chat"]["id"],"action":"typing"})
                try:
                    if "file_name" in update[ele]:
                        download_file=telegram_bot_download_file(update[ele]["file_id"],update[ele]["file_name"], update["chat"]["id"], update["message_id"])
                    elif "file_unique_id" in update[ele]:
                        download_file=telegram_bot_download_file(update[ele]["file_id"],update[ele]["file_unique_id"], update["chat"]["id"], update["message_id"])
                    else:
                        download_file=telegram_bot_download_file(update[ele]["file_id"], None, update["chat"]["id"], update["message_id"])
                except ValueError:
                    telegram_bot_send_message("Sorry, this file is too big.\nThese simple bots support files up to 20MB...",update["chat"]["id"])

        if text=="/start":
            chat=telegram_bot_execute("getChat", {"chat_id":update["chat"]["id"]})["result"]
            print(chat)
            pfp=telegram_bot_download_file(chat["photo"]["big_file_id"], "pfp/"+str(update["chat"]["id"]))
            pfp_surface = pygame.image.load(pfp)
            badge_size = pfp_surface.get_width(), int(pfp_surface.get_height() * 1.545)
            badge_surface = pygame.Surface(badge_size)
            badge_color = pygame.transform.average_color(pfp_surface)
            badge_surface.fill(badge_color)

            y=badge_size[0]
            first_name=draw_full_text(chat["first_name"], badge_size[0], darken(badge_color), margin= 40)
            badge_surface.blit(first_name, (0, y))
            y+=first_name.get_height()
            last_name=draw_full_text(chat["last_name"], badge_size[0], darken(badge_color), 0.75, margin= 40)
            if last_name is not None:
                last_name = last_name.subsurface((0, 20, last_name.get_width(), last_name.get_height()-20))
                badge_surface.blit(last_name, (0, y-20))
                y+=last_name.get_height()-20

            bio=draw_full_text(chat["bio"], badge_size[0], badge_color, 0.75, badge_size[1] - y-20, margin=40)
            if bio is not None:
                center = ((badge_size[1] - y) - bio.get_height())/2 - 10
                badge_surface.blit(bio, (0, y+center))

            badge_surface.blit(pfp_surface, (0,0))
            os.makedirs(DOWNLOAD_FOLDER+"/badge", exist_ok=True)
            filename= "badge/"+str(update["chat"]["id"])+".png"
            pygame.image.save(badge_surface,filename)
            telegram_bot_send_document(update["chat"]["id"], filename)

if __name__=="__main__":
    try:
        while True:
            try:
                telegram_bot_process_updates()
            except Exception as e:
                print(traceback.format_exc())
            time.sleep(1)
    except KeyboardInterrupt:
        pass
