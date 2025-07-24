# Core Gameplay Loop

This document defines a precise gameplay loop combining Travian-style resource management with Diablo-like randomized loot. All actions complete in real time—there is no energy system or daily turn cycle.

## Resources

Players manage three primary resources:

| Resource | Produced by | Base/hr at level 1 | Scaling per level |
|---------|-------------|------------------|------------------|
| Cash (¥) | Hideout | 100 | `100 * level^1.10` |
| Materials | Workshop | 30 | `30 * level^1.12` |
| Influence | Safehouse | 5 | `5 * level^1.15` |

Each building upgrade costs `base_cost * 1.6^(level-1)` and takes `base_time * level^1.5` minutes to complete. Buildings may be queued but only one upgrade runs at a time.

## Actions and Timers

| Action | Base Duration | Reward Formula | Failure Penalty |
|-------|--------------|---------------|----------------|
| Pickpocket | 3 min | `50 + 10*char_level` cash | −2 Influence |
| Rob Store | 10 min | `150 + 25*char_level` cash, 1–3 Materials | 5% injury risk |
| Heist | 30 min | `500 + 50*char_level` cash, 5–8 Materials, +3 Influence | 15% injury, lose half rewards |
| Attack Rival | 15 min | Steal up to 20% of target cash and materials | Lose 10% of own cash on failure |

Success chance is `Power / (Power + Difficulty)`. `Power` comes from character stats plus weapon bonuses. Difficulty scales with target level and action type.

## Itemization

Items drop from crimes and fights and follow a Diablo-style system:

- **Rarities:** Common, Rare, Epic, Legendary (multipliers: ×1, ×1.5, ×2, ×3).
- **Item Level:** equal to the player's level when found. Base stat is `item_level * rarity_multiplier`.
- **Affixes:** Up to 3 random modifiers. Example: `+5% crit`, `+2–4 damage`, `+1 Influence per hour`.
- **Set Bonuses:** Collecting full item sets grants extra bonuses like `+10% success chance`.

Items can be upgraded using Materials: each upgrade adds `+10%` to all stats and costs `5 * upgrade_level` Materials.

## Loop Summary

1. Queue a crime, building upgrade, or attack.
2. Wait for the timer to finish.
3. Collect resources and loot, then invest in buildings or gear.
4. Repeat to grow stronger and unlock tougher challenges.

This scalable loop lets players progress by accumulating resources and customizing loot without daily resets.
