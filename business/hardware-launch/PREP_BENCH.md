# Prep Bench — Equipment, Costs, and Throughput

**The physical setup to process CE Python units at the ~38 min/unit rate
[`../PREP_SOP.md`](../PREP_SOP.md) §10 assumes.**

Written 2026-08-12. [`../PREP_SOP.md`](../PREP_SOP.md) §1 lists *what* you need; this document prices
it, says where to buy it, tells you what to skip, and connects the kit to the throughput number the
whole economic model rests on.

**Labelling convention, matching the rest of `business/`:** **[RESEARCHED]** = a figure with a
citable source, given inline. **[ESTIMATE]** = my modelling. **[DERIVED]** = taken from the cost
stack in [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §4.

> ## ⚠️ TODO — price verification is incomplete
>
> **Most individual product prices below are [ESTIMATE], not verified retail quotes.** The live
> pricing pass for this document did not complete (the same automated-fetch blocking described in
> [`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) §0 affected Amazon and Walmart product pages).
> What *is* researched and citable is carried forward from
> [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §4 and [`../PREP_SOP.md`](../PREP_SOP.md) §1 — the
> part numbers, the connector types, the bubble-mailer per-unit cost, and the consumable rates — and
> those are the figures that actually drive the model.
>
> **What would finish this:** 30 minutes with an Amazon and a WebstaurantStore tab open, pricing the
> 14 **ESSENTIAL** rows in §2 and writing the real numbers into the Price column. The totals in §6
> should move by tens of dollars, not hundreds. **Do not let this block the first purchase** — the
> only items you need before unit 1 are a data-capable Mini-B cable, TI Connect CE, IPA, cloths, and
> mailers.

---

## 0. The short version

| | Essential-only | Full bench |
|---|---:|---:|
| **One-time equipment** | **≈ $155** | **≈ $400** |
| Per-unit consumables | $5.15 | $5.15 |
| Consumables for a 24-unit launch batch | $124 | $124 |
| **Total to start, 24 units** | **≈ $279** | **≈ $524** |

**[ESTIMATE]** on the equipment lines, **[DERIVED]** on the consumables.
[`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §4 budgets **~$140** for one-time setup and **$5.15**
per unit in materials; the essential-only figure above is deliberately close to that, because that
document's number is the one the whole P&L is built on and the bench should not blow through it.

**The one-time cost amortises to nothing.** At 24 units the essential bench adds **$6.46/unit**; at
60 units, **$2.58/unit**. Against a ~$28 net per unit that is real but not decisive —
[`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §8 is right that **acquisition cost dominates
everything**. Do not spend a day optimising the bench and then overpay $8 on a calculator.

---

## 1. Buy this before unit 1 — the five-item minimum

You can process a first unit end-to-end with these alone. Everything else in §2 makes you faster or
tidier.

| # | Item | Est. cost | Why it's non-negotiable |
|---|---|---:|---|
| 1 | **USB-A to Mini-B cable, DATA-capable** ×2 | $8 | Without this nothing happens. See §3 — the charge-only trap is real and it will waste an hour |
| 2 | **TI Connect™ CE** (Windows) | **$0** | Free from TI. 6.0.3, 2025-03-26 **[RESEARCHED — `../PREP_SOP.md` §1]** |
| 3 | **TI-84 Plus CE OS + Apps bundle** (`.b84`) | **$0** | Free from TI. **Must be the OS *and Apps* bundle**, not the OS-only file — see §4 |
| 4 | **70–91% isopropyl alcohol + microfibre cloths** | $12 | Cleaning is 6 min/unit of the SOP and it is what makes a $32 unit look like a $90 one |
| 5 | **#1 (7.25×12) kraft bubble mailers, 100-pack** | $18 | You cannot ship without them, and the size matters (§5) |

**Total to first unit: ≈ $38.** Everything else can wait until you know you're continuing.

---

## 2. Full shopping list

### 2.1 ESSENTIAL — cannot process units without it

| Item | Recommended | Est. cost | Where | Notes |
|---|---|---:|---|---|
| **USB-A to Mini-B cables ×6–8** | Generic 3 ft, **data-capable** multipack | **$18** [ESTIMATE] | Amazon, Monoprice, eBay | **The CE family uses Mini-B — not micro-USB, not USB-C. [RESEARCHED]** TI's spec: *"Standard A to Mini-B USB cable included."* One per bench slot plus spares. See §3 |
| **New generic Mini-B cables for the box** | Same, bought in bulk | **$1.50/unit** [DERIVED] | Same | Ships with every unit. [`../PREP_SOP.md`](../PREP_SOP.md) §9: never ship a filthy used cable. Removes an entire class of "it won't charge" tickets |
| **Powered USB hub, 7–10 port** | Sabrent HB-BUP7 / Anker 10-port, **with its own wall PSU** | **$35** [ESTIMATE] | Amazon | Charging 6 units at once. **Must be externally powered** — a bus-powered hub cannot supply 6 charging calculators, and laptop sleep kills a charge mid-flash |
| **TI Connect™ CE** | v6.0.3 | **$0** [RESEARCHED] | education.ti.com | **Install before first connecting a calculator** so drivers are in place |
| **OS + Apps bundle (`.b84`)** | Current release (**5.8.5**, April 2026) | **$0** [RESEARCHED] | education.ti.com | Verify the version before each batch |
| **Isopropyl alcohol, 70%** | 16 oz bottle | **$7** [ESTIMATE] | Any pharmacy | 70% not 91% for plastics. **Never acetone — it hazes the case** |
| **Microfibre cloths** | 12-pack | **$9** [ESTIMATE] | Amazon, auto section | Dedicate two to screens only |
| **Cotton swabs** | 500-pack | **$4** [ESTIMATE] | Pharmacy | Key edges and port surrounds |
| **Soft detail brush** | Anti-static or artist's brush | **$6** [ESTIMATE] | Amazon | **Brush and blow grit out before any liquid** |
| **Plastic spudger / pry set** | Nylon, non-marring | **$8** [ESTIMATE] | Amazon, iFixit | Battery connector. **Never pull the wires** |
| **Precision screwdriver, Phillips #00** | Small driver set | **$12** [ESTIMATE] | Amazon, iFixit | Back cover / battery access. **[RESEARCHED — `../PREP_SOP.md` §1 specifies #00]** |
| **Replacement batteries — TI `3.7L1200SPB`** | 3.7 V 1200 mAh Li-ion, 5–10 pack | **$8/cell** [RESEARCHED part no.] | Amazon, eBay, TI parts dealers | ~20% incidence → **$1.60/unit** [DERIVED]. `3.7L1200SPA` is the older revision, generally compatible; **buy the SPB.** See §4.2 |
| **Digital shipping scale** | 0.1 oz resolution, 50 lb capacity | **$18** [ESTIMATE] | Amazon | **Not optional — see §5.** Mercari rounds *up* to the tier ceiling |
| **#1 (7.25×12) kraft bubble mailers** | Case | **$0.14–$0.36/unit** [RESEARCHED] | WebstaurantStore, Uline, ValueMailers | E.g. Lavex #0 250/case at $33.99 = **$0.14/unit** (<https://www.webstaurantstore.com/lavex-packaging-self-sealing-kraft-bubble-mailer-0-6-x-10-case/442KBM0S.html>) |
| **Packing tape** | 2 in, 2-pack | **$8** [ESTIMATE] | Anywhere | ~$0.03/parcel [DERIVED] |
| **Cardboard stiffeners** | **Cut from inbound boxes** | **$0** | Your own recycling | The single most important packing item (§5) |

**ESSENTIAL one-time subtotal: ≈ $155.** **[ESTIMATE]**

### 2.2 NICE-TO-HAVE — pays for itself somewhere past ~20 units

| Item | Recommended | Est. cost | Verdict |
|---|---|---:|---|
| **Light tent / photo box, 16–20 in, LED** | Amazon generic | **$40** [ESTIMATE] | **Buy this one first of the optionals.** Photo consistency across 12 shots × 20 listings is a hard requirement of [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §2.1, and doing it by window light is fragile |
| **Neutral light-grey backdrop** | Matte poster board, 2 sheets | **$8** [ESTIMATE] | **Grey, never white** — a black calculator on white blows the exposure and the screen goes muddy ([`LISTING_TEMPLATES.md`](LISTING_TEMPLATES.md) §7.1) |
| **Phone tripod, adjustable** | Any cheap one | **$15** [ESTIMATE] | **Mark the position with tape.** Identical framing every unit is the whole point |
| **Replacement slide cases** | Aftermarket / parted-out units | **$6 each** [DERIVED] | ~15% incidence → **$0.90/unit**. A missing case measurably reduces price and sell speed |
| **DeoxIT D5 or contact cleaner** | Small spray | **$18** [ESTIMATE] | For dirty charge ports. [`../SOURCING.md`](../SOURCING.md) §6 notes "won't charge" is *frequently just a dirty port* — this is the tool that turns a $15 buy into a $32 unit. **Good ROI on 2 saves** |
| **Compressed air** | Duster can | **$7** [ESTIMATE] | Keypad seams and ports |
| **Anti-static mat + wrist strap** | Basic ESD kit | **$20** [ESTIMATE] | Cheap insurance during battery swaps |
| **Melamine foam ("magic eraser")** | Pack | **$5** [ESTIMATE] | Case scuffs. **Never on the screen or key legends — it is a mild abrasive and will remove printing** |
| **Plastic razor blades** | Pack | **$7** [ESTIMATE] | Adhesive label residue at a shallow angle |
| **Printed quick-start cards** | Home laser/inkjet, cardstock | **$0.25/unit** [DERIVED] | Required in every box ([`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §4). Print in sheets of 4 |
| **Fireproof Li-ion storage bag** | Small | **$12** [ESTIMATE] | For pulled and swollen cells awaiting recycling. See §4.2 |

**NICE-TO-HAVE one-time subtotal: ≈ $132.** **[ESTIMATE]**

### 2.3 Label printing — worth it, at the top of this tier

| Item | Est. cost | Verdict |
|---|---:|---|
| **Thermal label printer** — Rollo / MUNBYN / Brother QL-1100 | **$100–$180** [ESTIMATE] | **Direct thermal: no ink, ever.** That is the whole appeal |
| **4×6 direct-thermal labels**, 500–1,000 | **$20** [ESTIMATE] | ~**$0.02/label** [DERIVED — matches `../UNIT_ECONOMICS.md` §4] |

**Recommendation at 30–60 units/season: buy it in season two, not season one.**

The honest arithmetic: a printer saves roughly 60–90 seconds per parcel over taping a paper label,
plus the ink and the trimming. At 60 units that is **60–90 minutes saved for ~$120** — about
$80–$120/hour of saved time, which looks great until you notice it is 60 minutes across a whole
season and you have not yet proven the business works. **[ESTIMATE]**

**Buy it immediately if** you already print shipping labels for anything else, or if the launch test
comes back "keep loading" and you commit to a second season. It is genuinely one of the better
quality-of-life purchases in reselling — just not on day one, before the A/B test has told you
whether there is a day two.

### 2.4 SKIP — not worth it at this scale

| Item | Why not |
|---|---|
| **Ultrasonic cleaner** | Tempting and wrong. You cannot submerge a calculator with a Li-ion cell and an LCD in it, and there is nothing else to clean. IPA and a swab is the correct tool |
| **Hot-air rework / soldering station** | There is **no repair path**: TI and the aftermarket sell no CE screens, faceplates, keys, or key membranes ([`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) §3.3). You cannot fix what you cannot get parts for |
| **Second computer / dedicated bench PC** | One Windows machine runs TI Connect CE fine |
| **Barcode scanner / inventory gun** | 24 units. Type the serial |
| **Vacuum sealer, shrink wrap** | Reads as counterfeit "renewed" packaging on a used private-seller listing. Actively bad |
| **Branded boxes / custom mailers** | Real money for zero conversion at this volume. Revisit past ~200 units/yr |
| **TI-SmartView CE emulator** | Paid. **CEmu is free, open-source and more capable** (<https://www.cemetech.net>) — and you have real hardware anyway |
| **TI wall adapters** | **[`../PREP_SOP.md`](../PREP_SOP.md) §9: never ship a random third-party wall wart.** TI voids warranty on non-approved adapters and a bad one can damage a unit. Ship the cable; tell the buyer to use their phone charger |
| **A TI-84 Evo, as inventory** | **[`../SOURCING.md`](../SOURCING.md) §5: do not buy Evo units for this line.** But see §7 — one, as R&D, is a different question |

---

## 3. Cables — the trap that will cost you an hour

**Some cheap Mini-B cables are charge-only.** They have the power pins wired and the data pins
absent. The calculator charges perfectly, the LED behaves, and TI Connect CE never sees the device.
You will blame the driver, the port, the OS, and the calculator before you blame the cable.

**This matters more here than in most projects** because the entire workflow — the OS+Apps flash, the
program load, the exam-mode clear — is *data*. A charge-only cable makes every one of the five
checklist steps impossible while looking like it works.

### How to avoid it

| Do | Don't |
|---|---|
| Buy cables described as **"data and sync"** or **"data transfer"** | Buy anything sold as "charging cable" or "charger cord" |
| Prefer a **brand with a spec sheet** — Monoprice, Amazon Basics, StarTech, Tripp Lite | Buy the cheapest 10-pack on AliExpress for a bench you depend on |
| Buy from a listing that mentions **USB 2.0 480 Mbps** | Trust a cable that came free with something else |
| **Test each cable once, label the good ones**, and keep them separate from the ones that ship in boxes | Mix bench cables and outbound cables in one drawer |

### The 30-second incoming test

```
1. Connect a known-good calculator with the cable.
2. Open TI Connect CE. Does the unit appear in Connected Calculators?
   YES -> data-capable. Mark the connector shell with a paint pen or tape flag.
   NO  -> charge-only, or faulty. Bin it. Do not put it back in the drawer.
3. Do this for EVERY cable on arrival, before a batch, not during one.
```

**Buy 8 for a 6-slot bench.** Cables are the cheapest thing here and the most annoying failure.

### And the Evo cable, if you buy one

The **TI-84 Evo uses USB-C**, and it **does not use TI Connect CE** — it connects through a web tool
at `connectevo.ti.com`. **[RESEARCHED — [`../SOURCING.md`](../SOURCING.md) §0]** So an Evo needs a
data-capable **USB-C** cable (**$8** [ESTIMATE]) and a completely separate workflow. Nothing on the
CE bench transfers.

---

## 4. Batteries, and how to actually judge battery health

### 4.1 The part

| | |
|---|---|
| **Part number** | **`3.7L1200SPB`** — 3.7 V, 1200 mAh Li-ion **[RESEARCHED]** |
| Older revision | `3.7L1200SPA` — generally treated as compatible. **Buy the SPB** |
| Cost | **~$8/cell** [ESTIMATE]; buy in 5–10 packs |
| Incidence | **~20% of units** [ESTIMATE] → **$1.60/unit** in the cost stack [DERIVED] |
| Where | Amazon, eBay, TI parts dealers |

**On counterfeits and aftermarket cells — an honest [ESTIMATE], not a researched finding.** Generic
"1200 mAh" cells at $3–4 are common and are frequently under-capacity. The failure mode is
particularly bad for you: the unit charges, powers on, passes a quick bench check, and then fails the
buyer's real-world week — which surfaces as a not-as-described case 20 days after delivery, when it
costs you roughly $95 ([`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §6). **Pay the $8.
The $4 saving is not worth a third of an INAD.**

And note the claim value: *"New battery installed"* is one of the few statements that genuinely moves
price on a used calculator ([`../PREP_SOP.md`](../PREP_SOP.md) §7). Only make it when it's true — and
per [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §2.1 it must be true of **both arms of a pair or
neither.**

### 4.2 Judging battery health — the practical tests

The CE does not report a percentage or a cycle count. You get a four-segment battery icon and
behaviour. So health is assessed **behaviourally**, and the SOP's method is the right one:

| Test | Method | Fail → replace |
|---|---|---|
| **Overnight hold** — the primary test | Charge to full, unplug, leave on the shelf overnight, check in the morning | Icon down more than one segment overnight |
| **Idle drain** | From full, leave screen-on idle ~30–60 min | **Drops from full to under ~75% in an hour of idle** ([`../PREP_SOP.md`](../PREP_SOP.md) §2.6) |
| **Charge time** | Full charge from flat should take **4–6 hours** (TI's own charging FAQ) | Reaches "full" in well under an hour — a shot cell charges fast because it holds almost nothing |
| **Second hold, day of shipping** | Re-check the morning it ships ([`../PREP_SOP.md`](../PREP_SOP.md) §6b) | Any drop |
| **Swelling — physical** | Back cover no longer sits flush; faceplate slightly bowed; unit rocks on a flat surface instead of sitting flat | **Swollen cell** |

**The swelling rule, which is a grading rule not a repair rule:** a swollen cell is *replaceable*, but
a swell that has **deformed the housing** means the housing is done too — and there are no
replacement housings ([`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md) §3.3). **Reject at intake**
([`../PREP_SOP.md`](../PREP_SOP.md) §2.5), don't try to save it.

### 4.3 Safe handling and disposal

- **Never ship a swollen cell**, in a unit or loose. Never put a lithium cell in household waste
  ([`../PREP_SOP.md`](../PREP_SOP.md) §7.5).
- Disconnect at the **connector**, with a plastic spudger. Never pull the wires. Never pierce or bend
  a cell.
- Store pulled cells in a **fireproof bag** (§2.2) away from anything flammable, and take them to a
  battery recycling point — Home Depot, Lowe's, Best Buy, and Staples run drop-offs, as do most
  municipal hazardous-waste days.
- **Tape the terminals** of loose cells before storing them together.

### 4.4 The one-way door: check the OS version before you flash

Not a bench item, but it belongs next to the bench because it is irreversible.

**Units running OS 5.5 or older retain the ASM/C program capability TI removed in 5.6**, and are
specifically sought by the calculator homebrew community. Those units can be worth **more left
alone**, sold as-is with the OS version stated prominently. **[RESEARCHED —
[`../PREP_SOP.md`](../PREP_SOP.md) §4b]** TI does not support downgrading, so flashing is a one-way
door.

**So: read `[2nd]` `[MEM]` `1:About` and write the version down before you connect anything.** It
costs nothing and it is rare — but it is free money when it happens, and unrecoverable when you miss
it.

> **Tape this to the bench:** an **All-Memory reset deletes the Python App itself** (it is a Flash
> App). A wiped unit boots, looks completely normal, and has **no Python** until you send the
> **OS *and Apps* bundle** — not the OS-only file.
> ([`../PREP_SOP.md`](../PREP_SOP.md) §0.) This is the single easiest way to ship a broken product.

---

## 5. Packaging and shipping — the sub-pound rule is worth ~$1.50/unit

| Item | Spec | Cost | Basis |
|---|---|---:|---|
| **Bubble mailer** | **#1, 7.25 × 12 in**, self-sealing kraft | **$0.14–$0.36** | [RESEARCHED] |
| **Stiffener** | Corrugated, cut to the calculator's footprint | **$0.00** | Cut from inbound boxes |
| Tape | 2 in packing | $0.03 | [DERIVED] |
| Label | Thermal, or paper + tape | $0.02 | [DERIVED] |
| Quick-start card | Cardstock, both sides | $0.25 | [DERIVED] |
| **Materials subtotal per unit** | incl. cable, battery reserve, case reserve, cleaning | **$5.15** | [DERIVED — `../UNIT_ECONOMICS.md` §4] |
| **Shipping label** | USPS Ground Advantage, 12 oz, eBay Labels | **$5.50** blended | [ESTIMATE, $4.50–$7.00 by zone] |

### Why the mailer, not a box

A bare CE is **7.59 × 3.42 × 0.8 in, 0.44 lb**. Packed in a mailer with cable, case and cards it
lands at **9–12 oz**. In a 9×5×3 box it lands at 12–15 oz and **risks crossing 1 lb**, which is a
real price break. **[RESEARCHED — [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §4]**

**The stiffener is what makes the mailer safe, and it is free.** A calculator in a bare mailer will
eventually arrive with a cracked screen — and a cracked screen is unrepairable, so that is a total
loss plus an INAD. A calculator sandwiched between the bubble layer and a piece of corrugated cut to
its footprint will not. **Cut them in batches of 20 while you wait for an OS flash.**

### Weigh every single parcel

**Mercari rounds *up* to the tier ceiling — a 12.1 oz package pays the 1 lb rate**
(8 oz $5.66 / 12 oz $6.73 / 1 lb $7.48, Best Rate effective 2026-01-20). **[RESEARCHED]** eBay's
tiered structure survives for the continental US, so the cheap 8 oz and 12 oz tiers are still
available there. An $18 scale pays for itself in about 15 parcels.

**Always buy the label through the platform.** eBay's Seller Protection covers item-not-received on
orders up to $750 *without you refunding*, and removes the defect and the negative feedback — but
only on platform-purchased labels. **[RESEARCHED —
[`../LISTING_AND_SUPPORT.md`](../LISTING_AND_SUPPORT.md) §6]** A dollar saved at a third-party label
service is not worth forfeiting that on an $88 item.

---

## 6. Totals

### 6.1 One-time equipment

| Tier | Subtotal |
|---:|---:|
| ESSENTIAL (§2.1) | **$155** |
| \+ NICE-TO-HAVE (§2.2) | $132 → **$287** |
| \+ Label printing (§2.3) | $120 → **$407** |

**[ESTIMATE]**, pending the §0 TODO.

### 6.2 Startup cost for the 24-unit launch batch

| Line | Essential bench | Full bench |
|---|---:|---:|
| One-time equipment | $155 | $407 |
| Consumables, 24 units @ $5.15 | $124 | $124 |
| **Bench total** | **$279** | **$531** |
| Inventory, 24 units @ $30–$40 | $720 – $960 | $720 – $960 |
| **All-in capital at risk** | **$999 – $1,239** | **$1,251 – $1,491** |

**Sanity check against the model.** [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §4 budgets **~$140**
one-time and **$5.15/unit**. The essential bench at $155 is within 11% of that, so the P&L in that
document stands. **The full bench at $407 does not break the model either** — it amortises to
$6.78/unit over 60 units — **but it is $250 spent before you have sold one calculator, on a business
whose central premise is explicitly unproven.** Buy §1 now, §2.1 as you need it, and revisit §2.2–2.3
after the A/B test decides ([`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §7).

### 6.3 What the bench does not fix

At $30 acquisition and an $88 sale you net **$27.99/unit**. At $45 acquisition, **$12.99**.
**[RESEARCHED — [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §7]** That $15 swing in what you pay
for a calculator is larger than the entire nice-to-have tier of this bench, per six units. **Spend
your attention on §6–§7 of [`SOURCING_SHORTLIST.md`](SOURCING_SHORTLIST.md), not on the bench.**

---

## 7. Throughput — what this setup actually supports

### 7.1 The SOP's numbers

[`../PREP_SOP.md`](../PREP_SOP.md) §10: **~50 min/unit single, ~38 min/unit at a batch of six.** All
**[ESTIMATE]** — the SOP says so, and says to replace them with real stopwatch numbers after ten
units. Do that.

| Step | Single | Batch of 6 | Parallelises? |
|---|---:|---:|---|
| Intake, triage, serial, photos-as-received | 4 | 3 | Partly |
| Wipe | 3 | 2 | ✅ |
| Exam-mode clear (~30% of units) | 2 | 1 | ✅ one click for the whole batch |
| **OS + Apps bundle** | 6 | **2** | ✅ **the biggest batching win** |
| Press-to-Test verify + clean-screen photo | 2 | 2 | ✗ |
| Load programs | 5 | 4 | Partly |
| **Verify programs + hardware** | **8** | **8** | ❌ **the bottleneck** |
| Clean and grade | 6 | 5 | Partly |
| Battery swap (~20%) | 10 | 10 | ✗ |
| Listing photos | 6 | 4 | ✅ one session |
| Write/clone listing, publish | 5 | 3 | ✅ clone |
| Pack and label | 5 | 4 | Partly |
| **Weighted total** | **~50** | **~38** | |

### 7.2 What the bench items buy you, specifically

| Kit | Enables | Minutes saved/unit |
|---|---|---:|
| **Powered 7–10 port hub** | 6 units charging and flashing at once — collapses OS+Apps from 6 min to 2 | **~4** |
| **6–8 tested data cables** | No cable-swapping between slots, no charge-only mystery | **~1–2** |
| **Light tent + fixed tripod** | One photo session for the batch instead of per-unit setup | **~2** |
| **Known-answer card at the bench** | Program verification is a *glance*, not a calculation ([`../PREP_SOP.md`](../PREP_SOP.md) §6a) | **~2–3** |
| **Scale** | No re-weighing, no Mercari tier surprises | ~0.5 |

**Roughly the whole 50 → 38 min gap is the hub, the cables, the light tent and the verification card.
That is about $80 of the essential bench, and it is worth $14/hr of effective rate**
([`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §8: 53 → 36 min/unit moves you from ~$32/hr to
~$47/hr). **[DERIVED]**

### 7.3 Realistic session throughput

| Session | Units | Hours | At |
|---|---:|---:|---|
| One evening | 4–5 | ~3 | 38 min/unit |
| One Saturday | 8–10 | ~6 | 38 min/unit |
| **A 24-unit launch batch** | 24 | **~15 h** | 4 batches of 6, plus ~$124 consumables |
| Adding sourcing + post-sale (SOP §10 → 53 min all-in) | 24 | **~21 h** | The honest number |

**Verification does not parallelise, and it is 8 of the 38 minutes.** Launching 10 programs on 6 units
is 60 sequential launches. **[`../PREP_SOP.md`](../PREP_SOP.md) §6 is right that this is the step most
tempting to skip and the one you must not** — a dead program on a "pre-loaded" calculator is a
guaranteed return plus a bad review, and it costs more than the unit's entire margin.

**Two practical consequences:**

1. **A batch of six is the right size.** Bigger batches don't improve the bottleneck and they do
   increase the chance of mixing up which unit got which loadout — which, during the A/B test, is a
   ruined pair.
2. **Bare-arm units are ~9 minutes faster** (no load, no program verification —
   [`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §6 puts the loading delta at ~11 min). So a mixed
   A/B batch of 3 loaded + 3 bare runs a little quicker than 6 loaded. Do **not** let that tempt you
   into skipping any hardware check on the bare arm —
   [`AB_TEST_PROTOCOL.md`](AB_TEST_PROTOCOL.md) §3.2: **bare does not mean unprepared**, or you are
   testing refurbishment instead of software.

### 7.4 The Evo R&D unit — the highest-value ~$160 available, but not in week 1

Not bench kit, but it belongs in a spending plan.
[`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §10.5 calls it *"the highest-value $160 you can spend
on this business"*, and that is right.

> **Correction to an earlier version of this section.** It said "whether the `.8xv` programs run on
> the Evo is **[UNVERIFIED]** and it determines whether this product line has a two-season runway or
> a future." **Both halves of that are wrong**, and
> [`../EVO_TRANSITION.md`](../EVO_TRANSITION.md) is the better-sourced document on it:
>
> - **The `.8xv` AppVars definitively do not run on an Evo. [RESEARCHED]** Python AppVars there are
>   `.8xv2` and the format is *"entirely new & non-backwards compatible"* (TI KB 29430, TI-Toolkit).
>   That is settled, not unverified. The genuinely open question is whether the **`.py` sources**
>   transfer — and the evidence says they very probably do, unchanged, because TI Connect Evo
>   auto-converts `.py` on send ([`../SOURCING.md`](../SOURCING.md) §0).
> - **The CE Python line does not have a two-season runway.** Five production years at TI-84 scale
>   keeps the installed base viable **into roughly 2029–2030**
>   ([`../EVO_TRANSITION.md`](../EVO_TRANSITION.md) Q4).

**Sequencing, restated honestly.** The older docs say *buy one now*
([`../SOURCING.md`](../SOURCING.md) §0 point 4, [`../README.md`](../README.md)); this folder said
*wait for the A/B result*. **The conditional framing was the weaker argument** — the Evo unit is
justified by the digital line on its own, and the digital line is where
[`../UNIT_ECONOMICS.md`](../UNIT_ECONOMICS.md) §10 says the money is, so a "stop loading" verdict
would not moot it.

**What survives is a cash-timing point, and it is a good one:** week 1 is a **~$380** budget and $160
of Evo is 42% of it, spent on a question that has no bearing on whether you can ship a CE Python. So
**buy the Evo when cash allows — after the pilot pairs ship, not before them** — and do not let this
section be read as a reason to skip it.

It needs its own USB-C cable and the `connectevo.ti.com` web tool, so budget **$140–$170** all in and
expect **none** of the CE workflow to transfer.

---

## 8. Bench setup checklist

```
=== BEFORE UNIT 1 ===
[ ] TI Connect CE installed BEFORE first connecting a calculator (drivers)
[ ] Current OS + APPS bundle (.b84) downloaded - the BUNDLE, not the OS-only file
[ ] Version verified at education.ti.com (5.8.5 or later)
[ ] Every cable tested for DATA, not just charge, and the good ones marked
[ ] Powered hub on its own wall PSU, not bus-powered
[ ] 8xv/ payload folder organised by loadout; sizes re-measured
    (AB_TEST_PROTOCOL.md 3.4 - total must be <= 34,816 B)
[ ] Known-answer verification card PRINTED and taped to the bench
    (LISTING_TEMPLATES.md 7.2)
[ ] Photo station built, tripod position taped, grey backdrop up
[ ] Scale zeroed
[ ] Reject criteria from PREP_SOP.md 2.5 printed and visible
[ ] Walk-away price table from SOURCING_SHORTLIST.md 6.1 taped to the monitor

=== TAPE THESE TWO WARNINGS TO THE WALL ===
[ ] "All-Memory reset DELETES the Python App. Send the OS *AND APPS* bundle."
[ ] "NEVER enter Press-to-Test after programs are loaded. SOP 4c is the last
     moment exam mode is safe."

=== PER BATCH OF 6 ===
[ ] Read 1:About and record the OS version BEFORE flashing (5.5-or-older check)
[ ] All 6 on the hub overnight before the batch starts
[ ] Steps in SOP order: wipe -> exam clear -> OS+Apps -> programs -> verify
[ ] Every program launched with its known-answer input, on every unit
[ ] Every parcel weighed, target 9-12 oz
[ ] Labels bought through the platform, never a third party

=== RESTOCK TRIGGERS ===
[ ] Mailers below 20     [ ] Outbound cables below 6
[ ] Batteries below 2     [ ] IPA below 1/4 bottle
[ ] Cards below 10        [ ] Labels below 50
```

---

AP®, SAT®, and ACT® are trademarks registered by their respective owners, none of which are
affiliated with, or endorse, this product. TI-84 Plus CE Python™, TI Connect™ CE, and Texas
Instruments® are trademarks of Texas Instruments Incorporated, which is not affiliated with, and does
not endorse, this product. All trademarks are the property of their respective owners. Nothing in
this document is legal, safety, or electrical-engineering advice; handle lithium cells at your own
risk and dispose of them lawfully.
