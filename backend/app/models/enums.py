import enum

class ApplicationStatus(str, enum.Enum):
    APPLIED = "Applied"
    OA = "OA"
    INTERVIEW = "Interview"
    REJECTED = "Rejected"
    OFFER = "Offer"
    ACCEPTED = "Accepted"