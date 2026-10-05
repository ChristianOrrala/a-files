# ATLAS — Repair Desk

> The architecture map: each part of the repository, what it does, which files it works through, what it depends on and what checks it. A map, not a full file index.

## Map

| Part | What it does | Works through | Depends on | Checked by |
|---|---|---|---|---|
| Booking | Free slots, bookings, cancellations, work orders | `src/booking.py` | Storage | `tests/test_booking.py` |
| Notifications | Messages to customers | `src/notify.py` | Booking | `tests/test_booking.py` |
| Web | The customer's pages and the workshop's list | `src/app.py`, `web/templates/` | Booking | Read by hand |
| Tracking | The rules and the A-files | `AGENTS.md`, `ACTIVE.md`, `ABILITIES.md`, `AHEAD.md`, `ATLAS.md` | — | check_tracking.py, from the method package |

## Flow

```text
browser ─► Web (src/app.py) ─► Booking (src/booking.py) ─► storage
                                   └─► Notifications (src/notify.py)
```

Below: Parts in detail, How to maintain this file.

<!-- hot zone ends -->

## Parts in detail

### Booking

Every time rule uses the workshop's time zone; the conversion lives in three
functions today (ACTIVE, Debt). A day is full at 8 repairs.

## How to maintain this file

- A row per part, never file by file; every path in backticks must exist.
- Update it in the same commit that adds, moves, renames or removes a part.
