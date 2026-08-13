# Sourcing Shortlist — Buying CE Python Units This Week

**Actionable buying research for the launch batch.** Companion to
[`../SOURCING.md`](../SOURCING.md), which has the strategic channel analysis. This document is the
tactical layer: exact queries, exact walk-away prices, and the verification tests to run before money
changes hands.

Research date: **2026-08-12**, with additions on **2026-08-13**. Prices re-verify weekly in August.

> ## 🔴 If you are reading this on Aug 13, go to §7 first
>
> **[§7 is a same-day, in-person playbook for buying one unit today](#7-same-day-local-playbook--buying-the-gate-unit-in-person-today-new-2026-08-13)** —
> the hardware-gate unit. Added 2026-08-13 for the owner's decision to gate **before** the online orders
> go out rather than on the first shipment to arrive.
>
> It covers **which local channels can actually produce a unit today**, the
> **[point-of-sale variant test](#73-the-point-of-sale-variant-test--the-whole-reason-to-buy-locally)**
> that proves a unit is genuinely Python **before you pay**, what to pay in cash versus the online bands
> in §3, what to bring, and the five walk-aways. **§6.2 still applies — §7 is what changes when you are
> standing in front of the thing.**

**Labelling convention, matching the rest of `business/`:** **[RESEARCHED]** = a figure with a
citable source, given inline. **[ESTIMATE]** = modelling, not a researched figure.
**[DERIVED]** = computed from the baselines in [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) /
[`../SOURCING.md`](../SOURCING.md) rather than from a fresh comp.

---

## 0. ⚠️ READ FIRST — what I could not retrieve, and what that means for this document

**I could not obtain live eBay sold comps or live eBay active listings.** This is the single biggest
gap in this document and you need to know it before you use any number in it.

| Attempted | Result |
|---|---|
| `https://www.ebay.com/sch/i.html?...&LH_Sold=1&LH_Complete=1` (several keyword variants) | **HTTP 403 Forbidden** |
| `https://www.ebay.com/sch/i.html?_nkw=...&_sop=15` (active, price+shipping ascending) | **HTTP 403 Forbidden** |
| `https://www.ebay.com/itm/395431665951`, `https://www.ebay.com/itm/395431720336` | **HTTP 403 Forbidden** |
| `https://www.ebay.com/p/19048297204` (catalogue page) | **HTTP 403 Forbidden** |
| `https://www.ebay.com/b/...171558/bn_113651764` (browse node) | **HTTP 403 Forbidden** |
| `https://www.ebay.com.au/itm/...`, `https://www.ebay.ca/itm/...` (mirrors) | **Timed out** |
| `https://www.watchcount.com/sold/ti-84-plus-ce-python/0/1` | **Bot-gate** ("Validating request…") |
| `https://www.walmart.com/search?q=pre-owned+TI-84+Plus+CE+Python` | **Bot-gate** ("Robot or human?") |

eBay serves 403 to automated fetches across every surface — search, item, catalogue, and browse
node — and the third-party sold-comp aggregators are bot-gated too. **This is not fixable from here,
and I stopped retrying rather than burn more time or start guessing.**

### What follows from that

1. **There is not a single fabricated listing or invented sold price in this document.** Every price
   below is either **[RESEARCHED]** with a live URL from a source that *was* reachable (Walmart
   product pages via search index, a US dealer, Amazon, Cemetech, Wikipedia), or explicitly
   **[DERIVED]** from the existing repo baselines, or **[ESTIMATE]**. Nothing is dressed up as a comp
   that isn't one.
2. **§2 gives you a 15-minute manual comp routine** with the exact URLs to paste into a browser. Run
   it before your first purchase. A human browser session is not blocked, and **you will get better
   data in 15 minutes than any amount of automated retrying would produce** — sold comps in this
   category go stale within days anyway, so this was always going to be a task you repeat.
3. **The price ranges in §3 are inherited from [`../SOURCING.md`](../SOURCING.md) §5 and
   [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §7, not from fresh comps.** They are labelled
   **[DERIVED]** wherever that's the case. They are internally consistent with the rest of `business/`
   and with the retail anchors I *could* verify today — but they are not observed transactions.
4. **The genuinely new material in this document is the verification research, not the pricing.**
   §1.4, §1.5 and §3.3 contain three findings that materially improved on the existing docs, all
   independently sourced: an exact on-device test string that defeats faked Python units, a positive
   date-code filter that is stronger than the existing doc allowed, and evidence that the "buy broken
   units cheap" tier does not exist for this variant. **All three were adopted into
   [`../SOURCING.md`](../SOURCING.md) on 2026-08-13** — see §9 for how each was resolved.

> **TODO — the one thing this document is missing.** Run §2's manual comp routine and paste the
> results into §3 as a `[RESEARCHED 2026-08-__]` table: median sold price by condition tier, sample
> size, and 5–10 live listing URLs with what you'd pay for each. That converts §3 from derived to
> observed and is the last step before you should spend more than ~$200. Everything else in this
> folder is usable as-is.

---

## 1. The variant problem — how to actually isolate CE Python units

This is the hard part and it is worth more than any price table. Get it wrong and you have bought a
calculator that can never run the product.

### 1.1 The search keys, ranked

| Key | Value | Reliability | Notes |
|---|---|---|---|
| **eBay catalogue ePID** | **`19048297204`** | **Best available** | eBay's own catalogue entry for "Texas Instruments TI-84 Plus CE Python Color Graphing Calculator". **[RESEARCHED]** (<https://www.ebay.co.uk/p/19048297204>, accessed 2026-08-12 — the US equivalent is `ebay.com/p/19048297204`) |
| **UPC / GTIN** | **`0033317209101`** | Good, contaminated | Paste into eBay search directly. See the trap below |
| **MPN** | `TI84PLUSCEPYTHON` | Good when present | eBay's catalogue MPN for the ePID above |
| **Part number** | `84CEPY/...` | High when present | Only `84CEPY/` proves Python, and only positively |
| **Keyword** | `ti-84 plus ce python` | Mediocre | High recall, poor precision |

> ### ⚠️ Two traps in that table, and they matter
>
> **1. eBay's own `Model` aspect does NOT distinguish the variant.** The catalogue entry for ePID
> `19048297204` — the *Python* product — lists its `Model` field as **"TI-84 PLUS CE"**.
> **[RESEARCHED]** So filtering eBay's Model aspect to "TI-84 Plus CE" returns both variants mixed,
> and there is no Model value that isolates Python. **Do not rely on any eBay aspect filter for the
> variant.** This is the root cause of the contamination you will see in search results.
>
> **2. The UPC is shared across colours *and* is cross-listed against a plain-CE part number.**
> `033317209101` appears on `84CEPY/TBL/1L1/L` (Positive Coral) and `84CEPY/FC/1L1/E9` (Peach Pi)
> — different colours, same UPC — and Amazon's ASIN `B096NJHL8M`, which carries that UPC, lists its
> Model as **`84PLCE/TBL/1L1/ZL`**. **[RESEARCHED]**
> (<https://www.aztekcomputers.com/84cepy-tbl-1l1-l-ti84-plus-ce-graph-python-texas-instruments/p>,
> <https://www.aztekcomputers.com/84cepy-fc-1l1-e9-peach-texas-instruments/p>,
> <https://www.amazon.com/Python-Graphing-Calculator-Positive-Coral-ation/dp/B096NJHL8M>, all accessed
> 2026-08-12.) This corroborates [`../SOURCING.md`](../SOURCING.md) §1.1's warning that a `84PLCE/`
> number means "not proven Python," not "proven plain" — **the manufacturer's own identifiers are
> muddled at the source.**

### 1.2 Search strings — paste these into a browser

Run every one. Different sellers title the same object five different ways, and the badly-titled
listings are where the margin is.

```
# Sold comps (set these FIRST, then browse actives)
https://www.ebay.com/sch/i.html?_nkw=ti-84+plus+ce+python&LH_Sold=1&LH_Complete=1&_sop=13
https://www.ebay.com/sch/i.html?_nkw=0033317209101&LH_Sold=1&LH_Complete=1
https://www.ebay.com/sch/i.html?_nkw=84CEPY&LH_Sold=1&LH_Complete=1

# Active, cheapest first, price + shipping
https://www.ebay.com/sch/i.html?_nkw=ti-84+plus+ce+python&_sop=15
https://www.ebay.com/sch/i.html?_nkw=ti84+plus+ce+python&_sop=15
https://www.ebay.com/sch/i.html?_nkw=0033317209101&_sop=15

# Auctions only, ending soonest - this is where the deals are
https://www.ebay.com/sch/i.html?_nkw=ti-84+plus+ce+python&LH_Auction=1&_sop=1

# Untested / as-is / no accessories - the bread and butter
https://www.ebay.com/sch/i.html?_nkw=ti-84+ce+python+untested&_sop=15
https://www.ebay.com/sch/i.html?_nkw=ti-84+plus+ce+python+as+is&_sop=15
https://www.ebay.com/sch/i.html?_nkw=ti-84+ce+python+no+charger&_sop=15
https://www.ebay.com/sch/i.html?_nkw=ti-84+ce+python+press+to+test&_sop=15

# Misspellings and bad titles - fewer bidders, same object
https://www.ebay.com/sch/i.html?_nkw=ti84+ce+pyton&_sop=15
https://www.ebay.com/sch/i.html?_nkw=ti+84+phyton+calculator&_sop=15
https://www.ebay.com/sch/i.html?_nkw=texas+instruments+graphing+calculator+python&_sop=15

# Lots - read the model breakdown EVERY time
https://www.ebay.com/sch/i.html?_nkw=ti-84+plus+ce+lot&_sop=15
https://www.ebay.com/sch/i.html?_nkw=graphing+calculator+lot+ti-84+ce&_sop=15

# Catalogue page - see section 1.3 for why this is a trap
https://www.ebay.com/p/19048297204
```

**Useful URL parameters:**

| Parameter | Effect |
|---|---|
| `LH_Sold=1&LH_Complete=1` | Sold comps. **Always start here** |
| `_sop=15` | Price + shipping, lowest first |
| `_sop=1` | Auctions ending soonest |
| `_sop=13` | Newly listed (for sold comps, = most recent sales) |
| `LH_Auction=1` / `LH_BIN=1` | Auction only / Buy-It-Now only |
| `LH_BO=1` | Best Offer accepted |
| `_udhi=45` | Max price $45 — set this to your walk-away number and stop seeing retail |
| `LH_ItemCondition=3000` | Used |
| `LH_PrefLoc=1` | US only |
| `_ipg=240` | 240 results per page |

**Search-term discipline that actually moves price** — from
[`../SOURCING.md`](../SOURCING.md) §3.1, and it is correct: sort completed **sold** listings never
actives (asking prices in this category are fantasy); filter auctions ending 1am–6am Eastern; send
offers on listings 45+ days old with watchers; and **buy the seller, not the item** — someone
liquidating a classroom lists several at once.

### 1.3 The catalogue-page trap

`ebay.com/p/19048297204` looks like the perfect filter — it is eBay's Python-specific catalogue
product. **It systematically hides your best deals.** Only listings the seller *matched to the
catalogue* appear there, and private sellers offloading an untested as-is unit almost never bother to
catalogue-match. So the ePID page shows you the retail-priced, well-titled inventory and filters out
exactly the poorly-titled private listings you are hunting. **[ESTIMATE — this is my inference from
how eBay catalogue matching works, not a measured effect.]**

**Use it as a price reference, not as a sourcing feed.**

### 1.4 Identifying the variant from photos and listing text, before you buy

This extends [`../SOURCING.md`](../SOURCING.md) §1.1 with material I verified today. Work down the
list; stop at the first confirmation.

| Signal | What to look for | Reliability |
|---|---|---|
| **Faceplate wordmark** | Front reads **"TI-84 Plus CE PYTHON"**. Plain CE reads "TI-84 Plus CE" | **High** — demand a straight-on front photo |
| **On-device About screen** | `[2nd]` `[MEM]` → `1:About` shows the model name **and** the OS version in one shot | **Highest single request you can make** |
| **Part number** `84CEPY/` | On box, label, or listing | **High**, positively only |
| **Python Shell actually runs a line** | See §1.5 — this is the only conclusive remote test | **Conclusive** |
| **US-market date code 2021-07 → 2025-12** | Date code on the back reads `L-MMYYR` — e.g. `L-0519M` is May 2019, hardware revision M | **Better than the existing doc allows — see below** |
| **Hardware revision M** | Python Editions use revision **M** | Good corroborating signal |
| Python App present in `[apps]` | | **NOT conclusive — see §1.5** |
| Colour | Both variants shipped in every colour | **None** |
| OS version | A plain CE can run 5.8.x with no Python | **None — the classic mistake** |

> **The date code is a stronger *positive* filter than [`../SOURCING.md`](../SOURCING.md) §1.1 used
> to say.** ✅ **Now adopted there.** That document called manufacture date "weak as a positive one —
> plain CE was still sold alongside."
> For the **US market that is not quite right**: Wikipedia's TI-84 Plus CE series article states
> *"In the North American market, the TI-84 Plus CE Python replaced the existing TI-84 Plus CE in
> 2021."* **[RESEARCHED]** (<https://en.wikipedia.org/wiki/TI-84_Plus_CE_series>, accessed
> 2026-08-12.)
>
> So for a **US-market** unit, a date code between **07/21 and 12/25** is *probable* Python, not
> merely "not excluded." It remains weaker than the faceplate check and it does **not** hold for
> 2026 stock — TI began shipping non-Python CEs in early 2026 (§1.6) — so treat it as a tiebreaker
> that justifies bidding, never as a substitute for the faceplate or About screen.

### 1.5 The faked-Python trap, and the exact test that defeats it

[`../SOURCING.md`](../SOURCING.md) §1.1 warned that the Python App can be installed on non-Python
hardware via a certificate edit. **That is correct, and the specific mechanism and exact failure
string turn a vague warning into a test you can ask a seller to run.** ✅ **Now adopted** — this test
is in `../SOURCING.md` §1.1, §6 and the §8 checklist, and in [`../PREP_SOP.md`](../PREP_SOP.md) §2
step 4 and on the printable bench card.

Cemetech, *"I installed Python on a non-Python TI-84 Plus CE"* **[RESEARCHED]**
(<https://www.cemetech.net/forum/viewtopic.php?t=18856>, accessed 2026-08-12):

> *"the Python App only needs two things to install: 1. A supported OS version… 2. A 'P' in the
> certificate at field 43. This marks the calculator as a 'Python Edition'… I was able to send the
> Python App over. I ran the app and it seemed to function just fine. I even wrote a Hello World
> program. However, when I tried to run the code, I got an error that simply said **"Run and Shell
> are not available right now"**… the extra Python co-processor included in Python Editions is
> physically absent in non-Python Editions."*

A reply in the same thread sharpens it: *"you installed the Python **editor** on a non-Python TI-84
Plus CE, since the interpreter lives on the coprocessor."*

**So the faked unit looks completely convincing right up to the moment code runs.** The app list
shows Python. The editor opens. You can type a program. Only *running* it fails.

> ### The one request to make of every seller
>
> **"Please open the Python app, type `print(1+1)`, and press the Run key. Send me a photo of the
> screen."**
>
> - Shows **`2`** → genuine CE Python. Conclusive.
> - Shows **`Run and Shell are not available right now`** → **plain CE with a faked certificate.
>   Walk away, and consider reporting the listing.**
> - Seller won't or can't → price it as a plain CE (§3) and be pleasantly surprised.
>
> This costs the seller thirty seconds. **It is the single highest-value message you can send**, and
> it is strictly better than the App-list photo, which is precisely the thing a faked unit passes.

### 1.6 2026 stock needs checking too, including "new"

TI began removing Python from newly-manufactured plain CE units in early 2026. A US dealer states it
plainly — a better citation than the unnamed dealer notice
[`../SOURCING.md`](../SOURCING.md) §0 used to carry, and ✅ **now quoted there directly**
**[RESEARCHED]**
(<https://underwooddistributing.com/blogs/calculators/ti-84-plus-ce-python-update>, accessed
2026-08-12):

> *"As of early 2026, Texas Instruments has informed us that Python functionality on the Ti-84 Plus
> CE will be phased out on new calculators manufactured. The TI-84 Plus CE will still be sold;
> however, it will no longer include Python… The TI-84 Plus CE Python Edition is already being phased
> out by the manufacturer. We will begin selling regular Ti-84 Plus CE after the Python units are
> sold out… **There will be no price changes related to the switch.** … If purchasing your Ti-84 Plus
> CE from an alternative retailer, we recommend reaching out to them to clarify whether the Ti-84
> Plus CE you will receive includes python or not."*

Two consequences worth internalising:

1. **Same price, less product.** Because there is no price change, a 2026 retail CE is a coin flip
   between variants at identical cost — which makes buying new a bad way to acquire Python units.
2. **Amazon's plain-CE listing says so out loud.** ASIN `B00TFYYWQA` carries the line *"Customers may
   receive python version while supplies last."* **[RESEARCHED]**
   (<https://www.amazon.com/Texas-Instruments-TI-84-Graphing-Calculator/dp/B00TFYYWQA>, accessed
   2026-08-12.) A literal lottery. **Do not source this way.**

---

## 2. The 15-minute manual comp routine — do this before your first purchase

Because §0 means I could not do this for you, and because comps go stale in days, **this is a task
you own and repeat weekly through August.**

```
1. Open the three SOLD urls from section 1.2. Set the date filter to the last 30 days.
2. For each sold listing, write down: price, condition wording, case?, cable?, and
   whether the PHOTOS actually prove Python (faceplate or About screen).
   Discard any comp where the variant is unproven. This is the step people skip and
   it is the step that matters - a plain-CE comp is not a comp.
3. You need >= 10 variant-confirmed comps. If you have fewer, widen to 90 days
   and note that you are averaging across a seasonal boundary.
4. Compute the MEDIAN, not the mean. One boxed-mint outlier drags a mean badly.
   Record the interquartile range too - the middle 50% is your realistic band.
5. Split the median by condition tier: complete-and-tested / working-no-accessories /
   cosmetically-rough / untested / parts.
6. Write the numbers into section 3 of this file, labelled [RESEARCHED 2026-08-__].
7. THEN open the active urls and shortlist buys, applying section 6's walk-away table.
```

**Free tools that work in a browser when direct URLs are awkward:**

| Tool | What it gives | Note |
|---|---|---|
| **WatchCount.com** → "Search Sold" | 90 days of eBay sold prices, filterable by listing type and date | Bot-gated to automation, fine in a browser. <https://www.watchcount.com/> **[RESEARCHED]** |
| **Resellbot** free sold-comps search | Sold comps with median and interquartile range | <https://resellbot.com/ebay-sold-listings/> **[RESEARCHED]** |
| **eBay Terapeak** (in Seller Hub) | Official sold data, 1–2 years. **Free with any eBay seller account** | The best of these and you already qualify |
| Apify `skootle/ebay-sold-comps` | Programmatic 90-day sold scrape; returns median, P10/P90, sell-through, median days-to-sell | Paid. Only worth it if you scale. <https://apify.com/skootle/ebay-sold-comps> **[RESEARCHED]** |

**Use Terapeak first.** It is free with your seller account, it is eBay's own data rather than a
scrape, and it reports sell-through rate — which you need anyway for
[`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md).

**One methodological warning from WatchCount's own guidance, and it's right:** auctions with many
bids are the most trustworthy value signal; fixed-price sales next; **Best Offer sales are the least
precise because the accepted price is hidden.** Weight your comps accordingly — and note that a lot
of used-calculator volume moves via Best Offer, so your comp set will be noisier than it looks.

---

## 3. Price ranges by condition — **[DERIVED], not fresh comps**

> ⚠️ **Every figure in this section is inherited from [`../SOURCING.md`](../SOURCING.md) §5 and
> [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §7, or is an [ESTIMATE].** None is an observed
> 2026-08 transaction, because of §0. Replace this table with your §2 output.

### 3.1 What you should pay — TI-84 Plus CE **Python**

| Condition | Walk-away max (eBay/shipped) | Target (local/lot) | Basis |
|---|---:|---:|---|
| Grade A, complete (case + cable), tested | **$45** | $38 | [DERIVED — `../SOURCING.md` §5] |
| **Grade B, working, w/ cable — the standard buy** | **$40** | **$32** | [DERIVED] |
| Grade B/C, working, **no** cable/case | **$34** | $27 | [DERIVED]. Add ~$1.50 cable, ~$6 case |
| Grade C, cosmetically rough, working | **$28** | $22 | [DERIVED] |
| **Untested / unknown** | **$25** | $18 | [DERIVED]. Assume ~25% unsellable |
| Dead battery, otherwise fine | **$28** | $20 | [DERIVED]. ~$8 fix. Often the best-value listing on the page |
| **In Press-to-Test** | **$34** | $27 | **Price it as working.** A ~2-minute fix (`../PREP_SOP.md` §4a) that many sellers think is a fault. Genuine information edge |
| Won't charge (port suspect) | **$15** | $10 | [DERIVED]. Frequently a dirty port. Real risk |
| Cracked screen / water damage | **do not buy — §3.3** | — | **Parts only. Never sell as working.** Broken units go for $40+ |
| Lot of 5–10, mixed condition, verified Python | **$32/unit** | $25/unit | [DERIVED] |
| Lot of 10+, mixed **models** | value each unit by variant | — | `../SOURCING.md` §3.5 |

**Your target band is $25–$40, and $32 is the number to hold yourself to.** Anything at or above
~$60 is retail, not sourcing.

### 3.2 Retail and dealer anchors — **[RESEARCHED 2026-08-12]**

These I could verify. They bracket the top of the market and set the ceiling you must price under.

| Item | Price | Source |
|---|---:|---|
| **New** CE Python, Walmart, part no. `84CEPYTBL1L1H` | **$134.00** (was $149.00) | walmart.com, accessed 2026-08-12 |
| **New** CE Python ("Scientific, Python — Black"), Walmart | **$129.98** | same |
| **Pre-Owned CE Python**, Walmart marketplace **asking** | **$113.99** | same |
| **Pre-Owned plain CE**, Walmart marketplace | **$76.98** (was $86.49) | same |
| **Pre-Owned CE "with Preloaded Apps"**, Walmart marketplace | **$98.99** (was $109.99) | same |
| Plain CE promo, Walmart | **$89.20** (was $143.00) | same |
| **Open-box** CE Python `84CEPY/FC/1L1/Z2`, Aztek Computers (US dealer) | **$110.20** | <https://www.aztekcomputers.com/open-box-84cepy-fc-1l1-z2-ti-84-plus-ce-python-graphing-calculator-texas-instruments/p> |
| **New** CE Python `84CEPY/TBL/1L1/L`, Aztek | **$150.55** — **out of stock** | <https://www.aztekcomputers.com/84cepy-tbl-1l1-l-ti84-plus-ce-graph-python-texas-instruments/p> |
| CE Python Teacher Pack `84CEPY/TPK/2L1`, Aztek | **$1,420.53** | same |
| Amazon Renewed **monochrome** TI-84 Plus | **$89.99** | <https://www.amazon.com/Texas-Instruments-Calculator-Certified-Refurbished/dp/B07HG3WGVY> |

**Three things to take from that table:**

1. ~~**The `$95` hard ceiling in [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §2 has loosened.**~~
   **⚠️ Superseded by §3.2a below — the ceiling did not loosen, and this row was measuring the wrong
   thing.** The reasoning survives and was right about one thing: *do not raise prices on a supply
   observation.* The conclusion — that new CE Python starts at ~$130 — turned out to be an artefact of
   searching only **Python-labelled** SKUs. See §3.2a.
2. **A pre-owned *plain* CE asks $76.98 at Walmart while a pre-owned *Python* asks $113.99.** A ~$37
   asking-price spread between variants from the same retailer. Asking prices, not comps — but it is
   the clearest single indication that the Python variant genuinely commands more, which is what
   makes the variant discipline in §1 worth the effort.
3. **Amazon Renewed sells a *monochrome* TI-84 Plus for $89.99.** Your loaded CE Python at $90 is a
   dramatically better object at the same price. Worth remembering when a buyer haggles.

### 3.2a ✅ Resolved — the $95 ceiling stands, and here is the listing that proves it **[RESEARCHED 2026-08-13]**

**The §3.2 sweep and [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §2 appeared to contradict each
other — $93.99 versus $129.98 for a "new CE Python" on the same day. Both were correct. They were
measuring different SKUs**, and the distinction turns out to matter more for pricing than either
figure does.

| Retailer | Item | Price | Status | Source, accessed 2026-08-13 |
|---|---|---:|---|---|
| **Target** | "TI-84 Plus CE Graphing Calculator — Black" (**not** labelled Python) | **$94.99** (reg $110.59, 14% off) | **In stock** | <https://www.target.com/p/texas-instruments-84-plus-ce-graphing-calculator-black/-/A-82545755> |
| **Walmart** | "CE Color Graphing Calculator — Scientific, **Python** — Black" | **$129.98** | listed | <https://www.walmart.com/ip/Texas-Instruments-TI-84-Plus-CE-Graphing-Calculator-Impact-Resistant-Cover-Clock-Date-Time-Display-3-MB-154-KB-ROM-RAM-Battery-Powered-Space-Gray/55586377> |
| **Walmart** | CE Python `84CEPYTBL1L1H` | **$134.00** (was $149.00) | listed | same |
| **Walmart** | CE Python Galaxy Gray | **$139.99** (was $149.00) | listed | same |
| **Walmart** | CE Python Enhanced — White | **$149.95** | listed | same |
| **Walmart** | Plain CE promo | **$87.68** (was $139.00) | listed | same |
| **Best Buy** | Python-capable `84+CE` / `84CEPY` SKUs | **$142.66 – $169.99** | listed | <https://www.bestbuy.com/product/texas-instruments-ti-84-ce-graphing-calculator-black/J73SSTJ3HT> |
| **Staples** | CE **with Python** `84PLCE/RLP/1L1` | **no usable price** | **out of stock** | <https://www.staples.com/texas-instruments-ti-84-plus-ce-with-python-10-digits-battery-powered-graphing-calculator-black-84plce-rlp-1l1/product_24561818> |
| **TI direct** | `ti.com/product/TI-84-PLUS-CE-PYTHON` | — | **404 Not Found** | no consumer price captured |
| Amazon | plain CE — carried forward from §3.2 / economics §2, **not re-fetched today** | $117.50 | — | previously recorded 2026-08-12 |

**Honest notes on the sweep**, per this folder's labelling discipline:

- **Staples' scraped price fields were garbage** ($1,849.99 and $299.99 on a $150 calculator — page
  artefacts from unrelated products). The *stock status* was legible and the price was not, so **no
  price is recorded.** Not estimated, not inferred.
- **Best Buy's page carried stale delivery dates** ("Get it by Wed, May 13"), which means cached
  content. The $142.66–$169.99 band is directionally reliable and well above anything that binds on
  us, so it was not worth re-fetching.
- **TI's own product URL 404s.** No direct-from-TI consumer price was obtained. Not fabricated.
- **Amazon was not re-fetched this pass** — the existing anchor is 2026-08-12 and Amazon is bot-gated.
  Flagged rather than refreshed.

#### The finding that actually matters: Target ships Python units on a plain-CE listing

The **$94.99 Target listing is not labelled a Python model** — its title and description say plain CE,
and Target's own support rep says in the Q&A that it *"is the standard TI84 Plus CE which will not
support Python."* **Four separate customers on that same page say otherwise** [RESEARCHED — Target
Q&A, same URL, accessed 2026-08-13]:

> *"Why was I given the Texas Instruments 84 Plus CE Graphing Calculator Python ver instead of the
> normal one?"* — and the answers: *"Same as me."* · *"I too, was given the Python instead of the
> normal Ti-84CE. On Target's product description it does not say it's a Python. **This is being sold
> online & instores as Ti-84CE (but it's a python model).**"* · *"Just had the same experience. I
> specifically did not want the Python version but that is indeed what it is."* · *"the problem is when
> you pick it up it is the 84 plus ce python"*

Those complaints span roughly five months to a year and all run the same direction: buyers who wanted
the **plain** CE were shipped the **Python**. That is consistent with
[`../SOURCING.md`](../SOURCING.md)'s finding that TI's retail channel no longer cleanly separates the
variants, and with the Amazon listing that warns customers may receive either version.

**So the resolution is the opposite of "there is pricing headroom":**

1. **A new CE, in a box, in stock, at $94.99 today** — and per its own buyers, *sometimes a Python*.
2. **Therefore $95 is not a lapsed promo. It is a live price.** The §3.2 conclusion that new starts at
   ~$130 was true of Python-*labelled* SKUs and false of the shelf a shopper actually reaches.
3. **The ceiling stands, and its justification is now stronger than before.** It used to rest on *"a
   promo that lapsed once could return."* It now rests on *"here is the listing, in stock, at
   $94.99."*
4. **There is no unclaimed headroom to raise the loaded price into.** At a $90 ask the loaded arm is
   already within $5 of a new-in-box unit — which is exactly where the ceiling says it should sit, and
   an argument for *not* testing an $18 differential later without re-checking this first.

**Nothing in the test prices changes.** Bare $78 / loaded $90 in
[`LISTING_TEMPLATES.md`](LISTING_TEMPLATES.md) are set by the experiment, not by the ceiling.

### 3.3 ✅ Resolved — the "buy broken units cheap" tier does not exist for this variant

**[`../SOURCING.md`](../SOURCING.md) §5 and §3.1 were corrected on 2026-08-13 and now carry this
finding.** That document is the authority; what follows is the evidence behind it.

It previously priced *"Cracked screen / water damage"* at an **$8** walk-away max and *"For parts /
not working"* at **$20–$35**. **For the CE Python specifically that was wrong by a wide margin, in
the direction that costs you nothing but is worth knowing.**

Cemetech, in a thread from a parent trying to repair a CE Python **[RESEARCHED]**
(<https://www.cemetech.net/forum/viewtopic.php?t=17536>, accessed 2026-08-12):

> *"The only way I'm aware of to get these parts is to buy a broken calculator off of Ebay.
> Unfortunately, broken TI-84 Plus CEs (**especially Python Editions since they're so new**) are rare
> to come by and **often far more expensive than they [have] any right to be ($40+)**."*

The same thread confirms TI sells no faceplates, keys, or key membranes as parts, which is why the
repair community bids broken units up. That extends
[`../SOURCING.md`](../SOURCING.md) §6's "no repair path for screens" finding to the whole chassis.

**Two practical consequences, and the second is money:**

1. **Do not plan on broken units as a cheap acquisition channel.** At $40+ a cracked-screen CE
   Python is more expensive than your $32 target for a *working* one. The tier is a trap.
2. **When a dud arrives inside a lot, sell it as parts rather than eating it.** A cosmetically
   destroyed or screen-cracked CE Python is worth **[ESTIMATE] $30–$40** to the repair community —
   plausibly more than you paid for it as part of a lot. **[`../SOURCING.md`](../SOURCING.md) §6 has
   been reworded accordingly:** the 10–20% figure is now stated as a *dud rate*, not a write-off
   rate, because the duds have a real resale floor at roughly what a working unit costs. List them
   honestly as "for parts / not working," never as working.
   [`../PREP_SOP.md`](../PREP_SOP.md) §2 step 5 carries the same instruction at the bench.

### 3.4 ✅ Resolved — source-quality warning on the used-price bands

**[`../SOURCING.md`](../SOURCING.md) §2 was rewritten on 2026-08-13: the citation is withdrawn and
the three bands are relabelled [ESTIMATE] with the provenance stated.**
[`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 also dropped its quote from the same article and
records why.

One correction to what this section originally said, because it matters if you go looking:
**`UNIT_ECONOMICS.md` never cited that article for used-price bands.** Its single reference was in
**§6**, not §2, and it was a qualitative quote about how easily a student can load programs
themselves — an argument that stands on other evidence and survived the removal. Only
`SOURCING.md` §2 rested a price figure on it.

The article's used bands were **$80–$110** (good), **$60–$80** (worn), **$30–$50** (parts), already
flagged as a secondary source that "skews high." **It is worse than that: the same article contains a
demonstrable hardware error.**

It states the plain CE's *"Programming support: TI-BASIC only (**add-on module for Python**)"* and
*"Python support requires add-on module (extra $30) on base CE."* **That is false for the TI-84 Plus
CE.** The TI-Python adapter is an accessory for the **TI-83 Premium CE** (the French-market model),
not the TI-84 Plus CE — TI's own adapter guide describes it exclusively as *"an accessory to TI-83
Premium CE graphing calculator."* **[RESEARCHED]**
(<https://education.ti.com/-/media/9D0F92A32BFE460CAE00C7D2AF732171>;
<https://www.hackster.io/news/you-ll-be-able-to-run-adafruit-s-circuitpython-on-the-new-ti-83-premium-ce-calculator-7d86a55bd3f0>,
both accessed 2026-08-12.) The Cemetech thread in §1.5 independently confirms the plain CE has no
Python path at all: *"the extra Python co-processor included in Python Editions is physically absent
in non-Python Editions."*

**So: the repo's core variant thesis is confirmed** — a plain CE cannot run Python, full stop, and
there is no $30 module that changes that. **But the pricing source is compromised**, and its bands
should carry less weight than they currently do in two documents. Replace them with your §2 Terapeak
output.

**A related trap worth naming, because it will mislead you.** General calculator-flipping guides
quote wonderful economics: *"Graphing Calculators | Avg Buy $3-$10 | Avg Sell $45-$80 | Margin 85-95%
| Sell-Through 1-3 days"* **[RESEARCHED]**
(<https://www.underpriced.app/blog/flipping-electronics-for-profit-complete-guide-2026>; similarly
<https://www.thriftbrain.com/guides/flipping-graphing-calculators>, both accessed 2026-08-12).
**Those figures are for the monochrome TI-84 Plus at thrift stores.** They do not apply to the CE
Python at any channel, and mistaking one for the other is precisely how someone talks themselves into
this business with the wrong numbers. Your acquisition cost is **$25–$40**, not $3–$10, and that
single difference is the whole reason
[`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §12 is as cautious as it is.

---

## 4. Defect screening

Follows [`../SOURCING.md`](../SOURCING.md) §6, with two additions I verified.

| Check | What kills the deal |
|---|---|
| **Screen — be ruthless** | Any crack, delamination, dead line/column. **No repair path exists**: TI and the aftermarket sell no replacement CE screens, faceplates, keys, or key membranes (§3.3). A bad screen is permanent |
| **"Black splotches" on screen** | **Pressure-point damage, not dead pixels.** Cemetech's buyers guide: *"they can be an annoyance that's impossible to repair, [but] they do not get worse on their own."* **[RESEARCHED]** (<https://www.cemetech.net/forum/viewtopic.php?t=17926>, accessed 2026-08-12.) So a small splotch is a **permanent grade-C downgrade, not a progressive fault** — price it down, don't reject outright, and photograph it |
| **Charge port** | **USB Mini-B**, not micro-USB, not USB-C. Bent shell, widened opening, cable hanging loose in the photo. Most common terminal fault |
| **Battery** | Ask "does it hold a charge overnight?" Swelling shows as a back cover not sitting flush. Dead cell = ~$8 fix (part `3.7L1200SPB`); swollen-and-deformed housing = write-off |
| **Water damage** | Corrosion crust at the port, tide-lines under the screen, discolouration in the battery bay. **Walk away.** No liquid-damage indicator sticker exists on this family, so visible corrosion is your only signal |
| **Keypad** | Worn legends = grade C/D. Sticky or dead keys = reject; not economically fixable, and no key parts exist |
| **Missing cable / case** | Not dealbreakers. ~$1.50 and ~$6. Negotiating levers. Note that a slide cover measurably affects resale — one reseller guide: *"Calculators that include the hard plastic slide cover sell faster and for slightly more money"* and a bundled USB cable *"adds $5-$10 in value"* **[RESEARCHED]** (thriftbrain.com, accessed 2026-08-12) |
| **In Press-to-Test** | **Not a defect. A price lever.** ~2-minute fix. Sellers routinely discount these as broken |
| **Date code before 07/2021** | **Definitively not a Python unit.** Hard stop |
| **"SCHOOL PROPERTY" faceplate / yellow EZ-Spot back / engraving / district asset tag** | **Decline.** Unsellable at your price point regardless of legality. And the covert tell from [`../SOURCING.md`](../SOURCING.md) §7.1: a post-2021 date code **with a charging LED still present** is almost certainly a school unit in a swapped jacket |

---

## 5. Facebook Marketplace and local channels — manual playbook

**These cannot be searched programmatically, by me or by any tool you'd want to rely on.** Facebook
requires an authenticated session, blocks automation aggressively, and bans scraping in its terms.
OfferUp and Craigslist are similar. **So this is a manual discipline, and
[`../SOURCING.md`](../SOURCING.md) §3.2 is right that it is your best channel** — $0 fees, cash,
inspect-before-paying, and typical negotiated prices of **$30–$50** (**$25–$40** in June)
**[ESTIMATE, inherited]**.

> **§5 is the week-long version of local buying. §7 is the *today* version.** This section sets up the
> saved searches, the WANTED post and the classroom-liquidation conversations that pay off over days —
> **do all of it, it takes twenty minutes** — but do not sit waiting on it on Aug 13. **§7.2 is the
> channel list ordered by what can put a unit in your hand this afternoon**, which is a different
> question with a different answer (pawn shops and repair shops, mostly).

### 5.1 Set it up once — 20 minutes

```
[ ] Facebook Marketplace saved searches, 40-60 mile radius, notifications ON:
      "TI-84"   "TI 84"   "TI84"   "graphing calculator"   "Texas Instruments"
      "TI-84 Python"   "calculator lot"
[ ] Sort by "Date listed: newest". Speed is the entire advantage here
[ ] Same searches on OfferUp and Craigslist
[ ] Post a WANTED listing (see 5.3) - this inverts the search problem
[ ] Join local groups: your district's parent groups, nearby college
    "free & for sale" groups, homeschool groups, teacher groups
[ ] Set a phone alarm for 3pm-5pm weekdays - when parents post after school
```

### 5.2 The message script

Send this within minutes of a listing appearing. Speed beats charm.

```
Hi! Interested in the calculator. Two quick questions so I don't waste your
time:

1. Does the front of it say "TI-84 Plus CE PYTHON", or just "TI-84 Plus CE"?
2. Could you send one photo of the About screen? Press [2nd], then [MEM],
   then choose 1:About. It shows the model and version on one screen.

If it's the Python one and it powers on, I can do $__ cash and pick up today
or tomorrow, whatever suits you.
```

**Why this works:** it is specific, it is easy to answer, and it makes you the buyer who obviously
knows what they're doing — which in a cash negotiation is worth more than haggling. It also gets you
the variant answer **before** you drive.

**If they say "Python" but won't send the About screen, ask for the §1.5 test instead** (`print(1+1)`
in the Python app). If they can't manage that either, offer plain-CE money.

### 5.3 The WANTED post

```
WANTED: TI-84 Plus CE Python graphing calculator

Paying cash today for TI-84 Plus CE PYTHON calculators - the version that says
"PYTHON" on the front. Working or not working, with or without the case and
charger. Buying one or several.

Fair cash prices, I come to you, no haggling and no time wasted. If you have a
box of them from a classroom or a tutoring centre, I'll take the lot.

Also interested in regular TI-84 Plus CE and older TI-84s at lower prices.
```

Renew weekly. It is free and it makes sellers find you.

### 5.4 The channel that actually matters: classroom liquidations

[`../SOURCING.md`](../SOURCING.md) §3.5 names this as the best available source of CE Pythons in
quantity, and the logic is strong: schools bought CE Python heavily from 2021 and are the population
most likely to be migrating to the Evo now. Concretely:

- **Ask retiring or department-switching maths and science teachers directly.** Local teacher
  Facebook groups, district classifieds, and — bluntly — email the department head.
- **Ask closing tutoring centres.** Kumon, Mathnasium, independent tutors.
- **Ask for a photo of three random units' faceplates** before committing to a lot.
- **Value the lot honestly, per unit, by variant.** A 10-unit lot with 3 CE Pythons and 7 monochrome
  units is worth ~$174, not "10 calculators."
- **Get provenance in writing, in the message thread.** Ask every multi-unit private seller where
  they came from. It takes ten seconds and it is your record
  ([`../SOURCING.md`](../SOURCING.md) §7.2).

### 5.5 Local sale is also your best *sell*-side channel — but not during the test

At $30 acquisition, **a $70 local cash sale nets ~$37 against ~$28 for an $88 eBay sale**
([`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §7). Zero fees, zero shipping, no returns risk.

⚠️ **But not with the A/B test units.** [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §2.1 requires
every paired unit on eBay, same format, same hour. Sell your **duds, rejects, and any unpairable
survivors** locally — at 24 units bought that is expected to be 3–5 calculators
([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.1), and local cash is the best channel for exactly
those. Leave the paired units alone.

---

## 6. Per-purchase go/no-go checklist

**Print this. Tape it next to the monitor. The walk-away numbers are the whole skill.**

### 6.1 Walk-away prices **[DERIVED]** from the test's own targets

Using [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §7's inversion,
`max acquisition = 0.7845 × target price − $11.05 − target profit`, at the
[`LISTING_TEMPLATES.md`](LISTING_TEMPLATES.md) test prices:

| If you'll sell it as… | At… | And want… | **Pay no more than** |
|---|---:|---:|---:|
| Bare (test arm) | $78 | $20 profit | **$30** |
| Bare (test arm) | $78 | $15 profit | **$35** |
| **Loaded (test arm)** | **$90** | **$25 profit** | **$34** |
| Loaded (test arm) | $90 | $20 profit | **$39** |
| Loaded, peak-week grade A | $95 | $25 profit | **$38** |
| Local cash sale | $70 | $30 profit | **$37** |

> **The single number to remember: $32 for a standard grade-B unit. Absolute ceiling $40.**
> Above $40 you are working for free — at $45 acquisition and an $88 sale you make **$13 for 53
> minutes** ([`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §12), which is below minimum wage in most
> states once sourcing time is counted. **Do not do that.**

### 6.2 The checklist

```
=== BEFORE YOU BID OR OFFER ===

VARIANT  (get ONE of these or treat it as a plain CE)
[ ] ** IN PERSON: YOU ran print(1+1) yourself and it returned 2 **  <- STRONGEST
    ** Section 7.3. Do not accept a photo when you are holding the unit. **
[ ] Faceplate photo of the ACTUAL unit reads "TI-84 Plus CE PYTHON"
[ ] About-screen photo ([2nd][MEM] 1:About) shows the Python model name
[ ] Seller ran print(1+1) in the Python app and it returned 2   <- best REMOTE test
[ ] Part number 84CEPY/... visible on box or label
    !! OS version proves NOTHING. App list proves NOTHING (faked certs exist).
    !! Date code before 07/2021 = definitively NOT Python. Hard stop.
    !! "Run and Shell are not available right now" = faked certificate. WALK.

CONDITION
[ ] Screen photographed ON. No crack, delamination, dead line or column
[ ] Any dark splotch is small and disclosed (pressure damage - permanent, not spreading)
[ ] Mini-B port intact and square in the photo
[ ] Asked: does it hold a charge overnight? Any liquid exposure?
[ ] Back cover sits flush (no battery swelling)
[ ] Key legends readable; no reported sticky or dead keys

PROVENANCE
[ ] No "SCHOOL PROPERTY" faceplate, no yellow EZ-Spot back, no engraving,
    no district asset tag
[ ] Post-2021 date code does NOT also have a charging LED (school-unit tell)
[ ] Multi-unit seller: asked in writing where they came from, and got a
    specific answer
[ ] Not sequential serials from a private individual

PRICE
[ ] Total landed cost (item + shipping + tax) is at or under the 6.1 number
    (LOCAL, cash: use the section 7.4 column instead - it is lower, because
     there is no shipping and no fees)
[ ] Adjusted DOWN for missing case (~$6) and missing cable (~$1.50)
[ ] Adjusted UP only for a confirmed-Python, tested, complete unit
[ ] If untested: paid the untested price ($25 max), not the working price
[ ] If in Press-to-Test: paid the WORKING price and took the discount

=== GO / NO-GO ===
[ ] GO only if variant is confirmed OR the price is a plain-CE price
[ ] NO-GO on any screen crack, any liquid sign, any school marking
[ ] NO-GO if it costs more than $40 landed, whatever the photos look like

=== AFTER YOU BUY ===
[ ] Logged in AB_TEST_LOG.csv the DAY you buy: cost, channel, date. Then
    serial, variant, and how the variant was confirmed, on arrival
[ ] Photographed as-received, all six faces, BEFORE cleaning
[ ] Run ../PREP_SOP.md from section 2
[ ] Grade, colour, case, battery, screen recorded BEFORE you look at the
    arm column - that is the safeguard (AB_TEST_PROTOCOL.md 2.4 stage 2)
[ ] Pairs formed on matching rules only, then numbered by lowest serial.
    The arm is READ from the committed sequence, never chosen
[ ] Is this the GATE UNIT (the one bought locally on Aug 13)?
       -> run the hardware gate TONIGHT, before you place ANY online order
          (AB_TEST_PROTOCOL.md 3.5). BLOCKING.
       -> TRIG's expected value is in HW_VALIDATION.md 3.0, not in qa/
       -> record the result in HW_VALIDATION.md and in the CSV
```

---

## 7. Same-day local playbook — buying the gate unit in person, today **[NEW 2026-08-13]**

> ### Why this section exists, and why it is today's job
>
> **The owner decided on 2026-08-13 to buy the hardware-gate unit locally, in person, before the online
> orders go out.** The gate ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.5) is what finds out
> whether this repository's `.8xv` AppVars run on a real calculator — **they never have** — and under
> the old schedule it ran on the first shipment to arrive, i.e. **after $875–$1,115 was already
> committed.** One unit bought locally today moves that answer to *before* the money.
>
> **And local buying has one advantage over every online channel that this document has been
> under-selling: you can run the variant test yourself, before you pay.** §7.3. That is not a
> marginally better version of the seller-photo request in §1.5 — it is a categorically stronger test,
> and it is the reason a small premium on this unit is rational (§7.4).
>
> [`README.md`](README.md) has the calendar. This section is what to do between now and tonight.

### 7.1 What to bring

```
[ ] CASH, in small bills. Two amounts in separate pockets: your target (~$32)
    and your ceiling (~$45 for THIS unit only - see 7.4). Cash closes deals
    that "I can Venmo you" does not, and it caps what you can talk yourself into
[ ] A CHARGED PHONE, with section 6.2 and section 7.3 open in a browser tab.
    Do not rely on memory for the failure string
[ ] A USB MINI-B CABLE  <-- mini-B, NOT micro-USB, NOT USB-C (section 4)
       Not to test with - you cannot flash anything in a shop - but so that a
       unit sold "as-is, no charger, might just be flat" can be ruled in or out
       from a power bank instead of guessed at
[ ] A POWER BANK, if you have one. A dead battery is a $8 fix and a $10-$20
    discount; a dead MAINBOARD is a write-off. This is the cheapest way to
    tell them apart at a counter
[ ] Something to write on. Channel, price paid, and the seller's answer about
    provenance go into AB_TEST_LOG.csv the same day (section 6.2)
```

> **A note on the charged-unit check, because it is the one people get backwards.** *You* are not
> bringing a charged calculator — **the seller's unit needs to power on.** If it will not, that is not
> automatically a walk-away: plug your cable and power bank in, give it two minutes, and see whether it
> boots. A unit that boots on external power with a dead battery is a **$28 walk-away / $20 target**
> buy (§3.1) and a perfectly good gate unit. **A unit that shows nothing on external power is a
> write-off — walk away, today of all days.** You cannot run the gate on a calculator that will not
> turn on, and you do not have time to gamble the schedule on a repair.

### 7.2 The channels, by what they can realistically deliver *today*

**Written as channel types rather than named stores, because the right answer depends entirely on where
you live.** Work down the table — it is ordered by *probability of a unit in your hand today*, not by
price. **[ESTIMATE]** throughout: these are channel characteristics from
[`../SOURCING.md`](../SOURCING.md) §3 and §7 applied to a same-day constraint, not measured
conversion rates.

| Channel | Same-day? | Typical price posture | What to expect |
|---|---|---|---|
| **Pawn shops** | **Yes — the best same-day bet** | **Asks high, negotiates hard.** Expect a sticker at $50–$70 and a real price well below it | They buy calculators constantly and price them as generic electronics. **They will not know or care about the Python variant**, which cuts both ways: you can find one mislabelled cheap, and you must assume nothing. Cash, in person, walk-out-the-door — ideal for today. **Call first and ask "do you have any graphing calculators in?"** — five phone calls beats five drives |
| **Facebook Marketplace / OfferUp / Craigslist, local pickup** | **Yes, if a listing is already live and local.** No, if you are waiting for one to appear | **Best prices of any channel.** [`../SOURCING.md`](../SOURCING.md) §3.2: **$30–$50** negotiated, $0 fees | **Today this is a search of existing listings, not a strategy.** §5's saved searches and WANTED post are how this channel pays off over a week — set them up (they take 20 minutes) but do not sit waiting on them today. Message every live local listing within minutes and offer to collect immediately; "I can be there in an hour with cash" wins against a higher offer that involves shipping |
| **Independent electronics / phone repair shops** | **Sometimes, and badly under-rated** | Unpredictable — often $20–$40, occasionally free-with-a-favour | They accumulate un-collected repair drop-offs and trade-ins, and calculators are not their business, so they are not priced as inventory. **Also the one channel where the staff can competently answer "does this power on?"** Worth two phone calls |
| **Thrift and charity resale** | **Yes, but it is a lottery** | **Cheapest possible — $5–$25** when it happens | High variance and no way to check stock remotely. Worth a stop **only if one is on your route to somewhere else.** Note that the "avg buy $3–$10" figures in the flipping guides (§3.4) are for **monochrome TI-84s at thrift stores** — do not plan the day around finding a $10 CE Python |
| **School / university surplus, student sale boards, campus "free & for sale" groups** | **Rarely same-day — usually a few days**, and it is August, so timing is wrong-ish | **Best per-unit price in quantity.** [`../SOURCING.md`](../SOURCING.md) §3.5 calls classroom liquidation the best source of CE Pythons at volume | **This is your channel for the other 23, not for today.** Surplus offices work on their own schedule and student boards need a reply. Start the conversations today (§5.4) and expect units next week. **One exception worth ten minutes: a university surplus store with walk-in retail hours can absolutely produce a unit today** |
| **Big-box retail** | Yes | **$94.99 new and up** (§3.2a) | ⛔ **Not a sourcing channel.** Three times your target, and per §1.6 a new CE is a **coin flip between variants at identical cost.** Listed here only so you don't rationalise it at 6 PM. If the day fails, it fails — see [`README.md`](README.md)'s fallback |

**The efficient version of today, if you have two hours:** phone every pawn shop and repair shop within
range first (**"any graphing calculators?"**), message every live local marketplace listing, *then*
drive to the two or three that said yes. **Phone calls are free and driving is not.**

### 7.3 The point-of-sale variant test — **the whole reason to buy locally**

**This is the strongest form of the check in §1.5, and it is available only in person.**

[`../SOURCING.md`](../SOURCING.md) §1.1 establishes the mechanism (the Python App installs on plain-CE
hardware via a certificate edit, but the interpreter lives on a coprocessor that is **physically
absent**), and §6 puts the test at the top of the pre-purchase checklist. **That material is not
repeated here — read those two sections once, then use this.** What follows is only the adaptation to a
shop counter.

#### Why doing it yourself is categorically better, not just more convenient

| | Seller photo (§1.5) | **You, at the counter** |
|---|---|---|
| Proves the *variant* | Yes | Yes |
| Proves it is **this** unit | **No.** A photo can be of any calculator, including a genuine one the seller also owns | **Yes** |
| Proves it powers on **now** | Weakly | **Yes** |
| Lets you check screen, keys, port in the same minute | No | **Yes** |
| Seller can decline | **Often, and most private sellers can't manage it** | Not really — you are holding it |
| Costs | A message and a wait | **90 seconds** |

**The seller-photo request exists because online you have no alternative.** In person, accepting a
photo instead of pressing the keys yourself throws away the only real edge local buying has.

#### The 90-second sequence

```
1. Look at the FACEPLATE first.  It must read  "TI-84 Plus CE PYTHON".
   Plain CE reads "TI-84 Plus CE".  If the wordmark is absent, you are almost
   certainly done - but keep going anyway, because a swapped faceplate is a
   thing and the Shell test is the one that decides.

2. Power on.  [on]

3. [apps]                       -> the application list
4. Scroll to  Python  -> [enter]
       ** If Python is NOT in the list, it is not a Python unit and there is
          nothing further to test.  Offer plain-CE money (section 3) or walk. **

5. You are now in the Python App's FILE MANAGER.  The bottom row of the screen
   shows menu labels; the graph keys [y=] .. [graph] underneath select them.
   Choose the  Shell  label.

6. At the  >>>  prompt, enter:      print(1+1)
       Use the on-screen  Fns...  menu to insert  print(  rather than typing it
       letter by letter on the alpha keyboard - it is much faster and you are
       standing in a shop.
       [DERIVED shortcut] If you just want the fastest possible check, entering
       1+1 alone at the >>> prompt also requires the interpreter.  print(1+1)
       is the form the rest of this repo documents, so prefer it if in doubt.

7. Press [enter].  READ THE SCREEN.
```

| What the screen shows | What it means | What you do |
|---|---|---|
| **`2`** | **Genuine TI-84 Plus CE Python.** The interpreter ran. Conclusive — nothing fakes this | **Buy it**, subject to §6.2's condition and provenance checks and §7.4's price |
| **`Run and Shell are not available right now`** | **A plain CE with an edited certificate.** The app installed; the coprocessor is not there. **[RESEARCHED]** — the exact string, from the Cemetech thread quoted in §1.5 | **Walk away.** Do not "negotiate down to plain-CE money" on a unit whose certificate has been tampered with — you do not know what else was done to it, and you cannot use it as the gate unit |
| A `SyntaxError`, or a traceback | You mistyped. `print` is case-sensitive and the brackets matter | Retype it. This is not a unit failure |
| Python is absent from `[apps]` | Not a Python unit (or the app was removed — see §3.5.2's note that an All-Memory reset deletes it) | Plain-CE money or walk. **Not a gate unit either way** — you cannot install the app in a shop |
| It won't power on | Unknown | Try your cable and power bank (§7.1). Boots on external power → dead battery, buy at the §3.1 dead-battery price. Nothing at all → **walk** |

> **Say what you are doing, out loud, before you do it.** *"Mind if I turn it on and check the Python
> works? Takes a minute."* Nobody refuses that, and a seller who does has told you something. It also
> removes the "you broke it" argument later.

### 7.4 What to pay locally, and the one place a premium is justified

**Local prices are the *Target* column of §3.1, not the walk-away column.** The walk-away numbers in
§3.1 and §6.1 are for **eBay, landed** — item plus shipping plus tax. In person there is no shipping,
no fees, and no return risk, which is precisely why [`../SOURCING.md`](../SOURCING.md) §3.2 rates local
as the best channel. **[DERIVED]** from §3.1:

| Condition | Online walk-away (landed) | **Pay locally, in cash** |
|---|---:|---:|
| Grade B, working, with cable — **the standard buy** | $40 | **$32**, and open at $25 |
| Grade B/C, working, no cable or case | $34 | **$27** |
| Grade C, cosmetically rough but working | $28 | **$22** |
| Untested / unknown | $25 | **$18** |
| Dead battery, otherwise fine | $28 | **$20** |
| In Press-to-Test | $34 | **$27** — and say nothing; it is a 2-minute fix (§3.1) |

> ### The gate unit is worth a small premium, and here is the exact size of it
>
> **This unit's job is information, not margin.** It is the only unit whose *purchase* buys you an
> answer — whether ten programs run on real hardware — and that answer gates **$690–$920** of ordering
> ([`README.md`](README.md)). A unit that does not materialise today does not cost you $32 of margin;
> **it costs you the ability to place next week's orders against a known result.**
>
> **So: pay up to $45 for a variant-confirmed, powers-on, screen-clean unit today, rather than go home
> empty-handed.** That is above the $32 target and above the $40 standard ceiling, and it is
> deliberate — **for this one unit only.**
>
> **It is still inside the documented ceiling, which is the constraint that actually matters.** §6.1's
> table already prices a **grade-A complete unit at a $45 walk-away**, and §3.1 does too. **$45 is not
> a new number and it is not the $95 retail ceiling being tested** (§3.2a) — it is the top of the
> existing band, applied to a unit that has an extra job.
>
> **What the premium does NOT license:**
>
> - ⛔ **Not $60, not $70, not "it's only $25 more."** Above $45 you are paying retail-adjacent money
>   for a used calculator, and §6.1 is blunt about the arithmetic: at $45 acquisition and an $88 sale
>   you earn **$13 for 53 minutes.** The premium is a $5–$13 concession, not a suspension of the rules.
> - ⛔ **Not on an unconfirmed variant.** The premium exists *because* you verified the variant at the
>   counter. Paying it on a maybe inverts the entire logic.
> - ⛔ **Not on a cracked screen, a school unit, or a no-boot** — §7.5. Those are walk-aways at any
>   price, and today's schedule pressure is exactly the mood in which someone talks themselves past one.
>
> **And note the gate unit stays inside the experiment.** It is unit 1 of 24, graded and paired like
> any other ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.5.2), so overpaying for it also raises
> your average acquisition cost. **$45 is affordable once. It is not a new target.**

**One negotiation note that is worth more than the price table.** In a pawn shop, the sticker is an
opening position and the manager expects an offer. **Offer your target price in cash, in hand,
visible.** If the answer is no, the counter is *"what's the best you can do?"* — and then either accept
it if it is under your ceiling or leave a phone number. **Do not name your ceiling out loud, ever.**

### 7.5 Walk-away conditions — memorise these five

**§6.2 is the full checklist and it still applies in person.** These five are the ones that end the
conversation regardless of price, and they are the ones schedule pressure will tempt you past:

```
1. NO BOOT on external power.
      Not a discount. A write-off, and useless as a gate unit.

2. ANY SCREEN CRACK, delamination, or dead line/column.
      There is NO repair path - no screens, faceplates, keys or membranes
      exist as parts (section 3.3, section 4). And per section 3.3 a broken
      CE Python costs $40+ from the repair community, so this tier is a trap,
      not a bargain.

3. THE FAILURE STRING:  "Run and Shell are not available right now"
      A tampered certificate. Walk - do not renegotiate to plain-CE money.

4. ANY SCHOOL MARKING.  "SCHOOL PROPERTY" faceplate, yellow EZ-Spot back,
   engraving, district asset tag - or the covert tell from ../SOURCING.md
   section 7.1: a post-2021 date code that ALSO still has a charging LED.
      Unsellable at your price point regardless of legality.

5. OVER $45 LANDED, or over $40 for anything that is not today's gate unit.
      Section 6.1: above this you are working for free.

   Plus the two that are always true: visible liquid corrosion, and sticky
   or dead keys.  Both unfixable, both cheap to spot, both listed in section 4.
```

> **The thing to hold onto when a shop has one unit and it fails a check: there will be another unit.**
> Missing today costs you a day, and [`README.md`](README.md) has an explicit fallback — keep trying
> Aug 14–16, and if it still hasn't happened, **place the online orders on Aug 14–15 anyway and gate
> the first arrival.** Buying a cracked-screen unit because you drove forty minutes costs you the unit,
> the drive, *and* the gate. **Walking away is the cheap option every single time.**

---

## 8. The purchase plan — ⚠️ superseded 2026-08-13: all 24 up front

> ### The owner has decided to buy the full 24 units in this window
>
> **This section's original recommendation was 6 units first. That is no longer the plan**, and the
> sequence in [`README.md`](README.md) is now the authority for what to buy and when. The original
> reasoning is retained below because **the risk it identified did not go away — it was reassigned.**

| | |
|---|---|
| **Quantity** | **24 units** — **1 locally on Aug 13, then 23 online Aug 14–20** |
| **Pay** | **≤$32/unit target, $40 hard ceiling.** Budget **$720–$960**. The gate unit may go to **$45** — §7.4, once |
| **Yield** | **9–11 matched pairs**, not 12 ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.1) |
| **Buy FIRST, IN PERSON, TODAY** | **One gate unit.** ⚠️ **Revised 2026-08-13 (second pass): §7 is now a full same-day playbook, and the gate runs before the online orders rather than on the first arrival.** |
| **Hard deadline for drop 1** | **Aug 19–20 for online orders.** Aug 24 closes the window but is **not a usable order date** — see [`README.md`](README.md) |
| **Channel priority, today** | Pawn shops and repair shops by phone → live local marketplace listings → thrift if it's on your route. **§7.2** |
| **Channel priority, the other 23** | Facebook Marketplace local → eBay auctions ending overnight → eBay untested/as-is → school/tutoring-centre liquidation (§5.4) |

**What replaced the pilot's protection.** The original argument was sound: committing $720–$960 before
shipping a single calculator means discovering that your packaging, your photo setup, or your `.8xv`
loading workflow is wrong across 24 units instead of 4. The most serious version of that is the
untested software — **the repo's own README says the `.8xv` AppVars "have not been tested on physical
hardware"** ([`../PREP_SOP.md`](../PREP_SOP.md) §5).

**That specific risk is now handled by the blocking hardware gate in
[`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.5**, which is a defined pass/fail on all ten P6
programs, and **only one unit gets loaded until it passes.**

> **✅ And as of the second 2026-08-13 revision, the gate is now unambiguously *stronger* than the
> pilot was.** The sentence this paragraph used to end with — *"you just own the other 23 already"* —
> was the honest weak point, and it has been fixed rather than argued away. **The gate unit is bought
> locally today and the other 23 are ordered afterwards**, so the gate reports with **~$75 committed
> instead of ~$900.** The pilot risked ~$38 and took a week; this risks one unit and takes an evening.
> **§7 is the playbook.**

**The parts that were not fully replaced, stated plainly:**

- **The process shakedown is still gone.** No throwaway units. It is smaller than it was: the gate unit
  now arrives a week ahead of everything else, so it doubles as a shakedown for wipe / OS+Apps / load /
  photograph — **you just can't throw it away afterwards.** Mitigation in [`README.md`](README.md):
  prep one pair slowly, weigh the parcel, build both listings as unpublished drafts, fix what's wrong.
- **The pricing risk got sharper, and it lands on §2 of this document.** You are committing the whole
  budget in **seven days** against **price bands this document labels as derived from repo baselines
  rather than observed 2026-08 comps** (§0). **Run the §2 manual comp routine today, before the *first*
  purchase** — the day-0 change moved that from "before the third purchase" to "before you leave the
  house," because there is now a purchase happening today. Under the pilot plan a bad price band cost
  you 6 units of exposure; now it costs 24.
- **And one genuinely new exposure, named honestly: today's unit is bought before the comps exist.**
  You are walking into a shop with §3.1's **[DERIVED]** bands and no observed 2026-08 transactions
  behind them. **That is accepted deliberately** — §7.4 explains why an information-buying unit
  tolerates a wider price band than an inventory unit does — but it is a real cost of the day-0
  decision and it should not be glossed over.

⚠️ **Timing, stated honestly.** It is **2026-08-13** and peak sell-side runs to mid-September
([`../SOURCING.md`](../SOURCING.md) §4). The ideal buy window — late May to June, 20–35% below
annual average — **is gone for this year.** You are buying in the expensive month and selling into
the tail of the good one. Two consequences: expect to pay toward the top of the $25–$40 band, and
expect the A/B test's absolute sell-through to look worse than a true August cohort would
([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §5.2). **The paired comparison is unaffected**, which
is the point of pairing. **And put a calendar reminder for 2027-05-25** — buying in June instead of
August is worth more than everything in [`../PREP_SOP.md`](../PREP_SOP.md) combined.

---

## 9. Contradictions with existing docs — all resolved 2026-08-13

Originally flagged rather than edited, per the scope constraint on this folder. **Every row has since
been worked through in the owning document.** Where the resolution went the other way — the older doc
was right and this one was wrong — that is recorded too.

| # | Existing doc said | This document found | Resolution |
|---|---|---|---|
| 1 | `../SOURCING.md` §5: cracked screen walk-away **$8**; §3.1 for-parts **$20–$35** | Broken CE Pythons sell at **$40+** because no parts supply exists (§3.3). Your own duds have a **$30–$40** resale floor | ✅ **This doc won.** Both rows in `SOURCING.md` corrected; the tier is now marked "do not buy" with the Cemetech citation, and §6's write-off wording is fixed |
| 2 | `../SOURCING.md` §1.1: date code is "weak as a positive" filter | For **US-market** units, CE Python *replaced* plain CE in 2021, so a 07/21–12/25 date code is *probable* Python (§1.4). Not for 2026 stock | ✅ **This doc won.** Added to `SOURCING.md` §1.1 with the Wikipedia citation and both caveats |
| 3 | `../SOURCING.md` §1.1: "a photo of the app list is not proof" | Correct, and now testable: the exact failure string on faked units is **"Run and Shell are not available right now"** (§1.5) | ✅ **Improvement adopted.** The `print(1+1)` test is now in `SOURCING.md` §1.1, §6 and §8, and in `../PREP_SOP.md` §2 step 4 and the bench card |
| 4 | `../UNIT_ECONOMICS.md` §2: hard ceiling is the **$95** Walmart promo; new CE Python **$93.99** | Cheapest new CE Python found today is **$129.98**; the $150 dealer unit is out of stock (§3.2) | ⚖️ **Split.** The observation is recorded in `UNIT_ECONOMICS.md` §2, but **$95 stays the operating ceiling** — a lapsed promo can return, and a ceiling is meant to be conservative. Do not re-price on it |
| 5 | `../SOURCING.md` §2 and `../UNIT_ECONOMICS.md` §2 both cite storycircuit.us for used bands | That article contains a false hardware claim (a "$30 add-on module" for Python on the base CE, which is a **TI-83 Premium CE** accessory) | ⚖️ **Mostly this doc, with a correction.** Citation withdrawn in both documents. But **`UNIT_ECONOMICS.md` never used it for price bands** — its one reference was a qualitative quote in §6, not §2. See §3.4 |
| 6 | `../SOURCING.md` §6: budget **10–20%** write-off on untested buys | Possibly too pessimistic here, since duds resell for parts at $30–$40 (§3.3) | ✅ **This doc won, in wording not number.** The 10–20% is kept as a **dud rate**; what changed is that a dud is no longer modelled as a total loss |
| 7 | `../SOURCING.md` §0 cites an unnamed "dealer notice dated 2026-03-12" for the non-Python CE transition | Now citable to a named US dealer, with the added detail that **there is no price change** between variants (§1.6) | ✅ **This doc won.** `SOURCING.md` §0 now quotes Underwood Distributing directly and draws the "buying new is a coin flip" conclusion |
| 8 | `../LOADOUT_STRATEGY.md`: P6 STEM Sampler at 35,080 B | Re-derived at **33,956 B** with `PH` replacing `GASLAW` ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.4) | ✅ **This doc won on the number, lost on the framing.** P6 adopted upstream. But that document's filenames were *already* current — the "cannot be loaded as written" claim was overstated |

---

AP®, SAT®, and ACT® are trademarks registered by their respective owners, none of which are
affiliated with, or endorse, this product. TI-84 Plus CE Python™, TI Connect™ CE, and Texas
Instruments® are trademarks of Texas Instruments Incorporated, which is not affiliated with, and
does not endorse, this product. All trademarks are the property of their respective owners. Nothing
in this document is legal advice.
