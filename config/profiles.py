"""
Customer profile configurations and column coordinate mappings.
To add a new customer, simply append a new dictionary entry to CUSTOMER_PROFILES.
"""

CUSTOMER_PROFILES = {
    "expresso": {
        "display_name": "Expresso",
        "icon": "☕",
        "description": "Expresso daily order synchronizer (Columns N to AK)",
        "data_key_col": "K",           # OrdNo column in maintained DATA file
        "data_start_row": 4,           # Data starts on Row 4
        "workdata_key_col": "A",       # OrdNo column in system WorkDataNew file
        "workdata_start_row": 4,       # Data starts on Row 4
        "column_mapping": {
            "N": "CG",  # Total Bag Bal
            "O": "DJ",  # Bal To Exp Qty
            "P": "DQ",  # PSEGOMA
            "Q": "DX",  # GSIR
            "R": "DY",  # GSIT
            "S": "EA",  # CastBal
            "T": "EP",  # RHODIUM
            "U": "EZ",  # P3POLA
            "V": "FA",  # P3POLB
            "W": "FB",  # P3POLC
            "X": "FE",  # P4POLB
            "Y": "FF",  # P1SETA
            "Z": "FJ",  # SETP
            "AA": "FO", # P1SETFK
            "AB": "GA", # P3PPLA
            "AC": "GF", # P4PPLB
            "AD": "GJ", # PFMG
            "AE": "GM", # P1FILC
            "AF": "GX", # P4FILB
            "AG": "GY", # SAMPLE
            "AH": "HA", # OS
            "AI": "HU", # TACHE
            "AJ": "JI", # SPRU
            "AK": "KV"  # BalToOpnQty
        }
    },
    "stuller": {
        "display_name": "Stuller",
        "icon": "💎",
        "description": "Stuller daily order synchronizer (Columns S to AK)",
        "data_key_col": "K",           # OrdNo column in maintained DATA file
        "data_start_row": 4,           # Data starts on Row 4
        "workdata_key_col": "A",       # OrdNo column in system WorkDataNew file
        "workdata_start_row": 4,       # Data starts on Row 4
        "column_mapping": {
            "S": "CG",  # Total Bag Bal
            "T": "DJ",  # Bal To Exp Qty
            "U": "DQ",  # PSEGOMA
            "V": "DR",  # PSEGORDY
            "W": "DS",  # PKG
            "X": "DW",  # GSII
            "Y": "DX",  # GSIR
            "Z": "EP",  # RHODIUM
            "AA": "EZ", # P3POLA
            "AB": "FA", # P3POLB
            "AC": "FB", # P3POLC
            "AD": "IT", # P9STPLGD
            "AE": "FH", # P3SETA
            "AF": "GA", # P3PPLA
            "AG": "GB", # P3PPLB
            "AH": "GU", # P3FILC
            "AI": "JZ", # PPPCSHLD
            "AJ": "KO", # HOLD
            "AK": "KV"  # BalToOpnQty
        }
    }
}