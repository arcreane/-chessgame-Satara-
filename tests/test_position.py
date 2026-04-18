if __name__ == "__main__":
    p1 = Position("e", 4)
    print(f"Position test : {p1}")

    p_idx = Position.from_indices(4, 3)
    print(f"Test index (4,3) -> {p_idx}")

    print("Tests Position OK !")