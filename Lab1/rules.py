from production import (
    IF,
    AND,
    THEN,
    OR,
    NOT,
    forward_chain,
    backward_chain,
    instantiate,
)

TOURIST_RULES = (
    IF(
        AND(
            OR(
                "(?x) enjoy activities that are physically challenging",
                "(?x) involve an element of risk",
            ),
            OR(
                "(?x) likes activities such as hiking",
                "(?x) likes activities such as rock climbing",
                "(?x) likes activities such as extreme sports",
            ),
            OR(
                "(?x) tend to be young",
                "(?x) tend to be active",
            ),
            "(?x) prioritize experiences over luxury accommodations",
        ),
        THEN("(?x) areAdventureTourists"),
    ),
    IF(
        AND(
            "(?x) interested in immersing themselves in the local culture of the places",
            OR(
                "(?x) enjoy exploring historical sites",
                "(?x) visiting museums",
                "(?x) attending cultural events",
            ),
            "(?x) tend to be curious",
            "(?x) tend to be open-minded",
            "(?x) are interested in learning about the traditions",
        ),
        THEN("(?x) areCulturalTourists"),
    ),
    IF(
        AND(
            "(?x) are willing to spend a premium for high-end accommodations",
            "(?x) tend to have exclusive experiences",
            "(?x) seek out luxury hotels",
            "(?x) tend to have fine dining",
            OR(
                "(?x) tend to have private tours",
                "(?x) tend to have personal concierge services",
            ),
            "(?x) prioritize comfort and convenience over adventure",
        ),
        THEN("(?x) areLuxuryTourists"),
    ),
    IF(
        AND(
            OR(
                "(?x) travel with children",
                "(?x) travel with extended family",
            ),
            "(?x) tend to seek out low-cost accommodations and activities",
            "(?x) prioritize activities that are suitable for all ages",
            "(?x) tend to prioritize safety",
            "(?x) tend to prioritize convenience",
            "(?x) tend to prioritize affordability",
            "(?x) prioritize comfort and convenience over adventure",
        ),
        THEN("(?x) areFamilyTourists"),
    ),
    IF(
        AND(
            "(?x) prioritize affordability over luxury",
            "(?x) tend to seek out low-cost accommodations and activities",
            "(?x) travel on a shoestring budget",
            OR(
                "(?x) staying in hostels",
                "(?x) staying in budget hotels",
            ),
            NOT("(?x) seeking out expensive eats"),
        ),
        THEN("(?x) areBudgetTourists"),
    ),
)
