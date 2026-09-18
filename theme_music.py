# theme_music.py
#
# Importable module. Exposes play_theme_song() as an async coroutine
# so it can be run concurrently with another program using pybricks.tools.multitask()

intro = ["C2/8", "R/8", "R/4", "R/4", "R/4"]
riff_a = ["C2/8", "C2/8", "Eb2/8", "C2/8", "F2/8", "C2/8", "G2/8", "C2/8"]
riff_b = ["C2/8", "C2/8", "Eb2/8", "C2/8", "F2/8", "F2/8", "Ab2/8", "G2/8"]
fill = ["C3/16", "C3/16", "C3/16", "C3/16", "D3/16", "D3/16", "D3/16", "D3/16", "Eb3/16", "Eb3/16", "Eb3/16", "Eb3/16", "F3/16", "F3/16", "G3/16", "G3/16"]

def _build_notes():
    notes = []
    notes += intro * 4      # 4-bar intro
    notes += riff_a * 4     # 4-bar main groove
    notes += fill           # 1-bar buildup fill
    notes += riff_b * 4     # 4-bar drop (higher-tension riff)
    notes += fill * 4       # another buildup fill
    notes += riff_a * 8     # 8-bar extended groove
    notes += ["C2/1"]       # final low hit to close out
    return notes


async def play_theme_song(hub, tempo=170, loop=False):
    """
    Plays the theme song on hub.speaker.

        This is a coroutine - it must be awaited, and is meant to be run
        inside pybricks.tools.multitask() alongside another task so the
        music plays in the background while that other task runs.

        Parameters:
            hub   -- a hub object with a .speaker, e.g. PrimeHub()
            tempo -- beats per minute (default 170)
            loop  -- if True, repeats the track forever. Use this with
                    multitask(..., race=True) (see main.py) so the music
                    keeps going until your other task finishes, at which
                    point multitask() cancels the still-running music task.
    """
    notes = _build_notes()
    if loop:
        while True:
            await hub.speaker.play_notes(notes, tempo=tempo)
    else:
        await hub.speaker.play_notes(notes, tempo=tempo)