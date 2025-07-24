# Core Gameplay Loop

This document defines a precise gameplay loop combining Travian-style resource management with Diablo-like randomized loot. All actions complete in real time—there is no energy system or daily turn cycle.

## Resources

Cash is the only universal currency. The hideout generates it passively while
you're offline:

| Resource | Produced by | Base/hr at level 1 | Scaling per level |
|---------|-------------|-------------------|------------------|
| Cash (¥) | Hideout | 100 | `100 * level^1.10` |

Other commodities are produced separately by specialized buildings—drug labs,
brothels, chop shops and so on. Each commodity works like Idle Pixel's
item-based resources: it accrues over time at a rate of
`base_amount * level^scaling` and can be collected whenever you return.

Each building upgrade costs `base_cost * 1.6^(level-1)` and takes `base_time * level^1.5` minutes to complete. Buildings may be queued but only one upgrade runs at a time.

## Actions and Timers

| Action | Base Duration | Reward Formula | Failure Penalty |
|-------|--------------|---------------|----------------|
| Pickpocket | 3 min | `50 + 10*hero_level` cash | small heat increase |
| Rob Store | 10 min | `150 + 25*hero_level` cash, chance for common commodities | 5% injury risk |
| Heist | 30 min | `500 + 50*hero_level` cash, rare commodities | 15% injury, lose half rewards |
| Attack Rival | 15 min | Steal up to 20% of target cash and commodities | Lose 10% of own cash on failure |

Success chance is `Power / (Power + Difficulty)`. `Power` comes from your right hand's stats and equipped weapons. Difficulty scales with target level and action type.

## Itemization

The player has no personal stats. Instead, the selected right hand acts as a
hero—much like the hero unit in Travian—and carries all gear and levels. Items
dropped from crimes and fights follow a Diablo-style system. Gear is equipped
only by your right hand and directly influences their power:

- **Rarities:** Common, Rare, Epic, Legendary (multipliers: ×1, ×1.5, ×2, ×3).
- **Item Level:** equal to the right hand's level when found. Base stat is `item_level * rarity_multiplier`.
- **Affixes:** Up to 3 random modifiers. Example: `+5% crit`, `+2–4 damage`, `+1 commodity per hour`.
- **Set Bonuses:** Collecting full item sets grants extra bonuses like `+10% success chance`.

Items can be upgraded using cash: each upgrade adds `+10%` to all stats and costs `500 * upgrade_level` cash.

## Loop Summary

1. Queue a crime, building upgrade, or attack.
2. Wait for the timer to finish.
3. Collect resources and loot, then invest in buildings or gear.
4. Repeat to grow stronger and unlock tougher challenges.

This scalable loop lets players progress by accumulating resources and customizing loot without daily resets.
