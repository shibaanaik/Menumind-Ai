# backend/craving_suggestion.py

"""
This module provides craving suggestions based on user location.
It contains predefined cravings for various Indian cities and a default fallback list.
"""

# Craving suggestions based on location (all keys lowercase for consistency)
LOCATION_CRAVINGS = {
    "mumbai": ["vada pav", "pav bhaji", "bhel puri", "misal pav"],
    "delhi": ["chole bhature", "chaat", "paratha", "jalebi"],
    "bhubaneswar": ["dahibara aloodum", "chhena poda", "chakuli pitha", "rasgulla"],
    "chennai": ["idli", "dosa", "pongal", "filter coffee"],
    "lucknow": ["tunday kebab", "biryani", "chaat", "sheermal"],
    "kolkata": ["phuchka", "mishti doi", "kathi roll", "rasgulla"],
    "hyderabad": ["biryani", "haleem", "double ka meetha", "mirchi ka salan"],
    "ahmedabad": ["dhokla", "khandvi", "fafda", "undhiyu"],
    "jaipur": ["dal baati churma", "ghevar", "ker sangri", "laal maas"],
    "bengaluru": ["masala dosa", "idli vada", "rava idli", "bisibele bath"],
    "pune": ["misal pav", "puran poli", "sabudana khichdi", "bakarwadi"],
    "kanpur": ["thaggu ke laddu", "badnam kulfi", "samosa", "chaat"],
    "nagpur": ["tarri poha", "saoji mutton", "orange barfi", "patodi"],
    "indore": ["poha jalebi", "sev", "bhutte ka kees", "garadu"],
    "surat": ["locho", "undhiyu", "ghari", "sev khamani"],
    "patna": ["litti chokha", "khaja", "sattu paratha", "thekua"],
    "bhopal": ["biryani", "poha", "jalebi", "shahi tukda"],
    "varanasi": ["malaiyo", "tamatar chaat", "kachaudi sabzi", "banarasi paan"],
    "agra": ["petha", "bedai", "dal moth", "chaat"],
    "amritsar": ["amritsari kulcha", "lassi", "chole", "fish fry"],
    "ludhiana": ["butter chicken", "makki di roti", "sarson da saag", "paneer tikka"],
    "chandigarh": ["chole bhature", "rajma chawal", "paneer tikka", "lassi"],
    "coimbatore": ["kothu parotta", "idiyappam", "pongal", "vada curry"],
    "madurai": ["jigarthanda", "kari dosai", "parotta", "mutton chukka"],
    "trichy": ["sambar rice", "idli", "vada", "kothu parotta"],
    "kochi": ["appam", "stew", "fish curry", "puttu kadala"],
    "thiruvananthapuram": ["idiyappam", "nadan chicken curry", "banana chips", "avial"],
    "visakhapatnam": ["pootharekulu", "ulavacharu biryani", "gongura pachadi", "punugulu"],
    "vijayawada": ["andhra chicken curry", "gongura mutton", "punugulu", "mirchi bajji"],
    "guntur": ["guntur biryani", "natu kodi pulusu", "gongura pachadi", "idli"],
    "tirupati": ["pulihora", "laddu", "dosa", "upma"],
    "raipur": ["chana samosa", "faraa", "angakar roti", "jalebi"],
    "ranchi": ["thekua", "litti chokha", "dhuska", "malpua"],
    "jamshedpur": ["litti chokha", "sattu paratha", "dhuska", "malpua"],
    "dehradun": ["bal mithai", "singori", "kafuli", "chainsoo"],
    "haridwar": ["aloo puri", "kachaudi", "jalebi", "rabri"],
    "nainital": ["ras bhari", "bal mithai", "bhatt ki churkani", "aloo ke gutke"],
    "gangtok": ["momo", "thukpa", "phagshapa", "sel roti"],
    "aizawl": ["bai", "vawksa rep", "chhangban", "sanpiau"],
    "shillong": ["jadoh", "tungrymbai", "dohneiiong", "pukhlein"],
    "imphal": ["eromba", "ngari", "singju", "chakhao kheer"],
    "kohima": ["smoked pork", "bamboo shoot curry", "axone", "zutho"],
    "itanagar": ["thukpa", "momos", "chura sabzi", "apong"],
    "panaji": ["fish curry rice", "prawn balchão", "bebinca", "xacuti"],
    "margao": ["sorpotel", "vindaloo", "bebinca", "prawn curry"],
    "vasco da gama": ["goan sausage", "fish curry", "poi bread", "bebinca"],
    "siliguri": ["momo", "thukpa", "chowmein", "phaley"],
    "darjeeling": ["momo", "thukpa", "sel roti", "gundruk soup"],
    "howrah": ["kachori", "jalebi", "ghugni", "rasgulla"],
    "guwahati": ["masor tenga", "pitha", "duck curry", "aloo pitika"],
    "dibrugarh": ["pitha", "masor tenga", "duck curry", "aloo pitika"],
    "jorhat": ["pitha", "masor tenga", "duck curry", "aloo pitika"],
    "tezpur": ["pitha", "masor tenga", "duck curry", "aloo pitika"]
}

# Fallback cravings if location not found
DEFAULT_CRAVINGS = [
    "biryani", "chaat", "samosa", "dosa", "gulab jamun",
    "spicy", "sweet", "snack", "dessert", "tandoori",
    "paneer tikka", "kebab", "idli", "vada", "paratha"
]

def get_cravings_by_location(location: str):
    """
    Return a list of craving suggestions for the given location.
    Location lookup is case-insensitive.
    If location not found, return DEFAULT_CRAVINGS.
    """
    if not location:
        return DEFAULT_CRAVINGS
    
    loc_key = location.strip().lower()
    return LOCATION_CRAVINGS.get(loc_key, DEFAULT_CRAVINGS)

def get_all_locations():
    """
    Returns a list of all supported locations for craving suggestions.
    """
    return list(LOCATION_CRAVINGS.keys())

def add_or_update_location_cravings(location: str, cravings: list):
    """
    Add or update cravings for a given location.
    This can be used to dynamically update the suggestions.
    """
    if location and cravings:
        loc_key = location.strip().lower()
        LOCATION_CRAVINGS[loc_key] = cravings

