import aiosqlite
import random



async def conn():
    return await aiosqlite.connect('base.db')


async def add_admin(login, password):
    db = await conn()
    sql = await db.cursor()
    await sql.execute("INSERT INTO admins VALUES (?, ?)", (login, password))
    await db.commit()
    await db.close()

async def check_admin(login, password):
    db = await conn()
    sql = await db.cursor()
    await sql.execute("SELECT * FROM admins WHERE login = ?", (login,))
    acc = await sql.fetchone()
    if acc != None:
        if str(acc[1]) == str(password):
            return True
        else:
            return False

    else:
        return "None"

async def add_session(login):
    db = await conn()
    sql = await db.cursor()
    key = ''
    for i in range(86):
        key += random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0987654321')
    await sql.execute("INSERT INTO sessions VALUES (?, ?)", (login, key))
    await db.commit()
    await db.close()
    return str(key)

async def check_session(session):
    db = await conn()
    sql = await db.cursor()
    await sql.execute("SELECT * FROM sessions WHERE session_id = ?", (session,))
    session = await sql.fetchone()
    if session == None:
        await db.commit()
        await db.close()
        return False
    else:
        await db.commit()
        await db.close()
        return True

async def get_track(track):
    db = await conn()
    sql = await db.cursor()
    await sql.execute("SELECT * FROM tracks WHERE track = ?", (track,))
    res = await sql.fetchone()
    await db.commit()
    await db.close()
    return res

async def new_track(track, sender, recipient, weight):
    db = await conn()
    sql = await db.cursor()
    await sql.execute("SELECT * FROM tracks WHERE track = ?", (track,))
    res = await sql.fetchone()
    if res == None:
        await sql.execute("INSERT INTO tracks (track, sender, recipient, weight, status) VALUES (?, ?, ?, ?, ?)", (track, sender, recipient, weight, 0))
        await sql.execute("INSERT INTO statuses VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (track, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        await db.commit()
        await db.close()
    else:
        return "Not"

async def updateStatusTrack(track, status_number, status):
    db = await conn()
    sql = await db.cursor()
    await sql.execute(f"UPDATE statuses SET status{status_number} = ? WHERE track = ? ", (status, track))
    await db.commit()
    await db.close()

async def newStatusTrack(old_track, track):
    db = await conn()
    sql = await db.cursor()
    await sql.execute(F"UPDATE statuses SET track = ? WHERE track = ?", (track, old_track,))
    await db.commit()
    await db.close()

async def track_check(track):
    db = await conn()
    sql = await db.cursor()
    check = await sql.execute("SELECT * FROM tracks WHERE track = ?", (track,))
    res = await sql.fetchone()
    if res == None:
        await db.commit()
        await db.close()
        return False
    else:
        data = {
            'track_number': str(res[0]),
            'sender': str(res[1]),
            'recipient': str(res[2]),
            'weight': str(res[3]),
            'status': str(res[4])
        }
        await db.commit()
        await db.close()
        return data 

async def firststatus(track):
    db = await conn()
    sql = await db.cursor()
    await sql.execute("SELECT * FROM statuses WHERE track = ?", (track,))
    res = await sql.fetchone()
    if res != None:
        await db.commit()
        await db.close()
        return res

async def getStatuses(track):
    db = await conn()
    sql = await db.cursor()
    await sql.execute("SELECT * FROM statuses WHERE track = ?", (track,))
    res = await sql.fetchone()
    if res != None:
        await db.commit()
        await db.close()
        return res
        data = {
            'status0': str(res[1].split('|')[1]),
            'status1': str(res[2].split('|')[1]),
            'status2': str(res[3].split('|')[1]),
            'status3': str(res[4].split('|')[1]),
            'status4': str(res[5].split('|')[1]),
            'status5': str(res[6].split('|')[1]),
            'status6': str(res[7].split('|')[1]),
            'status7': str(res[8].split('|')[1]),
            'status8': str(res[9].split('|')[1]),
            'status9': str(res[10].split('|')[1]),
            'status10': str(res[11].split('|')[1]),
            'status11': str(res[12].split('|')[1]),
            'status12': str(res[13].split('|')[1]),
            'status13': str(res[14].split('|')[1]),
            'status14': str(res[15].split('|')[1]),
            'status15': str(res[16].split('|')[1]),
            'status16': str(res[17].split('|')[1]),
            'status17': str(res[18].split('|')[1]),
            'status18': str(res[19].split('|')[1]),
            'status19': str(res[20].split('|')[1]),
            'status20': str(res[21].split('|')[1]),
            'status21': str(res[22].split('|')[1]),
            'status22': str(res[23].split('|')[1]),
            'status23': str(res[24].split('|')[1]),
            'status24': str(res[25].split('|')[1]),
            'status25': str(res[26].split('|')[1]),
            'status26': str(res[27].split('|')[1]),
            'status27': str(res[28].split('|')[1]),
            'status28': str(res[29].split('|')[1]),
            'status29': str(res[30].split('|')[1]),
            'status30': str(res[31].split('|')[1]),
            'status31': str(res[32].split('|')[1]),
            'status32': str(res[33].split('|')[1]),
            'status33': str(res[34].split('|')[1]),
            'status34': str(res[35].split('|')[1]),
            'status35': str(res[36].split('|')[1]),
            'status36': str(res[37].split('|')[1]),
            'status37': str(res[38].split('|')[1]),
            'status38': str(res[39].split('|')[1]),
            'status39': str(res[40].split('|')[1]),
            'date0': str(res[1].split('|')[0]),
            'date1': str(res[2].split('|')[0]),
            'date2': str(res[3].split('|')[0]),
            'date3': str(res[4].split('|')[0]),
            'date4': str(res[5].split('|')[0]),
            'date5': str(res[6].split('|')[0]),
            'date6': str(res[7].split('|')[0]),
            'date7': str(res[8].split('|')[0]),
            'date8': str(res[9].split('|')[0]),
            'date9': str(res[10].split('|')[0]),
            'date10': str(res[11].split('|')[0]),
            'date11': str(res[12].split('|')[0]),
            'date12': str(res[13].split('|')[0]),
            'date13': str(res[14].split('|')[0]),
            'date14': str(res[15].split('|')[0]),
            'date15': str(res[16].split('|')[0]),
            'date16': str(res[17].split('|')[0]),
            'date17': str(res[18].split('|')[0]),
            'date18': str(res[19].split('|')[0]),
            'date19': str(res[20].split('|')[0]),
            'date20': str(res[21].split('|')[0]),
            'date21': str(res[22].split('|')[0]),
            'date22': str(res[23].split('|')[0]),
            'date23': str(res[24].split('|')[0]),
            'date24': str(res[25].split('|')[0]),
            'date25': str(res[26].split('|')[0]),
            'date26': str(res[27].split('|')[0]),
            'date27': str(res[28].split('|')[0]),
            'date28': str(res[29].split('|')[0]),
            'date29': str(res[30].split('|')[0]),
            'date30': str(res[31].split('|')[0]),
            'date31': str(res[32].split('|')[0]),
            'date32': str(res[33].split('|')[0]),
            'date33': str(res[34].split('|')[0]),
            'date34': str(res[35].split('|')[0]),
            'date35': str(res[36].split('|')[0]),
            'date36': str(res[37].split('|')[0]),
            'date37': str(res[38].split('|')[0]),
            'date38': str(res[39].split('|')[0]),
            'date39': str(res[40].split('|')[0])
        }
        await db.commit()
        await db.close()
        return data

async def getOrders():
    db = await conn()
    sql = await db.cursor()
    await sql.execute("SELECT * FROM tracks ORDER BY id DESC")
    res = await sql.fetchall()
    await db.close()
    return res

async def changeTrack(track, sender, recipient, weight, track_number):
    db = await conn()
    sql = await db.cursor()
    await sql.execute("UPDATE tracks SET sender = ? WHERE track = ?", (sender, track,))
    await sql.execute("UPDATE tracks SET recipient = ? WHERE track = ?", (recipient, track,))
    await sql.execute("UPDATE tracks SET weight = ? WHERE track = ?", (weight, track,))
    await sql.execute("UPDATE tracks SET track = ? WHERE track = ?", (track_number, track,))
    await db.commit()
    await db.close()

async def logout(session):
    try:
        db = await conn()
        sql = await db.cursor()
        await sql.execute("DELETE FROM sessions WHERE session_id = ?", (session,))
        await db.commit()
        await db.close()
        return "yes"
    except Exception as E:
        return str(E)