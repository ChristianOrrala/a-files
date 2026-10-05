# 01. Text reminders the day before

> Spike, for AH-002. Done 2026-09-27. Answer in one line: a text the day before is feasible for the workshop's volume, through any provider with a plain HTTP API, for about the price of one coffee a week.

## Question

Can the workshop send one text message the day before each booked repair,
reliably and cheaply, without storing more customer data than it has today?

## What we did

Two hours with two providers' test accounts (called A and B here): sent ten
test messages each from a throwaway script, read their pricing and their data
terms.

## What we found

- Both delivered all ten messages within a minute.
- At about 40 bookings a week, both cost a few currency units a week.
- Both need only the phone number the booking already has.
- Provider B keeps message content for 30 days; A keeps none.

## Answer and recommendation

Feasible. Recommend provider A for the shorter data retention. Still unsure:
how many customers will reply to the text, which we will not read.

## Sources

- Provider A and B test accounts and pricing pages (names left out of the example)
