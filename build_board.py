#!/usr/bin/env python3
"""Marzia Prince / UGC Fasttrack — wired swipe board.

One pannable canvas. Every funnel step is the real screenshot captured by the
Part A engine (F119), embedded as base64 so the file opens standalone.

The story: this is the closest structural analogue to UGC World in the whole
swipe file. A creator front (Marzia, 25K followers) on top of an agency-operated
funnel (House of Leap). Free live Zoom masterclass, $37 VIP pass sold BEFORE the
event, WhatsApp group as the pre-class nurture channel, replay into a Typeform
application into a Google Meet sales call.

Layout rule: one column per funnel STEP. Parallel variants stack vertically
inside that column so an arrow never crosses a card it is not pointing at.

Run:  python3 build_board.py   ->  board.html
"""
import base64, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DIMS = json.load(open(os.path.join(HERE, "dims.json")))
SHOTS_SRC = os.path.join(HERE, "media", "full")

CARD_W = 330
CHROME = 166
X = {1: 60, 2: 470, 3: 880, 4: 1290, 5: 1700, 6: 2110, 7: 2520, 8: 2930, 9: 3340}

# id -> (asset, col, y, lane, title, url, note)
SHOTS = {
    "reg": ("01_Webinar_registration", 2, 150, "paid", "Registration page",
            "https://masterclass.ugcfasttrack.com/",
            "Countdown timer, localized session time, and a written "
            "<b>“NOT for you if”</b> list sitting next to the “FOR you if” list. "
            "It disqualifies get-rich-quick traffic in the copy, before the form. "
            "Form asks name, email and <b>phone (required)</b> with two "
            "pre-ticked SMS consent boxes."),
    "vip": ("02_Upsell_OTO", 3, 150, "paid", "$37 VIP pass — the OTO",
            "https://masterclass.ugcfasttrack.com/vip-pass",
            "A paid upsell on a FREE masterclass, sold before the event happens. "
            "3m33s Wistia VSL (<code>l1ia31bjo1</code>, named “Vsl draft 3_1”) "
            "over a 5-item stack. Monetises the registration itself."),
    "ty": ("03_Thank-you_page", 4, 150, "paid", "Thank-you (free path)",
           "https://masterclass.ugcfasttrack.com/completed",
           "“90%” progress bar — you are never told you are finished. "
           "1m23s video, then three steps: <b>join the WhatsApp group</b>, "
           "check email, add to calendar."),
    "tyvip": ("04_VIP_thank-you_page", 4, 800, "paid", "Thank-you (VIP path)",
              "https://masterclass.ugcfasttrack.com/vip-completed",
              "Same three steps, different video (1m21s). Bonus delivery is "
              "pushed to email, which forces an inbox open before the class."),
    "preframe": ("07_Pre-frame_breakdown", 5, 150, "paid",
                 "Pre-frame explainer",
                 "https://masterclass.ugcfasttrack.com/breakdown",
                 "A 22,760px-tall teaching page: influencer vs UGC, a 6-step "
                 "workflow, two cited stats, an age/demographic reframe. "
                 "Ends “This page is the what and the why. The masterclass is "
                 "the how.” Served at <b>two</b> slugs — <code>/breakdown</code> "
                 "and <code>/what-is-UGC</code> — byte-identical."),
    "replay": ("05_Replay_page", 7, 150, "ever", "Replay + offer",
               "https://masterclass.ugcfasttrack.com/replay",
               "Carries the full 2h05m recording <b>publicly, with no gate</b> "
               "(Wistia <code>gwc4s7t8fu</code>, named “July 28”). "
               "“Only a few spaces left to work with me &amp; my team directly.”"),
    "callconf": ("09_Calendar_confirmation", 9, 150, "ever", "Call booked",
                 "https://masterclass.ugcfasttrack.com/call-confirmed",
                 "Google Meet with “one of our UGC Fasttrack advisors”. "
                 "Carries a pre-call objection FAQ plus <b>27 Wistia "
                 "testimonials</b> — the heaviest proof page in the funnel."),
}

# id -> (col, y, h, lane, kicker, title, rows[], foot)
DATA = {
    "traffic": (1, 150, 470, "paid", "TRAFFIC", "Meta ads → registration",
                [("Meta Pixel", "1135267478240733"),
                 ("Clarity", "xufintorxl"),
                 ("Also loaded", "Contentsquare, flock.js"),
                 ("Ad-library coverage", "NONE FOUND"),
                 ("Creatives on file", "2 (Foreplay export)")],
                "The pixel and session-recording stack are confirmed off the "
                "live pages. The ad set itself is a GAP — Gethookd has no brand "
                "record for UGC Fasttrack, so creative volume and survival rate "
                "are unmeasured. Do not infer spend from this card."),
    "live": (6, 150, 470, "paid", "THE EVENT · GENUINELY LIVE", "Zoom masterclass",
             [("Platform", "Zoom webinar (not WebinarJam)"),
              ("Webinar ID", "81455479178"),
              ("Next session", "Tue 4 Aug 2026, 8pm ET"),
              ("Recording pulled", "2h 05m 22s · 1920x1200"),
              ("Registration backend", "aEvent 42161280")],
             "Genuinely live, unlike App Publishing and Richard Yu. The Zoom "
             "confirmation is sent by Zoom itself and replies route to "
             "christian@houseofleap.com."),
    "typeform": (8, 150, 470, "ever", "THE GATE", "Typeform application",
                 [("Form", "ugcmasterclass.typeform.com"),
                  ("ID", "Jg7V8Car"),
                  ("Sits on", "the replay page"),
                  ("Price shown", "NEVER, anywhere in the funnel"),
                  ("Questions", "not captured — no_submit")],
                 "The only route from content to a sales call. Nothing in the "
                 "captured funnel states a price — not the pages, not the "
                 "emails, not the replay page."),
    "operator": (1, 2260, 500, "event", "WHO ACTUALLY RUNS THIS",
                 "House of Leap (Denmark)",
                 [("Partner / systems", "Christian Mailind"),
                  ("Partner / content", "Mathias Keimling"),
                  ("Partner / marketing", "Victor Prager"),
                  ("Creative", "Nicolai Balzano"),
                  ("Marzia's following", "~25K")],
                 "Marzia is the face, not the operator. An agency builds and "
                 "runs the funnel across a roster of creator-founders. "
                 "Structurally identical to Will behind Gloria."),
    "whatsapp": (3, 2260, 500, "event", "PRE-CLASS NURTURE", "WhatsApp group",
                 [("Channel", "WhatsApp group invite"),
                  ("Link", "chat.whatsapp.com/JHBIq5CUWpl9ZGJbGJ04cO"),
                  ("Position", "STEP 1 on both thank-you pages"),
                  ("Pitched as", "content “not available anywhere else”"),
                  ("Status", "LIVE — not joined")],
                 "The single most copyable mechanic here. They move registrants "
                 "off email into a group chat they own, then run pre-class "
                 "content in it. UGC World runs this job over SMS (AI-LNS)."),
    "proof": (5, 2260, 500, "event", "PROOF", "The testimonial wall",
              [("Video testimonials", "27 Wistia medias"),
               ("Named on-page", "12"),
               ("Men in the set", "3 (Mike, Kyle, one more)"),
               ("Claimed students", "1,000+"),
               ("Claimed brands / revenue", "600+ · $50M+")],
              "Their proof set is NOT all-female. Ours is. That is a deliberate "
              "difference worth deciding on, not drifting into."),
    "stale": (7, 2260, 500, "event", "MAINTENANCE FAILURE", "The funnel is unmaintained",
              [("Reg page says", "Tue 4 Aug"),
               ("Thank-you pages say", "“lead up to July 21st”"),
               ("Pre-frame page says", "“Tuesday, July 21st”"),
               ("Add-to-Calendar writes", "2026-07-22T00:00Z"),
               ("Founder photo alt text", "“Leo Grundström”")],
              "Not cosmetic. Every registrant who clicks Add to Calendar books "
              "a date that has already passed. A live, ongoing show-rate leak "
              "in a competitor's funnel."),
}


# ---------------------------------------------------------------- routing logic
# Hangs BELOW the clean funnel line. state: "yes" | "no" | "dq" | "unver"
BRANCH = [
    ("b_fork", X[3] + 15, 1520, "yes", "Registration → forced VIP fork",
     "You cannot reach a confirmation page without answering the money question. "
     "<b>“YES — I want the VIP pass for $37”</b> or "
     "<b>“No thanks, keep my free registration.”</b> There is no skip link and no "
     "close button on the choice. The free option is styled as the lesser card, "
     "under a “BEST VALUE” badge on the paid one.",
     "VERIFIED · captured page 02_Upsell_OTO, both CTAs present in the DOM"),
    ("b_deck", X[4] + 15, 1520, "yes", "The slide deck is the VIP bonus",
     "“Every slide from the live masterclass delivered straight to your inbox "
     "<b>when we're done</b>. No scrambling to screenshot mid-session.” "
     "A show-up-<i>and-stay</i> incentive that costs them nothing to deliver and "
     "is only earned by sitting through the pitch. Stacked with a private group "
     "coaching recording and a module from the paid program.",
     "VERIFIED · VIP stack, 5 items, captured verbatim"),
    ("b_cal", X[6] + 15, 1520, "dq", "Add to Calendar → a date in the past",
     "The Google Calendar link on the thank-you pages hardcodes "
     "<code>dates=20260722T000000Z</code> — <b>21 July, 8pm ET</b>. The "
     "registration page sells 4 August. Anyone who does the responsible thing "
     "and saves it to their calendar is booked for a session that happened "
     "thirteen days ago and will not be reminded on the right night.",
     "VERIFIED · raw href read off the captured DOM, three pages affected"),
    ("b_replay", X[7] + 15, 1520, "no", "Did not show → ungated replay",
     "The full two-hour masterclass sits on <code>/replay</code> behind no login, "
     "no token and no email gate — the Wistia media resolves to a direct MP4. "
     "The scarcity line on the same page (“only a few spaces left”) is doing all "
     "the work that a replay expiry would normally do.",
     "VERIFIED · pulled the full 7,522-second file with plain curl"),
    ("b_call", X[8] + 15, 1520, "unver", "Application → advisor call",
     "A Typeform decides who reaches a “UGC Fasttrack advisor” on Google Meet. "
     "The qualification questions, the price, and whether there is a DQ path are "
     "all unknown — the form is flagged <code>no_submit</code> and nothing was "
     "entered.",
     "UNVERIFIED · form definition not read; would need a submit run"),
]


def branch_card(b):
    bid, x, y, state, cond, body, ev = b
    cls = "br " + ("unver" if "UNVERIFIED" in ev else state)
    return (f'<div class="{cls}" style="left:{x}px;top:{y}px">'
            f'<span class="cond">{cond}</span><p>{body}</p>'
            f'<span class="ev">{ev}</span></div>')


A = []
PAID, EVER, EVENT = "#818cf8", "#34d399", "#fb923c"


def b64(step):
    p = os.path.join(SHOTS_SRC, "ugcft_%s.jpg" % step)
    with open(p, "rb") as fh:
        return "data:image/jpeg;base64," + base64.b64encode(fh.read()).decode()


def node_box(nid):
    if nid in SHOTS:
        asset, col, y = SHOTS[nid][0], SHOTS[nid][1], SHOTS[nid][2]
        return X[col], y, CARD_W, DIMS["assets/%s" % asset][1] + CHROME
    col, y, h = DATA[nid][0], DATA[nid][1], DATA[nid][2]
    return X[col], y, CARD_W, h


def right(n):
    x, y, w, h = node_box(n); return (x + w, y + h / 2)


def left(n):
    x, y, w, h = node_box(n); return (x, y + h / 2)


def bottom(n):
    x, y, w, h = node_box(n); return (x + w / 2, y + h)


def top(n):
    x, y, w, h = node_box(n); return (x + w / 2, y)


def h_arrow(a, b, col=PAID, label=None):
    (x1, y1), (x2, y2) = right(a), left(b)
    mx = (x1 + x2) / 2
    A.append(("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
              % (x1 + 6, y1, mx, y1, mx, y2, x2 - 13, y2),
              col, False, label, ((x1 + x2) / 2, min(y1, y2) - 16)))


def v_arrow(a, b, col=EVER, label=None):
    (x1, y1), (x2, y2) = bottom(a), top(b)
    my = (y1 + y2) / 2
    A.append(("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
              % (x1, y1 + 6, x1, my, x2, my, x2, y2 - 13),
              col, False, label, ((x1 + x2) / 2, (y1 + y2) / 2 - 12)))


# ------- the one clean line: ad -> reg -> paid fork -> confirm -> pre-frame -> live
h_arrow("traffic", "reg", PAID, "cold traffic, destination = registration")
h_arrow("reg", "vip", PAID, "form posts to aEvent, THEN the paywall")
h_arrow("vip", "ty", PAID, "declined $37")
h_arrow("vip", "tyvip", PAID, "paid $37")
h_arrow("ty", "preframe", PAID, "emailed + dropped in WhatsApp")
h_arrow("preframe", "live", PAID, "show up Tue 8pm ET")
h_arrow("live", "replay", EVER, "no-shows and re-watchers")
h_arrow("replay", "typeform", EVER, "“apply for the special offer”")
h_arrow("typeform", "callconf", EVER, "qualified → Google Meet")

# the VIP path rejoins the same pre-frame and the same room
(_x1, _y1), (_x2, _y2) = right("tyvip"), left("preframe")
A.append(("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
          % (_x1 + 6, _y1, _x1 + 200, _y1, _x2 - 200, _y2, _x2 - 13, _y2),
          PAID, False, "VIP rejoins the same room", (_x1 + 40, _y1 - 16)))

# ------- the always-on nurture layer
v_arrow("ty", "whatsapp", EVENT, "STEP 1 on both confirmations")
v_arrow("callconf", "proof", EVENT, "27 testimonials load here")
v_arrow("reg", "operator", EVENT, "built and run by the agency, not the face")
v_arrow("preframe", "stale", EVENT, "three pages still say July 21st")


def drop(nid, bx, by, col):
    """A soft dotted line from a funnel card down to its routing-logic card."""
    x, y, w, h = node_box(nid)
    sx, sy = x + w / 2, y + h
    A.append(("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
              % (sx, sy + 4, sx, (sy + by) / 2, bx + 150, (sy + by) / 2, bx + 150, by - 8),
              col, True, None, (0, 0)))


drop("vip", X[3] + 15, 1520, "#be123c")
drop("tyvip", X[4] + 15, 1520, EVER)
drop("live", X[6] + 15, 1520, "#be123c")
drop("replay", X[7] + 15, 1520, "#f59e0b")
drop("typeform", X[8] + 15, 1520, EVER)

BANDS = [
    (125, "1 · FREE LIVE MASTERCLASS — REGISTRATION THROUGH TO THE SALES CALL", PAID),
    (2235, "2 · THE LAYER UNDERNEATH — OPERATOR, NURTURE CHANNEL, PROOF, DECAY", EVENT),
]

LANE_TAG = {"paid": "REGISTRATION", "ever": "POST-CLASS / SALES",
            "event": "ALWAYS ON"}


def shot_card(nid):
    asset, col, y, lane, title, url, note = SHOTS[nid]
    w, h = DIMS["assets/%s" % asset]
    x, yy, cw, ch = node_box(nid)
    return (f'<a class="n {lane}" href="{url}" target="_blank" rel="noopener" '
            f'style="left:{x}px;top:{yy}px;width:{cw}px">'
            f'<div class="nh"><span class="tag">{LANE_TAG[lane]}</span>'
            f'<span class="go">open ↗</span></div>'
            f'<div class="nt">{title}</div><div class="nu">{url}</div>'
            f'<div class="ni" style="height:{h}px"><img src="{b64(asset)}" alt=""></div>'
            f'<div class="nn">{note}</div></a>')


def data_card(nid):
    col, y, h, lane, kick, title, rows, foot = DATA[nid]
    x, yy, cw, ch = node_box(nid)
    rs = "".join(f'<div class="dr"><span>{k}</span><b>{v}</b></div>' for k, v in rows)
    return (f'<div class="n {lane}" style="left:{x}px;top:{yy}px;width:{cw}px;'
            f'height:{h}px">'
            f'<div class="nh"><span class="tag">{kick}</span></div>'
            f'<div class="nt">{title}</div><div class="drs">{rs}</div>'
            f'<div class="nn">{foot}</div></div>')


W, H = 3830, 2900
paths = "".join(
    (f'<path d="{d}" stroke="{c}" stroke-width="1.6" fill="none" stroke-dasharray="5 5" '
     f'opacity=".65"/>' if dashed else
     f'<path d="{d}" stroke="{c}" stroke-width="2.5" fill="none" marker-end="url(#a{c[1:]})"/>')
    + (f'<text class="alabel" x="{lx:.0f}" y="{ly:.0f}">{lab}</text>' if lab else "")
    for d, c, dashed, lab, (lx, ly) in A)
markers = "".join(
    f'<marker id="a{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
    f'markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>'
    for c in (PAID, EVER, EVENT))
bands = "".join(
    f'<div class="band" style="top:{y - 52}px"><span style="color:{c}">{t}</span></div>'
    for y, t, c in BANDS)
nodes = ("".join(shot_card(n) for n in SHOTS)
         + "".join(data_card(n) for n in DATA)
         + "".join(branch_card(b) for b in BRANCH))

tpl = open(os.path.join(HERE, "board_template.html")).read()
out = (tpl.replace("{{W}}", str(W)).replace("{{H}}", str(H))
          .replace("{{NODES}}", nodes).replace("{{BANDS}}", bands)
          .replace("{{MARKERS}}", markers).replace("{{PATHS}}", paths))
open(os.path.join(HERE, "board.html"), "w").write(out)
print(f"board.html  {len(out)/1024:.0f} KB  ({len(SHOTS)} screenshots, "
      f"{len(DATA)} data cards, {len(A)} wires)")
