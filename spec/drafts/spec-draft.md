# Hitch v4 Spec Draft

## Working Goal
- Faithfully preserve the current Hitch core product identity and demo UX
- Extend Hitch beyond onboarding into ongoing relationship maintenance
- Add relationship-specific memory and wiki accumulation
- Support recurring check-ins rather than only cold-start quiz usage
- Keep the result compatible with future graph visualization of relationship memory

## Agreed Direction So Far
- v4 is not just a cold-start onboarding reconstruction
- v4 should preserve main Hitch identity and core UX philosophy
- v4 should also extend into ongoing relationship memory behavior
- v4 should include a recurring relationship check ritual
- inspiration from SumOne is valid: one recurring relationship question/check that deepens mutual understanding over time
- Hitch should go beyond simple question logging by interpreting, summarizing, and coaching from accumulated answers

## Relationship Seeds
### Girlfriend
- described as a fairly typical INFJ
- tends to respond well to words and acts of service
- likely relevant love-language tendencies:
  - words of affirmation
  - acts of service

### Mother
- described as ESTJ-like
- tends to respond more to material/practical gestures and problem solving
- likely relevant love-language tendencies:
  - receiving gifts or materially legible care
  - practical problem solving / acts of service

## Product Shift in v4
Current Hitch versions focus heavily on:
- onboarding
- short demo quiz
- reveal
- loved-moment capture
- one-shot coaching

v4 should shift the center of gravity toward:
- post-onboarding recurring use
- relationship-specific check-ins
- memory accumulation
- wiki updates
- graph-ready structure
- long-term coaching relevance

## Candidate Core Loop
1. user selects or enters a relationship context
   - girlfriend
   - mother
   - potentially more later
2. Hitch performs a recurring check-in
   - daily or biweekly cadence to be decided
3. user answers a lightweight prompt or relationship question
4. Hitch stores the raw interaction
5. Hitch updates a structured relationship wiki summary
6. Hitch may return a short reflective coaching response
7. repeated check-ins accumulate into long-term relationship knowledge

## SumOne Influence
- daily or recurring relationship question ritual is desirable
- lightweight repeated prompts can build intimacy and memory over time
- however Hitch must go beyond record-keeping
- Hitch should interpret patterns and translate them into coaching and relationship understanding

## Memory / Wiki Direction
v4 should move closer to the original long-term Hitch memory idea:
- private raw input layer
- relationship-level structured state
- wiki-like long-term summary layer
- graph-ready references between people, relationships, episodes, patterns, and interventions

## Graph Direction
The stored wiki/memory should later be visualizable as a graph.
This suggests future nodes such as:
- person
- relationship
- episode
- preference
- mismatch pattern
- successful repair behavior
- recurring need
- coaching suggestion

The storage structure should be designed so later graph visualization is straightforward.

## Open Questions
- daily question vs biweekly check as the primary cadence
- how much of the original onboarding should remain prominent in v4
- whether relationship selection is explicit or inferred
- whether each relationship has separate quiz state or a shared self-model + relationship-specific deltas
- how much coaching should be returned every check-in vs only on larger summaries


## Check-in Cadence Decision
- both rhythms should exist
- lightweight daily question ritual
- deeper biweekly relationship check

### Daily Layer
- one lightweight relationship-oriented question per day is desirable
- this supports low-friction accumulation of relationship memory
- it should feel easy enough to answer without emotional overhead every time
- this layer is partly inspired by SumOne-style question rituals

### Biweekly Layer
- every two weeks, Hitch should run a deeper relationship check
- this should feel closer to a structured reflection / synthesis checkpoint
- the biweekly check should draw on the prior daily answers and other accumulated signals
- this is the natural place for deeper interpretation, relationship state updates, and more explicit coaching

## Conversational Access Requirement
- the user should be able to message Hitch at any time and ask about their relationship
- this should not be restricted to scheduled prompts only
- Hitch should be able to answer ongoing questions about the relationship using accumulated memory/wiki

However:
- this should become meaningfully useful only after ambiguity about the relationship has been reduced enough
- early in a relationship context, Hitch may need more information before giving high-confidence relationship reasoning
- therefore Hitch should be able to distinguish between low-context, medium-context, and high-context relationship states

## Ongoing Interview Framing
- the daily question ritual + biweekly deeper check effectively act like an ongoing Ouroboros-style deep interview for the relationship
- instead of one fixed intake interview only, relationship understanding should be accumulated over time
- Hitch is not just collecting logs; it is progressively lowering ambiguity about the people and the relationship
- over time, the relationship model should become more specific, more personalized, and more useful for future coaching and answers

## Emerging Product Principle
- Hitch should behave like a relationship understanding system, not just a quiz bot
- scheduled prompts help memory accumulate
- open conversational access lets the user ask for help anytime
- the combination of daily signals, deeper periodic synthesis, and open-ended questions is what makes the wiki layer useful


## Relationship Selection Decision
- relationship selection should be explicit
- the user should choose the relationship context during onboarding
- initial relationship options may include:
  - girlfriend / partner
  - mother
  - potentially others later

This is preferred over silent inference because:
- it reduces ambiguity early
- it lets memory/wiki attach to the correct relationship from the beginning
- it supports stronger long-term relationship-specific summaries

Natural inference inside later conversation can still be helpful, but the primary entry model should be explicit selection during onboarding.

## Next Deep-Dive Area
- onboarding now needs a deeper pass
- onboarding must not only introduce Hitch as a relationship coach
- it must also introduce the idea that the user is choosing which relationship Hitch is helping with
- onboarding likely needs to transition from cold-start identity explanation into relationship-context selection


## Onboarding Structure Direction
- onboarding should be relatively deep, not ultra-short
- a richer onboarding is acceptable if it increases product understanding and emotional buy-in
- the goal is not only to introduce a bot, but to frame a long-term relationship understanding system

### Onboarding Goals
The onboarding should establish:
1. what Hitch is
2. why relationships drift even when love exists
3. why understanding love-language differences matters
4. why repeated questions/check-ins help uncover unconscious relational patterns
5. what the user can expect from using Hitch over time

### Onboarding Length
- 4 to 5 short messages is acceptable
- each message should still be readable and not feel like a wall of text
- depth is preferred over overly compressed onboarding, as long as cadence stays humane

### Onboarding Sequence (Current Draft)
1. introduce Hitch as a relationship coach
2. explain that love can exist without landing well
3. explain that different people receive love differently
4. explain that repeated questions/check-ins reveal hidden patterns and can help fill each other's love tank
5. transition into relationship selection and setup

## Love Language Test CTA Clarification
- "간단하게 알아보기" and "깊게 알아보기" are explicit CTA options for the love-language test mode
- this is not a general product mode selection, but a decision about how much love-language profiling to do at onboarding time
- simple mode should be around 5 questions
- deep mode should be the much longer full version
- this CTA should appear after the user understands why Hitch is asking these questions


## Relationship Follow-up Question Tone
- after explicit relationship selection, follow-up questions should stay natural and product-like
- rather than overly clinical phrasing, UX writing should feel simple and warm
- for early emotional state capture, a preferred prompt is effectively:
  - "지금 서로의 관계가 어떤가요?"
- this should be treated as a lightweight relationship-state prompt, not a heavy therapy intake question

## Tone and Manner Constraint
- Hitch tone and manner must be preserved across the entire product
- this is a very important instruction-level rule
- when ambiguity appears, preserving Hitch tone is part of correctness, not a cosmetic detail

Tone qualities to preserve:
- warm
- product-like
- emotionally legible
- not stiff
- not overly corporate
- not overly therapeutic
- not generic chatbot language

## Language Rule
- Korean is preferred by default
- however, if an English product/system term is clearly more direct and intuitive, it can be used as-is
- there is no need to awkwardly over-translate terms that are already clearer in English
- for example, terms like system may remain system if that is the clearest and most natural option in context


## Daily Question Delivery Model
- long-term direction is bidirectional usage, where the partner also receives prompts
- however v4 should first implement a single-user version that simulates a future bidirectional system
- the internal product model should still assume that relationships are inherently two-sided

## Partner Invitation During Onboarding
- onboarding should include a way to invite or later share the experience with the partner
- candidate invitation mechanisms may include:
  - QR code
  - bot link
  - bot handle or invite code
- this should feel like a natural extension: "if you want, invite the other person too"
- however v4 does not need true multi-user completion yet; a mock/simulated single-user mode is acceptable as the first implementation

## Mock Bypass / Easter Egg
- if the user proceeds without full partner participation, v4 may continue in a mock-driven mode
- there can be an internal or quiet bypass that effectively says: if the user just moves forward, the system starts in simulated/mock mode
- this should not dominate the primary UX, but it is acceptable as a practical easter egg for testing/demo usage

## Daily Question Time Preference
- instead of hardcoding a universal 10 PM schedule, onboarding should ask the user when they want to receive the daily question
- this makes the ritual feel more personal and more usable
- an initial default can still exist, but user preference should be captured during onboarding if possible


## Love Language Model Decision
- v4 should use a shared core self-model plus relationship-specific deltas
- the user is not treated as a completely different person in every relationship
- however, the way needs surface and the way love lands can vary by relationship context

### Core Self-Model
- Hitch should maintain a baseline understanding of the user's general love-language tendencies
- this core model can be informed by the simple or deep love-language test taken during onboarding

### Relationship-Specific Delta Model
- each relationship should be able to add contextual differences on top of the core self-model
- for example:
  - with a romantic partner, affirmation and tenderness may surface differently
  - with a mother, practical support or material care may dominate the relevant translation layer

This allows Hitch to say, in effect:
- "your general model looks like X"
- "but in this specific relationship, the active mismatch and active need look like Y"

### Why This Matters
- it preserves continuity of identity
- it still respects that relationships activate different emotional and behavioral patterns
- it makes the wiki/memory system more realistic and more graphable


## Daily Question Category Direction
Current agreed daily-question categories are:
1. reflection questions
2. inference questions
3. action questions
4. understanding questions

These should be mixed dynamically based on relationship stage, recent answers, and ambiguity level.

## Playful / Scenario-Based Question Layer
- add a fifth category: playful scenario simulation questions
- these are light, imaginative, or slightly witty prompts that still reveal relationship patterns
- examples of the spirit (not fixed wording):
  - if the two of you were stranded on a deserted island, what would each of you bring first and why?
  - if you had one completely free day together, how would each of you want to spend it?
  - if one of you had a terrible week, what would comfort ideally look like?

### Why This Matters
This category is useful because:
- it lowers pressure compared with direct emotional interrogation
- it can reveal preferences, comfort styles, hidden expectations, humor, and mismatch indirectly
- it makes the product feel more alive and less clinical
- it helps gather relational signal even when the user does not want to answer a heavy reflective prompt that day

### Product Framing
These questions should not feel random for randomness' sake.
They should be framed as a natural, playful way to understand:
- what each person values
- what kind of care lands well
- what kind of comfort, fun, or safety each person imagines
- where subtle mismatch may exist

### Design Rule
- the playful layer should enrich the system, not cheapen it
- the tone can have wit, but it should still feel like Hitch
- the goal is still relational understanding, not party-game trivia


## Daily Question Answer Depth Decision
- daily answers should not stay too shallow by default
- information density matters because the long-term wiki depends on enough signal being captured
- therefore the system should gently push for a minimum meaningful answer depth rather than fully accepting ultra-thin replies as the norm

### Expected Answer Behavior
- short answers may be accepted technically, but the product should encourage fuller answers
- if the user gives something too thin, Hitch should prompt for one more clarifying sentence or reflection
- the goal is not verbosity for its own sake, but enough substance for useful interpretation and memory accumulation

### Product Reason
This matters because:
- weak daily inputs make the wiki too vague
- vague wiki state lowers coaching quality
- stronger answer depth improves pattern detection, relationship understanding, and graph usefulness over time


## Daily Question Response Style Decision
- after a daily question answer, Hitch should usually respond with a short interpretive reflection
- not just acknowledgement
- not usually a concrete action prescription every day

### Preferred Response Style
- a short reading of what the answer may signal
- for example, a small interpretation of:
  - what kind of care landed
  - what kind of reassurance mattered
  - what kind of hidden expectation may be present

### Why This Style Wins
- pure acknowledgement is too thin and does not fully use the system's interpretive value
- daily concrete action coaching may feel too heavy if done every time
- a short interpretive reflection gives the user immediate value while keeping the rhythm sustainable


## Weekly Deep Check Decision
- the deeper recurring check should move from biweekly to weekly
- weekly is a better rhythm for relationship tracking, continuity, and usable reporting
- this deeper check should be semi-structured rather than fully freeform or fully rigid

### Weekly Core Questions (Current Direction)
The weekly check should currently anchor around questions like:
1. what did you do this week to express love?
2. when did you feel the most loved this week?

These questions matter because they naturally capture both sides:
- outgoing expression
- incoming experience

### Why Weekly Wins
- biweekly may feel too delayed for relationship rhythm
- weekly creates a tighter reflection loop
- weekly also makes it easier to generate a meaningful one-week relationship report

## Weekly Report Model
- after the weekly check, Hitch should generate a one-week relationship report
- this report is not just a log dump; it should act as a short synthesis of the week

### Weekly Report Purpose
The report should help surface:
- how love was expressed
- how love was actually received
- where there may have been alignment or mismatch
- what kind of emotional pattern seems to be emerging

### Structural Direction
- the weekly check remains semi-structured
- a few core questions should stay stable for comparability over time
- additional follow-up interpretation can vary depending on accumulated context and relationship stage


## Weekly Report Tone Decision
- the weekly report should use a middle tone between warm essay and cold analysis
- it should feel emotionally aware, but still clearly structured like a product summary

### Tone Characteristics
The weekly report should be:
- warm enough to feel relational
- structured enough to feel useful
- reflective without becoming melodramatic
- analytical without sounding sterile

### Why This Tone Fits
- a pure essay tone risks becoming vague or overly sentimental
- a pure analysis tone risks making the product feel emotionally dead
- the blended tone better matches Hitch's identity as a relationship understanding product


## Weekly Report Structure Decision
- the weekly report should use a relatively stable five-part structure for comparability, summary quality, and wiki ingestion

### Weekly Report Sections
1. one-line summary of the week
2. how love was expressed this week
3. when love was most strongly felt this week
4. alignment or mismatch points
5. interpretation of the week's relationship signal

### Why This Structure Works
- it is compact enough to stay readable
- it captures both action and experience
- it creates a stable rhythm for weekly comparison over time
- it is easy to map into structured memory/wiki updates later


## Weekly Focus Line Decision
- the weekly report may include a final one-line next-week focus, but only conditionally
- this should appear when the relationship signal is clear enough to support a credible recommendation
- Hitch should avoid forcing an artificial lesson every week when the signal is weak or mixed

## Weekly Gap Interpretation Direction
- a key purpose of the weekly report is to help reveal the gap between:
  - how love was intended or expressed
  - how love was actually received or felt
- in practice, the report should be able to say something like:
  - "the point where your girlfriend most strongly seems to feel loved this week was X"
  - "the likely gap is that you tried to give love through Y, but what seems to land more is X"

### Important Constraint
- this kind of interpretation should be grounded in accumulated evidence
- the interpretation should rely on:
  - the LLM wiki / accumulated relationship memory
  - that week's user answers
  - and, when available in the future, the partner-side weekly data from the other Hitch participant

### Product Value
This gap-reading layer is one of the main reasons Hitch matters:
- not just tracking events
- not just labeling love language
- but translating between intent and impact inside a specific relationship


## Weekly Gap Wording Decision
- weekly gap interpretation should usually use medium-direct wording
- if the signal is especially strong and well-supported, Hitch may use a more direct comparison between intended love and received love
- however directness should scale with evidence strength and confidence

### Preferred Default Tone
The default form should sound like:
- there seems to be a small gap between what you tried to give and what landed most strongly
- or a similarly clear but not overly absolute phrasing

### Escalation Rule
- stronger and more explicit wording is allowed only when:
  - the wiki context is sufficiently rich
  - that week's signals are consistent
  - and the interpretation is not resting on a thin guess


## Weekly Check Depth Decision
- the weekly check should use two stable core questions by default
- if needed, Hitch may ask one follow-up question
- do not expand into a long interrogation by default

### Why This Depth Works
- two fixed questions preserve rhythm and reduce friction
- one follow-up gives enough room to clarify signal when needed
- this keeps the weekly ritual sustainable while still giving enough material for synthesis


## Weekly Report Confirmation Decision
- after showing the weekly report, Hitch should ask for a light confirmation rather than simply ending or demanding a full correction pass
- this confirmation step should help calibrate the wiki without adding heavy friction

### Confirmation UX Rule
- the confirmation prompt must preserve Hitch tone and manner
- it should feel warm, natural, and product-like
- it should not sound like a cold QA survey or explicit model-evaluation form

### Purpose
- confirm whether the weekly reading broadly feels right
- use that signal to improve future relationship interpretation and wiki calibration


## Partner Answer Reveal After Daily Question
- after the user answers a daily question, Hitch should also tell the user how the partner answered the same or equivalent prompt, when that data exists
- this should help the user compare perspectives rather than answer in isolation

### Product Value
This matters because:
- relationship understanding improves when both sides become legible together
- the contrast between the user's answer and the partner's answer can reveal hidden alignment, mismatch, expectation gaps, and emotional asymmetry
- this makes the daily ritual feel more relational and less like a solo journaling exercise

### Important Constraint
- any reveal of the partner's answer should remain tone-safe and context-safe
- it should help translation and understanding, not create unnecessary defensiveness or scorekeeping
- in the single-user simulated v4 mode, this may be represented through mock/derived partner-side data until true bidirectional usage exists


## Relationship Wiki Memory Unit Decision
- the relationship wiki should use five primary memory units:
  1. person
  2. relationship
  3. episode
  4. pattern
  5. signal

### Why These Five Units Work
- person captures relatively stable traits, tendencies, and context anchors
- relationship captures the higher-level state, phase, and summary of a specific bond
- episode captures concrete events, conversations, and moments
- pattern captures repeated mismatch, need, repair, and interpretation structures
- signal captures smaller inferred meaning units extracted from daily and weekly answers

### Structural Benefit
- together these units create a bridge from raw moment -> interpreted signal -> repeated pattern -> relationship understanding
- this makes the system more graph-ready and more useful for long-term LLM wiki retrieval


## Storage Flow Decision
- relationship memory ingestion should follow this general flow:
  1. store raw answer or raw imported text
  2. extract signal units from it
  3. accumulate and update pattern candidates
  4. update episode and relationship-level summaries as needed
  5. store weekly reports as separate synthesized artifacts

### Why This Flow Works
- it preserves raw evidence
- it creates a clean interpretation layer
- it allows relationship understanding to improve gradually instead of rewriting everything from scratch each time

## Raw Ingest Scope Decision
- v4 should include raw txt intake in a limited, semi-supported way
- this is not a fully generalized KakaoTalk ingestion engine in MVP
- however the system should still assume that the user may drop rough raw text into the project and expect Hitch to help structure it

### Practical MVP Framing
- the user may paste raw chat logs as txt files
- Hitch should support human-assisted or semi-structured extraction from these files
- the system should not require perfectly formatted source material to begin producing value

## Raw Structure Ownership Decision
- the user is allowed to dump raw relationship material in rough txt form
- Hitch / Atlas should take on the responsibility of structuring, extracting, and integrating that material into the relationship wiki over time

## Repo Role Decision
- hitch-test-v4 is an independent build target
- hitch is a later migration target, not the active v4 build target right now
- v4 should first prove the product, runtime, wiki, and ingest structure on its own
- after stabilization, the validated structure/spec can later be moved into hitch


## Ops Requirement for v4
- v4 should also include an ops layer, not just product/runtime/wiki logic
- the user intends to control the Mac mini Hitch environment from a MacBook
- therefore operational guidance and remote-control assumptions should be part of the spec from the beginning

### Ops Direction
- v4 should include ops-oriented structure and documentation similar in spirit to prior Hitch test repos
- this should cover how the system is run, monitored, and recovered on the Mac mini environment
- remote operator control from the user's MacBook should be treated as a real operating assumption, not an afterthought


## Partner Answer Reveal Style Decision
- the default partner-answer reveal should be summarized rather than shown as raw verbatim text
- in special cases, Hitch may show the partner answer together with a short interpretation

### Why Summary First
- summary-first presentation is less likely to trigger defensiveness
- it preserves product tone better than blunt raw transcript exposure
- it helps the user focus on meaning, not wording-level friction

### Special-Case Expansion
- when especially useful, Hitch may pair the partner answer with a short interpretive explanation
- this should be used selectively, not as the default every time


## Daily Question Interaction Flow Decision
- the daily interaction should follow a fairly stable five-step sequence:
  1. today's question
  2. user answer
  3. Hitch short interpretation
  4. partner answer summary reveal
  5. one-line note about a small alignment or gap between the two sides

### Why This Flow Works
- it gives the user immediate reflection value
- it makes the interaction feel relational rather than solo
- it keeps the daily rhythm compact while still producing useful signal


## Relationship Scope Simplification Decision
- v4 should avoid overcomplicating multi-relationship orchestration at first
- the user's immediate real target is the romantic partner relationship
- therefore the practical first operating assumption is one active relationship context

## Hitch-Per-Relationship Model
- conceptually, each relationship should have its own Hitch context
- each Hitch context should operate independently for:
  - daily questions
  - weekly checks
  - relationship memory
  - summaries
  - interpretation flow
- however the broader wiki layer may still be connected across contexts as an LLM wiki system

### Structural Meaning
- each relationship behaves like its own operational relationship-space
- but the underlying wiki architecture can still share higher-level memory conventions, schemas, and cross-context retrieval logic
- this means operational separation with knowledge-layer connectedness


## Relationship Unit Naming Decision
- the preferred product/spec term for each relationship-specific Hitch unit is: relationship space
- this term should be used instead of instance, thread, or workspace when describing the operating unit for a specific relationship

### Meaning of Relationship Space
- a relationship space is the independent operating context for one relationship
- it owns that relationship's:
  - daily flow
  - weekly flow
  - memory accumulation
  - summaries
  - interpretation logic
- multiple relationship spaces may exist in the broader system, while the wiki layer still remains connected underneath


## Relationship Space Creation Timing Decision
- the relationship space should be created after Hitch receives a bit of basic setup information, not immediately at the first selection tap and not only after the entire love-language onboarding is finished

### Why This Timing Works
- creating it too early risks making it an empty shell
- creating it too late slows the connection between onboarding and memory structure
- a small amount of setup first gives the relationship space a more meaningful initial state


## Relationship Space Minimum Creation Set
- the minimum setup information before creating a relationship space should be:
  1. relationship type
  2. what the user calls the other person (name / label)
  3. a one-line current relationship state
  4. preferred daily question delivery time
  5. simple vs deep love-language test choice

### Why This Minimum Set Works
- it is small enough to keep onboarding moving
- it gives the relationship space enough identity and context to start meaningfully
- it links onboarding directly to scheduling, memory, and interpretation behavior


## First Daily Question Start Timing Decision
- after onboarding, the user should be able to choose whether to start the first daily question immediately or begin at the configured delivery time later

### Why This Choice Matters
- immediate start is good for demo flow, momentum, and emotional activation
- delayed start is better for ritual realism and real-life pacing
- giving the user a choice supports both product authenticity and practical demo use


## Onboarding Final CTA Direction
- the preferred onboarding-ending CTA should be closer to: "지금 바로 시작해볼까요?"
- it should feel simple, warm, and activating rather than overly explanatory or system-like

### Why This CTA Works
- it keeps momentum high at the end of onboarding
- it feels more product-native than a procedural schedule prompt
- it still leaves room for the actual choice between immediate start and later scheduled start


## Partner Invite Timing Reconsideration
- partner invite may be surfaced earlier in onboarding than previously assumed
- showing the partner-invite possibility near the front can help frame Hitch as a genuinely relational product from the beginning
- however it should still be presented lightly, not as a blocking requirement


## Onboarding Copy Ownership Decision
- detailed onboarding copy does not need to be user-micromanaged at this stage
- Atlas / Hitch can draft the onboarding copy in a tone aligned with hitch-base product identity
- the important requirement is that the copy preserve Hitch tone and manner rather than forcing the user to specify every line manually

## Partner Invite Skip Requirement
- partner invite presentation must include a visible skip / 건너뛰기 option
- the product should make it clear that solo progression is allowed
- this is important both for operator/demo use and for reducing onboarding friction


## Onboarding Ordering Revision
- in onboarding, relationship selection should come before partner invite
- this ordering makes the invite feel more concrete and relevant, because the product already knows which relationship space is being formed
- partner invite should still be optional and skippable, but it should be framed after the relationship choice rather than before it

## Pre-Visualization Structured Data Requirement
- the system needs an intermediate structured data layer that is ready for simulation and visualization before final graph rendering
- this matters especially when starting from raw text material

### Purpose of This Layer
From raw text, Hitch should be able to produce a pre-visualization data representation that can support:
- simulated relationship reasoning
- daily/weekly interpretation bootstrapping
- graph-ready visualization later

### Practical Meaning
- raw text should not jump directly into final visual output
- there should be a structured intermediate representation containing extracted people, episodes, signals, patterns, and relationship summaries
- this intermediate layer is the immediate substrate for both simulation and later visualization


## Intermediate Structured Data Decision
- before final graph visualization, Hitch should maintain an intermediate structured data layer
- this layer is for simulation, retrieval, summary generation, and graph materialization
- it is not the same thing as the final ontology view or the final visualization surface

### Minimum Intermediate Components
1. people
2. relationships
3. episodes
4. signals
5. patterns
6. weekly_reports
7. open_questions
8. confidence

## Ontology-Based Visualization Direction
- final visualization should be ontology-based rather than being a direct dump of the intermediate data schema
- schema, ontology, and visualization should be treated as related but distinct layers

## Ontology Core Node Types (v1)
1. person
2. relationship
3. episode
4. need
5. preference
6. expression
7. reception
8. mismatch
9. repair
10. question


## Ontology Edge Vocabulary Direction
- the ontology should also maintain a first-pass standard edge vocabulary rather than inventing connection labels ad hoc during implementation
- this is a v1 standardization decision, not a claim that the vocabulary can never evolve

### Core Edge Vocabulary (v1)
1. has_relationship
2. involves
3. expresses
4. receives
5. prefers
6. needs
7. contains_mismatch
8. resolved_by
9. raises
10. informs

## Ops Guidance and Review Role
- the ops layer should explicitly acknowledge that Atlas may use accumulated background understanding from prior product conversations when guiding implementation, unblocking ambiguous choices, and reviewing Codex output
- the spec does not need to be 100 percent closed before implementation begins, as long as Atlas is actively providing product-intent guidance and drift control

### Meaning of This Role
- Atlas can act as:
  - implementation guide
  - ambiguity resolver
  - drift detector
  - product-tone reviewer
- this is especially important when the implementation agent produces something plausible but subtly off-product


## Open Conversation Mode Decision
- open conversation mode should default to a relationship-aware coaching mode
- Hitch should answer with awareness of the current relationship space and wiki context when that context meaningfully improves the answer

### Important Constraint
- Hitch should not force wiki references unnaturally
- if the stored context does not add meaningful value, Hitch may simply respond more like a strong general relationship coach
- in other words, relationship awareness should be helpful, not performative


## Open Conversation Wiki Update Decision
- open-conversation exchanges should update the wiki only when they add meaningful relationship signal
- not every conversational turn should be stored as long-term structure

### Why Selective Update Wins
- always storing everything would create too much noise
- selective update preserves the quality of signals, patterns, and relationship summaries
- this keeps the wiki useful rather than bloated


## Meaningful Open Conversation Criteria
- an open-conversation exchange becomes a wiki-update candidate when at least one of the following is true:
  1. a new fact appears
  2. an existing relationship interpretation changes
  3. a repeated pattern is confirmed
  4. an important episode is recorded
  5. an unresolved question is surfaced

### Why These Criteria Matter
- they create a usable threshold for memory updates
- they help separate durable relationship signal from ordinary chat noise


## Simulated Partner Answer Source Decision
- in the current one-way v4 stage, the primary source for simulated partner answers should be raw text material
- the system should not pretend it has real partner-side daily or weekly input when it does not

### Current Source-of-Truth Rule
- raw conversation text is the strongest first-order source for partner-side simulation in v4
- wiki context may assist, but it should not replace raw textual grounding at this stage

### Future Expansion
- if true two-sided participation exists later, simulated partner reasoning can expand to include:
  - real partner daily answers
  - real partner weekly answers
  - richer accumulated wiki state


## Simulation Primary Purpose Decision
- the primary purpose of simulation is partner-perspective estimation rather than mere answer mimicry
- however the simulation layer should support multiple practical outcomes around that center

### Core Goal
- simulation should help Hitch infer how the partner may be seeing, receiving, or interpreting the relationship
- this is part of building background consciousness for the specific pair context (for example, Taeyong-Eunseo)

### Practical Uses of Simulation
The simulation layer should support:
1. partner answer reconstruction when useful
2. partner perspective estimation as the main function
3. relationship gap interpretation support
4. demo and visualization support

### Important Framing
- the real center is not theatrical imitation
- the center is building a usable, relationship-specific model of perspective that can power understanding, reporting, simulation, and visual explanation


## Simulation Output Set Decision
- the simulation layer should produce a compact but meaningful output set that supports partner modeling, gap interpretation, demo, and visualization

### Default Simulation Outputs
1. partner likely answer
2. partner likely feeling or state
3. why this likely matters to them
4. confidence or uncertainty level

### Why This Output Set Works
- it covers both surface response and underlying meaning
- it provides enough structure for relationship reasoning and visual explanation
- it avoids reducing simulation to a single fake chat reply


## Simulation Input Set Decision
- the simulation layer should take the following five input types:
  1. current question or scenario
  2. relevant raw text snippets
  3. related episodes
  4. stable patterns
  5. current relationship summary

### Why This Input Set Works
- it combines immediate prompt context with both raw evidence and higher-level interpretation
- it gives simulation enough grounding without requiring the entire corpus every time

## Time-Compression Simulation Framing
- the simulation layer can be understood as running the love-language / relationship-understanding service inside a time-compressed virtual environment
- rather than waiting for months of real interaction, Hitch uses available relationship material to approximate how the system might understand, compare, and interpret the pair over a longer arc
- this framing is especially useful for demo, bootstrapping, and visualization


## Simulation-to-Wiki Update Decision
- simulation outputs may update the wiki layer directly in v4
- this is acceptable because the environment is partly exploratory and time-compressed
- visible wiki growth is part of the intended demo value

## Demo Flow Requirement
- the product should support a flow where a Telegram-started session leads into simulation, wiki growth, and visible system evolution
- the initial user session start in Telegram should remain part of the demo story rather than being skipped over

## Private Data Boundary Decision
- girlfriend-related raw data and private wiki data must not be pushed to remote git
- private relationship material should remain local-only or otherwise excluded from remote publication

## Demo-Safe Push Decision
- if commit/push visibility is shown during demo, the pushed layer should be a sanitized demo-safe artifact layer rather than raw private relationship data
- this allows visible repository evolution without leaking sensitive personal relationship material


## Demo Value of LLM Wiki Growth
- a major part of the product and demo value is the visible growth of the LLM wiki over time
- the system should make it legible that relationship understanding is being accumulated, structured, and evolved rather than merely producing one-off chatbot replies

## Demo-Safe Artifact Scope Decision
- the product repo may include demo-safe artifacts that help show wiki growth and system structure without exposing private relationship data

### Allowed Demo-Safe Artifact Types
1. sanitized wiki snapshots
2. genericized pattern or signal files
3. graph payload samples
4. sanitized weekly report samples
5. ontology and schema examples


## Simulation Confidence Exposure Decision
- simulation confidence should usually be expressed implicitly rather than shown as an explicit score to the user
- Hitch may signal uncertainty through natural phrasing such as soft interpretive language

### Why This Works
- it preserves product tone better than explicit confidence metrics
- it reduces false authority without making the product feel technical or clinical


## Simulation Safety Rules (v1)
1. do not make strong claims without raw evidence support
2. do not present the partner's emotional state as a certainty
3. avoid overreaching relationship diagnosis from thin signal
4. do not package mock answers as if they were real partner answers
5. when signal is weak, fall back toward more general coaching rather than overconfident simulation

### Why These Rules Matter
- they reduce hallucinated certainty
- they preserve trust
- they keep simulation useful without turning it into fake authority


## Simulation Persistence Structure Decision
- simulation outputs should be stored in three related units:
  1. simulation_runs
  2. simulation_snapshots
  3. simulation_effects

### Meaning of Each Unit
- simulation_runs store the concrete question/input/output/basis/confidence of a simulation execution
- simulation_snapshots store the summarized simulation state of a relationship space at a particular moment
- simulation_effects store what changed in wiki, patterns, summaries, or reports because of the simulation

### Why This Structure Works
- it helps debugging
- it makes demo evolution more legible
- it supports visualization and downstream reasoning
