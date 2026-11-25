import os
from PIL import Image, ImageDraw, ImageFont
W, H = 1024, 1024
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def F(p, s):
    try: return ImageFont.truetype(p, s)
    except Exception: return ImageFont.load_default()
INK = (22, 22, 22); RED = (178, 34, 34); CREAM = (250, 246, 236); NAVY = (24, 48, 96); GREY = (90, 90, 90); LAND = (198, 206, 178); SEA = (226, 238, 244)
def wrap(d, t, f, mw):
    ls, cur = [], ""
    for w in t.split():
        x = (cur + " " + w).strip()
        if d.textlength(x, font=f) <= mw: cur = x
        else:
            if cur: ls.append(cur)
            cur = w
    if cur: ls.append(cur)
    return ls
def T(d, x, y, s, f, c=INK): d.text((x, y), s, font=f, fill=c)
def chip(d, x, y, s, c):
    f = F(SANSB, 9); w = d.textlength(s, font=f) + 10; d.rounded_rectangle([x, y, x + w, y + 13], 2, fill=c); d.text((x + 5, y + 1.5), s, font=f, fill=(255, 255, 255)); return x + w + 4
def headline(d, x, y, s, f, mw, lh=15):
    ls = wrap(d, s, f, mw)
    for i, ln in enumerate(ls): T(d, x, y + i * lh, ln, f)
    return y + len(ls) * lh
def deck(d, x, y, s, mw, lh=12, fs=10):
    f = F(SANS, fs); ls = wrap(d, s, f, mw)
    for i, ln in enumerate(ls): T(d, x, y + i * lh, ln, f)
    return y + len(ls) * lh
def bldg(d, x, y, w, h, c, win=(255, 220, 120)):
    d.rectangle([x, y, x + w, y + h], fill=c, outline=(0, 0, 0))
    for r in range(y + 6, y + h - 4, 10):
        for cx in range(x + 4, x + w - 4, 9): d.rectangle([cx, r, cx + 4, r + 5], fill=win)
def smoke(d, x, y, s=1):
    for i, r in enumerate([8, 10, 12, 10, 8]): d.ellipse([x + i * 10 * s, y - 4 - i * 2, x + i * 10 * s + r * 2, y - 4 - i * 2 + r * 2], fill=(120, 120, 120))
NA = [(-168, 66), (-165, 60), (-158, 58), (-152, 60), (-140, 60), (-135, 58), (-130, 54), (-125, 49), (-124, 42), (-120, 34), (-114, 29), (-110, 24), (-105, 20), (-97, 16), (-94, 17), (-90, 14), (-86, 12), (-83, 9), (-80, 8), (-79, 9), (-83, 10), (-87, 13), (-88, 15), (-90, 14), (-92, 15), (-94, 18), (-97, 19), (-97, 26), (-93, 30), (-89, 30), (-84, 30), (-81, 26), (-80, 32), (-76, 35), (-74, 40), (-70, 42), (-68, 45), (-65, 44), (-60, 47), (-55, 52), (-60, 55), (-65, 58), (-68, 58), (-72, 62), (-78, 62), (-85, 66), (-90, 69), (-95, 69), (-110, 68), (-125, 70), (-140, 70), (-155, 71), (-165, 68), (-168, 66)]
GL = [(-58, 64), (-52, 60), (-44, 60), (-40, 64), (-32, 68), (-25, 70), (-20, 74), (-25, 76), (-35, 77), (-50, 76), (-58, 74), (-62, 70), (-58, 64)]
SA = [(-79, 9), (-77, 4), (-80, -3), (-81, -6), (-77, -12), (-72, -18), (-70, -23), (-70, -30), (-72, -37), (-73, -44), (-74, -50), (-70, -54), (-66, -55), (-65, -45), (-62, -41), (-58, -35), (-52, -32), (-48, -28), (-41, -23), (-39, -17), (-35, -9), (-35, -6), (-40, -3), (-44, -2), (-50, 0), (-53, 4), (-58, 6), (-62, 9), (-68, 11), (-72, 12), (-77, 8), (-79, 9)]
AF = [(-17, 15), (-17, 21), (-15, 27), (-10, 31), (-6, 34), (0, 36), (10, 37), (11, 34), (15, 32), (20, 32), (25, 32), (30, 31), (32, 31), (35, 28), (37, 22), (39, 18), (43, 12), (48, 11), (51, 10), (46, 5), (42, 0), (40, -5), (40, -10), (36, -18), (33, -26), (28, -33), (20, -35), (17, -32), (15, -27), (13, -18), (12, -12), (13, -6), (9, -1), (9, 4), (-8, 4), (-13, 8), (-17, 15)]
EU = [(-9, 37), (-9, 43), (-2, 44), (-1, 46), (-4, 48), (-2, 49), (0, 51), (3, 53), (5, 53), (8, 57), (10, 59), (5, 60), (5, 62), (10, 64), (13, 66), (18, 69), (25, 71), (30, 70), (35, 68), (40, 68), (45, 68), (55, 69), (60, 69), (70, 72), (80, 73), (90, 75), (100, 76), (110, 74), (120, 73), (130, 72), (140, 72), (150, 70), (160, 70), (170, 67), (178, 65), (178, 64), (170, 60), (162, 56), (158, 52), (150, 59), (142, 54), (140, 50), (138, 46), (135, 43), (130, 42), (127, 40), (122, 38), (120, 34), (122, 31), (120, 28), (118, 25), (112, 22), (108, 18), (106, 10), (104, 9), (101, 7), (98, 10), (95, 16), (92, 21), (90, 22), (88, 22), (86, 20), (82, 17), (80, 13), (77, 8), (75, 12), (72, 20), (68, 22), (66, 25), (62, 25), (58, 25), (56, 26), (54, 26), (52, 28), (50, 29), (48, 30), (44, 29), (42, 26), (40, 22), (39, 21), (35, 29), (34, 31), (36, 36), (33, 36), (30, 36), (27, 37), (26, 38), (23, 36), (22, 37), (20, 40), (19, 42), (16, 44), (14, 45), (12, 44), (8, 44), (6, 43), (3, 43), (0, 40), (-2, 37), (-6, 36), (-9, 37)]
AU = [(113, -22), (114, -30), (115, -35), (118, -35), (124, -33), (129, -32), (132, -32), (135, -35), (138, -35), (140, -38), (145, -38), (150, -37), (153, -32), (153, -27), (150, -22), (146, -19), (142, -11), (141, -13), (136, -12), (132, -11), (130, -13), (126, -14), (122, -17), (118, -20), (113, -22)]
LANDS = [NA, GL, SA, AF, EU, AU]

def scene_riyadh(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 22, 48)); base = y + h
    for sx, sy, r in [(20, 14, 2), (70, 8, 1), (150, 18, 2), (220, 10, 1), (280, 16, 2), (310, 8, 1)]: d.ellipse([x + sx, y + sy, x + sx + r, y + sy + r], fill=(255, 255, 255))
    d.ellipse([x + w - 62, y + 8, x + w - 38, y + 32], fill=(240, 230, 190))
    bldg(d, x + 8, base - 52, 26, 52, (40, 52, 88)); bldg(d, x + 38, base - 70, 30, 70, (52, 66, 110)); bldg(d, x + 72, base - 44, 24, 44, (36, 46, 80)); bldg(d, x + 100, base - 60, 28, 60, (46, 58, 96)); bldg(d, x + 232, base - 48, 26, 48, (40, 52, 88)); bldg(d, x + 262, base - 66, 30, 66, (52, 66, 110)); bldg(d, x + 296, base - 40, 24, 40, (36, 46, 80))
    tx = x + 190; d.polygon([(tx, base - 92), (tx + 34, base - 92), (tx + 30, base), (tx + 4, base)], fill=(70, 88, 140)); d.polygon([(tx, base - 92), (tx + 34, base - 92), (tx + 22, base - 82), (tx + 8, base - 82)], fill=(120, 150, 200))
    for r in range(base - 86, base - 6, 9):
        for cx in range(tx + 6, tx + 28, 8): d.rectangle([cx, r, cx + 4, r + 5], fill=(255, 220, 120))
    d.ellipse([tx - 4, base - 96, tx + 20, base - 74], fill=(255, 120, 30)); d.ellipse([tx + 1, base - 91, tx + 15, base - 79], fill=(255, 200, 60)); smoke(d, tx + 26, base - 84, 1)
    dx, dy = x + 96, y + 16; d.line([dx - 12, dy, dx + 12, dy], fill=(200, 200, 200), width=2); d.rectangle([dx - 6, dy - 3, dx + 6, dy + 3], fill=(60, 60, 60)); d.ellipse([dx - 16, dy - 7, dx - 8, dy + 1], fill=(180, 180, 180)); d.ellipse([dx + 8, dy - 7, dx + 16, dy + 1], fill=(180, 180, 180)); d.line([dx, dy + 3, dx, dy + 12], fill=(255, 120, 30), width=2)
def scene_shanghai(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 222, 205)); d.rectangle([x + 14, y + 46, x + w - 14, y + h], fill=(150, 30, 30)); d.polygon([(x + 8, y + 50), (x + w // 2, y + 18), (x + w - 8, y + 50)], fill=(120, 20, 20)); d.ellipse([x + w // 2 - 13, y + 26, x + w // 2 + 13, y + 52], fill=(255, 215, 0))
    for i in range(5): d.polygon([(x + w // 2 - 8 + i * 3, y + 33), (x + w // 2 + 2 + i * 3, y + 39), (x + w // 2 - 2 + i * 3, y + 45)], fill=(255, 215, 0))
    for cx in range(x + 30, x + w - 30, 34): d.rectangle([cx, y + 62, cx + 12, y + h - 6], fill=(200, 190, 160))
    d.rectangle([x + w - 108, y + h - 52, x + w - 18, y + h - 4], fill=(255, 255, 255), outline=(40, 40, 40)); d.rectangle([x + w - 104, y + h - 48, x + w - 58, y + h - 30], fill=(250, 250, 250), outline=(120, 120, 120))
    for r in range(y + h - 46, y + h - 32, 5): d.line([x + w - 102, r, x + w - 60, r], fill=(150, 150, 150))
    d.rectangle([x + w - 96, y + h - 26, x + w - 22, y + h - 8], fill=(178, 34, 34)); T(d, x + w - 94, y + h - 25, "CCDI", F(SANSB, 10), (255, 255, 255)); d.ellipse([x + 18, y + 8, x + 52, y + 42], outline=(90, 60, 20), width=3); d.line([x + 46, y + 36, x + 66, y + 56], fill=(90, 60, 20), width=3); T(d, x + 70, y + 10, "PROBE", F(SANSB, 13), (120, 20, 20))
def scene_court(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 226, 240)); d.rectangle([x + 20, y + 58, x + w - 20, y + h], fill=(240, 238, 230)); d.polygon([(x + 10, y + 62), (x + w // 2, y + 26), (x + w - 10, y + 62)], fill=(180, 40, 40)); d.ellipse([x + w // 2 - 16, y + 34, x + w // 2 + 16, y + 66], fill=(255, 215, 0))
    for cx in range(x + 36, x + w - 36, 44): d.rectangle([cx, y + 66, cx + 12, y + h - 8], fill=(200, 195, 180), outline=(120, 115, 100))
    d.rectangle([x + 14, y + h - 10, x + w - 14, y + h - 2], fill=(120, 115, 100)); cx, cy = x + 66, y + 86
    for a, b in [(-1, -1), (1, -1), (0, 1)]: d.ellipse([cx + a * 16 - 7, cy + b * 10 - 7, cx + a * 16 + 7, cy + b * 10 + 7], fill=(178, 34, 34))
    d.line([x + w - 96, y + 20, x + w - 52, y + 46], fill=(120, 80, 40), width=5); d.rectangle([x + w - 104, y + 12, x + w - 88, y + 26], fill=(120, 80, 40)); d.ellipse([x + w - 52, y + 40, x + w - 36, y + 54], fill=(120, 80, 40)); d.rectangle([x + w - 100, y + 52, x + w - 30, y + 58], fill=(90, 60, 30)); T(d, x + w - 96, y + 62, "10 / 12", F(SANSB, 13), RED)
def strip_scene(d, x, y, w, h, kind):
    d.rectangle([x, y, x + w, y + h], fill=(30, 40, 60))
    if kind == "drone":
        d.rectangle([x, y, x + w, y + h], fill=(16, 22, 48))
        for sx in range(6, w - 6, 22): d.ellipse([x + sx, y + 6, x + sx + 2, y + 8], fill=(255, 255, 255))
        bldg(d, x + 10, y + h - 26, 18, 26, (52, 66, 110)); bldg(d, x + 32, y + h - 34, 22, 34, (70, 88, 140)); d.ellipse([x + w - 40, y + 6, x + w - 22, y + 24], fill=(255, 120, 30)); smoke(d, x + w - 46, y + 10, 0.5)
    elif kind == "trophy":
        d.rectangle([x, y, x + w, y + h], fill=(24, 90, 50)); d.ellipse([x + w // 2 - 16, y + 4, x + w // 2 + 16, y + 26], fill=(255, 215, 0)); d.rectangle([x + w // 2 - 4, y + 24, x + w // 2 + 4, y + h - 4], fill=(255, 215, 0)); d.rectangle([x + 8, y + h - 12, x + 66, y + h - 2], fill=(0, 120, 60)); d.rectangle([x + w - 74, y + h - 12, x + w - 8, y + h - 2], fill=(200, 30, 30))
    elif kind == "ship":
        d.rectangle([x, y, x + w, y + h], fill=(40, 90, 120)); d.rectangle([x, y + h - 12, x + w, y + h], fill=(20, 50, 80)); d.rectangle([x + 20, y + h - 26, x + w - 60, y + h - 12], fill=(178, 34, 34))
        for i in range(4): d.rectangle([x + 28 + i * 26, y + h - 24, x + 46 + i * 26, y + h - 14], fill=(255, 255, 255))
        d.polygon([(x + w - 56, y + h - 26), (x + w - 56, y + 6), (x + w - 40, y + h - 26)], fill=(220, 220, 220)); d.ellipse([x + w - 30, y + 4, x + w - 12, y + 22], fill=(255, 120, 30))
    elif kind == "chart":
        d.rectangle([x, y, x + w, y + h], fill=(250, 246, 236)); d.line([x + 8, y + h - 8, x + w - 8, y + 6], fill=(24, 120, 60), width=3); d.line([x + 8, y + 14, x + w - 8, y + 14], fill=(178, 34, 34), width=1); T(d, x + 10, y + 2, "50,000", F(SANSB, 11), RED); T(d, x + w - 66, y + h - 14, "50,018", F(SANSB, 11), (24, 120, 60))
    elif kind == "server":
        d.rectangle([x, y, x + w, y + h], fill=(40, 40, 48))
        for i in range(3): d.rectangle([x + 10 + i * 34, y + 5, x + 36 + i * 34, y + h - 5], fill=(70, 70, 80), outline=(150, 150, 150))
        d.rectangle([x + 120, y + 5, x + w - 8, y + h - 5], fill=(178, 34, 34)); T(d, x + 126, y + 10, "CODE RED", F(SANSB, 12), (255, 255, 255))
    elif kind == "heli":
        d.rectangle([x, y, x + w, y + h], fill=(200, 220, 235)); d.polygon([(x + 6, y + h - 4), (x + 70, y + 8), (x + 130, y + h - 4)], fill=(120, 130, 120)); d.ellipse([x + 70, y + 8, x + 120, y + 26], fill=(60, 80, 60)); d.line([x + 60, y + 10, x + 150, y + 10], fill=(60, 60, 60), width=3); d.line([x + 118, y + 16, x + 160, y + 22], fill=(60, 60, 60), width=2)
    elif kind == "shop":
        d.rectangle([x, y, x + w, y + h], fill=(240, 230, 200)); d.rectangle([x + 14, y + 10, x + w - 14, y + h - 4], fill=(200, 60, 60)); d.rectangle([x + 24, y + 16, x + w - 24, y + h - 8], fill=(255, 255, 255)); d.line([x + 14, y + 10, x + w - 14, y + 10], fill=(255, 215, 0), width=3); T(d, x + 30, y + 18, "25 HELD", F(SANSB, 11), RED)
    elif kind == "desert":
        d.rectangle([x, y, x + w, y + h], fill=(235, 215, 170)); d.ellipse([x + w - 40, y + 2, x + w - 10, y + 32], fill=(255, 200, 80)); d.polygon([(x + 6, y + h - 4), (x + 60, y + 12), (x + 120, y + h - 4)], fill=(200, 170, 110)); d.rectangle([x + 30, y + h - 18, x + 90, y + h - 6], fill=(90, 70, 50)); d.line([x + 100, y + h - 12, x + w - 10, y + h - 20], fill=(178, 34, 34), width=2)
    elif kind == "truck":
        d.rectangle([x, y, x + w, y + h], fill=(220, 200, 160)); d.rectangle([x + 16, y + h - 22, x + 110, y + h - 6], fill=(180, 180, 180), outline=(40, 40, 40)); d.rectangle([x + 112, y + h - 20, x + 140, y + h - 6], fill=(178, 34, 34)); d.ellipse([x + 34, y + h - 8, x + 46, y + h + 2], fill=(30, 30, 30)); d.ellipse([x + 120, y + h - 8, x + 132, y + h + 2], fill=(30, 30, 30)); d.ellipse([x + w - 40, y + 4, x + w - 16, y + 28], fill=(255, 120, 30))
    elif kind == "rocket":
        d.rectangle([x, y, x + w, y + h], fill=(10, 16, 40))
        for sx in range(6, w - 6, 20): d.ellipse([x + sx, y + 5, x + sx + 2, y + 7], fill=(255, 255, 255))
        d.polygon([(x + w // 2 - 8, y + 4), (x + w // 2 + 8, y + 4), (x + w // 2 + 5, y + h - 14), (x + w // 2 - 5, y + h - 14)], fill=(230, 230, 230)); d.polygon([(x + w // 2 - 8, y + 4), (x + w // 2, y - 6), (x + w // 2 + 8, y + 4)], fill=(178, 34, 34)); d.polygon([(x + w // 2 - 12, y + h - 16), (x + w // 2 - 4, y + h - 16), (x + w // 2 - 8, y + h - 2)], fill=(255, 120, 30)); d.polygon([(x + w // 2 + 12, y + h - 16), (x + w // 2 + 4, y + h - 16), (x + w // 2 + 8, y + h - 2)], fill=(255, 120, 30))

def build():
    im = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(im); d.rectangle([0, 0, W, 5], fill=RED)
    T(d, 8, 10, "THE WORLD ON ONE PAGE", F(SANSB, 11), RED); d.text((1016 - d.textlength("38 STORIES  ·  6 REGIONS  ·  13 FIELDS", font=F(SANSB, 11)), 10), "38 STORIES  ·  6 REGIONS  ·  13 FIELDS", font=F(SANSB, 11), fill=INK)
    T(d, 8, 26, "Tuesday 24 November 2026", F(SERIF, 36), INK); T(d, 8, 66, "Houthi drone hits Riyadh's tallest tower again  ·  China probes Shanghai party chief  ·  Huawei guilty on 10 of 12 counts", F(SERIF, 13), RED)
    regs = [("Europe", 9, (24, 48, 96)), ("Middle East", 8, (178, 34, 34)), ("Asia", 8, (176, 132, 30)), ("Africa", 2, (24, 120, 60)), ("Americas", 7, (90, 60, 140)), ("World / Space", 4, (40, 120, 130))]; x = 8
    for name, n, c in regs:
        w = 1008 * n / 38; d.rectangle([x, 84, x + w - 2, 102], fill=c); T(d, x + 4, 88, f"{name} {n}", F(SANSB, 10), (255, 255, 255)); x += w
    T(d, 8, 108, "THE DAY IN UTC", F(SANSB, 10), RED); ux = 8
    for t, s in [("02:15", "NATO vows space defence"), ("08:16", "Hanoi blast"), ("10:42", "Saudi strikes Yemen"), ("14:27", "Riyadh tower hit"), ("16:51", "Houthis 60 km from Aden"), ("18:58", "Hormuz ship attack"), ("20:41", "Huawei guilty")]:
        T(d, ux, 122, t, F(SANSB, 10), RED); T(d, ux + 36, 122, s, F(SANS, 10)); ux += 36 + d.textlength(s, font=F(SANS, 10)) + 14
    d.line([8, 138, 1016, 138], fill=(180, 180, 180)); T(d, 8, 144, "THE DAY IN NUMBERS", F(SANSB, 10), RED); nx = 150
    for v, s in [("11", "hurt in Riyadh"), ("9", "killed in Ukraine"), ("50,018", "Dow closes"), ("+8.99%", "Taiex record"), ("25", "killed / missing, Yemen"), ("26", "Cikande fire toll")]:
        T(d, nx, 142, v, F(SERIF, 20), INK); T(d, nx, 164, s, F(SANS, 9), GREY); nx += 146
    d.line([8, 180, 1016, 180], fill=(180, 180, 180))
    heroes = [("1  RIYADH  ·  MIDDLE EAST", "CONFIRMED", (24, 120, 60), "Saudi officials", "Houthi drone hits Riyadh's tallest tower again, 11 hurt", "A Houthi drone hits the PIF tower, Riyadh's tallest, for a second time in a week. At least 11 people are hurt.", scene_riyadh), ("2  SHANGHAI  ·  ASIA", "OFFICIAL", (24, 48, 96), "CCDI", "China probes Shanghai party chief Chen Jining", "Shanghai party chief Chen Jining, 62, is probed for \u201cserious violations\u201d — the 4th Politburo member to fall this year.", scene_shanghai), ("3  NEW YORK  ·  US / TECH", "CONFIRMED", (24, 120, 60), "US federal court", "Huawei guilty on 10 of 12 counts", "A US jury finds Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. Sentencing is set for Sep 2027.", scene_court)]
    for i, (kick, ch, cc, src, hl, dk, fn) in enumerate(heroes):
        hx = 8 + i * 336; d.rectangle([hx, 186, hx + 328, 374], fill=(255, 255, 255), outline=(150, 150, 150)); fn(d, hx + 1, 187, 326, 96); T(d, hx + 8, 287, kick, F(SANSB, 10), RED); cx = chip(d, hx + 8, 300, ch, cc); T(d, cx, 301, f"({src})", F(SANS, 9), GREY); y = headline(d, hx + 8, 314, hl, F(SERIF, 15), 312, 16); deck(d, hx + 8, y + 2, dk, 312, 11, 9)
    return im, d
def cards_map_also(d, im):
    cards = [(4, "ZAPORIZHZHIA · EUROPE / WAR", "REPORTED", (90, 90, 90), "Ukrainian officials", "Russian attacks kill 9 across Ukraine in a day", "Russian attacks kill 9 across Ukraine in a day and wound 81. Kyiv says 96 drones came and 73 were downed.", "drone"), (5, "CAS · AFRICA / SPORT", "OFFICIAL", (24, 48, 96), "CAS", "CAS hands Senegal back the AFCON title", "CAS hands the Africa Cup title back to Senegal after Morocco forfeit 3-0. Senegal win the final 1-0.", "trophy"), (6, "HORMUZ · MIDDLE EAST", "REPORTED", (90, 90, 90), "UKMTO / wires", "IRGC attacks container ship in Hormuz", "The IRGC attacks a container ship in the Strait of Hormuz, cutting its navigation. A no-go area is set near Khasab.", "ship"), (7, "NEW YORK · WORLD / MARKETS", "CONFIRMED", (24, 120, 60), "Market close", "Dow closes above 50,000 for the first time", "The Dow closes above 50,000 for the first time at 50,018. The Taiex jumps a record 8.99% while Nasdaq slides 1.5%.", "chart"), (8, "REDMOND · WORLD / TECH", "REPORTED", (90, 90, 90), "Reuters", "Microsoft declares \u2018Code Red\u2019 after historic outage", "Microsoft declares \u2018Code Red\u2019 after a historic 24-hour Exchange outage. It targets recovery within one hour.", "server"), (9, "ESKISEHIR · EUROPE", "REPORTED", (90, 90, 90), "Turkish officials", "Turkish military helicopter crash kills 5", "A Turkish military AS-532 helicopter crashes in Eskisehir, killing all 5 aboard. The crash is reported at 19:52 UTC.", "heli"), (10, "CARTAGENA · AMERICAS", "REPORTED", (90, 90, 90), "Colombian officials", "Supermarket hostages: 25 held in Cartagena", "Gunmen hold 25 in a Cartagena supermarket and free 5 elderly women. Landings stop for 45 minutes.", "shop"), (11, "ADEN · MIDDLE EAST", "REPORTED", (90, 90, 90), "Wires", "Houthis advance within 60 km of Aden", "Houthi forces advance to within 60 km of Aden in Yemen. The push is reported at 16:51 UTC.", "desert"), (12, "LAHJ · MIDDLE EAST", "REPORTED", (90, 90, 90), "Yemeni officials", "Saudi strikes kill 25, wound 6 in Yemen", "Saudi strikes hit a bus and trucks in Wadi Maabaq, Lahj. 25 are killed, 6 wounded; the toll counts the missing.", "truck"), (13, "JIUQUAN · WORLD / SPACE", "OFFICIAL", (24, 48, 96), "CMSA", "China names first foreign astronaut for Tiangong", "China names the Shenzhou-24 crew, with Muhammad Zeeshan Ali of Pakistan, the first foreign astronaut for Tiangong.", "rocket")]
    for i, (n, kick, ch, cc, src, hl, dk, kind) in enumerate(cards):
        cx = 8 + (i % 5) * 203; cy = 380 + (i // 5) * 126; d.rectangle([cx, cy, cx + 197, cy + 126], fill=(255, 255, 255), outline=(150, 150, 150)); strip_scene(d, cx + 1, cy + 1, 195, 30, kind); T(d, cx + 5, cy + 34, f"{n}  {kick}", F(SANSB, 8), RED); cx2 = chip(d, cx + 5, cy + 46, ch, cc); T(d, cx2, cy + 47, f"({src})", F(SANS, 8), GREY); y = headline(d, cx + 5, cy + 61, hl, F(SERIF, 11), 187, 13); deck(d, cx + 5, y + 1, dk, 187, 11, 9)
    mx0, my0, mw, mh = 8, 638, 1008, 168; d.rectangle([mx0, my0, mx0 + mw, my0 + mh], fill=SEA, outline=(120, 120, 120))
    def P(lon, lat):
        la = max(-15, min(58, lat)); return (mx0 + (lon + 170) / 360 * mw, my0 + 4 + (58 - la) / 73 * (mh - 8))
    for poly in LANDS: d.polygon([P(lo, la) for lo, la in poly], fill=LAND, outline=(120, 130, 100))
    d.rectangle([mx0, my0, mx0 + 215, my0 + 16], fill=SEA); T(d, mx0 + 4, my0 + 3, "THE WORLD  —  13 STORIES PINNED", F(SANSB, 10), NAVY)
    pins = [(1, 24.63, 46.72), (2, 31.23, 121.47), (3, 40.71, -74.01), (4, 47.85, 35.14), (5, 14.69, -17.45), (6, 26.50, 56.50), (7, 40.71, -74.01), (8, 47.67, -122.12), (9, 39.78, 30.52), (10, 10.39, -75.51), (11, 12.79, 45.04), (12, 13.05, 44.88), (13, 39.77, 98.49)]; off = {7: (26, 18), 12: (26, 18)}
    for n, la, lo in pins:
        px, py = P(lo, la)
        if n in off:
            ox, oy = px + off[n][0], py + off[n][1]; d.line([px, py, ox, oy], fill=INK, width=1); px, py = ox, oy
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=(255, 255, 255), width=2); T(d, px, py - 6, str(n), F(SANSB, 9), (255, 255, 255))
    T(d, mx0 + 4, my0 + mh - 16, "Pins 1–13 = stories 1–13.  7 and 12 are offset with leader lines.", F(SANS, 9), GREY)
    also = [("Ankara", "Haftar visits Turkey for the first time"), ("London", "UK sanctions the Houthis and 4 officials"), ("Villavicencio", "Car bomb injures 23 people"), ("Gaza", "Israel kills a Hamas internal security chief"), ("Baghdad", "Iraq orders federal control of Kurdish oilfields"), ("Gaza", "Meningitis epidemic alert as cases hit 272"), ("DR Congo", "Cessna 208 missing as rebels claim a shootdown"), ("Hanoi", "Hot-pot blast kills at least 6 people"), ("Gulf of Finland", "Ukraine hits Russian ship Sparta II"), ("Kuala Lumpur", "Malaysia to return thousands of migrants to Myanmar"), ("Ulleungdo", "South Korea orders shelter as Russian jets enter ADIZ"), ("Dhaka", "Hasina plans to return on 16 December"), ("The Hague", "14 nations endorse the ICJ Myanmar ruling"), ("Jakarta", "Indonesia nominates 2 vice-president candidates"), ("Beijing", "China sentences official Ma to death for spying"), ("Brussels", "NATO vows defence against a space threat"), ("Mexico City", "US drone aided the El Chapo Isidro capture"), ("San Salvador", "Bukele names 3 soldiers killed in Haiti"), ("Ottawa", "Pentagon rebukes Canada as only 41.9% of air fleet ready"), ("Washington", "US adds Megaspeed to the trade blacklist"), ("Kyiv", "Zelensky urges Ukraine-Russia-US-Europe talks soon"), ("Ras Al Khaimah", "UAE bus-truck crash kills 13 people"), ("London", "England records 5,258 heat deaths in summer 2026"), ("Kourou", "Ariane 6 lofts 36 Amazon satellites"), ("Cikande", "Factory-fire toll rises to 26")]
    T(d, 8, 812, "ALSO ON TUESDAY  —  25 MORE STORIES", F(SANSB, 11), RED)
    for i, (city, s) in enumerate(also):
        col, row = i // 9, i % 9; ax = 8 + col * 340; ay = 828 + row * 13; T(d, ax, ay, f"{14 + i}. {city}: {s}.", F(SANS, 9))
    d.rectangle([8, 946, 1016, 1002], outline=RED, width=2); T(d, 14, 950, "DATE CHECK", F(SANSB, 10), RED)
    T(d, 14, 963, "Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.", F(SANS, 9))
    T(d, 14, 975, "LEFT OUT (not 24 Nov): Hormuz mine claims (23 Nov) · Nvidia Huang returns as CEO (23 Nov) · EU 22nd sanctions package (23 Nov) · COP31 ends no deal (22 Nov) · Merkury sinks (22 Nov) · El Chapo Isidro arrested (20 Nov) · Cikande fire starts (21 Nov) · Trump hush-money appeal ruling (23 Nov) · Russia warns Estonia (23 Nov) · ATP Finals (22 Nov) · Las Vegas GP (21 Nov).", F(SANS, 9))
    T(d, 14, 987, "NOT YET: Shenzhou-24 launch (25 Nov 00:18 UTC) · MPR session picks VP (11 Dec) · Huawei sentencing (Sep 2027) · Hasina returns (16 Dec) · COP32 final decision / venue (not set).", F(SANS, 9))
    T(d, 8, 1006, "Sources: dailysummaryof.com · Reuters · AP · UKMTO · CAS · CMSA · CCDI · US federal court.  CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side's claim.  Scenes are drawn illustrations, not photographs.", F(SANS, 8), GREY)
def main():
    im, d = build(); cards_map_also(d, im); out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"), "entry.png"); os.makedirs(os.path.dirname(out), exist_ok=True); im.save(out, optimize=True); print("saved", out, os.path.getsize(out))
if __name__ == "__main__":
    main()
