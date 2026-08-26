# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class NewGamePlus(Toggle):
    """Mostly changes logical requirements for weapon upgrades, also adds upgrades for the Matilda and Handcannon if setting is enabled"""
    display_name = "Use NG+ logic (mostly affects Merchant checks)."
    default = True

class Crates(Toggle):
    """Adds all crates, barrels, and vases to location pool. Some of these will be on top of herbs/treasures/ammo found within them. (470 locations)"""
    display_name = "Include crates and vases in main story."
    default = False

class Animals(Toggle):
    """Adds animals to the location pool (Crows, Fish, Snakes)  (110 locations)"""
    display_name = "Include animal checks in main story."
    default = False

class Memos(Toggle):
    """Adds memos and letters found around the game to item pool (excluding player manuals and NPC transmissions) (23 locations)"""
    display_name = "Include memos from main story."
    default = False

class Ammo(Toggle):
    """Adds main story guaranteed ammo pickup locations to the pool. (482 Locations)"""
    display_name = "Include main story static ammo pickups."
    default = False

class Chapters(Toggle):
    """Turns main story chapters into required items for progression."""
    display_name = "Require progressive chapters to advance main story."
    default = False

class SeparateWays(Toggle):
    """Include "Separate Ways" herbs and treasures to location pool."""
    display_name = "Add Separate Ways side-mission."
    default = False

class SeparateWaysCrates(Toggle):
    """Adds all Separate Ways crates, barrels, and vases to location pool. Some of these will be on top of herbs/treasures/ammo found within them. (119 locations)"""
    display_name = "Include Separate Ways crates and vases."
    default = False

class SeparateWaysAnimals(Toggle):
    """Adds Separate Ways animals to the location pool. (16 locations)"""
    display_name = "Include Separate Ways animals."
    default = False

class SeparateWaysAmmo(Toggle):
    """Adds Separate Ways guaranteed ammo pickup locations to the pool. (141 locations)"""
    display_name = "Include Separate Ways static ammo drops."
    default = False

class SeparateWaysChapters(Toggle):
    """Turns Separate Ways chapters into required items for progression."""
    display_name = "Require progressive chapters to advance Separate Ways."
    default = False

class Mercenaries(Toggle):
    """Include "Mercenaries" side-game to location pool. (202 locations)"""
    display_name = "Add Mercenaries minigames."
    default = False

class EmblemCaps(Toggle):
    """Adds the blue medallions and bottle caps to the location pool. (39 locations)"""
    display_name = "Collect blue medallions and bottle caps."
    default = False

class Weapons(Toggle):
    """Adds weapon purchases to the location pool, excluding NG+ weapons. (13 locations)"""
    display_name = "Include weapon purchases."
    default = False

class Upgrades(Toggle):
    """Adds weapon upgrades to location pool (Recommended for New_Game_Plus only) (182 locations; 158 w/o Matilda & Handcannon))"""
    display_name = "Include memos from main story."
    default = False

class Exclusives(Toggle):
    """Any upgrades/exclusives purchased in prior saves can be marked off as soon as they become logically available and have been found/been sent required items. (14 locations; 12 w/o Matilda & Handcannon)"""
    display_name = "Include memos from main story."
    default = False

class Matilda(Toggle):
    """Affects Merchant logic if added while New_Game_Plus, Merchant_Weapons, and Merchant_Upgrades options are enabled."""
    display_name = "Include the Matilda in starting inventory."
    default = False

class Handcannon(Toggle):
    """Affects Merchant logic if added while New_Game_Plus, Merchant_Weapons, and Merchant_Upgrades options are enabled."""
    display_name = "Include the Handcannon in starting inventory."
    default = False

class InfiniteLauncher(Toggle):
    """Affects story progression logic."""
    display_name = "Include the Infinite Launcher in starting inventory."
    default = False

class ChicagoTypewriter(Toggle):
    """For fun, does not affect logic"""
    display_name = "Include the Chicago Typewriter in starting inventory."
    default = False

class PRL412(Toggle):
    """For fun, does not affect logic"""
    display_name = "Include the P.R.L.-412 in starting inventory."
    default = False

class Death(Toggle):
    """This adds a button to the client for sending deathlink to other players. When sent to you, use the "Restart From Last Checkpoint" option."""
    display_name = "Deathlink"
    default = False

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["New_Game_Plus"] = NewGamePlus
    options["Cratesanity"] = Crates
    options["Animalsanity"] = Animals
    options["Memosanity"] = Memos
    options["Ammosanity"] = Ammo
    options["Chaptersanity"] = Chapters
    options["Separate_Ways"] = SeparateWays
    options["SW_Cratesanity"] = SeparateWaysCrates
    options["SW_Animalsanity"] = SeparateWaysAnimals
    options["SW_Ammosanity"] = SeparateWaysAmmo
    options["SW_Chaptersanity"] = SeparateWaysChapters
    options["Mercenaries_Mode"] = Mercenaries
    options["Merchant_Sidequests"] = EmblemCaps
    options["Merchant_Weapons"] = Weapons
    options["Merchant_Upgrades"] = Upgrades
    options["Merchant_Exclusives"] = Exclusives
    options["Matilda"] = Matilda
    options["Handcannon"] = Handcannon
    options["Infinite_Launcher"] = InfiniteLauncher
    options["Chicago_Typewriter"] = ChicagoTypewriter
    options["PRL_412"] = PRL412
    options["death_link"] = Death
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
