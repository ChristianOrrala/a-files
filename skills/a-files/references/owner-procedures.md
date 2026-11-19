# Two procedures the owner starts

Both change files the owner reads to decide what happens next, so neither is
run by a session on its own, and nothing moves before he has ruled on the
whole list. The rules behind them are in the method guide, sections 2, 5 and 6.

## Sort a full AHEAD

For an `AHEAD.md` that filled up with items the owner never chose.

1. The owner starts it. No session starts it on its own.
2. Read every open item and propose one of four for each: **keep**; **join**
   with named others into one item; **do now** with the other small ones;
   **remove**. Show the whole list at once, grouped by proposal, each line
   with the identifier, the title and one reason.
3. The owner rules on the list. He may change any line. Nothing moves before
   that.
4. One commit applies it. A kept item gains its **Entered** line with the date
   of the sort. Joined items become one: the item that stays is rewritten to
   hold them, and the others are dropped with "joined into AH-0xx". A removed
   item's row and entry go, and History names it in one line, `Removed on the
   owner's word:` with the identifiers, the date and his words; its number
   stays used. Items to do now become the current work in `ACTIVE.md`, in a
   work section when they are several.

## Review AGENTS.md

For an `AGENTS.md` that exists: one adopted earlier, or one that grew.

1. The owner starts it. No session starts it on its own.
2. Read the file and propose, passage by passage, one of three, each with its
   evidence: **keep**; **move** to the file that owns the fact, leaving that
   file's name; **drop**. A date or a story on a rule is proposed for its
   decision record, with the rule and its reason left in place. Apply three
   questions, and show the whole list at once:
   - What could an agent get wrong before it finds the fuller source? Keep the
     shortest wording that still carries the trigger, the exception and the
     reason.
   - Which file owns this fact? If it changes with the work, it lives there,
     and `AGENTS.md` names the file.
   - What is the evidence for dropping it? An obsolete claim, a conflict, an
     exact copy. Check that the instruction can still be reached when it is
     needed.

   A file that is already right passes with no edits.
3. A section another tool writes and updates, such as a specification
   method's, is not edited. Say what you would propose to that tool's owner.
4. Offer to take out the `<!-- hot zone ends -->` line and the `Below:` line
   only when every reader installed in the repository accepts the file without
   them: `python3 tools/check_tracking.py --version` for the check, and the
   version constant of a specification method's scripts where they are
   installed. The check reads both forms from a-files 2.2.0, and upspec's
   scripts from upspec 2.1.0; another method's changelog names its own
   release. Otherwise say which one is behind, and leave the marker.
5. The owner rules on the list. He may change any line.
6. One commit applies it. A rule that changes follows the repository's own way
   of recording decisions.
