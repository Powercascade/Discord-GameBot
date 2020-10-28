
#POSITION
pos = {
"pos_1": 0,
"pos_2": 1,
"pos_3": 2,
"pos_4" : 3,
"pos_5": 4,
"pos_6" : 5,
"pos_7": 6,
"pos_8": 7,
"pos_9": 8
}
# Status
BLANK = "BLANK"

global user_1
global user_2

global GAME_BOARD
GAME_BOARD = [BLANK,BLANK,BLANK,
              BLANK,BLANK,BLANK,
              BLANK,BLANK,BLANK]
onetoninereal = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "❗"]
onetonine = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "❗"]

def reset_icons(icon):
    icon.clear()
    for x in range(len(onetoninereal)):
        icon.append(onetoninereal[x])
    return icon

def remove_icon(icon,reaction):
    for x in range(len(icon)):
        if icon[x] == reaction:
            icon.remove(reaction)
            return

def check_win(USER_X,USER_O):
    if (GAME_BOARD[pos["pos_1"]] == GAME_BOARD[pos["pos_2"]] == GAME_BOARD[pos["pos_3"]]) and (GAME_BOARD[pos["pos_1"]] != BLANK):
        if GAME_BOARD[pos["pos_1"]] == USER_X:
            return USER_X
        elif GAME_BOARD[pos["pos_1"]] == USER_O:
            return USER_O
    elif (GAME_BOARD[pos["pos_4"]] == GAME_BOARD[pos["pos_5"]] == GAME_BOARD[pos["pos_6"]]) and (GAME_BOARD[pos["pos_4"]] != BLANK):
        if GAME_BOARD[pos["pos_4"]] == USER_X:
            return USER_X
        elif GAME_BOARD[pos["pos_4"]] == USER_O:
            return USER_O
    elif (GAME_BOARD[pos["pos_7"]] == GAME_BOARD[pos["pos_8"]] == GAME_BOARD[pos["pos_9"]]) and (GAME_BOARD[pos["pos_7"]] != BLANK):
        if GAME_BOARD[pos["pos_7"]] == USER_X:
            return USER_X
        elif GAME_BOARD[pos["pos_7"]] == USER_O:
            return USER_O
    elif (GAME_BOARD[pos["pos_1"]] == GAME_BOARD[pos["pos_5"]] == GAME_BOARD[pos["pos_9"]]) and (GAME_BOARD[pos["pos_1"]] != BLANK):
        if GAME_BOARD[pos["pos_1"]] == USER_X:
            return USER_X
        elif GAME_BOARD[pos["pos_1"]] == USER_O:
            return USER_O
    elif (GAME_BOARD[pos["pos_3"]] == GAME_BOARD[pos["pos_5"]] == GAME_BOARD[pos["pos_7"]]) and (GAME_BOARD[pos["pos_3"]] != BLANK):
        if GAME_BOARD[pos["pos_3"]] == USER_X:
            return USER_X
        elif GAME_BOARD[pos["pos_3"]] == USER_O:
            return USER_O
    else:
        return BLANK
def return_board():
    return GAME_BOARD


def give_move(emoji, user):
    onetonine = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
    if emoji == onetonine[0]:
        make_move(0, user)
    elif emoji == onetonine[1]:
        make_move(1, user)
    elif emoji == onetonine[2]:
        make_move(2, user)
    elif emoji == onetonine[3]:
        make_move(3, user)
    elif emoji == onetonine[4]:
        make_move(4, user)
    elif emoji == onetonine[5]:
        make_move(5, user)
    elif emoji == onetonine[6]:
        make_move(6, user)
    elif emoji == onetonine[7]:
        make_move(7, user)
    elif emoji == onetonine[8]:
        make_move(8, user)
    else:
        print("error")


def print_game_board(user1, user2):
    blank_char = "⬜"
    board_message = ""
    BLANK = 'BLANK'
    game_board = return_board()
    tile = 1
    for x in range(9):
        if game_board[x] == BLANK:
            if tile % 3 == 0:
                board_message = board_message + blank_char + "\n"
            else:
                board_message = board_message + blank_char
            tile += 1
        if game_board[x] == user1:
            if tile % 3 == 0:
                board_message = board_message + user1 + "\n"
            else:
                board_message = board_message + user1
            tile += 1
        if game_board[x] == user2:
            if tile % 3 == 0:
                board_message = board_message + user2 + "\n"
            else:
                board_message = board_message + user2
            tile += 1

    return board_message


def reset_board(gameboard1):
    gameboard1.clear()
    for x in range(9):
        gameboard1.append(BLANK)
    return gameboard1

def make_move(position,user):
    if position in pos.values():
        if GAME_BOARD[position] == BLANK:
            GAME_BOARD[position] = user


