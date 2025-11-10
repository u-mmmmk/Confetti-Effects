from aqt import mw, gui_hooks
from aqt.qt import QAction, qconnect
from datetime import datetime, date, timedelta

from .config import CONFIG
from .settings import open_settings

def graduated_confetti(rev):
    # Card is graduated when it wont be seen again before test date
    js = """
    var script = document.createElement('script');
    script.src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.4/dist/confetti.browser.min.js"
    script.onload = function() {
    confetti({particleCount:150, spread:360, startVelocity:30, ticks:150});
    };
    document.body.appendChild(script);
    """
    rev.web.eval(js)
    
def matured_confetti(rev):
    js = """
    var script = document.createElement('script');
    script.src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.4/dist/confetti.browser.min.js"
    script.onload = function() {
    confetti({particleCount:30, startVelocity:35, ticks:150});
    };
    document.body.appendChild(script);
    """
    rev.web.eval(js)

def confetti(rev, card, ease):
    test_date = datetime.date(datetime.strptime(CONFIG["Test_Date"], "%m-%d-%Y"))
   
    if not CONFIG["Confetti"]:
        return
    elif ease == 1: #some weird edge cases where 1 sets the ivl to a day
        return

    if date.today() + timedelta(days=card.ivl) > test_date:
        graduated_confetti(rev)
    if CONFIG["Mature_Cards"] and card.ivl >= 21:
        matured_confetti(rev)

# initialize test date
if not CONFIG["Test_Date"]:
    default_date = date.today() + timedelta(30)
    CONFIG["Test_Date"] = default_date.strftime("%m-%d-%Y")

# menu item for settings
action = QAction("Confetti Effects", mw)
qconnect(action.triggered, open_settings)
mw.form.menuTools.addAction(action)

# doing the confetti
gui_hooks.reviewer_did_answer_card.append(confetti)
