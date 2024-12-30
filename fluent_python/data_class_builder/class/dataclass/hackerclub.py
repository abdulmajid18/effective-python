from dataclasses import dataclass
from club import ClubMember


@dataclass
class HackerClubMember(ClubMember):
    all_handles = set()
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)


try:
    member1 = HackerClubMember(name="Alice", handle="alice123")
    print(member1)  # Expected: HackerClubMember(name='Alice', handle='alice123')

    member2 = HackerClubMember(name="Bob")  # This should automatically set handle to "Bob"
    print(member2)  # Expected: HackerClubMember(name='Bob', handle='Bob')

    # Try to create a member with an already taken handle
    member3 = HackerClubMember(name="Charlie", handle="alice123")  # This should raise an error
except ValueError as e:
    print(e)  # Expected: handle 'alice123' already exists.
