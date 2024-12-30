from dataclasses import dataclass, field


@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)
    athlete: bool = field(default=False, repr=False)


member1 = ClubMember(name="Alice")
member2 = ClubMember(name="Bob", athlete=True)

print(member1)
print(member2)

# Accessing the fields
print(member1.athlete)  # Output: False
print(member2.athlete)  # Output: True

# Modify the guests list for member1
member1.guests.append("Charlie")

print(member1.guests)  # Output: ['Charlie']
print(member2.guests)  # Output: []  (A separate list for each member)
