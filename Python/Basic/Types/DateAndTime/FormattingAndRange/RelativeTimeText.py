# Previous input
dt_str = input("Enter datetime (YYYY-MM-DD HH:MM:SS): ")

# Process
from datetime import datetime

def get_Relative_Time_Text(dt_str, reference_dt_str=None):
    target = datetime.strptime(dt_str.strip(), "%Y-%m-%d %H:%M:%S")
    ref = datetime.strptime(reference_dt_str.strip(), "%Y-%m-%d %H:%M:%S") if reference_dt_str else datetime.now()
    diff_secs = int((ref - target).total_seconds())
    is_past = diff_secs >= 0
    secs = abs(diff_secs)
    if secs < 60:
        return "just now"
    minutes = secs // 60
    if minutes < 60:
        unit = f"{minutes} minute{'s' if minutes > 1 else ''}"
    else:
        hours = minutes // 60
        if hours < 24:
            unit = f"{hours} hour{'s' if hours > 1 else ''}"
        else:
            days = hours // 24
            if days < 30:
                unit = f"{days} day{'s' if days > 1 else ''}"
            else:
                months = days // 30
                if months < 12:
                    unit = f"{months} month{'s' if months > 1 else ''}"
                else:
                    years = months // 12
                    unit = f"{years} year{'s' if years > 1 else ''}"
    return f"{unit} ago" if is_past else f"in {unit}"

# Post process
print("Relative time:", get_Relative_Time_Text(dt_str))
