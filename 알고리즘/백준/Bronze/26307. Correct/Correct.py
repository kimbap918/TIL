from datetime import datetime


def correct(HH, MM):
    start_time = datetime(year=2022, month=1, day=1, hour=9)
    
    end_time = datetime(year=2022, month=1, day=1, hour=HH, minute=MM)
    
    consumed_time = end_time - start_time
    
    return consumed_time.seconds // 60


if __name__ == "__main__":
    HH, MM = map(int, input().split())
    
    print(correct(HH=HH, MM=MM))