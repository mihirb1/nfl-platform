class Team:
    # yards maps this team's oppponents to the number of yards they got in total
    def __init__(self, name: str):
        self.name = name
        self.yards = {}

    def add_game(self, opponent: str, yards: int) -> None:
        self.yards[opponent] = self.yards.get(opponent, 0) + yards

    def total(self) -> int:
        total_yards = 0
        for yards in self.yards.values():
            total_yards += yards

        return total_yards

buffalo_bills = Team("BUF")
buffalo_bills.add_game("KS", 292)
buffalo_bills.add_game("SF", 358)
print(buffalo_bills.total())

        