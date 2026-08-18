#!/usr/bin/env python3
"""Build the Marzia Prince / UGC Fasttrack swipe site.

Run: python3 build_site.py
"""
import sys, os, glob
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/UGC_FASTTRACK_Swipe")
tx = sorted(glob.glob(os.path.join(PKG, "Transcript/transcript.md")))

CONFIG = {
    "SITE": "UGC Fasttrack — Marzia Prince",
    "CREATOR": "Marzia Prince",
    "ADS_KEY": None,
    "FUNNEL_IDS": ["F119"],
    "CAPTURED": "3 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/UGC_FASTTRACK_Swipe",
    "BLURB": "The closest competitor to UGC World in the whole swipe file &mdash; same offer, "
             "same customer, opposite end of the journey. A free live Zoom masterclass with a "
             "<b>$37 VIP pass sold before the event</b>, a WhatsApp group as the pre-class "
             "nurture channel, and an ungated two-hour replay into a Typeform application. "
             "Marzia is the face; a Danish agency called <b>House of Leap</b> runs the funnel.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("pages.html", "Funnel pages"),
        ("slides.html", "Slides"),
        ("transcripts.html", "Transcript"),
        ("decks.html", "Decks"),
        ("videos.html", "Video library"),
        ("copybank.html", "Copy bank"),
    ],

    "STATS": [
        ("VIP price", "$37"),
        ("Program price", "never stated"),
        ("Masterclass", "2h 05m 22s"),
        ("Slides extracted", "437"),
        ("Transcript", "26,074 words"),
        ("Platform", "Zoom (live)"),
        ("Funnel steps", "11"),
        ("Captured", "3 Aug 2026"),
    ],

    "OFFER": [
        ("Product", "UGC Fasttrack &mdash; mentorship for existing UGC creators"),
        ("Face", "Marzia Prince (~25K followers)"),
        ("Actual operator", "<b>House of Leap</b> (Denmark) &mdash; Christian Mailind, "
                            "Mathias Keimling, Victor Prager, Nicolai Balzano"),
        ("Big idea", "&ldquo;How to Build a $10K/Month UGC Business Without a Following&rdquo;"),
        ("Hook", "&ldquo;The 5-Step System That Took Me From $200 One-Off Deals to $15K "
                 "Months With UGC&rdquo;"),
        ("ICP", "creators <b>already earning $1K&ndash;$5K/month</b> and stuck under $10K"),
        ("Mechanism", "The UGC Fasttrack System &mdash; 5 steps on 2 pillars "
                      "(<i>The Skill</i> and <i>The Acquisition</i>)"),
        ("Core reframe", "3&ndash;4 <b>retainer</b> clients beat a pile of one-off projects"),
        ("Entry", "Free. Name, email and <b>phone (required)</b>, two pre-ticked SMS consents"),
        ("Front-end", "<b>$37 VIP pass</b> on a free masterclass, sold before the event"),
        ("Deliverable", "45 video modules, 10-step roadmap, community, 4 weekly group "
                        "coaching calls, 5 named bonuses"),
        ("Price", "<b>never stated anywhere</b> &mdash; not on a page, not in an email, "
                  "not in two hours of masterclass. Revealed only on the call."),
        ("Guarantee", "None. She says so out loud: &ldquo;I don't want to sell on guarantees "
                      "and fancy promises.&rdquo;"),
        ("Backend", "Typeform &rarr; Google Meet with a &ldquo;UGC Fasttrack Advisor&rdquo;"),
    ],

    "FINDINGS": [
        ("Marzia is the face, not the operator",
         "The Zoom confirmation replies to <code>christian@houseofleap.com</code>. House of Leap "
         "is a four-partner Danish growth agency that builds and runs funnels for creator-founders "
         "&mdash; Marzia is listed on their site alongside Loop Fitness and three fitness coaches. "
         "<b>This is structurally the same business Will runs behind Gloria.</b> The competitor is "
         "not a solo creator who got lucky; it is an agency with a roster."),
        ("They sell the ceiling, we sell the start",
         "Their &ldquo;FOR you if&rdquo; list names the customer precisely: <i>&ldquo;You're "
         "already making $1,000 to $5,000 a month, but you're feeling stuck.&rdquo;</i> That is a "
         "sharper, more solvent segment than the beginner. A creator already earning $3K has "
         "proven they can do the work and has cash flow to pay from."),
        ("The price is never stated &mdash; on purpose",
         "Eleven captured pages, three emails and 26,074 transcribed words contain no number. "
         "An attendee named Michelle asks live, <i>&ldquo;do you have to have the call tonight to "
         "lock in the price and bonuses?&rdquo;</i> and Marzia answers about honouring bonuses "
         "without ever naming a figure. Instead she anchors: <i>&ldquo;This is not a cheap $47 "
         "ebook. It's not just a $500 course.&rdquo;</i> and states plainly "
         "<i>&ldquo;I'm NOT going to drop a checkout link.&rdquo;</i>"),
        ("The slide deck is the show-up-and-stay bribe",
         "The VIP stack promises &ldquo;every slide from the live masterclass delivered straight "
         "to your inbox <b>when we're done</b>. No scrambling to screenshot mid-session.&rdquo; "
         "It costs nothing to deliver, it can only be earned by sitting through the pitch, and it "
         "is sold for $37 <i>before</i> the event."),
        ("WhatsApp, not email, is the pre-class channel",
         "<b>Step 1</b> on both thank-you pages is joining a WhatsApp group, pitched as content "
         "&ldquo;not available anywhere else&rdquo;. They pull registrants off email into a group "
         "chat they control. UGC World does this job over SMS (AI-LNS) &mdash; a group is a "
         "different animal, because registrants see each other's enthusiasm."),
        ("She pre-empts the pitch objection, twice",
         "A slide reads: <i>&ldquo;at the end they hit you with a pitch and you realize the whole "
         "thing was just a sales presentation disguised as a class.&rdquo;</i> She names the "
         "audience's suspicion out loud, early, then again later &mdash; then pitches anyway. "
         "Disarming the objection before it forms."),
        ("A commitment loop bookends the class",
         "She asks &ldquo;on a scale of 1 to 10, how confident are you that you know how to earn "
         "consistent $10K months?&rdquo; and makes them type a number in chat. At the close she "
         "asks the <b>same question again</b>. The delta is the sale."),
        ("Ungated two-hour replay",
         "The full masterclass sits on <code>/replay</code> behind no login, no token and no "
         "email gate. The Wistia media resolves to a direct MP4 &mdash; that is how this capture "
         "was made with plain <code>curl</code>. Scarcity copy does the work an expiry usually does."),
        ("The funnel is unmaintained, and it costs them show rate",
         "The registration page sells <b>Tue 4 Aug</b>. Both thank-you pages say &ldquo;in the "
         "lead up to <b>July 21st</b>&rdquo;. The pre-frame page says &ldquo;Tuesday, <b>July "
         "21st</b>&rdquo;. And the Add-to-Calendar link hardcodes "
         "<code>dates=20260722T000000Z</code>. Every registrant who saves it to their calendar "
         "books a date that has already passed. The founder photo's alt text still reads "
         "&ldquo;Leo Grundstr&ouml;m&rdquo; from whichever funnel this template came from."),
        ("Two slugs, one page",
         "<code>/breakdown</code> and <code>/what-is-UGC</code> serve byte-identical content &mdash; "
         "a 22,760px-tall teaching page. Same asset, two entry points, presumably for two "
         "different traffic sources."),
        ("Their proof set is not all-female",
         "27 Wistia testimonials on the call-confirmation page; of the 12 named on-page, three "
         "are men. Their age angle is explicit too: <i>&ldquo;There are almost none over 40 or 50, "
         "and the brands selling to that customer are desperate for someone who looks like "
         "them.&rdquo;</i> Ours is a deliberately narrower set. Worth deciding, not drifting into."),
        ("The insecurity reframe is the emotional core",
         "She runs slides listing HAIRLOSS / ACNE / WEIGHT GAIN / WRINKLES over her own photos, "
         "then: <i>&ldquo;Flaws and insecurities that you think are working against you, are the "
         "things that make you authentic. Authenticity is what sells.&rdquo;</i> She converts the "
         "reason a woman thinks she can't do this into the reason she can."),
        ("Night two is buyers-only",
         "&ldquo;Tomorrow, I go into the deep dive of how to prepare for Q4&hellip; and that call "
         "is only available in the fast track.&rdquo; A second session gated behind purchase, "
         "announced live, on the biggest-seasonality argument of the year."),
        ("No ad-library coverage",
         "<span class=\"tag warn\">GAP</span> Gethookd has no brand record for UGC Fasttrack, so "
         "creative volume, spend and survival rate are unmeasured. The Meta pixel "
         "(<code>1135267478240733</code>), Clarity (<code>xufintorxl</code>) and Contentsquare "
         "are all confirmed on the live pages, but nothing here supports a claim about their "
         "traffic."),
    ],

    "FUNNEL": [
        ("Registration", "masterclass.ugcfasttrack.com/",
         "Countdown, localized session time, and a written &ldquo;NOT for you if&rdquo; "
         "disqualifier list. Form posts to <b>aEvent</b> account 42161280, Zoom webinar "
         "<code>81455479178</code>."),
        ("VIP pass &mdash; $37", "masterclass.ugcfasttrack.com/vip-pass",
         "Forced fork. 3m33s Wistia VSL over a 5-item stack. No skip link."),
        ("Thank-you (free)", "masterclass.ugcfasttrack.com/completed",
         "&ldquo;90%&rdquo; progress bar. Step 1 is the WhatsApp group."),
        ("Thank-you (VIP)", "masterclass.ugcfasttrack.com/vip-completed",
         "Same three steps, bonus delivery pushed to email."),
        ("Pre-frame explainer", "masterclass.ugcfasttrack.com/breakdown",
         "Also served at <code>/what-is-UGC</code>. Influencer-vs-UGC, a 6-step workflow, "
         "cited stats, and the age reframe."),
        ("Live room", "Zoom, Tue 8pm ET",
         '<span class="tag good">genuinely live</span> — not WebinarJam, not fake-live'),
        ("Replay", "masterclass.ugcfasttrack.com/replay",
         "Full 2h05m recording, <b>ungated</b>. Typeform loads on the same page."),
        ("Application", "ugcmasterclass.typeform.com/to/Jg7V8Car",
         '<span class="tag warn">not submitted</span> — questions and DQ path unknown'),
        ("Call booked", "masterclass.ugcfasttrack.com/call-confirmed",
         "Google Meet with a &ldquo;UGC Fasttrack Advisor&rdquo;. Pre-call objection FAQ plus "
         "27 video testimonials."),
    ],

    "TRANSCRIPT_GROUPS": [("Masterclass — 28 July 2026", tx)],

    "SLIDE_PAGES": [
        ("Masterclass slides", "slides.html", "Screenshots", "web_",
         "Every materially different frame from the two-hour masterclass, after three passes "
         "of talking-head filtering (281 webcam frames removed, 437 real slides kept)."),
    ],

    "DECKS": [
        ("Marzia Prince — UGC Fasttrack Masterclass (28 Jul 2026)", 437,
         "https://docs.google.com/presentation/d/1AU53rOGBg06zMhCsRAe04WNyvatJDX7R4vp6TnwdEDk/edit"),
    ],

    "VIDEOS": [
        ("UGCFastTrack_MASTERCLASS_2026-07-28.mp4", 7522, "815 MB",
         "The full masterclass. Pulled ungated from the replay page (Wistia "
         "<code>gwc4s7t8fu</code>, named &ldquo;July 28&rdquo;)."),
        ("VIPpass_VSL_3m33s.mp4", 213, "282 MB",
         "The $37 VIP pitch. Wistia <code>l1ia31bjo1</code>, named &ldquo;Vsl draft 3_1&rdquo;."),
        ("ThankYou_video_1m23s.mp4", 83, "52 MB",
         "Free-path confirmation video. Drives the WhatsApp join."),
        ("ThankYouVIP_video_1m21s.mp4", 81, "38 MB",
         "VIP-path confirmation video."),
    ],

    "EMAIL_NOTE": "Only the Zoom-sent confirmation has landed so far &mdash; registration was "
                  "1 Aug and the session is 4 Aug, so the run-up sequence is still arriving. "
                  "Note the reply-to: <code>christian@houseofleap.com</code>.",

    "ANALYSIS": """
<div class="note"><b>The one-line read.</b> This is not a solo creator competing with us. It is
an agency-operated funnel with a creator front, aimed one rung up the ladder from our customer
&mdash; at the creator who already earns $1K&ndash;$5K a month and cannot break $10K. They sell
the ceiling. We sell the start.</div>

<h2 class="sec">How the two hours are built</h2>
<div class="tablewrap"><table>
<tr><th>Time</th><th>Beat</th><th>What she is doing</th></tr>
<tr><td>00:00</td><td>Commitment</td><td>&ldquo;Drop a YES in the chat&rdquo;, then
&ldquo;on a scale of 1 to 10, type your number&rdquo;</td></tr>
<tr><td>~00:07</td><td>Pre-empt</td><td>Names the &ldquo;sales presentation disguised as a
class&rdquo; suspicion out loud, and promises not to gatekeep</td></tr>
<tr><td>~00:15</td><td>Origin</td><td>2017 fitness coach &rarr; hamster wheel of one-off deals
&rarr; income swinging between $1,500 and $5,000</td></tr>
<tr><td>~00:29</td><td>Mechanism</td><td>The 5-step Fasttrack System on two pillars: The Skill
and The Acquisition. Order matters and you cannot skip a step</td></tr>
<tr><td>~01:00</td><td>Proof</td><td>Named students &mdash; Angela, Jillian, Velma, Leisha,
Kelly, Jennifer. Leisha a nurse of 30 years; Kelly's husband had lost his job</td></tr>
<tr><td>~01:10</td><td>Reframe</td><td>HAIRLOSS / ACNE / WEIGHT GAIN / WRINKLES &rarr;
&ldquo;authenticity is what sells&rdquo;</td></tr>
<tr><td>~01:20</td><td>Offer</td><td>45 modules, 10-step roadmap, weekly coaching, community,
5 bonuses. <b>No price. No checkout link.</b></td></tr>
<tr><td>~01:25</td><td>Re-ask</td><td>The 1&ndash;10 confidence question again &mdash; the delta
is the sale</td></tr>
<tr><td>01:30+</td><td>Live Q&amp;A</td><td>~35 minutes answering by name, with her team working
the chat to fix booking problems in real time</td></tr>
</table></div>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Sell the VIP pass before the event</h3><p>$37 on a free masterclass, with
the slide deck as the headline bonus &mdash; delivered only when the session ends. It monetises
registration and buys stay-rate at zero marginal cost. We currently monetise nothing between
registration and the room.</p></div>
<div class="card"><h3>Put the disqualifier in the copy</h3><p>A written &ldquo;NOT for you
if&rdquo; list beside the &ldquo;FOR you if&rdquo; list, on the registration page. It filters
get-rich-quick traffic before the form rather than after the setter has spent an hour on it.</p></div>
<div class="card"><h3>Bookend with a scored question</h3><p>Same 1&ndash;10 confidence question at
the open and the close. The prospect measures their own movement and types it publicly. Cheap,
and it manufactures the &ldquo;something changed&rdquo; feeling the close depends on.</p></div>
<div class="card"><h3>Name the suspicion first</h3><p>&ldquo;You've probably attended
masterclasses before&hellip; at the end they hit you with a pitch.&rdquo; Saying it before the
audience thinks it converts a defence into rapport.</p></div>
<div class="card"><h3>A group chat, not a broadcast list</h3><p>WhatsApp group as Step 1 on the
confirmation page. Registrants see each other's momentum, which a one-to-one SMS thread cannot
manufacture. Worth testing against AI-LNS rather than replacing it.</p></div>
<div class="card"><h3>Insecurity as the qualification</h3><p>She converts the exact reason a
woman believes she cannot do this &mdash; her age, her skin, her weight &mdash; into the reason
brands will pay her. That is a stronger emotional move than any income claim on the page.</p></div>
</div>

<h2 class="sec">Where they are weak</h2>
<div class="grid g2">
<div class="card"><h3>The calendar link is broken</h3><p>Add-to-Calendar writes 22 July 2026 on a
funnel selling 4 August. Three pages still reference July 21st. Anyone diligent enough to save
the event is the person most likely to attend, and they are being sent to a dead date.</p></div>
<div class="card"><h3>The replay is a free download</h3><p>Two hours of their best sales asset,
ungated, resolving to a direct MP4. It cost nothing to take.</p></div>
<div class="card"><h3>The funnel is bought, not built</h3><p>Leftover alt text from another
operator's funnel, duplicate slugs, stale dates. Whatever House of Leap is good at, maintaining
this one is not it.</p></div>
<div class="card"><h3>No guarantee at all</h3><p>She turns it into a virtue &mdash; &ldquo;I don't
want to sell on guarantees and fancy promises&rdquo; &mdash; but it is still a missing risk
reversal against an unstated price.</p></div>
</div>

<h2 class="sec">Open questions</h2>
<p>The Typeform (<code>Jg7V8Car</code>) was not submitted, so the qualification questions, the DQ
path and the price are unobserved. There is no ad-library coverage of this brand, so nothing here
supports any claim about their traffic or spend. The WhatsApp group is live and was
<b>not</b> joined &mdash; doing so would expose a real personal number, so the pre-class content
inside it is unseen.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
