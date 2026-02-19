def second_max(arr):
    try:
        sec_max = sorted(set(arr))
        if len(sec_max) < 2:
            raise ValueError("Not enough unique elements to find second maximum")
        return sec_max[-2]
    except ValueError as ve:
        print("ValueError:", ve)
        return None
    except Exception as e:
        print("Unexpected error:", e)
        return None