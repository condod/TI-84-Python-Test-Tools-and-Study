# Sourcing — Where to Buy Used TI-84 Plus CE Python Units Cheaply

**Labelling convention:** **[RESEARCHED]** = a figure with a citable source, given inline.
**[ESTIMATE]** = my modelling, not a researched figure. Marketplace sold-comp APIs are not publicly
fetchable, so several price bands below are informed estimates triangulated from retail anchors,
published guides, and auction aggregator data — each is labelled.

Research date: **2026-08-12.**

---

## 0. Read this first: the product you're buying was discontinued four months ago

**Texas Instruments discontinued the TI-84 Plus CE Python on 2026-04-27 and launched its
replacement, the TI-84 Evo, on 2026-04-28.** [RESEARCHED]

- TI press release, 2026-04-28: *"Texas Instruments Education Technology today announced the launch
  of the TI-84 Evo Graphing Calculator, the latest and most powerful addition to the TI-84 series…
  3x faster processor, 50% more graphing space, and a redesigned keypad."*
  (<https://texasinsturments.mediaroom.com/2026-04-28-Texas-Instruments-launches-the-TI-84-Evo-Graphing-Calculator-the-most-advanced-TI-84-ever-built>)
- *"the TI-84 Plus CE Python, the calculator the TI-84 Evo replaces, was in production from
  July 27, 2021 to April 27, 2026."*
  (<http://edspi31415.blogspot.com/2026/05/the-new-ti-84-evo.html>, accessed 2026-08-12)
- Cemetech, 2026-04: *"the now-obsolete mini-USB socket has been replaced with a universal USB-C
  socket."* The Evo has Python and TI-BASIC, no C/ASM, a new icon-based UI, and — critically for you
  — **does not use TI Connect CE**; it connects through a web tool at `connectevo.ti.com`.
  (<https://www.cemetech.net/news/2026/4/1062/_/ti-84-evo-calculator-released-fast-graphing-new-ui-new-hardware>)

**A second, quieter change compounds this.** Independent of the Evo launch, TI appears to be
**removing Python from newly manufactured TI-84 Plus CE units.** A dealer notice dated **2026-03-12**
told customers the CE would continue but without the Python feature, and TI-Planet's OS teardown
records boot code **5.8.4.0058** identifying the hardware as **"TI-84 Plus CE (non-Python)"**.
[RESEARCHED, corroborated by two independent sources]

That is the more important fact for you, because it means:

> **The population of Python-capable TI-84 CE hardware is now closed.** Every CE Python that will
> ever exist was built between 2021-07-27 and 2026-04-27. Nothing new is entering the pool, on either
> the Evo side (different platform) or the CE side (Python removed). Your entire addressable supply
> is a fixed, ageing, slowly-attriting set of units.

Closed populations do two things at once: they get cheaper as institutions dump them, and they get
scarcer as units die. Which effect dominates determines whether this line has two good years or five.

**Five consequences for sourcing, and they cut both ways:**

1. **Medium-term, used CE Python supply rises and prices fall.** Schools and students will migrate to
   the Evo across the next few adoption cycles and dump CE Pythons. **This is good for you as a
   buyer** and it is the strongest structural argument for building inventory in 2026–2027.
2. **Short-term, new retail stock is draining.** Once channel inventory clears, the "just buy it new
   for $95 on sale" alternative disappears, which supports used prices for a while. **[ESTIMATE]**
   Expect the used market to be firm through the 2026 back-to-school season and to soften from 2027.
3. **The programs are CE-Python-specific.** The `.8xv` Python AppVar format and the TI Connect CE
   workflow are the CE platform. Whether they carry to the Evo is **[UNVERIFIED]** — one write-up
   says the Evo's new OS architecture is not natively backward compatible with CE programs. **Do not
   assume your product transfers.** Before you invest heavily in inventory, get one Evo and find out.
4. **Do not buy Evo units for this line.** Different port, different connection software, unproven
   compatibility. Bare-resale only, if at all.
5. **Verify Python on every single unit from 2026 stock, including "new."** With TI shipping
   non-Python CEs from early 2026, a sealed-box "TI-84 Plus CE" bought in 2026 may have no Python at
   all. The faceplate wordmark check in §1.1 now matters for new inventory too, not just used.

Net: **2026–2027 is a good window to buy and a decent window to sell. It is not a durable business
to build on**, and the inventory you buy has a declining half-life. Buy for the season you're
selling into, not for a warehouse.

---

## 1. The variant problem — this is the whole game

**Only the TI-84 Plus CE Python runs Python.** TI's own footnote, repeated across its product
pages and its dealer literature: *"Only the Python version of the TI-84 Plus CE graphing calculator
has Python programming capability."* [RESEARCHED]
(<https://education.ti.com/en-au/products/calculators/graphing-calculators/ti-84-plus-ce-python/product-support>,
<https://www.bachcompany.com/Documents/TI-Graphing-Calculators-2025.pdf>, accessed 2026-08-12)

The reason is hardware, not software: the Python interpreter runs on a **separate ARM coprocessor**
(an Atmel ATSAMD21E18A running CircuitPython, communicating with the eZ80 over UART), which plain CE
units do not contain. [RESEARCHED]
(<http://www.datamath.org/Graphing/TI-84PLUS_CEPE_II2021.htm>,
<https://en.wikipedia.org/wiki/TI-84_Plus_CE_series>, accessed 2026-08-12) A plain CE cannot be
upgraded to Python by any OS update, at any version.

**Practical effect:** most of the cheap used TI-84 supply — monochrome TI-84 Plus, TI-84 Plus Silver
Edition, TI-84 Plus C Silver Edition, and plain TI-84 Plus CE — is worthless for the loaded SKU.
This is why acquisition cost in [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) is stubbornly high, and why
the surplus channel (§5) mostly doesn't work.

### 1.1 How to tell a CE Python from a plain CE, from a photo, before you buy

Work down this list. Stop at the first one you can confirm.

| Signal | What to look for | Reliability |
|---|---|---|
| **Faceplate wordmark** | CE Python units are labelled **"TI-84 Plus CE PYTHON"** on the front faceplate. Plain CE reads **"TI-84 Plus CE"**. This is the primary check and it is visible in any straight-on front photo. | **High** — but only if you can read the faceplate. Demand a clear front photo. |
| **Part number** (box, label, or seller listing) | Python: **`84CEPY/...`** — e.g. `84CEPY/FC/1L1`, `84CEPY/TBL/1L1/L`. Plain CE and older: `84PL/FC/1L1` (TI-84 Plus), `84PLCE/...` (plain CE). Teacher packs use `/TPK/`. [RESEARCHED] (<https://www.aztekcomputers.com/84cepy-tbl-1l1-l-ti84-plus-ce-graph-python-texas-instruments/p>, Bach Company 2025 TI dealer catalogue) | **High** when present |
| **On-device model name** | `[2nd]` `[MEM]` → `1:About` displays the model name. Ask the seller for this photo — it is the single most useful request you can make, because it shows model **and** OS version in one shot. | **Highest** |
| **Python App present** | `[apps]` list contains `Python`. | **High, but not conclusive — see below** |
| **Manufacture date** | CE Python production ran **2021-07-27 → 2026-04-27**. A CE with a serial date code before mid-2021 is definitively **not** a Python unit. Date code on the back reads `L-MMYYR` (month, year, hardware revision letter) — e.g. `L-0620O` is June 2020, revision O. [RESEARCHED] (Cemetech, <https://www.cemetech.net/forum/viewtopic.php?t=18642>) | High as a **negative** filter, weak as a positive one — plain CE was still sold alongside |
| **Colour** | Not reliable. Both variants shipped in many colours. Ignore colour as a signal. | None |
| **OS version** | Not reliable on its own. Both variants run 5.x OS; a plain CE can be on 5.8.x and still have no Python. | **None — this is the classic mistake** |

**Two traps in that table worth spelling out.**

**The Python App can appear on hardware that cannot run Python.** Community testing has shown the
Python App can be installed onto a non-Python CE via a certificate edit, where it appears in the
`[apps]` menu and then fails or misbehaves because the ARM coprocessor isn't there. **So a photo of
the app list is not proof of Python hardware.** Ask instead for the **About screen** (which reports
the model name) or, better, a photo of the Python shell with a one-line program actually having run.
The faceplate wordmark plus the About screen together are what you should insist on. [RESEARCHED —
Cemetech community testing]

**Part numbers are less clean than they look.** `84CEPY/...` is reliably Python. But `84PLCE/TBL/1L1`
is used inconsistently across distributor catalogues and has been observed attached to both variants,
so **treat a `84PLCE/` number as "not proven Python," not as "proven plain."** Only `84CEPY/` proves
anything, and only positively.

**Buying rules that follow:**

- **Never buy a "TI-84 Plus CE" from a stock photo.** Require an actual photo of the actual unit's
  faceplate, or the About screen.
- Treat a listing that says "TI-84 Plus CE" in the title and "Python" nowhere else as a plain CE
  until proven otherwise. Many sellers don't know the difference; a few exploit it.
- If a seller can't or won't send an About-screen photo, price the unit as a plain CE and be
  pleasantly surprised.

---

## 2. Price anchors — what "cheap" means

New retail, as of 2026-08-12 [RESEARCHED]:

| Item | Price | Source |
|---|---:|---|
| TI-84 Plus CE Python, Walmart, promo | **$93.99** (was $149.00) | walmart.com listing 172706185 |
| TI-84 Plus CE, Walmart, promo | **$87.68** (was $139.00) | walmart.com listing 55586377 |
| TI-84 Plus CE Python, Walmart, various sellers | **$129.98 – $149.95** | same |
| TI-84 Plus CE, Amazon | **$117.50** | amazon.com/dp/B01FY73EI8 |
| TI-84 Plus CE Python Teacher Pack of 10, Walmart | **$1,548.53** (≈$155/unit) | walmart.com |
| TI-84 Evo (the replacement), Walmart | **$160.00** | walmart.com |
| "Pre-Owned TI-84 Plus CE Python," Walmart marketplace **asking** | **$113.99 – $129.99** | walmart.com — **asking prices from resellers, not sold comps. Ignore as a valuation signal.** |

Third-party used-market commentary [RESEARCHED, secondary source, treat as indicative]:
<https://storycircuit.us/blog/ti-84-plus-ce-comparison/> (accessed 2026-08-12) reports used CE units
in good condition at **$80–$110**, cosmetically worn at **$60–$80**, and broken/parts at **$30–$50**,
and a new-price floor that *"rarely dips below $110"* with the Python version at *"$140–$160."*
Those figures skew high relative to what an actual eBay sold comp will show for a private-seller
used unit, but they bracket the retail end correctly.

**What this means for you as a buyer:** anything at or above ~$60 is not a sourcing opportunity, it
is retail. Your target is **$25–$40**.

---

## 3. Channel-by-channel

### 3.1 eBay

**Verdict: mediocre for buying, excellent for selling.** You are competing against the same buyers
you will later sell to, which caps your discount.

| Segment | Realistic acquisition, CE Python | Notes |
|---|---:|---|
| "Tested, working, w/ charger" BIN | $55–$75 [ESTIMATE] | No margin. Skip. |
| Auction, ends at an odd hour, poor photos | $40–$55 [ESTIMATE] | Where the deals are. |
| "Untested / as-is / no charger" | $35–$50 [ESTIMATE] | Your bread and butter, with real risk. |
| "For parts / not working" | $20–$35 [ESTIMATE] | Only worth it if you can diagnose; most are dead batteries or dirty ports, both fixable. |
| Multi-unit lots (5–20) | $35–$50/unit [ESTIMATE] | **Read the model list.** Most "TI-84 lots" are monochrome. |

**Tactics that actually move the price:**

- **Search misspellings and bad titles.** `TI84 Plus CE Python`, `TI-84 CE Pyton`,
  `Texas Instruments graphing calculator python`, `84CEPY`. Poorly-titled listings get fewer bids.
- **Filter to auctions ending 1am–6am Eastern.** Fewer live bidders.
- **Sort by "no bids," lowest price + shipping.**
- **Send offers on aged listings.** A listing 45+ days old with watchers and no sale takes ~60–70%
  of ask surprisingly often.
- **Buy the seller, not the item.** Someone liquidating a classroom or an estate lists several at
  once; message and buy all of them off-platform-ish (through eBay, as a combined order) at a
  discount.
- **Always sort completed *sold* listings, never active ones.** Asking prices in this category are
  fantasy, especially the Walmart-marketplace resellers above.

**Hard rule from [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) §7: your maximum bid is $31 if you're
targeting an $88 sale and $25 of profit.** Write it on a sticky note next to the monitor. Auction
discipline is the entire skill here.

### 3.2 Facebook Marketplace

**Verdict: the best realistic channel, and the only one where you both buy AND sell at good margin.**
[ESTIMATE for all figures]

- Typical asking: **$50–$80.** Typical negotiated: **$30–$50.** In June, **$25–$40.**
- Zero fees, zero shipping, cash, immediate inspection. You can power the unit on before you pay,
  which eliminates most of the risk that makes eBay sourcing expensive.
- **Set saved-search alerts** for "TI-84," "TI 84," "graphing calculator," "Texas Instruments" across
  a 40–60 mile radius and respond within minutes. Speed is the whole advantage on Facebook.
- **Ask for the About-screen photo before driving.** Non-negotiable — see §1.1.
- Bundle offers work: "I'll take all three for $90 cash today" beats haggling each one.
- **Post a "wanted" listing.** Cheap, and it inverts the search problem.

### 3.3 OfferUp / Mercari

**Verdict: secondary. [ESTIMATE] $40–$55 realistic.** Similar dynamics to Facebook with less volume
and more friction. Worth a saved search, not worth a strategy. Mercari sellers ship, which means you
can't inspect first — price the risk in.

### 3.4 Thrift, Goodwill, ShopGoodwill, pawn

**Verdict: real but unplannable.** [ESTIMATE]

- Physical Goodwill/Salvation Army: **$10–$30** when a graphing calculator appears at all, which is
  rarely and unpredictably. Electronics often get routed to shopgoodwill.com rather than the shelf.
- **shopgoodwill.com**: auction-priced, and calculators there frequently run **close to eBay comps**
  because the same resellers are bidding. Check anyway; occasionally a lot is miscategorised.
- Pawn shops: **$30–$60**, and they know what they have. Negotiate; they carry inventory cost and
  will move on aged stock.

Treat this as opportunistic. Don't build routes around it.

### 3.5 Bulk and lot buying

The single biggest lever on [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md), and the hardest to execute.

- **Teacher/classroom liquidations.** A retiring teacher or a department switching to the Evo may
  have 10–30 units. Find them through local teacher Facebook groups, district classified sections,
  and — bluntly — by asking. This is the best available source of CE Pythons in quantity, because
  schools bought CE Python heavily from 2021 onward and are now the population most likely to
  upgrade.
- **eBay lots.** Read the model breakdown, every time. A "lot of 20 TI-84s" is usually 18 monochrome
  units and 2 CEs.
- **Buy at the right time.** See §4.
- **Verify before committing to a big lot** by asking for a photo of three random units' faceplates.

**Model your lot the honest way:** value each unit at its actual variant. A 10-unit lot with 3 CE
Pythons at $30 each ($90) plus 7 monochrome units worth maybe $12 each in bare resale ($84) is worth
about $174 total before your labour — not "10 calculators."

### 3.6 Government / school-district surplus — the trap

**Verdict: genuinely cheap, and almost never the right hardware.** [RESEARCHED, with caveat]

Three verified auction results, which together tell the whole story:

| Lot | Result | Per unit, incl. premium | What was actually in it |
|---|---|---:|---|
| GovDeals, Montvale NJ, 45 calculators | **$200** after 37 bids, +12.5% BP | **$5.00** | TI-73 ×3, TI-30SLR+ ×10, TI-30Xa ×2, TI-83 ×4, TI-84 Plus mono ×25, TI-84 Plus SE ×1. **Not one CE.** |
| Bryan ISD, TX, **250 × TI-84 Plus CE** | **$4,750** + 10% BP | **$20.90** | CE — but **EZ-Spot school-property editions** (see §7.1) |
| HiBid, single TI-84 Plus CE | $16 hammer + 20% BP | **$19.20** | Single consumer unit |

(<https://bidprowl.com/listing/lot-of-calculators-45-nj-govdeals-8869-90>, accessed 2026-08-12.)

**Read those three rows carefully.** The dirt-cheap lot was all obsolete monochrome hardware. The one
lot that genuinely delivered CE units at ~$21 delivered *EZ-Spot* units, which §7.1 explains you
should not build the loaded SKU on. And note the **buyer's premium ran 10–20%** across these —
consistently higher than people assume when they bid.

Aggregate government-surplus electronics medians in Texas run **$81 on GovDeals** and **$21 on
PublicSurplus** per lot (<https://bidprowl.com/sold/electronics/texas>, accessed 2026-08-12) — cheap,
but overwhelmingly older equipment.

**Why school surplus lags:** districts run calculators for 8–12 years and surplus them at
end-of-life. CE Pythons only entered classrooms from 2021 and are, in 2026, current classroom
inventory. They will start appearing in surplus channels as the Evo rolls out — plausibly
**[ESTIMATE] 2028 onward** — and that will be the moment this channel becomes the right one.

**If you do bid:**

- **Buyer's premium is real** and typically runs ~7.5–12.5% on GovDeals [ESTIMATE — verify per
  auction; each listing states it]. Add sales tax. Add the drive.
- **Pickup is usually mandatory and local.** A cheap lot 300 miles away is not cheap.
- Lots are sold **as-is, untested,** frequently in unknown condition, and frequently in
  Press-to-Test.
- **Only bid when the lot description or photos individually identify CE Python units**, or when the
  price is so low that the monochrome units alone justify it as a separate bare-resale line.

### 3.7 Channel summary

| Channel | Cost/unit (CE Python) | Volume | Reliability | Use it? |
|---|---:|---|---|---|
| Facebook Marketplace, local | **$30–$50** [EST] | Medium | Good | **Primary** |
| Teacher/classroom liquidation | **$25–$40** [EST] | Lumpy | Good when found | **Primary — pursue actively** |
| eBay auctions / as-is | **$35–$55** [EST] | High | Fair | Secondary |
| eBay lots | **$35–$50** [EST] | Lumpy | Fair | Secondary, read the model list |
| OfferUp / Mercari | **$40–$55** [EST] | Low | Fair | Opportunistic |
| Thrift / pawn | **$10–$60** [EST] | Very low | Poor | Opportunistic |
| shopgoodwill.com | near eBay comps [EST] | Low | Fair | Check, rarely buy |
| Gov/school surplus | **$1–$25** [RESEARCHED] but wrong models | High | Poor **for this product** | **Not yet — revisit ~2028** |

---

## 4. Seasonality

Calculator prices swing hard and predictably. **[ESTIMATE — the direction is well established; the
magnitudes are my modelling.]**

| Window | Buy-side | Sell-side | What to do |
|---|---|---|---|
| **May – late June** | **Cheapest of the year.** Graduating students and families dump units the week school ends. Prices **20–35% below annual average**. | Worst. Nobody's buying. | **Buy hard. Do not list.** This is the whole edge. |
| **July – mid September** | Expensive. Everyone is buying. | **Peak.** Highest prices and fastest sell-through of the year. | **Sell everything.** Don't discount. |
| **Late September – November** | Moderate | Thin | Keep listings live; don't add inventory. |
| **December – early January** | Moderate; some post-holiday dumping | **Secondary peak** for spring semester, real but smaller than August | Sell into early January. |
| **February – April** | Moderate | Thin | Quietest quarter. Good time to build process, not inventory. |

**The June-to-August spread is larger than the software premium.** [ESTIMATE] Buying at $30 in June
and selling at $90 in August is a materially better trade than buying at $42 in August and selling at
$92. That spread is the most reliable money in this business and it requires no labour at all — only
capital and patience.

Practical implication: **this is a seasonal operation.** Concentrate acquisition in a 6-week window
starting the last week of May, prep through July, and list from the last week of July.

---

## 5. What to pay — the table

Print this. All figures **[ESTIMATE]**, derived from the retail anchors in §2 and the break-even
maths in [`UNIT_ECONOMICS.md`](UNIT_ECONOMICS.md) §7.

### TI-84 Plus CE **Python** (the product)

| Condition | Walk-away max (eBay/shipped) | Target (local/lot) | Notes |
|---|---:|---:|---|
| Grade A, complete (case + cable), tested | **$45** | $38 | Only worth the premium in a slow month. |
| Grade B, working, w/ cable | **$40** | $32 | The standard buy. |
| Grade B/C, working, **no** cable/case | **$34** | $27 | Add ~$1.50 cable, ~$6 case. |
| Grade C, cosmetically rough, working | **$28** | $22 | Bare resale or low-tier loaded. |
| **Untested / unknown** | **$25** | $18 | Assume 25% are unsellable. |
| Dead battery, otherwise fine | **$28** | $20 | ~$8 fix. Often the best-value listing on the page. |
| Won't charge (port suspect) | **$15** | $10 | Frequently just a dirty port. Real risk. |
| Cracked screen / water damage | **$8** | $5 | **Parts only. Do not attempt to sell as working.** |
| Lot of 5–10, mixed condition, verified Python | **$32/unit** | $25/unit | |
| Lot of 10+, mixed **models** | value each unit by variant | — | See §3.5 |

### Plain TI-84 Plus CE (bare-resale line only — no Python, no loaded SKU)

| Condition | Walk-away max | Notes |
|---|---:|---|
| Grade A/B, complete | **$32** | Resells ~$60–$70 [ESTIMATE] |
| Grade C, working | **$22** | |
| Untested | **$16** | |

### Older monochrome (TI-84 Plus / Silver Edition / C Silver)

| Condition | Walk-away max | Notes |
|---|---:|---|
| Working, any grade | **$10** | Resells ~$25–$40 [ESTIMATE]. Thin, but takes almost no prep. |
| Lot | **$4/unit** | The realistic use for a cheap surplus lot. |

### TI-84 Evo

**Do not buy for this line.** Different port, different connection software (`connectevo.ti.com`,
not TI Connect CE), and program compatibility with the CE `.8xv` format is **[UNVERIFIED]**. Buy one
single unit, once, as R&D — not as inventory.

---

## 6. Defect screening

### Before you buy (photos / in person)

| Check | What kills the deal |
|---|---|
| **Screen** | Any crack, delamination, dead line/column, or a pressure bruise larger than a fingernail. Ask for a photo with the screen **on** — a dark screen in every photo is a red flag. **There is no repair path: replacement CE screens are not sold as parts by TI or by any aftermarket supplier.** A bad screen is a permanent write-off, so this is the one defect to be ruthless about. |
| **Charge port** | The CE family uses **USB Mini-B**, not micro-USB and not USB-C. [RESEARCHED — TI spec: *"Standard A to Mini-B USB cable included"*] Look for a bent shell, a widened opening, or a cable that hangs loose in the photo. Port damage is the most common terminal fault. |
| **Battery** | Ask "does it hold a charge overnight?" Swelling shows as a back cover that no longer sits flush, or a slightly bowed faceplate. A dead cell is a **$8** fix (TI part **3.7L1200SPB**, 3.7 V 1200 mAh); a swollen one that has deformed the housing is a write-off. [RESEARCHED part number] |
| **Water damage** | Corrosion crust around the port, tide-line staining under the screen, discolouration in the battery bay. **Walk away** — intermittent faults surface after the buyer has it. Note there is **no documented liquid-damage indicator sticker** on the CE family, unlike phones, so visual corrosion is your only signal. Look hard at the port pins. |
| **Missing charger** | Not a dealbreaker; a generic mini-B cable is ~$1.50. Use it as a negotiating lever, not a rejection. |
| **Missing slide case** | ~$6 to replace. Same — negotiate. |
| **Keypad** | Worn-off legends are a cosmetic downgrade to grade C/D. Sticky or unresponsive keys are a reject; you cannot economically fix them. |
| **Back cover / screws** | Missing back cover or stripped screws suggests a prior teardown. Ask why. |
| **In Press-to-Test** | Not a defect. A ~2-minute fix ([`PREP_SOP.md`](PREP_SOP.md) §4a). Use it as a price lever — many sellers think it's broken. **This is a genuine information edge; sellers routinely discount "stuck in test mode" units.** |

### After you buy

Run [`PREP_SOP.md`](PREP_SOP.md) §2. The reject criteria there are the ones that matter.

**[ESTIMATE] Budget a 10–20% write-off rate on untested purchases.** If you're not occasionally
buying a dud, you're bidding too conservatively and leaving volume on the table.

---

## 7. Stolen and school-property units

Buying stolen goods is a legal and reputational problem, and school-marked units are near-impossible
to resell cleanly. Screen for these.

### 7.1 TI "EZ Spot" / School Property Edition — avoid entirely

TI sells school-specific variants: *"Each EZ-Spot calculator has a bright 'School Bus Yellow' backing
and slide case; each calculator also has a face plate inscribed with the words 'SCHOOL PROPERTY'.
… Each EZ-Spot Teacher Pack contains 10 calculators."* [RESEARCHED]
(<https://education.ti.com/en/customer-support/knowledge-base/ti-83-84-plus-family/general-information/12191>,
accessed 2026-08-12). Available in TI-84 Plus CE among other models; sold through instructional
dealers in `/TPK/` teacher packs.

**These are not illegal to own in themselves** — schools do legitimately surplus them, and dealers
sell singles. But:

1. A unit with "SCHOOL PROPERTY" printed on the faceplate is **unsellable at your price point.** No
   student wants it and every buyer assumes it's stolen.
2. From a private seller with no institutional paperwork, a yellow EZ Spot unit is a **strong theft
   signal**. Decline.
3. From a documented district surplus auction, it's legitimate — but see point 1. Value it as parts.

**Rule: don't buy EZ Spot units for the loaded SKU.** If one arrives inside a lot, part it out,
donate it, or move it to the bare-resale line at a 30–50% discount with provenance disclosed in the
listing. Sourced from a documented district surplus auction they are perfectly legal to resell —
they're just the wrong product for a premium student-facing SKU.

**The covert tell: the charging LED.** A seller can swap a yellow back cover for a standard one, but
they can't change the board. Consumer TI-84 Plus CE units built from roughly **June 2021** (hardware
revision T onward) **dropped the charging LED**. EZ-Spot and School Property units **kept it.** So:

> **A CE with a post-2021 manufacture date code that still has a charging LED is almost certainly a
> school unit wearing a different jacket.** Cross-check the `L-MMYYR` date code on the back against
> the presence of the LED. [RESEARCHED — Cemetech hardware-revision documentation]

This is the single most useful physical check in this section, because it defeats the one form of
disguise a reseller can cheaply apply.

### 7.2 Other red flags

| Signal | Read |
|---|---|
| Engraved or acid-etched school/district name, or a riveted asset tag | Institutional property. Cannot be removed cleanly. **Decline.** |
| Adhesive asset/barcode/inventory label | Weaker signal — students label their own too. Ask; if it's a district barcode, decline. |
| Seller has **several identical units**, no business account, no explanation | Classic classroom-theft pattern. Ask directly: *"Where did these come from?"* A legitimate seller (retiring teacher, tutoring centre closing, parent of three) answers instantly and specifically. Evasion is your answer. |
| **Sequential serial numbers** across multiple units from a private seller | Same purchase order — i.e. an institutional buy. Legitimate if the seller is/was the institution; not if they're a random individual. |
| Unit is in Press-to-Test **and** carries a school's TI-BASIC programs or class datasets | Came straight out of a classroom set. Ask. |
| "Found it," "it was my cousin's," meet-only-at-night, cash-only-no-questions | Standard stolen-goods pattern. Walk. |
| Price far below every comp with no condition explanation | If it's too cheap, there's a reason, and "stolen" is one of the reasons. |

**Practical policy:**

- Ask every multi-unit private seller where the units came from, in writing, in the platform's
  message thread. It takes ten seconds and it's your record.
- Photograph or note serial numbers on everything you buy (the inventory app already tracks this).
  If a unit is later reported stolen, contemporaneous records showing what you paid, to whom, and
  when are what separate a mistake from a problem.
- **Never buy anything with a school's name physically on it.** No exceptions; the resale math
  doesn't work anyway.

---

## 8. Sourcing checklist

```
BEFORE BUYING
[ ] Confirmed CE PYTHON: faceplate wordmark, 84CEPY part number, or About-screen photo
    (OS version alone proves NOTHING)
[ ] Screen photographed ON, no cracks/dead lines/bruises
[ ] Mini-B port intact in photo
[ ] Asked: does it hold a charge? Any water exposure?
[ ] Cable/case present? (adjust price, don't reject)
[ ] No "SCHOOL PROPERTY" faceplate, no engraving, no district asset tag
[ ] Multi-unit seller: asked where they came from, in writing
[ ] Price is at or below the §5 walk-away number
[ ] It is the right season to be buying (May-June best; July-Sept worst)

AFTER BUYING
[ ] Logged in the inventory app: acquisition cost, channel, date, serial, variant
[ ] Photographed as-received before cleaning
[ ] Run PREP_SOP.md
```

---

AP®, SAT®, and ACT® are trademarks registered by their respective owners, none of which are
affiliated with, or endorse, this product. TI-84 Plus CE Python™, TI Connect™ CE, and Texas
Instruments® are trademarks of Texas Instruments Incorporated, which is not affiliated with, and
does not endorse, this product. All trademarks are the property of their respective owners. Nothing
in this document is legal advice.
