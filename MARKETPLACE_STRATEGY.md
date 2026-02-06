# Marketplace Strategy — Product Manager Skills

**Last Updated:** February 6, 2026
**Status:** Quality Audit Complete ✅ | Ready for Submission
**Next Review:** February 7, 2026

## 🚀 Next Session Action Items (Feb 7, 2026)

**Priority 1: Get GitHub Stars (SkillsMP Requirement)**
- [ ] Share repo on LinkedIn with PM network
- [ ] Post to r/ProductManagement subreddit
- [ ] Share in PM Slack communities (Lenny's, Product School, Mind the Product)
- [ ] Email to Productside client list
- **Goal:** Achieve 2+ stars for SkillsMP auto-indexing

**Priority 2: Quick Wins (Low Effort, High Visibility)**
- [ ] Fork and submit PR to [Awesome Claude Skills](https://github.com/travisvn/awesome-claude-skills)
- [ ] Join ClaudeSkills.ai waitlist
- [ ] Add GitHub topics: `product-management`, `claude-skills`, `ai-agents`, `pm-frameworks`

**Priority 3: Strategic Decisions Needed**
- [ ] Decide: Monetization approach (Free+Consulting vs. Freemium vs. PWYW)
- [ ] Decide: Submit all 34 skills to Anthropic or curate 5 "showcase" skills first?
- [ ] Review: Do any 200-char descriptions need optimization for clarity?

---

## Overview

This document outlines AI skill marketplaces where Product Manager Skills can be listed, submission requirements, and a rollout plan to maximize discoverability and adoption.

---

## ✅ Quality Audit Results (Feb 6, 2026)

**Status:** All skills pass marketplace requirements

**Validation Script:** `scripts/check-skill-metadata.py`

### What Was Checked
- ✅ **YAML Frontmatter:** All 34 skills have valid frontmatter
- ✅ **Name Field:** Present and ≤ 64 characters (all skills)
- ✅ **Description Field:** Present and ≤ 200 characters (all skills)
- ✅ **Folder Names:** Match frontmatter `name` values (all 34 skills)

### Sample Validation Results
| Skill | Name Length | Description Length | Status |
|-------|-------------|-------------------|--------|
| ai-shaped-readiness-advisor | 27 chars | 123 chars | ✅ Pass |
| prioritization-advisor | 22 chars | 200 chars | ✅ Pass (at limit) |
| user-story | 10 chars | 199 chars | ✅ Pass (at limit) |
| discovery-process | 17 chars | 200 chars | ✅ Pass (at limit) |

### Marketplace Readiness
✅ **Ready for immediate submission:**
- SkillsMP (needs 2+ GitHub stars only)
- SkillHub (ready now)
- Anthropic official skills repo (ready now)
- Awesome Claude Skills (ready now)

⚠️ **Note:** 3 skills have descriptions at exactly 200 characters. Consider slight optimization for clarity if needed.

---

## 🎯 Goals

1. **Increase discoverability** — Help PMs find these skills when searching for product management frameworks
2. **Build credibility** — Leverage marketplace validation (stars, ratings, reviews) as social proof
3. **Drive adoption** — Make it frictionless for users to install and use these skills
4. **Generate revenue** (optional) — Some marketplaces support paid skills (90% creator revenue share)
5. **Community engagement** — Gather feedback, feature requests, and contributions

---

## 🔍 Assumptions to Verify (Before Submitting)

- [ ] Confirm SkillsMP current indexing rules (stars threshold, crawl cadence)
- [ ] Confirm SkillHub submission path (auto discovery vs. curated PR)
- [ ] Confirm ClaudeSkills.ai submission flow and paid-skill policy
- [ ] Confirm Anthropic skills repo requirements (tests/examples expectations)
- [ ] Confirm each marketplace accepts CC BY-NC-SA 4.0 or requires an alternate license

---

## 🧭 Marketplace Fit Matrix (Initial)

| Marketplace | PM Audience Fit | Submission Effort | License Compatibility | Monetization Support | Expected ROI | Notes |
|-------------|-----------------|-------------------|-----------------------|----------------------|--------------|-------|
| SkillsMP | High | Low | TBD | Unknown | High | Auto indexing from GitHub; star threshold applies |
| SkillHub | Medium | Medium | TBD | Unknown | Medium | AI scoring could amplify visibility |
| ClaudeSkills.ai | Medium | Medium | TBD | Yes | Medium | Waitlist; paid skills |
| Anthropic official skills | High | Medium | TBD | No | High | Official endorsement value |
| Awesome Claude Skills | Medium | Low | N/A | No | Medium | Community discovery via GitHub |
| Agent Skills Market | TBD | TBD | TBD | Unknown | TBD | Needs research |

---

## 🏪 Available Marketplaces (2026)

### Primary Targets

#### 1. **SkillsMP** — Agent Skills Marketplace
- **URL:** https://skillsmp.com/
- **Status:** Active, 145,000+ skills indexed
- **Compatible With:** Claude Code, Codex CLI, ChatGPT
- **Pricing Model:** Free (aggregates from GitHub)
- **Submission Process:** Automatic discovery from public GitHub repos
- **Requirements:**
  - Public GitHub repository
  - Minimum 2 GitHub stars (quality filter)
  - Valid `SKILL.md` file following Anthropic open standard
  - Optional: `scripts/` and `template.md` files
- **Discovery Features:**
  - Smart search with semantic matching
  - Category filtering (Product Management, Software Engineering, etc.)
  - Quality indicators (stars, usage stats)
  - AI-powered skill recommendations

**Action Items:**
- ✅ Already meets requirements (public repo, SKILL.md format)
- ⏳ Get to 2+ GitHub stars (currently unknown)
- ⏳ Wait for automatic indexing by SkillsMP crawler
- 📋 Monitor when skills appear on platform

---

#### 2. **SkillHub** — Claude Skills & Agent Skills Marketplace
- **URL:** https://www.skillhub.club/
- **Status:** Active, 7,000+ AI-evaluated skills
- **Compatible With:** Claude, Codex, Gemini, OpenCode
- **Pricing Model:** Free (aggregates from GitHub)
- **Evaluation System:** AI rates skills on 5 dimensions:
  1. **Practicality** — Real-world usefulness
  2. **Clarity** — Documentation quality
  3. **Automation** — Efficiency gains
  4. **Quality** — Code/instruction quality
  5. **Impact** — Strategic value
- **Rating Scale:** S-rank (9.0+), A-rank, B-rank, etc.
- **Submission Process:** Appears to be automatic discovery (details unclear)
- **Requirements:**
  - Public GitHub repository
  - Valid `SKILL.md` format
  - GitHub repository: `github.com/keyuyuan/skillhub-awesome-skills` (curated list)

**Action Items:**
- 📋 Investigate submission process (contact SkillHub or check docs)
- 📋 Submit to curated `skillhub-awesome-skills` GitHub repo
- 🎯 Optimize skills for AI evaluation criteria (practicality, clarity, impact)

---

#### 3. **ClaudeSkills.ai** — The Marketplace for Claude AI Skills
- **URL:** https://claudeskills.ai/
- **Status:** Waitlist / Early Access
- **Compatible With:** Claude AI (all platforms)
- **Pricing Model:** Paid skills supported
  - Creators keep 90%
  - Payouts via Stripe Connect
- **Submission Process:** TBD (platform in development)
- **Requirements:** Unknown (likely standard SKILL.md format)

**Action Items:**
- 📋 Join waitlist at https://claudeskills.ai/
- 📋 Monitor for platform launch announcements
- 💡 Consider monetization strategy:
  - **Option A:** All skills free (maximize adoption)
  - **Option B:** Basic skills free, premium bundles paid (e.g., "AI PM Pro Pack")
  - **Option C:** Free skills + consulting/training upsell

---

#### 4. **Anthropic Official Skills Repository**
- **URL:** https://github.com/anthropics/skills
- **Status:** Active (official Anthropic repo)
- **Compatible With:** Claude Code, Claude AI
- **Pricing Model:** Free (community contributions)
- **Submission Process:** Pull request to public repo
- **Requirements:**
  - Follow Anthropic SKILL.md specification
  - Pass quality review by Anthropic maintainers
  - Include tests/examples when applicable

**Action Items:**
- 📋 Review Anthropic's contribution guidelines
- 📋 Select 3-5 "showcase" skills to submit (highest quality, most useful)
- 📋 Submit PR with selected skills
- 🎯 Goal: Get official Anthropic endorsement

**Recommended Skills to Submit:**
1. `user-story` — Fundamental, widely applicable
2. `prioritization-advisor` — Interactive, high-value
3. `discovery-process` — Complete workflow, demonstrates sophistication
4. `pol-probe-advisor` — Unique, based on Dean's proprietary framework
5. `context-engineering-advisor` — Cutting-edge, aligns with Anthropic's focus

---

### Secondary Targets

#### 5. **Agent Skills Market**
- **URL:** https://www.agentskillsmarket.space/
- **Status:** Active (#1 Agent Skills Library for Claude AI & LLMs 2025)
- **Action Items:** 📋 Research submission process

#### 6. **Awesome Claude Skills (GitHub)**
- **URL:** https://github.com/travisvn/awesome-claude-skills
- **Status:** Active (3,200+ stars)
- **Submission Process:** Pull request to add link
- **Action Items:**
  - ✅ Fork repo
  - 📋 Add Product Manager Skills to relevant category
  - 📋 Submit PR with description and link

#### 7. **ChatPRD** — AI Platform for Product Managers
- **URL:** https://www.chatprd.ai/
- **Status:** Active (popular PM-specific tool)
- **Action Items:** 📋 Explore partnership/integration opportunities

---

## 📋 Rollout Plan

### Phase 1: Preparation (Week 1)
**Goal:** Ensure skills are marketplace-ready

- [x] **Quality Audit** ✅ COMPLETE (Feb 6, 2026)
  - [x] Run `scripts/check-skill-metadata.py` on all skills — All 34 pass
  - [x] Verify all skills have proper YAML frontmatter — Validated
  - [x] Ensure `name` ≤ 64 chars, `description` ≤ 200 chars — Confirmed
  - [ ] Validate all cross-references between skills — TODO

- [ ] **Documentation Enhancement**
  - Add "Featured Skills" section to README.md
  - Create `/docs/Marketplace Listings.md` (this file)
  - Add badges to README for marketplace presence

- [ ] **GitHub Optimization**
  - Add relevant tags: `product-management`, `claude-skills`, `ai-agents`, `pm-frameworks`
  - Ensure GitHub description is compelling
  - Add social preview image (repo settings)
  - Request stars from early users/testers

- [ ] **Create Showcase Materials**
  - Record demo video (3-5 min) showing skills in action
  - Create screenshot gallery for each skill type (Component, Interactive, Workflow)
  - Write "Getting Started in 60 Seconds" guide

---

## ✅ Submission Checklist & Standard Listing Blurb

**Checklist**
- [ ] Repo URL
- [ ] One-paragraph description (PM-focused)
- [ ] Top 3 featured skills (with one-line value props)
- [ ] License statement (CC BY-NC-SA 4.0)
- [ ] Contact email
- [ ] Demo link (video or screenshots)
- [ ] Tags/keywords (product management, discovery, roadmap, PRD, metrics, GTM)

**Standard Listing Blurb (Draft)**
```md
Product Manager Skills is a curated set of 34 practical, agent-ready skills for PMs.
Use them to improve discovery, prioritization, roadmapping, and PRD quality.
All skills are open-source and structured for immediate use in Claude/Codex workflows.
```

---

### Phase 2: Primary Marketplace Submissions (Week 2)
**Goal:** Get listed on major skill marketplaces

- [ ] **SkillsMP (Automatic)**
  - Achieve 2+ GitHub stars (quality threshold)
  - Monitor for automatic indexing
  - Once indexed, optimize skill descriptions for search
  - Share SkillsMP links in README.md

- [ ] **SkillHub (Manual Submission)**
  - Contact SkillHub via https://www.skillhub.club/
  - Submit to `skillhub-awesome-skills` GitHub repo
  - Request AI evaluation
  - Track rating scores (target: S-rank or A-rank)

- [ ] **Anthropic Official Skills (Curated PR)**
  - Select 3-5 showcase skills
  - Prepare high-quality PR with:
    - Clear descriptions
    - Usage examples
    - Tests/validation
  - Submit PR and engage with maintainer feedback
  - Promote official listing in marketing materials

- [ ] **Awesome Claude Skills (Community)**
  - Fork `travisvn/awesome-claude-skills`
  - Add entry under "Product Management" category (create if needed)
  - Write compelling 2-sentence description
  - Submit PR

---

### Phase 3: Secondary Platforms & Promotion (Week 3)
**Goal:** Expand reach and build community

- [ ] **Additional Marketplaces**
  - Research and submit to Agent Skills Market
  - Join ClaudeSkills.ai waitlist
  - Explore ChatPRD partnership opportunities

- [ ] **Community Outreach**
  - Post on r/ProductManagement (Reddit)
  - Share on Product Hunt (as "launch")
  - Write LinkedIn post with demo
  - Post on X/Twitter with #ProductManagement #AI hashtags
  - Cross-post to relevant Slack/Discord communities (Lenny's, Product School, etc.)

- [ ] **Content Marketing**
  - Write Substack article: "34 AI Skills Every PM Should Have"
  - Create YouTube tutorial (or partner with PM influencer)
  - Guest post on PM blogs (Mind the Product, Product Coalition, etc.)

---

### Phase 4: Monitoring & Optimization (Ongoing)
**Goal:** Track performance and iterate

- [ ] **Analytics Tracking**
  - Set up GitHub traffic monitoring
  - Track marketplace listing views (where available)
  - Monitor stars, forks, issues, PRs
  - Survey users: "How did you discover these skills?"

- [ ] **Feedback Loop**
  - Create GitHub Discussions for Q&A
  - Set up issue templates for:
    - Bug reports
    - Feature requests
    - New skill suggestions
  - Monthly review of user feedback
  - Quarterly skill quality audit

- [ ] **Marketplace Optimization**
  - A/B test skill descriptions (if platform allows)
  - Update skills based on user feedback
  - Add new skills based on demand
  - Maintain top ratings on SkillHub (target: S-rank)

---

## 🛠️ Maintenance & Ownership

- Assign a single owner for marketplace updates and PR submissions
- Define update cadence (monthly sync, quarterly quality audit)
- Track where updates are manual vs. auto-synced
- Keep a changelog of marketplace listings and dates submitted

---

## ⚠️ Risks & Mitigations

- **License mismatch:** Some marketplaces may not accept CC BY-NC-SA  
  Mitigation: Confirm policy up front; consider dual-licensing if needed
- **Low AI evaluation scores:** Poor ratings reduce visibility  
  Mitigation: Optimize clarity, examples, and practical framing
- **Slow auto-indexing:** Discovery delays impact momentum  
  Mitigation: Reach out to maintainers and include in curated lists
- **PRs stalled in curation repos:** Review queues can be slow  
  Mitigation: Submit early and follow up politely

---

## 🎯 Success Metrics

### Quantitative
- **GitHub Stars:** Target 100+ in first 3 months
- **Marketplace Views:** Track when data available
- **Installation/Usage:** Monitor via GitHub traffic (clone/download stats)
- **Community Growth:** Contributors, issues filed, discussions started

### Qualitative
- **Ratings:** Achieve S-rank or A-rank on SkillHub
- **Official Recognition:** Get accepted into Anthropic official skills repo
- **Testimonials:** Collect user success stories
- **Media Mentions:** Coverage in PM blogs, newsletters, podcasts

---

## 💰 Monetization Strategy (Optional)

### License Compatibility Note

- CC BY-NC-SA 4.0 limits commercial use; confirm each marketplace’s paid-skill policy
- If monetization is required, consider dual-licensing or a separate paid bundle with a commercial-friendly license

### Option A: Free + Consulting (Recommended)
- All 34 skills remain **free and open-source**
- Use as lead generation for Productside consulting
- Offer paid workshops: "Mastering AI-Assisted Product Management"
- Premium support tier: $99/month (priority support, custom skill development)

### Option B: Freemium Model
- **Free Tier:** 20 core skills (user-story, positioning-statement, etc.)
- **Pro Tier:** All 34 skills + future additions ($19/month or $149/year)
- **Enterprise Tier:** Custom skills, team training, white-label ($499/month)

### Option C: Pay-What-You-Want
- All skills free by default
- "Support this project" link (GitHub Sponsors, Buy Me a Coffee)
- Suggested donation: $20 (covers cost of 1 hour consulting)

**Recommendation:** Start with Option A (Free + Consulting) to maximize adoption and brand building.

---

## 📚 Resources for Submission

### Required Files (Already Have)
- ✅ Individual `SKILL.md` files (34 skills)
- ✅ YAML frontmatter with `name`, `description`, `type`
- ✅ Templates and examples separated (recent refactor)
- ✅ Optional scripts (deterministic, documented)
- ✅ LICENSE.md (CC BY-NC-SA 4.0)
- ✅ CONTRIBUTING.md
- ✅ README.md with comprehensive catalog

### Optional Enhancements
- 📋 Demo videos (Loom or YouTube)
- 📋 Social preview image (1200x630px)
- 📋 Skill showcase page (GitHub Pages)
- 📋 Badge system (e.g., "Featured on SkillHub")

---

## 🔗 References

### Marketplace Research
- [SkillsMP — Agent Skills Marketplace](https://skillsmp.com/)
- [SkillHub — Claude Skills Marketplace](https://www.skillhub.club/)
- [ClaudeSkills.ai](https://claudeskills.ai/)
- [Anthropic Official Skills Repository](https://github.com/anthropics/skills)
- [Awesome Claude Skills](https://github.com/travisvn/awesome-claude-skills)
- [SkillsMP Complete Guide 2026](https://smartscope.blog/en/blog/skillsmp-marketplace-guide/)
- [Claude Code Has a Skills Marketplace Now](https://medium.com/@markchen69/claude-code-has-a-skills-marketplace-now-a-beginner-friendly-walkthrough-8adeb67cdc89)

### PM Tools & Marketplaces
- [ChatPRD — AI Platform for Product Managers](https://www.chatprd.ai/)
- [18 Best AI Product Management Tools Reviewed in 2026](https://cpoclub.com/tools/best-ai-product-management-tools/)
- [HBR: To Drive AI Adoption, Build Your Team's Product Management Skills](https://hbr.org/2026/02/to-drive-ai-adoption-build-your-teams-product-management-skills)

---

## 📞 Next Steps

**Immediate Actions (This Week):**
1. Run quality audit (`scripts/check-skill-metadata.py`)
2. Achieve 2+ GitHub stars (share with PM community)
3. Fork and PR to `awesome-claude-skills`
4. Join ClaudeSkills.ai waitlist

**Questions to Resolve:**
- Do we want to monetize, or keep 100% free?
- Should we submit all 34 skills to Anthropic, or curate a subset?
- What's our brand positioning: "Open-source PM skills" vs. "Premium PM training"?

---

## 📊 Summary

### What We Have
✅ **34 marketplace-ready skills** (all validated)
✅ **Comprehensive rollout plan** (4 phases over 3 weeks)
✅ **5 target marketplaces identified** (SkillsMP, SkillHub, Anthropic, Awesome Claude Skills, ClaudeSkills.ai)
✅ **Quality audit complete** (all metadata requirements met)

### What We Need
⏳ **2+ GitHub stars** to trigger SkillsMP auto-indexing
📋 **PR to Awesome Claude Skills** (quick visibility win)
🤔 **Strategic decisions** on monetization and curation approach

### Recommended Path Forward (Feb 7, 2026)
1. **Morning:** Share repo to get stars (LinkedIn, Reddit, Slack)
2. **Afternoon:** Submit PR to Awesome Claude Skills
3. **Evening:** Make strategic decisions, prepare Anthropic submission

**Timeline:** First listings live within 7-10 days

---

**Ready to execute when you are. See you tomorrow!**
