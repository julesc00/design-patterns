"""
SRP: Single Responsibility Principle
SOC: Separation of Concerns
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text: str):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos: int):
        del self.entries[pos]

    def __str__(self):
        """Human-readable representation of entries"""
        return "\n".join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


if __name__ == "__main__":
    j = Journal()
    j.add_entry("I'm learning Python today.")
    j.add_entry("I had some hot cocoa today.")

    f = r"journal.txt"
    PersistenceManager.save_to_file(j, f)

    print(j)
